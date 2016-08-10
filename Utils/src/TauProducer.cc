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
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "FWCore/Framework/interface/EDProducer.h"
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
class TauProducer : public edm::EDProducer {

 public:
      explicit TauProducer(const edm::ParameterSet&);
  //    ~TrackAndPointsProducer()
         ~TauProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;


      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);


 const edm::EDGetTokenT<std::vector<pat::Tau> > tauInputToken_;

};


TauProducer::TauProducer(const edm::ParameterSet& iConfig):
 tauInputToken_ (consumes<std::vector<pat::Tau> >(iConfig.getParameter<edm::InputTag>("tautag")))
{

   
    produces<std::vector<double>>( "tEta" );
    produces<std::vector<double>>( "tPt");
    produces<std::vector<double>>( "tPhi");


}


TauProducer::~TauProducer()
{}



void TauProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace reco;
    using namespace std;
  edm::Handle<std::vector<pat::Tau> > tau;
  iEvent.getByToken(tauInputToken_, tau);

    
    std::auto_ptr<std::vector<double> >tEta(new std::vector<double>());
    std::auto_ptr<std::vector<double> > tPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > tPhi(new std::vector<double>());


    for(std::vector<pat::Tau>::const_iterator ta=tau->begin(); ta!=tau->end(); ++ta){

    tEta->push_back(ta->eta());
    tPt->push_back(ta->pt());
    tPhi->push_back(ta->phi());
              
     }               


      iEvent.put(tEta , "tEta");
      iEvent.put(tPt , "tPt");
      iEvent.put(tPhi , "tPhi");


}

void
TauProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------


void
TauProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------


void
TauProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------


void
TauProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------


void
TauProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------


void
TauProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TauProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
 //  // Please change this to state exactly what you do use, even if it is no parameters


  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in


DEFINE_FWK_MODULE(TauProducer);



                                                            

