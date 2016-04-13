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

};


MuonProducer::MuonProducer(const edm::ParameterSet& iConfig)
{
    muontag_  = iConfig.getParameter<edm::InputTag>( "muontag" );
    produces<std::vector<double>>( "Eta" );
 //   produces<std::vector<double>>( "Et" );
    produces<std::vector<double>>( "mPt");
    produces<std::vector<double>>( "mPhi");
   

}


MuonProducer::~MuonProducer()
{}



void MuonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace reco;
    using namespace std;
    edm::Handle<std::vector<pat::Muon> > muon;


    std::auto_ptr<std::vector<double> >Eta(new std::vector<double>());
   // std::auto_ptr<std::vector<double> > Et(new std::vector<double>());
    std::auto_ptr<std::vector<double> > mPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > mPhi(new std::vector<double>());
    



iEvent.getByLabel( muontag_, muon );

    for(std::vector<pat::Muon>::const_iterator mu=muon->begin(); mu!=muon->end(); ++mu){

     Eta->push_back(mu->eta());
 //    Et->push_back(mu->et());
     mPt->push_back(mu->pt());
     mPhi->push_back(mu->phi());
}

      iEvent.put(Eta , "Eta");
//      iEvent.put(Et , "Et");
      iEvent.put(mPt , "mPt");
      iEvent.put(mPhi , "mPhi");



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



                                                            

