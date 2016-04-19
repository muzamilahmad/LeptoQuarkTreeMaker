//Stores useful HEEP ID and Isolation Variables
//        [Notes on implementation]
//        */
//        //
//        // Original Author:  Muzamil Ahmad Bhat
//        //         Created:  Thu, 17 Sep 2015 06:55:01 GMT
//                   Updated by Bibhuprasad Mahakud
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
class HEEPProducer : public edm::EDProducer {
   public:
      explicit HEEPProducer(const edm::ParameterSet&);
  //    ~TrackAndPointsProducer()
         ~HEEPProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;


      virtual void beginRun(edm::Run&, edm::EventSetup const&);
      virtual void endRun(edm::Run&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

    edm::InputTag eletag_;
    //edm::InputTag rhotag_;
    edm::InputTag vtxtag_;
    //edm::InputTag srcJet_;
};


HEEPProducer::HEEPProducer(const edm::ParameterSet& iConfig)
{ 
    eletag_  = iConfig.getParameter<edm::InputTag>( "eletag" );
    vtxtag_  = iConfig.getParameter<edm::InputTag>( "vtxtag" );
    produces<std::vector<double>>( "Eta" );
    //produces<std::vector<double>>( "Phi" );
    produces<std::vector<double>>( "Et" );
    //produces<std::vector<double>>( "Eta" );
    produces<std::vector<bool>>( "ecalDriven" );
    produces<std::vector<double>>( "DeltaEtain" );
    produces<std::vector<double>>( "DeltaPhiin" );
    produces<std::vector<double>>( "HbE" );
    produces<std::vector<double>>( "SiEtaiEta" );
    produces<std::vector<double>>( "Ecaliso" );
    produces<std::vector<double>>( "HD1iso" );
    produces<std::vector<double>>( "HD2iso" );
    produces<std::vector<double>>( "trackiso" );
    produces<std::vector<double>>( "e25max");
    produces<std::vector<double>>( "e55");
    produces<std::vector<double>>( "e25bye55");
    produces<std::vector<double>>( "DeltaEtaSeed");
    produces<std::vector<double>>( "rho");
    produces<std::vector<int>>( "Charge");
    produces<std::vector<double>>( "ePt");
    produces<std::vector<double>>( "e15");
    produces<std::vector<double>>( "ecalEnergy");
    produces<std::vector<double>>( "full55SiEtaiEta");
    produces<std::vector<double>>( "sce25max");
    produces<std::vector<double>>( "sce55");
    produces<std::vector<double>>( "sce25bye55");
    produces<std::vector<double>>( "e15bye55");
    produces<std::vector<double>>( "DeltaEtaSeedscandTrack");
    produces<std::vector<double>>( "Phi");
    produces<std::vector<double>>( "eEnergy");
    produces<std::vector<double>>( "dxy");
    produces<std::vector<int>>( "losthits");
    produces<std::vector<double>>( "ePz");
    produces<std::vector<double>>( "eTheta");
    produces<std::vector<double>>( "ePx");
    produces<std::vector<double>>( "ePy");
    produces<std::vector<double>>( "normalizedChi2");
   //produces< std::vector< TLorentzVector > >("genParticle");
    produces< std::vector< int > >("PDGID");
    produces< std::vector< int > >("gencharge");
    produces< std::vector< double > >("genPt");
    produces< std::vector< double > >("genEta");
    produces< std::vector< double > >("genPhi");
    produces< std::vector< double > >("genEnergy");
    produces<std::vector<double>>( "PtHEEP");
    produces<std::vector<double>>( "scEta" );


    /*
    produces< std::vector< int > >("refpdgid");
    produces< std::vector< double > >("refe");
    produces< std::vector< double > >("refpt");
    produces< std::vector< double > >("refeta");
    produces< std::vector< double > >("refphi");
   */
 
    produces< std::vector< int > >("motherPDGID");
    produces< std::vector< int > >("elstatus");
    /* produces< std::vector< double > >("refm");
    produces< std::vector< double > >("refy");
    produces< std::vector< double > >(" refarea");
    produces< std::vector< double > >("refdrjt");
    produces<std::vector<bool>>( "isMatched");

   */

}


HEEPProducer::~HEEPProducer()
{}



void HEEPProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm; 
    using namespace reco; 
    using namespace std;
   //  using namespace pat;
    edm::Handle<std::vector<pat::Electron> > electron;


    edm::Handle< double > rho_;
    iEvent.getByLabel("fixedGridRhoFastjetAll", rho_);
    double rh = *rho_;


    edm::Handle<std::vector<reco::Vertex> > vtxh;
    iEvent.getByLabel( vtxtag_, vtxh );
    const reco::Vertex vtx  = vtxh->at(0);




    std::auto_ptr<std::vector<double> >Eta(new std::vector<double>());
    // std::auto_ptr<std::vector<double> > Phi(new std::vector<double>());
    std::auto_ptr<std::vector<double> > Et(new std::vector<double>());
    std::auto_ptr<std::vector<bool> > ecalDriven(new std::vector<bool>());
    std::auto_ptr<std::vector<double> > DeltaEtain(new std::vector<double>());
    std::auto_ptr<std::vector<double> > DeltaPhiin(new std::vector<double>());
    std::auto_ptr<std::vector<double> > HbE(new std::vector<double>());
    std::auto_ptr<std::vector<double> > SiEtaiEta(new std::vector<double>());
    std::auto_ptr<std::vector<double> >Ecaliso(new std::vector<double>());
    std::auto_ptr<std::vector<double> > HD1iso(new std::vector<double>());
    std::auto_ptr<std::vector<double> > HD2iso(new std::vector<double>());
    std::auto_ptr<std::vector<double> > trackiso(new std::vector<double>());
    std::auto_ptr<std::vector<double> > e25max(new std::vector<double>());
    std::auto_ptr<std::vector<double> > e55(new std::vector<double>());
    std::auto_ptr<std::vector<double> > e25bye55(new std::vector<double>());
    std::auto_ptr<std::vector<double> > DeltaEtaSeed(new std::vector<double>());
    std::auto_ptr<std::vector<double > > rho(new std::vector<double>());
    std::auto_ptr<std::vector<int > > Charge(new std::vector<int>());
    std::auto_ptr<std::vector<double > > ePt(new std::vector<double>());
    std::auto_ptr<std::vector<double > >e15 (new std::vector<double>());
    std::auto_ptr<std::vector<double > > ecalEnergy(new std::vector<double>());
    std::auto_ptr<std::vector<double > > full55SiEtaiEta(new std::vector<double>());
    std::auto_ptr<std::vector<double > > sce25max(new std::vector<double>());
    std::auto_ptr<std::vector<double > > sce55(new std::vector<double>());
    std::auto_ptr<std::vector<double > > sce25bye55(new std::vector<double>());
    std::auto_ptr<std::vector<double > >e15bye55 (new std::vector<double>());
    std::auto_ptr<std::vector<double > >DeltaEtaSeedscandTrack (new std::vector<double>());
    std::auto_ptr<std::vector<double > >Phi (new std::vector<double>());
    std::auto_ptr<std::vector<double > >eEnergy (new std::vector<double>());
    std::auto_ptr<std::vector<double > >dxy (new std::vector<double>());
    std::auto_ptr<std::vector<int > >losthits (new std::vector<int>());
    std::auto_ptr<std::vector<double > >ePz (new std::vector<double>());
    std::auto_ptr<std::vector<double > >eTheta (new std::vector<double>());
    std::auto_ptr<std::vector<double > >ePx (new std::vector<double>());
    std::auto_ptr<std::vector<double > >ePy (new std::vector<double>());
    std::auto_ptr<std::vector<double > >normalizedChi2 (new std::vector<double>());
    //std::auto_ptr<std::vector<double > >Phi (new std::vector<double>());
    //std::auto_ptr< std::vector< TLorentzVector > > genParticle( new std::vector< TLorentzVector > () );
    std::auto_ptr<std::vector<double > > PtHEEP(new std::vector<double>());
    std::auto_ptr<std::vector<double> > scEta(new std::vector<double>());
   

     
    std::auto_ptr< std::vector< int > > PDGID( new std::vector< int > () );
    std::auto_ptr< std::vector< int > >gencharge( new std::vector< int > () );
    std::auto_ptr<std::vector<double > >genPt (new std::vector<double>());
    std::auto_ptr<std::vector<double > >genEta (new std::vector<double>());
    std::auto_ptr<std::vector<double > >genPhi (new std::vector<double>());
    std::auto_ptr<std::vector<double > >genEnergy (new std::vector<double>());
    std::auto_ptr< std::vector< int > > motherPDGID( new std::vector< int > () );
    std::auto_ptr< std::vector< int > > elstatus( new std::vector< int > () );
    

    /*
    std::auto_ptr<std::vector<double > >refpt (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refeta (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refphi (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refe (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refm (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refy (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refarea (new std::vector<double>());
    std::auto_ptr<std::vector<double > >refdrjt (new std::vector<double>());
    std::auto_ptr<std::vector<bool> > isMatched(new std::vector<bool>());
    std::auto_ptr< std::vector< int > > refpdgid( new std::vector< int > () );
    */


    iEvent.getByLabel( eletag_, electron );

    for(std::vector<pat::Electron>::const_iterator elect=electron->begin(); elect!=electron->end(); ++elect){

if(elect->pt() > 0.0){//pt cut

     Eta->push_back(elect->eta());
     //Phi->push_back(elect->phi());
     Et->push_back(elect->caloEnergy()*sin(elect->p4().theta()));
     ecalDriven->push_back(elect->ecalDrivenSeed());
     DeltaEtain->push_back(elect->deltaEtaSuperClusterTrackAtVtx());
     DeltaPhiin->push_back(elect->deltaPhiSuperClusterTrackAtVtx());
     HbE->push_back(elect->hadronicOverEm());
     SiEtaiEta->push_back(elect->scSigmaIEtaIEta());

     Ecaliso->push_back(elect->dr03EcalRecHitSumEt());
     HD1iso->push_back(elect->dr03HcalDepth1TowerSumEt());
     HD2iso->push_back(elect->dr03HcalDepth2TowerSumEt());
     trackiso->push_back(elect->dr03TkSumPt());
     e25max->push_back(elect->e2x5Max());
     e55->push_back(elect->e5x5());
     e25bye55->push_back((elect->e2x5Max())/(elect->e5x5()));
     DeltaEtaSeed->push_back(elect->deltaEtaSuperClusterTrackAtVtx()-elect->superCluster()->eta() + elect->superCluster()->seed()->eta());  
     Charge->push_back(elect->charge());
     ePt->push_back(elect->pt());
     e15->push_back(elect->e1x5());
     ecalEnergy->push_back(elect->ecalEnergy());
     full55SiEtaiEta->push_back(elect->full5x5_sigmaIetaIeta());
     sce25max->push_back(elect->scE2x5Max());
     sce55->push_back(elect->scE5x5());
     sce25bye55->push_back(elect->scE2x5Max()/elect->scE5x5());
     e15bye55->push_back((elect->e1x5())/(elect->e5x5()));
     DeltaEtaSeedscandTrack->push_back(elect->deltaEtaSeedClusterTrackAtVtx());
     Phi->push_back(elect->phi());
     eEnergy->push_back(elect->energy());
     dxy->push_back(elect->gsfTrack()->dxy(vtx.position()));
     
     constexpr reco::HitPattern::HitCategory missingHitType = reco::HitPattern::MISSING_INNER_HITS;
     losthits->push_back(elect->gsfTrack()->hitPattern().numberOfHits(missingHitType));

    //losthits->push_back(elect->gsfTrack()->numberOfLostHits());
     ePz->push_back(elect->pz());
     eTheta->push_back(elect->theta());
     ePx->push_back(elect->px());
     ePy->push_back(elect->py());
     normalizedChi2->push_back(elect->gsfTrack()->normalizedChi2());
     PtHEEP-> push_back(elect->caloEnergy()*sin(elect->p4().theta()) );
     scEta->push_back( elect->superCluster()->energy()/cosh(elect->superCluster()->eta()) );
}//pt cut
}

     rho->push_back(rh);  




    
    edm::Handle< View<reco::GenParticle> > genParticles;
    iEvent.getByLabel( "prunedGenParticles" ,genParticles);
 
if(genParticles.isValid()) {//gen level stuff

     for(View<reco::GenParticle>::const_iterator iPart = genParticles->begin();
         iPart != genParticles->end();
         ++iPart){
   

    //for(size_t i = 0; i < genParticles->size(); ++ i) {
    //   const GenParticle & iPart = *genParticles->at(i);
    //  const GenParticle & iPart = (*genParticles)[i];
    if( fabs(iPart->pdgId()) == 11){// && iPart->status() == 1 ){
      
    //std::cout<<"Status is given as:        "<<iPart->status()<<"                  motherPDGID ====        "<<mom->pdgId()<<std::endl;
    const Candidate * mom = iPart->mother();
    //std::cout<<"Status is given as:        "<<iPart->status()<<"                  motherPDGID ====        "<<mom->pdgId()<<std::endl;
    elstatus->push_back(iPart->status());
    PDGID->push_back( iPart->pdgId() );
    gencharge->push_back( iPart->charge() );
    genPt->push_back(iPart->pt());
    genEta->push_back(iPart->eta());
    genPhi->push_back(iPart->phi());
    genEnergy->push_back(iPart->energy());
    motherPDGID->push_back(mom->pdgId());
    //motherPDGID->push_back(iPart->mother()->pdgId());
    }
    }
}//gen level stuff
    


    //edm::Handle<std::vector<pat::Jet> >  jets;
    /*
    edm::Handle< edm::View<pat::Jet> > jets;
    iEvent.getByLabel(srcJet_, jets);
    //iEvent.getByToken(srcGenJet_, genjets);
    //loop over the jets and fill the ntuple
    size_t nJet = jets->size();
    for (size_t iJet = 0; iJet < nJet; iJet++) {

    pat::Jet const & jet = jets->at(iJet);


  
    if(jet.pt() < 5)
         continue;

     const reco::GenJet* ref = jet.genJet();

     if (ref) {
       refdrjt->push_back( reco::deltaR(jet.eta(),jet.phi(),ref->eta(),ref->phi()) );
       isMatched->push_back(true);
     }
     else {
       refdrjt->push_back(0);
       isMatched->push_back(false);
     }

     //    refrank.push_back( nref );
     //  refpdgid_algorithmicDef.push_back( 0 );
     // refpdgid_physicsDef.push_back( 0 );
     if(ref) {
        refpdgid->push_back( ref->pdgId() );
        refe->push_back( ref->energy() );
        refpt->push_back( ref->pt() );
        refeta->push_back( ref->eta() );
        refphi->push_back( ref->phi() );
        refm->push_back( ref->mass() );
        refy->push_back( ref->rapidity() );
        refarea->push_back( ref->jetArea() );
     }
     else {
        refpdgid->push_back( 0. );
        refe->push_back( 0. );
        refpt->push_back( 0. );
        refeta->push_back( 0. );
        refphi->push_back( 0. );
        refm->push_back( 0. );
        refy->push_back( 0. );
        refarea->push_back( 0. );
     }



     }

     */




      iEvent.put(Eta , "Eta");
      iEvent.put(Et , "Et");
      //iEvent.put(eisEcalDriven , "isEcalDriven");
      iEvent.put(ecalDriven , "ecalDriven");
      iEvent.put(DeltaEtain , "DeltaEtain");
      iEvent.put(DeltaPhiin ,"DeltaPhiin");
      iEvent.put(HbE ,"HbE");
      iEvent.put(SiEtaiEta , "SiEtaiEta");
      iEvent.put(Ecaliso ,"Ecaliso");
      iEvent.put(HD1iso ,"HD1iso");
      iEvent.put(HD2iso , "HD2iso");
      iEvent.put(trackiso , "trackiso");
      iEvent.put(e25max , "e25max");
      iEvent.put(e55 , "e55");
      iEvent.put(e25bye55 , "e25bye55");
      iEvent.put(DeltaEtaSeed , "DeltaEtaSeed");
      iEvent.put(rho , "rho");
      iEvent.put(Charge , "Charge");
      iEvent.put(ePt , "ePt");
      iEvent.put(e15 , "e15");
      iEvent.put(ecalEnergy, "ecalEnergy");
      iEvent.put(full55SiEtaiEta , "full55SiEtaiEta");
      iEvent.put(sce25max , "sce25max");
      iEvent.put(sce55 , "sce55");
      iEvent.put(sce25bye55 , "sce25bye55");
      iEvent.put(e15bye55 ,"e15bye55");
      iEvent.put(DeltaEtaSeedscandTrack , "DeltaEtaSeedscandTrack");
      iEvent.put(Phi , "Phi");
      iEvent.put(eEnergy ,"eEnergy");
      //iEvent.put(ePz "ePz");
      iEvent.put(dxy , "dxy");
      iEvent.put(losthits ,"losthits");
      iEvent.put(ePz, "ePz");
      iEvent.put(eTheta ,"eTheta");
      iEvent.put(ePx ,"ePx");
      iEvent.put(ePy ,"ePy");
      iEvent.put(normalizedChi2, "normalizedChi2");
      //iEvent.put(genParticle, "genParticle");
      iEvent.put(PDGID , "PDGID" );
      iEvent.put(gencharge , "gencharge" );
      iEvent.put(genPt, "genPt");
      iEvent.put(genEta, "genEta");
      iEvent.put(genPhi, "genPhi");
      iEvent.put(genEnergy, "genEnergy");
      iEvent.put(motherPDGID, "motherPDGID");
      iEvent.put( elstatus, "elstatus");
      iEvent.put(PtHEEP, "PtHEEP");
      iEvent.put(scEta, "scEta");
      /*
      iEvent.put(refpdgid, "refpdgid");
      iEvent.put(  refe, "  refe");
      iEvent.put( refpt, " refpt");
      iEvent.put( refeta, " refeta");
      iEvent.put( refphi, " refphi");
      iEvent.put(refm, "refm");
      iEvent.put(refy, "refy");
      iEvent.put(refarea, "refarea");
      iEvent.put(refdrjt, "refdrjt");
      iEvent.put(motherPDGID, "motherPDGID");
      iEvent.put(isMatched, "isMatched");
      */





}

void
HEEPProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------


void
HEEPProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------


void
HEEPProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------


void
HEEPProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------


void
HEEPProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------


void
HEEPProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HEEPProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
 //The following says we do not know what parameters are allowed so do no validation
 //  // Please change this to state exactly what you do use, even if it is no parameters


  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in


DEFINE_FWK_MODULE(HEEPProducer);



