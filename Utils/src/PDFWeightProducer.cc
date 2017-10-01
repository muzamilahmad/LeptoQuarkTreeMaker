#include <cmath>
#include <memory>

// user include files
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include <iostream>
#include <string>

#include "TVector2.h"

//
// class declaration
//



class PDFWeightProducer : public edm::EDProducer {
public:
  explicit PDFWeightProducer(const edm::ParameterSet&);
  ~PDFWeightProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
	
  virtual void beginRun(edm::Run&, edm::EventSetup const&);
  virtual void endRun(edm::Run&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  
  // ----------member data ---------------------------
//  edm::GetterOfProducts<LHEEventProduct> getterOfProducts_;
 // edm::EDGetTokenT<GenEventInfoProduct> genProductToken_;
  const edm::EDGetTokenT<GenEventInfoProduct> genEvtInfoInputToken_;
  const bool  storePDFWeights = true;
  const edm::EDGetTokenT<std::vector<double> > pdfCTEQWeightsInputToken_;
  const edm::EDGetTokenT<std::vector<double> > pdfMMTHWeightsInputToken_;
  const edm::EDGetTokenT<std::vector<double> > pdfNNPDFWeightsInputToken_;
  //const edm::EDGetTokenT<std::vector<double> > pdfPDF4LHCWeightsInputToken_;
  //const edm::EDGetTokenT<std::vector<PileupSummaryInfo> >   pileupInfoSrcToken_;
  const edm::EDGetTokenT<LHERunInfoProduct>    LHERunInfoToken_;
  const edm::EDGetTokenT<LHEEventProduct> LHEEventProductToken_;

};


PDFWeightProducer::PDFWeightProducer(const edm::ParameterSet& iConfig) :
// getterOfProducts_(edm::ProcessMatch("*"), this), genProductToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator"))),
  genEvtInfoInputToken_(consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("GenEventInfoInputTag"))),
  storePDFWeights(iConfig.getParameter<bool>("StorePDFWeights")),
  pdfCTEQWeightsInputToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("PDFCTEQWeightsInputTag"))),
  pdfMMTHWeightsInputToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("PDFMMTHWeightsInputTag"))),
  pdfNNPDFWeightsInputToken_(consumes<std::vector<double> >(iConfig.getParameter<edm::InputTag>("PDFNNPDFWeightsInputTag"))),
//  pileupInfoSrcToken_(consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupInfo"))),
  LHERunInfoToken_(consumes<LHERunInfoProduct, edm::InRun >(iConfig.getParameter<edm::InputTag>("LHERunInfoProductInputTag"))),
  LHEEventProductToken_(consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("LHEEventProductInputTag")))
{
//std::cout<<" hi I am in producer "<<std::endl;
  produces <unsigned int>        ( "ProcessID" );
  produces <float>               ( "PtHat" );
  produces <std::vector<double> > ( "PDFCTEQWeights" );
  produces <std::vector<double> > ( "PDFMMTHWeights" );
  produces <std::vector<double> > ( "PDFNNPDFWeights" );
  produces <std::vector<double> > ( "PDFNNPDFWeightsAMCNLO" );
  produces <std::vector<double> > ( "ScaleWeights" );
  produces <std::vector<double> > ( "ScaleWeightsAMCNLO" );
  produces <double>               ( "genWeight" );
 // produces <std::vector<int> >   ( "PileUpInteractions");
 // produces <std::vector<int> >   ( "PileUpOriginBX" ) ;
 // produces <std::vector<float> > ( "PileUpInteractionsTrue" );
 // produces <float>               ( "Weight" );

}

PDFWeightProducer::~PDFWeightProducer()
{
	
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
	
}
void PDFWeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
//std::cout<<"hi I am inside MC"<<std::endl;

  using namespace edm;

  std::auto_ptr<unsigned int >        processID   ( new unsigned int() );
  std::auto_ptr<float >               ptHat ( new float() );
  std::auto_ptr<std::vector<double> >  pdfCTEQWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pdfMMTHWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pdfNNPDFWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pdfNNPDFWeightsAMCNLO (new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  scaleWeights  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  scaleWeightsAMCNLO  ( new std::vector<double>()  );
  std::auto_ptr<double>                genWeight  ( new double()  );
 // std::auto_ptr<float >               weight ( new float() );

  *processID.get() = 0;
  *ptHat.get() = 0.;
  //*weight.get() = 0.;


//std::cout<<"hi I am inside MC"<<std::endl;





if( !iEvent.isRealData() ) {
//std::cout<<"hi I am inside MC"<<std::endl;
    edm::Handle<GenEventInfoProduct> genEvtInfoProduct;
    iEvent.getByToken(genEvtInfoInputToken_, genEvtInfoProduct);


    edm::Handle<LHEEventProduct> EvtHandle;
    iEvent.getByToken(LHEEventProductToken_, EvtHandle );

    edm::Handle<GenEventInfoProduct> genEvtInfo;
    iEvent.getByToken(genEvtInfoInputToken_, genEvtInfo);

    if( genEvtInfoProduct.isValid() ) {
      edm::LogInfo("RootTupleMakerV2_GenEventInfoInfo") << "Successfully obtained genEvtInfoInputToken_";
  //    std::cout<<"genEvtInfoProduct.isValid()"<<std::endl;//...remove it later
      *processID.get() = genEvtInfoProduct->signalProcessID();
      *ptHat.get() = ( genEvtInfoProduct->hasBinningValues() ? genEvtInfoProduct->binningValues()[0] : 0. );
   //   *weight.get() = genEvtInfoProduct->weight();

    } else {
      edm::LogError("RootTupleMakerV2_GenEventInfoError") << "Error! Can't get the genEvtInfoInputToken_";
    }

    if( storePDFWeights ) {
  //if(true){
      bool doExternalWeights=true;
 //std::cout<<"storePDFWeights"<<std::endl;//...remove it later

      if (EvtHandle.isValid() && genEvtInfo.isValid()){

	if (EvtHandle->weights().size()>0){
	  doExternalWeights=false;
	}
      }
      if (doExternalWeights==true){
      edm::Handle<std::vector<double> > pdfCTEQWeightsHandle;
      edm::Handle<std::vector<double> > pdfMMTHWeightsHandle;
      edm::Handle<std::vector<double> > pdfNNPDFWeightsHandle;

   //   std::cout<<"doExternalWeights==true"<<std::endl;//...remove it later

      iEvent.getByToken(pdfCTEQWeightsInputToken_, pdfCTEQWeightsHandle);
      iEvent.getByToken(pdfMMTHWeightsInputToken_, pdfMMTHWeightsHandle);
      iEvent.getByToken(pdfNNPDFWeightsInputToken_, pdfNNPDFWeightsHandle);


      if( pdfCTEQWeightsHandle.isValid() ) {
     //   std::cout<<"pdfCTEQWeightsHandle.isValid"<<std::endl;//...remove it later

        edm::LogInfo("RootTupleMakerV2_GenEventInfoInfo") << "Successfully obtained pdfCTEQWeightsInputToken_";
	std::vector<double> weights = (*pdfCTEQWeightsHandle);
	std::vector<double> reWeightsCTEQ;
	unsigned int nmembers = weights.size();	
	for (unsigned int i=0; i<nmembers; i++) {

	  if(weights[0]>1.e-4)reWeightsCTEQ.push_back(weights[i]/weights[0]);
	  else reWeightsCTEQ.push_back(1.0);
	}
        *pdfCTEQWeights.get() = reWeightsCTEQ;

      } else {
        edm::LogError("RootTupleMakerV2_GenEventInfoError") << "Error! Can't get the pdfCTEQWeightsInputToken_";
      }

      if( pdfMMTHWeightsHandle.isValid() ) {
        edm::LogInfo("RootTupleMakerV2_GenEventInfoInfo") << "Successfully obtained pdfMMTHWeightsInputToken_";

	std::vector<double> weights = (*pdfMMTHWeightsHandle);
	std::vector<double> reWeightsMMTH;
	unsigned int nmembers = weights.size();	
	for (unsigned int i=0; i<nmembers; i++) {
	  if(weights[0]>1.e-4)reWeightsMMTH.push_back(weights[i]/weights[0]);
	  else reWeightsMMTH.push_back(1.0);
	}
        *pdfMMTHWeights.get() = reWeightsMMTH;
      } else {
        edm::LogError("RootTupleMakerV2_GenEventInfoError") << "Error! Can't get the pdfMMTHWeightsInputToken_";
      }
      
      if( pdfNNPDFWeightsHandle.isValid() ) {
        edm::LogInfo("RootTupleMakerV2_GenEventInfoInfo") << "Successfully obtained pdfNNPDFWeightsInputToken_";
//std::cout<<"hi I am fixing it"<<std::endl;
	std::vector<double> weights = (*pdfNNPDFWeightsHandle);
	std::vector<double> reWeightsNNPDF;
	unsigned int nmembers = weights.size();	
	for (unsigned int i=0; i<nmembers; i++) {

	  if(weights[0]>1.e-4)reWeightsNNPDF.push_back(weights[i]/weights[0]);
	  else reWeightsNNPDF.push_back(1.0);
	}
        *pdfNNPDFWeights.get() = reWeightsNNPDF;
      } else {
        edm::LogError("RootTupleMakerV2_GenEventInfoError") << "Error! Can't get the pdfNNPDFWeightsInputToken_";
      }
 
      }
    }

    //edm::Handle<std::vector<PileupSummaryInfo> >  puInfo;
    //iEvent.getByToken(pileupInfoSrcToken_, puInfo);
    
    
   
    if (EvtHandle.isValid() && genEvtInfo.isValid()){

      if (EvtHandle->weights().size()>0){

      	float theWeight = genEvtInfo->weight();
      	float thisWeight = -1.;
	
 
      	for (unsigned int i=0; i <= 8; i++) {

      		thisWeight = theWeight * (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); 
		scaleWeights->push_back(thisWeight);
      		thisWeight = (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); //fixme todo: removed theWeight, was multiplying by a factor +-200000 in amc@NLO
		scaleWeightsAMCNLO->push_back(thisWeight);
      	}
	
	for (unsigned int i=9; i <= 109; i++) {
	  thisWeight = theWeight * (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); 
	  pdfNNPDFWeights->push_back(thisWeight);
	  thisWeight = (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); //fixme todo: removed theWeight, was multiplying by a factor +-200000 in amc@NLO
	//std::cout<<thisWeight<<std::endl; 
	  pdfNNPDFWeightsAMCNLO->push_back(thisWeight);

	}
	
      	for (unsigned int i=315; i <= 365; i++) {
	//  thisWeight = theWeight * (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); 
	 // pdfMMTHWeights->push_back(thisWeight);
	}
      	for (unsigned int i=392; i <= 444; i++) {
	 // thisWeight = theWeight * (EvtHandle->weights()[i].wgt/EvtHandle->originalXWGTUP()); 
	 // pdfCTEQWeights->push_back(thisWeight);
	}
	
    
      	EvtHandle->weights()[0].wgt < 0 ? *genWeight.get()=-1. : *genWeight.get()=1.;
      
      
      }
    }
  }
   iEvent.put( processID, "ProcessID" );
  iEvent.put( ptHat, "PtHat" );
  iEvent.put( pdfCTEQWeights, "PDFCTEQWeights" );
  iEvent.put( pdfMMTHWeights, "PDFMMTHWeights" );
  iEvent.put( pdfNNPDFWeights, "PDFNNPDFWeights" );

  iEvent.put( pdfNNPDFWeightsAMCNLO, "PDFNNPDFWeightsAMCNLO");
  iEvent.put( std::move(scaleWeights), "ScaleWeights" );
  iEvent.put( scaleWeightsAMCNLO, "ScaleWeightsAMCNLO" );
  iEvent.put( genWeight, "genWeight" );

  //iEvent.put( weight, "Weight" );















/*

  std::vector<edm::Handle<LHEEventProduct> > handles;
  getterOfProducts_.fillHandles(iEvent, handles);
  
  std::vector<double> scaleweights;
  std::vector<double> pdfweights;
  std::vector<int> pdfids;
  std::vector<double> genWeight; 
  bool found_weights = false;
 
//....................this  is the new added part...
//edm::Handle<LHEEventProduct> EvtHandle;
//iEvent.getByToken("externalLHEProducer", EvtHandle );


//edm::Handle<GenEventInfoProduct> genHandle;
  //  iEvent.getByToken(genProductToken_, genHandle);



//...................till here................

 
  if(!handles.empty()){
    edm::Handle<LHEEventProduct> LheInfo = handles[0];


    
    std::vector< gen::WeightsInfo > lheweights = LheInfo->weights();
    if(!lheweights.empty()){
      found_weights = true;
//std::cout<<"event weight is      "<<lheweights[0].wgt<<std::endl;
        
      genWeight.push_back(lheweights[0].wgt < 0 ? -1 :1);    
//std::cout<<genWeight.at(0); 
//if(genHandle.isValid()){
//std::cout<<"event weight is      "<<lheweights[0].wgt<<std::endl;
//}
//std::cout<<genWeight.at(0)<<std::endl;  
// these numbers are hard-coded by the LHEEventInfo
      //renormalization/factorization scale weights
      for (unsigned int i = 0; i < 9; i++){
        scaleweights.push_back(lheweights[i].wgt/lheweights[0].wgt);
      }
      //pdf weights
      for (unsigned int i = 9; i < 110; i++){
        pdfweights.push_back(lheweights[i].wgt/lheweights[9].wgt);
        pdfids.push_back(i-9);
      }
    }
  }
  
  //check GenEventInfoProduct if LHEEventProduct not found or empty
  if(!found_weights){
//std::cout<<"foundweight===    "<<found_weights<<std::endl;
   edm::Handle<GenEventInfoProduct> genHandle;
   iEvent.getByToken(genProductToken_, genHandle);
	const std::vector<double>& genweights = genHandle->weights();
    // these numbers are hard-coded by the GenEventInfo (shifted by 1 wrt LHE)
    //renormalization/factorization scale weights
    for (unsigned int i = 1; i < 10; i++){
      scaleweights.push_back(genweights[i]/genweights[1]);
    }
    //pdf weights
    for (unsigned int i = 10; i < 111; i++){

       pdfweights.push_back(genweights[i]/genweights[10]);
      pdfids.push_back(i-10);
    }
  }

  std::auto_ptr<std::vector<double> > scaleweights_(new std::vector<double>(scaleweights));
  iEvent.put(scaleweights_,"ScaleWeights");
  
  std::auto_ptr<std::vector<double> > pdfweights_(new std::vector<double>(pdfweights));
  iEvent.put(pdfweights_,"PDFweights");
  
  std::auto_ptr<std::vector<int> > pdfids_(new std::vector<int>(pdfids));

  iEvent.put(pdfids_,"PDFids");

  std::auto_ptr<std::vector<double> > genWeight_(new std::vector<double>(genWeight));
    iEvent.put(genWeight_, "genWeight");
*/
}

// ------------ method called once each job just before starting event loop  ------------
void
PDFWeightProducer::beginJob()
{
std::cout<<"hi I am testing the code"<<std::endl;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PDFWeightProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void 
PDFWeightProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PDFWeightProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PDFWeightProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PDFWeightProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PDFWeightProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PDFWeightProducer);
