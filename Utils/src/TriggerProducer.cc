// -*- C++ -*-
//
// Package:    TriggerProducer
// Class:      TriggerProducer
// 
/**\class TriggerProducer TriggerProducer.cc RA2Classic/TriggerProducer/src/TriggerProducer.cc
 */
//
//         Created:  Wednesday Nonember 25 2016
//         Modified by Muzamil Ahmad Bhat 
// system include files
#include <memory>
#include <algorithm>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"

#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtTrigReport.h"
#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"
#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtTrigReportEntry.h"
#include "CondFormats/DataRecord/interface/L1GtStableParametersRcd.h"

#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
//#include "DataFormats/L1Trigger/interface/BXVector.h"

#include <cassert>
#include <string>
#include<vector>

using namespace CLHEP;
using namespace trigger;
using namespace math;
// class declaration
//

class TriggerProducer : public edm::EDProducer {
public:
  explicit TriggerProducer(const edm::ParameterSet&);
  ~TriggerProducer();
	
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  
  void GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default);
  edm::InputTag trigResultsTag_;
  edm::InputTag trigPrescalesTag_;
  edm::InputTag objecttag_;
  edm::EDGetTokenT<edm::TriggerResults> trigResultsTok_;
  edm::EDGetTokenT<pat::PackedTriggerPrescales> trigPrescalesTok_;
  edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjectsTok_;//Vangelis
 
  std::vector<std::string> parsedTrigNamesVec;
   HLTPrescaleProvider hltPrescaleProvider_;
//  HLTConfigProvider hltPrescaleProvider_;	
 bool prescale_fallback_;
HLTConfigProvider hlt_config_;

 // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TriggerProducer::TriggerProducer(const edm::ParameterSet& iConfig):
hltPrescaleProvider_(iConfig, consumesCollector(), *this)
// prescale_fallback_(iConfig.getParameter<bool>("prescaleFallback"))
{

//if (prescale_fallback_) {
    consumes<BXVector<GlobalAlgBlk>>(edm::InputTag("gtStage2Digis"));
 // }
  parsedTrigNamesVec = iConfig.getParameter <std::vector<std::string> > ("triggerNameList");
  //sort the trigger names
  std::sort(parsedTrigNamesVec.begin(), parsedTrigNamesVec.end());
  //print triggers
  std::cout << "List of stored triggers:" << std::endl;
  for(unsigned t = 0; t < parsedTrigNamesVec.size(); ++t){
    std::cout << t << ": " << parsedTrigNamesVec[t] << std::endl;
  }
  
  GetInputTag(trigResultsTag_,
              iConfig.getParameter <std::string> ("trigTagArg1"),
              iConfig.getParameter <std::string> ("trigTagArg2"),
              iConfig.getParameter <std::string> ("trigTagArg3"),
              "TriggerResults");

  GetInputTag(trigPrescalesTag_,
              iConfig.getParameter <std::string> ("prescaleTagArg1"),
              iConfig.getParameter <std::string> ("prescaleTagArg2"),
              iConfig.getParameter <std::string> ("prescaleTagArg3"),
              "patTrigger");
 
/*  GetInputTag(objecttag_,
              iConfig.getParameter <std::string> ("objecttag"),
              iConfig.getParameter <std::string> ("objecttag"),
              iConfig.getParameter <std::string> ("objecttag"),
              "selectedPatTrigger");*/
   trigResultsTok_ = consumes<edm::TriggerResults>(trigResultsTag_);
   trigPrescalesTok_ = consumes<pat::PackedTriggerPrescales>(trigPrescalesTag_);
//   triggerObjectsTok_ =  consumes<pat::TriggerObjectStandAloneCollection>(objecttag_);
// hltPrescaleProvider_(iConfig, consumesCollector(), *this)
//triggerObjectsTok_ =  consumes<pat::TriggerObjectStandAloneCollection>(bjecttag_);
triggerObjectsTok_ = consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objecttag"));
//  triggerObjectsTok_ =  "selectedPatTrigger";

   produces<std::vector<std::string> >("TriggerNames");
   produces<std::vector<int> >("TriggerPass");
   produces<std::vector<int> >("TriggerPrescales");
   produces<std::vector<std::string> >("FilterNames");
   produces<std::vector<double> >("objectPt");
   produces<std::vector<double> >("objecteta");
   produces<std::vector<double> >("objectphi");
   produces<std::vector<double> >("objectE");
   produces<std::vector<double> >("ColumnNum");
}


TriggerProducer::~TriggerProducer()
{}

//
// member functions
//

// ------------ helper function to make InputTags ------------
void
TriggerProducer::GetInputTag(edm::InputTag& tag, std::string arg1, std::string arg2, std::string arg3, std::string arg1_default=""){
  // We we make the producer a little smarter. There are four cases we look at
  // 1) arg1 and arg3 are set, if this is the case we create the label bases on all three arguments
  // 2) arg3 is not set, in this case we create the label based only on arg1
  // 3) Neither arg1 nor arg3 are set, in this case we default to searching for arg1_default
  // 4) arg1 is not set, but arg3 is set, we look for arg1_default in the process defined by arg3

  if(arg1.empty()) arg1 = arg1_default;
  
  if(arg3.empty()){
    tag = edm::InputTag(arg1);
  } else {
    tag = edm::InputTag(arg1,arg2,arg3);
  }	
}

// ------------ method called to produce the data  ------------
void
TriggerProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::auto_ptr<std::vector<int> > passTrigVec(new std::vector<int>(parsedTrigNamesVec.size(),-1));
  std::auto_ptr<std::vector<int> > trigPrescaleVec(new std::vector<int>(parsedTrigNamesVec.size(),1));
  std::auto_ptr<std::vector<std::string> > trigNamesVec(new std::vector<std::string>(parsedTrigNamesVec.size(),""));
  std::auto_ptr<std::vector<double> >objectPt(new std::vector<double>());
  std::auto_ptr<std::vector<double> >objecteta(new std::vector<double>());
  std::auto_ptr<std::vector<double> >objectphi(new std::vector<double>());
  std::auto_ptr<std::vector<double> >objectE(new std::vector<double>());
  std::auto_ptr<std::vector<std::string> >FilterNames(new std::vector<std::string>());
  std::auto_ptr<std::vector<double> >ColumnNum(new std::vector<double>());

 //int passesTrigger;

  edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;//Vangelis
  iEvent.getByToken(triggerObjectsTok_, triggerObjects);//Vangelis

if(triggerObjects.isValid()){
//std::cout<<"handle found"<<std::endl;
}

//*******************************************************************************************For L1 prescale**********************
   edm::Handle<BXVector<GlobalAlgBlk>> l1algo_handle;
  //  if (prescale_fallback_) {
      iEvent.getByLabel(edm::InputTag("gtStage2Digis"), l1algo_handle);
   
  //                           std::cout<<"Yay I have succeeded in accessing the trigger information   "<<std::endl;
// }


  edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
  iEvent.getByToken(trigResultsTok_,trigResults);


 // std::cout<<"Trig Tag:  "<<trigResultsTag_<<std::endl;

  const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);
  edm::Handle<pat::PackedTriggerPrescales> trigPrescales;
  iEvent.getByToken(trigPrescalesTok_,trigPrescales);


double  column = l1algo_handle->at(0, 0).getPreScColumn();
ColumnNum->push_back(column);
// cout<<"column is   "<<column<<endl;

  //Find the matching triggers
  std::string testTriggerName;
  for(unsigned int parsedIndex = 0; parsedIndex < parsedTrigNamesVec.size(); parsedIndex++){
    trigNamesVec->at(parsedIndex) = parsedTrigNamesVec[parsedIndex];
    for(unsigned int trigIndex = 0; trigIndex < trigNames.size(); trigIndex++){
      testTriggerName = trigNames.triggerName(trigIndex);
//std::cout<<testTriggerName<<std::endl; 
      if(testTriggerName.find(parsedTrigNamesVec.at(parsedIndex)) != std::string::npos){
        trigNamesVec->at(parsedIndex) = testTriggerName;
        passTrigVec->at(parsedIndex) = trigResults->accept(trigIndex);
        trigPrescaleVec->at(parsedIndex) = trigPrescales->getPrescaleForIndex(trigIndex);
         //std::cout<<"trigger path is    "<<testTriggerName<<std::endl;
//        const std::pair<std::vector<std::pair<std::string,int> >,int> prescalesInDetail(hltPrescaleProvider_.prescaleValuesInDetail(iEvent,iSetup,testTriggerName));  
//        const std::pair<std::vector<std::pair<std::string,int> >,int> prescalesInDetail(hltConfig_.prescaleValuesInDetail(iEvent,iSetup, testTriggerName));
          	    //l1pres->at(parsedIndex) = i
          	    //std::cout<<"L1 prescale is    "<<prescalesInDetail.first[0].second<<std::endl;
                   // cout<<prescalesInDetail.second<<endl;
        //            if(prescalesInDetail.second ==trigPrescales->getPrescaleForIndex(trigIndex)){
          //                   std::cout<<"Yay I have succeeded in accessing the trigger information   "<<std::endl;}
       



          //unsigned column = l1algo_handle->at(0, 0).getPreScColumn();
        //if(column != 5)
      //   cout<<"column is   "<<column<<"         "<<testTriggerName<<endl;
        //  unsigned other_prescale = hlt_config_.prescaleValue(column, "L1_SingleEG18");
  //        if(other_prescale !=1)
    //       std::cout<<"other_prescale    "<<other_prescale<<std::endl;


        //std::cout << "Matched: " << testTriggerName << std::endl;
        break; //We only match one trigger to each trigger name fragment passed
      }
    }
  }




for (pat::TriggerObjectStandAlone obj : *triggerObjects) {



     obj.unpackPathNames(trigNames);


  if(obj.hasFilterLabel("hltEG22HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){

//std::cout<<"Hi I am testing the triggerproducer0"<<std::endl;
  
                 FilterNames->push_back("hltEG22HEFilter");
	           objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }

if(obj.hasFilterLabel("hltEG30HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer1"<<std::endl;

                   FilterNames->push_back("hltEG30HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }

if(obj.hasFilterLabel("hltEG36HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){

//std::cout<<"Hi I am testing the triggerproducer2"<<std::endl;
                   FilterNames->push_back("hltEG36HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }

if(obj.hasFilterLabel("hltEG50HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer3"<<std::endl;

                   FilterNames->push_back("hltEG50HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }



if(obj.hasFilterLabel("hltEG75HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer4"<<std::endl;

                   FilterNames->push_back("hltEG75HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }



if(obj.hasFilterLabel("hltEG90HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer5"<<std::endl;

                   FilterNames->push_back("hltEG90HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }


if(obj.hasFilterLabel("hltEG120HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer6"<<std::endl;

                   FilterNames->push_back("hltEG120HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }

if(obj.hasFilterLabel("hltEG175HEFilter") && obj.hasTriggerObjectType(trigger::TriggerPhoton)){
//std::cout<<"Hi I am testing the triggerproducer7"<<std::endl;

                   FilterNames->push_back("hltEG175HEFilter");
                   objectPt->push_back( obj.pt());
                   objecteta->push_back( obj.eta());
                   objectphi->push_back( obj.phi());
                   objectE->push_back( obj.energy());

   }


 }


  iEvent.put(FilterNames,"FilterNames");
  iEvent.put(passTrigVec,"TriggerPass");
  iEvent.put(trigPrescaleVec,"TriggerPrescales");
  iEvent.put(trigNamesVec,"TriggerNames");
  iEvent.put(objectPt, "objectPt");
  iEvent.put(objecteta, "objecteta");
  iEvent.put(objectphi, "objectphi");
  iEvent.put(objectE, "objectE");
  iEvent.put(ColumnNum, "ColumnNum");
}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
TriggerProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
TriggerProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
TriggerProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
TriggerProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerProducer);
