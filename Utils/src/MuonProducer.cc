//        [Notes on implementation]
//        */
//        //
//        // Original Author:  Muzamil Ahmad Bhat
//        //         Created:  Thu, 13 April 2016 06:55:01 GMT
//        //
//        //
//
//
//        // system includes files

#include <memory>
// user include files
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
//#include "FWCore/Utilities/interface/InputTag.h"
//#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
//#include "TreeMaker/Utils/interface/genParticlesProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "TVector2.h"
class MuonProducer : public edm::EDProducer {

 public:
      explicit MuonProducer(const edm::ParameterSet&);
  //    ~TrackAndPointsProducer()
         ~MuonProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;


      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

    edm::InputTag muontag_;
    edm::InputTag tautag_;

};


MuonProducer::MuonProducer(const edm::ParameterSet& iConfig)
{
    muontag_  = iConfig.getParameter<edm::InputTag>( "muontag" );
    tautag_  = iConfig.getParameter<edm::InputTag>( "tautag" );

    produces<std::vector<double>>( "Eta" );
   // produces<std::vector<int>>( "Charge" );
    produces<std::vector<double>>( "mPt");
    produces<std::vector<double>>( "mPhi");
    produces<std::vector<int>>( "mCharge");
   
    produces<std::vector<double>>( "tEta" );
    produces<std::vector<double>>( "tPt");
    produces<std::vector<double>>( "tPhi");


}


MuonProducer::~MuonProducer()
{}



void MuonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace reco;
    using namespace std;
    edm::Handle<std::vector<pat::Muon> > muon;
    edm::Handle<std::vector<pat::Tau> > tau;


    std::auto_ptr<std::vector<double> >Eta(new std::vector<double>());
  //  std::auto_ptr<std::vector<int> > Charge(new std::vector<int>());
    std::auto_ptr<std::vector<double> > mPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > mPhi(new std::vector<double>());
    std::auto_ptr<std::vector<int> > mCharge(new std::vector<int>());
    
    std::auto_ptr<std::vector<double> >tEta(new std::vector<double>());
  //  std::auto_ptr<std::vector<int> > Charge(new std::vector<int>());
    std::auto_ptr<std::vector<double> > tPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > tPhi(new std::vector<double>());



iEvent.getByLabel( muontag_, muon );
iEvent.getByLabel( tautag_, tau );



    for(std::vector<pat::Muon>::const_iterator mu=muon->begin(); mu!=muon->end(); ++mu){
    //cout<<mu->pt()<<"          "<<mu->charge()<<endl;
     Eta->push_back(mu->eta());
     mCharge->push_back(mu->charge());
     mPt->push_back(mu->pt());
     mPhi->push_back(mu->phi());
}


     for(std::vector<pat::Tau>::const_iterator ta=tau->begin(); ta!=tau->end(); ++ta){

    tEta->push_back(ta->eta());
    tPt->push_back(ta->pt());
    tPhi->push_back(ta->phi());
               }
               

      iEvent.put(Eta , "Eta");
      iEvent.put(mCharge , "mCharge");
      iEvent.put(mPt , "mPt");
      iEvent.put(mPhi , "mPhi");

      iEvent.put(tEta , "tEta");
    //  iEvent.put(Charge , "Charge");
      iEvent.put(tPt , "tPt");
      iEvent.put(tPhi , "tPhi");


}

void
MuonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------


void
MuonProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------


void
MuonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------


void
MuonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------


void
MuonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------


void
MuonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
 //  // Please change this to state exactly what you do use, even if it is no parameters


  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in


DEFINE_FWK_MODULE(MuonProducer);



                                                            

