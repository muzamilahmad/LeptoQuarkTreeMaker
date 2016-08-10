#include <memory>
#include "DataFormats/MuonReco/interface/MuonCocktails.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/MuonReco/interface/MuonPFIsolation.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include <iostream>
#include <DataFormats/TrackReco/interface/Track.h>
#include "TLorentzVector.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "TVector2.h"


class MuonProducer : public edm::EDProducer {

 public:
      explicit MuonProducer(const edm::ParameterSet&);
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


  const unsigned int    maxSize=10;
  const double          muonIso=0.05 ;
  const bool            beamSpotCorr=true ;
  const bool            useCocktailRefits=true;
  const std::string muonID = "GlobalMuonPromptTight";
//edm::InputTag vtxInputToken_;
 // edm::InputTag beamSpotToken_;
  edm::EDGetTokenT<std::vector<pat::Muon> > muonInputToken_;
  edm::EDGetTokenT<reco::VertexCollection> vtxInputToken_;
  edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;


};


MuonProducer::MuonProducer(const edm::ParameterSet& iConfig):

 muonInputToken_ (consumes<std::vector<pat::Muon> >(iConfig.getParameter<edm::InputTag>("muontag"))),
     vtxInputToken_ (consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("VertexInputTag"))),
     beamSpotToken_ (consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("BeamSpotInputTag")))



{
  //  muontag_  = iConfig.getParameter<edm::InputTag>( "muontag" );
 //   tautag_  = iConfig.getParameter<edm::InputTag>( "tautag" );

 /* maxSize  =iConfig.getParameter<unsigned int> ("MaxSize"),

  muonIso = iConfig.getParameter<double>       ("MuonIso"),

  muonID   =iConfig.getParameter<std::string>  ("MuonID"),
  beamSpotCorr      =iConfig.getParameter<bool>("BeamSpotCorr"),
  useCocktailRefits =iConfig.getParameter<bool>("UseCocktailRefits"),
 
     muonInputToken_ (consumes<std::vector<pat::Muon> >(iConfig.getParameter<edm::InputTag>("muontag"))),
     vtxInputToken_ (consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("VertexInputTag"))),
     beamSpotToken_ (consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("BeamSpotInputTag")))


   // vtxInputToken_ =iConfig.getParameter<edm::InputTag>("VertexInputTag");
   // beamSpotToken_ =iConfig.getParameter<edm::InputTag>("BeamSpotInputTag");
*/

/*    produces<std::vector<double>>( "Eta" );
produces<std::vector<double>>( "mPt");
    produces<std::vector<double>>( "mPhi");
    produces<std::vector<int>>( "mCharge");

    produces<std::vector<double>>( "tEta" );
    produces<std::vector<double>>( "tPt");
    produces<std::vector<double>>( "tPhi");
*/

  produces <std::vector<bool> >   (  "MuonisLooseMuon"             );
  produces <std::vector<bool> >   (  "MuonisMediumMuon"            );
  produces <std::vector<bool> >   (  "MuonisTightMuon"             );
  produces <std::vector<bool> >   (  "MuonisHighPtMuon"            );
  produces <std::vector<double> > (  "MuonEta"                     );
  produces <std::vector<double> > (  "MuonPhi"                     );
  produces <std::vector<double> > (  "MuonPt"                      );
  produces <std::vector<double> > (  "MuonEtaError"                );
  produces <std::vector<double> > (  "MuonPhiError"                );
  produces <std::vector<double> > (  "MuonPtError"                 );
  produces <std::vector<double> > (  "MuonTrkEta"                  );
  produces <std::vector<double> > (  "MuonTrkPhi"                  );
  produces <std::vector<double> > (  "MuonTrkPt"                   );
  produces <std::vector<double> > (  "MuonTrkEtaError"             );
  produces <std::vector<double> > (  "MuonTrkPhiError"             );
  produces <std::vector<double> > (  "MuonTrkPtError"              );
  produces <std::vector<double> > (  "MuonQOverPError"             );
  produces <std::vector<double> > (  "MuonP"                       );
  produces <std::vector<double> > (  "MuonEnergy"                  );
  produces <std::vector<int> >    (  "MuonCharge"                  );
  produces <std::vector<int> >    (  "MuonTrkHits"                 );
  produces <std::vector<int> >    (  "MuonTrkHitsTrackerOnly"      );
  produces <std::vector<int> >    (  "MuonGlobalTrkValidHits"      );
  produces <std::vector<int> >    (  "MuonPixelHits"               );
  produces <std::vector<int> >    (  "MuonTrkPixelHits"            );
  produces <std::vector<int> >    (  "MuonSegmentMatches"          );
  produces <std::vector<int> >    (  "MuonStationMatches"          );
  produces <std::vector<double> > (  "MuonTrkValidFractionOfHits"  );
  produces <std::vector<double> > (  "MuonTrkD0"                   );
  produces <std::vector<double> > (  "MuonTrkD0Error"              );
  produces <std::vector<double> > (  "MuonTrkDz"                   );
  produces <std::vector<double> > (  "MuonTrkDzError"              );
  produces <std::vector<double> > (  "MuonTrkVx"                   );
  produces <std::vector<double> > (  "MuonTrkVy"                   );
  produces <std::vector<double> > (  "MuonTrkVz"                   );
  produces <std::vector<double> > (  "MuonTrackChi2"               );
  produces <std::vector<double> > (  "MuonGlobalChi2"              );
  produces <std::vector<double> > (  "MuonTrkIso"                  );
  produces <std::vector<double> > (  "MuonTrackerIsoSumPT"         );
  produces <std::vector<double> > (  "MuonEcalIso"                 );
  produces <std::vector<double> > (  "MuonHcalIso"                 );
  produces <std::vector<double> > (  "MuonHOIso"                   );
  produces <std::vector<double> > (  "MuonEcalVetoIso"             );
  produces <std::vector<double> > (  "MuonHcalVetoIso"             );
  produces <std::vector<double> > (  "MuonPFIsoR03ChargedHadron"   );
  produces <std::vector<double> > (  "MuonPFIsoR03ChargedParticle" );
  produces <std::vector<double> > (  "MuonPFIsoR03NeutralHadron"   );
  produces <std::vector<double> > (  "MuonPFIsoR03Photon"          );
  produces <std::vector<double> > (  "MuonPFIsoR03NeutralHadronHT" );
  produces <std::vector<double> > (  "MuonPFIsoR03PhotonHT"        );
  produces <std::vector<double> > (  "MuonPFIsoR03PU"              );
  produces <std::vector<double> > (  "MuonPFIsoR04ChargedHadron"   );
  produces <std::vector<double> > (  "MuonPFIsoR04ChargedParticle" );
  produces <std::vector<double> > (  "MuonPFIsoR04NeutralHadron"   );
  produces <std::vector<double> > (  "MuonPFIsoR04Photon"          );
  produces <std::vector<double> > (  "MuonPFIsoR04NeutralHadronHT" );
  produces <std::vector<double> > (  "MuonPFIsoR04PhotonHT"        );
  produces <std::vector<double> > (  "MuonPFIsoR04PU"              );
  produces <std::vector<int> >    (  "MuonPassID"                  );
  produces <std::vector<int> >    (  "MuonVtxIndex"                );
  produces <std::vector<double> > (  "MuonVtxDistXY"               );
  produces <std::vector<double> > (  "MuonVtxDistZ"                );
  produces <std::vector<int> >    (  "MuonBestTrackVtxIndex"      );
  produces <std::vector<double> > (  "MuonBestTrackVtxDistXY"     );
  produces <std::vector<double> > (  "MuonBestTrackVtxDistZ"      );
  produces <std::vector<double> > (  "MuonPrimaryVertexDXY"        );
  produces <std::vector<double> > (  "MuonPrimaryVertexDXYError"   );
  produces <std::vector<double> > (  "MuonBeamSpotDXY"             );
  produces <std::vector<double> > (  "MuonBeamSpotDXYError"        );
  produces <std::vector<int> >    (  "MuonIsGlobal"                );
  produces <std::vector<int> >    (  "MuonIsTracker"               );
  produces <std::vector<double> > (  "MuonMatchedGenParticlePt"    );
  produces <std::vector<double> > (  "MuonMatchedGenParticleEta"   );
  produces <std::vector<double> > (  "MuonMatchedGenParticlePhi"   );
  
  produces <std::vector<int> >     (  "MuonIsPF"                       );
  produces <std::vector<int> >     (  "MuonTrackLayersWithMeasurement" );

  
  produces <std::vector<bool  > > (  "HLTSingleMuonMatched"      );
  produces <std::vector<double> > (  "HLTSingleMuonMatchPt"      );
  produces <std::vector<double> > (  "HLTSingleMuonMatchEta"     );
  produces <std::vector<double> > (  "HLTSingleMuonMatchPhi"     );

  produces <std::vector<bool  > > (  "HLTSingleIsoMuonMatched"   );
  produces <std::vector<double> > (  "HLTSingleIsoMuonMatchPt"   );
  produces <std::vector<double> > (  "HLTSingleIsoMuonMatchEta"  );
  produces <std::vector<double> > (  "HLTSingleIsoMuonMatchPhi"  );

  
  if ( useCocktailRefits )
    {
      produces <std::vector<int>    > (  "CocktailRefitID"                ) ;
      produces <std::vector<double> > (  "CocktailEta"                    ) ;
      produces <std::vector<double> > (  "CocktailPhi"                    ) ;
      produces <std::vector<double> > (  "CocktailPt"                     ) ;
      produces <std::vector<double> > (  "CocktailEtaError"               ) ;
      produces <std::vector<double> > (  "CocktailPhiError"               ) ;
      produces <std::vector<double> > (  "CocktailPtError"                ) ;
      produces <std::vector<double> > (  "CocktailQOverPError"            ) ;
      produces <std::vector<double> > (  "CocktailP"                      ) ;
      produces <std::vector<int   > > (  "CocktailCharge"                 ) ;
      produces <std::vector<int   > > (  "CocktailTrkHits"                ) ;
      produces <std::vector<double> > (  "CocktailTrkValidFractionOfHits" ) ;
      produces <std::vector<double> > (  "CocktailTrkD0"                  ) ;
      produces <std::vector<double> > (  "CocktailTrkD0Error"             ) ;
      produces <std::vector<double> > (  "CocktailTrkDz"                  ) ;
      produces <std::vector<double> > (  "CocktailTrkDzError"             ) ;
      produces <std::vector<double> > (  "CocktailGlobalChi2"             ) ;

      produces <std::vector<double> > (  "CocktailTrkVtxDXY"                 ) ;
      produces <std::vector<double> > (  "CocktailTrkVtxDZ"                  ) ;
      produces <std::vector<int> >    (  "CocktailTrkVtxIndex"               ) ;

    }

}


MuonProducer::~MuonProducer()
{}
void MuonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace reco;
    using namespace std;
  //  edm::Handle<std::vector<pat::Muon> > muon;
 //   edm::Handle<std::vector<pat::Tau> > tau;


 // edm::Handle<reco::VertexCollection> primaryVertices;
 // iEvent.getByLabel(vtxInputToken_,primaryVertices);

 // edm::Handle<reco::BeamSpot> beamSpot;
 // iEvent.getByLabel(beamSpotToken_,beamSpot);


  edm::Handle<std::vector<pat::Muon> > muon;
  iEvent.getByToken(muonInputToken_, muon);

  edm::Handle<reco::VertexCollection> primaryVertices;
  iEvent.getByToken(vtxInputToken_,primaryVertices);

  edm::Handle<reco::BeamSpot> beamSpot;
  iEvent.getByToken(beamSpotToken_,beamSpot);





 /*   std::auto_ptr<std::vector<double> >Eta(new std::vector<double>());
    std::auto_ptr<std::vector<double> > mPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > mPhi(new std::vector<double>());
    std::auto_ptr<std::vector<int> > mCharge(new std::vector<int>());

    std::auto_ptr<std::vector<double> >tEta(new std::vector<double>());
    std::auto_ptr<std::vector<double> > tPt(new std::vector<double>());
    std::auto_ptr<std::vector<double> > tPhi(new std::vector<double>());
*/

 std::auto_ptr<bool>                  hasVeryForwardPFMuon    ( new bool() );
  std::auto_ptr<std::vector<bool> >    isLooseMuon             ( new std::vector<bool>()    );
  std::auto_ptr<std::vector<bool> >    isMediumMuon            ( new std::vector<bool>()    );
  std::auto_ptr<std::vector<bool> >    isTightMuon             ( new std::vector<bool>()    );
  std::auto_ptr<std::vector<bool> >    isHighPtMuon            ( new std::vector<bool>()    );
  std::auto_ptr<std::vector<double> >  eta                     ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  phi                     ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pt                      ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  etaError                ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  phiError                ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ptError                 ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkEta                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPhi                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPt                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkEtaError             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPhiError             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkPtError              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  qoverpError             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  p                       ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  energy                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     charge                  ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkHits                 ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkHitsTrackerOnly      ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     GlobaltrkValidHits      ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     pixelHits               ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     trkPixelHits            ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     segmentMatches          ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     stationMatches          ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     Valid                   ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  trkValidFractionOfHits  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkD0                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkD0Error              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkDz                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkDzError              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVx                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVy                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkVz                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trackChi2               ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  globalChi2              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trkIso                  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  trackerIsoSumPT         ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ecalIso                 ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hcalIso                 ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hoIso                   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ecalVetoIso             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  hcalVetoIso             ( new std::vector<double>()  );
  
  std::auto_ptr<std::vector<double> >  pfisor03chargedhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03chargedparticle ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03neutralhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03photon          ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03neutralhadronht ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03photonht        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor03pu              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04chargedhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04chargedparticle ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04neutralhadron   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04photon          ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04neutralhadronht ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04photonht        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  pfisor04pu              ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     passID                  ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     vtxIndex                ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  vtxDistXY               ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  vtxDistZ                ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     bestTrackVtxIndex       ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  bestTrackVtxDistXY      ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  bestTrackVtxDistZ       ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  primaryVertexDXY        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  primaryVertexDXYError   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  beamspotDXY             ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  beamspotDXYError        ( new std::vector<double>()  );
  std::auto_ptr<std::vector<int> >     IsGlobal                ( new std::vector<int>()     );
  std::auto_ptr<std::vector<int> >     IsTracker               ( new std::vector<int>()     );
  std::auto_ptr<std::vector<double> >  matchedgenparticlept    ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  matchedgenparticleeta   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  matchedgenparticlephi   ( new std::vector<double>()  );
  
  
  std::auto_ptr<std::vector<int> >     isPF                       ( new std::vector<int>()    );
  std::auto_ptr<std::vector<int> >     trackLayersWithMeasurement ( new std::vector<int>()    );
  
  std::auto_ptr<std::vector<bool  > >  HLTSingleMuonMatched     ( new std::vector<bool  >()  );
  std::auto_ptr<std::vector<double> >  HLTSingleMuonMatchPt     ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  HLTSingleMuonMatchEta    ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  HLTSingleMuonMatchPhi    ( new std::vector<double>()  );
  std::auto_ptr<std::vector<bool  > >  HLTSingleIsoMuonMatched  ( new std::vector<bool  >()  );
  std::auto_ptr<std::vector<double> >  HLTSingleIsoMuonMatchPt  ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  HLTSingleIsoMuonMatchEta ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  HLTSingleIsoMuonMatchPhi ( new std::vector<double>()  );
  
  std::auto_ptr<std::vector<int   > >  ctRefitID    ( new std::vector<int   > () );
  std::auto_ptr<std::vector<double> >  ctEta        ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctPhi        ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctPt         ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctEtaError   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ctPhiError   ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ctPtError    ( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ctQoverpError( new std::vector<double>()  );
  std::auto_ptr<std::vector<double> >  ctP          ( new std::vector<double> () );
  std::auto_ptr<std::vector<int   > >  ctCharge     ( new std::vector<int   > () );
  std::auto_ptr<std::vector<int   > >  ctTrkHits    ( new std::vector<int   > () );
  std::auto_ptr<std::vector<double> >  ctTrkValidFractionOfHits ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctTrkD0      ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctTrkD0Error ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctTrkDz      ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctTrkDzError ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctGlobalChi2 ( new std::vector<double> () );

  std::auto_ptr<std::vector<double> >  ctTrkvtxDistXY      ( new std::vector<double> () );
  std::auto_ptr<std::vector<double> >  ctTrkvtxDistZ      ( new std::vector<double> () );
  std::auto_ptr<std::vector<int> >  ctTrkvtxIndex      ( new std::vector<int> () );



//iEvent.getByLabel( muontag_, muon );
//iEvent.getByLabel( tautag_, tau );

if(muon.isValid())
    {
      edm::LogInfo("RootTupleMakerV2_MuonsInfo") << "Total # Muons: " << muon->size();

      

    for(std::vector<pat::Muon>::const_iterator it=muon->begin(); it!=muon->end(); ++it){


if( !it->isGlobalMuon() && !it->isTrackerMuon() ) continue;
	  if( it->pt()<5 ) continue;
          double genparPt = -999.;
	  double genparEta= -999.;
	  double genparPhi= -999.;

	  if ( !iEvent.isRealData() ){
 for(uint igen = 0 ; igen < it->genParticleRefs().size() ; ++igen )
	      {
		if(it->genParticleRef(igen).isNonnull()) {
                   if( it->genParticle(igen)->status()==1 || it->genParticle(igen)->status()==3 || it->genParticle(igen)->status()==23){
		    genparPt =it->genParticle(igen)->pt();
		    genparEta=it->genParticle(igen)->eta();
		    genparPhi=it->genParticle(igen)->phi();
		  }
		}

	      }
	  }
	  matchedgenparticlept     -> push_back ( (double)(genparPt) );
	  matchedgenparticleeta    -> push_back ( (double)(genparEta) );
	  matchedgenparticlephi    -> push_back ( (double)(genparPhi) );

          double trkd0   = it->track()->d0();

	  if( beamSpotCorr && beamSpot.isValid() )
	    {
	      trkd0   = -(it->track()   ->dxy( beamSpot->position()));
	    }

 double minVtxDist3D = 9999.;
	  int    vtxIndex_    = -1;
	  double vtxDistXY_   = -9999.;
	  double vtxDistZ_    = -9999.;
 double bt_minVtxDist3D = 9999.;
	  int    bt_vtxIndex_    = -1;
	  double bt_vtxDistXY_   = -9999.;
	  double bt_vtxDistZ_    = -9999.;

	  if(primaryVertices.isValid())
	    {	 
     for( reco::VertexCollection::const_iterator v_it=primaryVertices->begin() ; v_it!=primaryVertices->end() ; ++v_it )
		{
		  
 double distXY = it->track()->dxy(v_it->position());
		  double distZ  = it->track()->dz(v_it->position());
		  double dist3D = sqrt(pow(distXY,2) + pow(distZ,2));
		  if( dist3D < minVtxDist3D )
		    {
		      minVtxDist3D = dist3D;
		      vtxIndex_    = int(std::distance(primaryVertices->begin(),v_it));
		      vtxDistXY_   = distXY;
		      vtxDistZ_    = distZ;
		    }
                   if( (it->muonBestTrack()).isNonnull() )
		    {
		      double bt_distXY = it->muonBestTrack()->dxy(v_it->position());
		      double bt_distZ  = it->muonBestTrack()->dz(v_it->position());
		      double bt_dist3D = sqrt( pow(bt_distXY,2) + pow(bt_distZ,2) );
		      if( bt_dist3D < bt_minVtxDist3D )
			{
			  bt_minVtxDist3D = bt_dist3D;
			  bt_vtxIndex_    = int(std::distance(primaryVertices->begin(),v_it));
			  bt_vtxDistXY_   = bt_distXY;
			  bt_vtxDistZ_    = bt_distZ;
			}
		    }

		}				 //loop over primaryVertices

   }

         const pat::TriggerObjectStandAloneCollection matchesSingleMu = it->triggerObjectMatchesByPath("HLT_Mu45_eta2p1_v*");
	  if (matchesSingleMu.size() > 0)
	    {
	      HLTSingleMuonMatched  -> push_back ( true ) ;
	      HLTSingleMuonMatchPt  -> push_back ( matchesSingleMu[0].pt() );
	      HLTSingleMuonMatchEta -> push_back ( matchesSingleMu[0].eta());
	      HLTSingleMuonMatchPhi -> push_back ( matchesSingleMu[0].phi());
	    }
	  else
	    {
	      HLTSingleMuonMatched  -> push_back ( false ) ;
	      HLTSingleMuonMatchPt  -> push_back ( -999. );
	      HLTSingleMuonMatchEta -> push_back ( -999. );
	      HLTSingleMuonMatchPhi -> push_back ( -999. );
	    }
            const pat::TriggerObjectStandAloneCollection matchesSingleIsoMu = it->triggerObjectMatchesByPath("HLT_IsoMu27_v*");
	  if (matchesSingleIsoMu.size() > 0)
	    {
	      HLTSingleIsoMuonMatched  -> push_back ( true ) ;
	      HLTSingleIsoMuonMatchPt  -> push_back ( matchesSingleIsoMu[0].pt() );
	      HLTSingleIsoMuonMatchEta -> push_back ( matchesSingleIsoMu[0].eta());
	      HLTSingleIsoMuonMatchPhi -> push_back ( matchesSingleIsoMu[0].phi());
	    }
	  else
	    {
	      HLTSingleIsoMuonMatched  -> push_back ( false ) ;
	      HLTSingleIsoMuonMatchPt  -> push_back ( -999. );
	      HLTSingleIsoMuonMatchEta -> push_back ( -999. );
	      HLTSingleIsoMuonMatchPhi -> push_back ( -999. );
	    }


	  reco::VertexCollection::const_iterator v_it_muId=primaryVertices->begin();
	  isLooseMuon->push_back(  it->isLooseMuon()  );
	  isMediumMuon->push_back( it->isMediumMuon() );
	  isTightMuon->push_back(  it->isTightMuon(*v_it_muId)  );
	  isHighPtMuon->push_back( it->isHighPtMuon(*v_it_muId) );

	  eta->push_back( it->eta() );
	  phi->push_back( it->phi() );
	  pt ->push_back( it->pt()  );
	  p  ->push_back( it->p()   );

	  if( it->isGlobalMuon() )
	    {
	      etaError    -> push_back ( it->globalTrack()->etaError()    );
	      phiError    -> push_back ( it->globalTrack()->phiError()    );
	      ptError     -> push_back ( it->globalTrack()->ptError ()    );
	      qoverpError -> push_back ( it->globalTrack()->qoverpError() );
	    }
	  else
	    {
	      etaError    -> push_back ( it->track()->etaError()    );
	      //track() returns innerTrack();
	      phiError    -> push_back ( it->track()->phiError()    );
	      //	      	      //track() returns innerTrack();
	      ptError     -> push_back ( it->track()->ptError ()    );
	      qoverpError -> push_back ( it->track()->qoverpError() );
	    }

	  trkPt  -> push_back ( it->track()->pt()  );
	  trkEta -> push_back ( it->track()->eta() );
	  trkPhi -> push_back ( it->track()->phi() );

	  trkPtError  -> push_back ( it->track()->ptError()  );
	  trkEtaError -> push_back ( it->track()->etaError() );
	  trkPhiError -> push_back ( it->track()->phiError() );

	  charge            ->push_back( it->charge() );
	   trkHits           ->push_back( it->track()->hitPattern().numberOfValidHits() );
	  trkHitsTrackerOnly->push_back( it->track()->hitPattern().numberOfValidTrackerHits() );

	  if( it->isGlobalMuon() )
	    {
	      GlobaltrkValidHits->push_back( it->globalTrack()->hitPattern().numberOfValidMuonHits()  );
	      pixelHits         ->push_back( it->globalTrack()->hitPattern().numberOfValidPixelHits() );
	      globalChi2        ->push_back( it->globalTrack()->normalizedChi2()                      );
	    }
	  else
	    {
	      GlobaltrkValidHits->push_back( -1 );
	      pixelHits         ->push_back( -1 );



	      globalChi2        ->push_back( -1 );
	    }

	  trkPixelHits->push_back(it->track()->hitPattern().numberOfValidPixelHits());

	  segmentMatches  ->push_back(it->numberOfMatches());
	  stationMatches  ->push_back(it->numberOfMatchedStations());

	  trkValidFractionOfHits->push_back( it->track()->validFraction() );

	  trkD0     ->push_back( trkd0                         );
	  trkD0Error->push_back( it->track()->d0Error()        );
	  trkDz     ->push_back( it->track()->dz()             );
	  trkDzError->push_back( it->track()->dzError()        );
	  trkVx     ->push_back( it->track()->vx()             );
	  trkVy     ->push_back( it->track()->vy()             );
	  trkVz     ->push_back( it->track()->vz()             );
	  trackChi2 ->push_back( it->track()->normalizedChi2() );



	  if ( useCocktailRefits )
	    {
	      if ( it->isGlobalMuon())	
		{
		  int refit_id = -999;
		
		  reco::TrackRef cocktail_track = it->tunePMuonBestTrack();

		  double cttrkd0  = cocktail_track -> d0() ;
		  if( beamSpotCorr && beamSpot.isValid() )
		    cttrkd0 = -(cocktail_track->dxy( beamSpot->position()));
				
		  ctRefitID     -> push_back ( refit_id ) ;
				
		  ctEtaError    -> push_back ( cocktail_track->etaError()    );
		  ctPhiError    -> push_back ( cocktail_track->phiError()    );
		  ctPtError     -> push_back ( cocktail_track->ptError ()    );
		  ctQoverpError -> push_back ( cocktail_track->qoverpError() );
				
		  ctEta                    ->push_back( cocktail_track->eta()    );
		  ctPhi                    ->push_back( cocktail_track->phi()    );
		  ctPt                     ->push_back( cocktail_track->pt()     );
		  ctP                      ->push_back( cocktail_track->p()      );
		  ctCharge                 ->push_back( cocktail_track->charge() );
		  ctTrkHits                ->push_back( cocktail_track->hitPattern().numberOfValidTrackerHits() );
		  ctTrkValidFractionOfHits ->push_back( cocktail_track->validFraction()   );
		  ctTrkD0                  ->push_back( cttrkd0                           );
		  ctTrkD0Error             ->push_back( cocktail_track->d0Error()         );
		  ctTrkDz                  ->push_back( cocktail_track->dz()              );
		  ctTrkDzError             ->push_back( cocktail_track -> dzError()       );
		  ctGlobalChi2            ->push_back( cocktail_track ->normalizedChi2() );
                  int    bct_vtxIndex_    = -1;
		  double bct_vtxDistXY_   = -9999.;
		  double bct_vtxDistZ_    = -9999.;
				  if(primaryVertices.isValid())
		    {
		      double bct_bestdist3D = 999999.;
				    
		      for( reco::VertexCollection::const_iterator v_it=primaryVertices->begin() ; v_it!=primaryVertices->end() ; ++v_it )
			{
			  double bct_distXY = cocktail_track->dxy(v_it->position());
			  double bct_distZ  = cocktail_track->dz(v_it->position());
			  double bct_dist3D = sqrt( pow(bct_distXY,2) + pow(bct_distZ,2) );
					
			  if( bct_dist3D < bct_bestdist3D )
			    {
			      bct_bestdist3D = bct_dist3D;
			      bct_vtxIndex_    = int(std::distance(primaryVertices->begin(),v_it));
			      bct_vtxDistXY_   = bct_distXY;
			      bct_vtxDistZ_    = bct_distZ;
			    }
					}				 //loop over primaryVertices
		    }
				
				
		  ctTrkvtxDistXY           ->push_back( bct_vtxDistXY_ );
		  ctTrkvtxDistZ            ->push_back( bct_vtxDistZ_ );
		  ctTrkvtxIndex            ->push_back( bct_vtxIndex_ );
				
                          }

	      else	
		{
		  ctRefitID     -> push_back ( -99 ) ;
		  ctEtaError    -> push_back ( -99 );
		  ctPhiError    -> push_back ( -99 );
		  ctPtError     -> push_back ( -99 );
		  ctQoverpError -> push_back ( -99 );
		  ctEta                    ->push_back( -99 );
		  ctPhi                    ->push_back( -99 );
		  ctPt                     ->push_back( -99 );
		  ctP                      ->push_back( -99 );
		  ctCharge                 ->push_back( -99 );
		  ctTrkHits                ->push_back( -99 );
		  ctTrkValidFractionOfHits ->push_back( -99 );
		  ctTrkD0                  ->push_back( -99 );
		  ctTrkD0Error             ->push_back( -99 );
		  ctTrkDz                  ->push_back( -99 );
		  ctTrkDzError             ->push_back( -99 );
		  ctGlobalChi2             ->push_back( -99 );
				
		  ctTrkvtxDistXY           ->push_back( -99 );
		  ctTrkvtxDistZ            ->push_back( -99 );					
		  ctTrkvtxIndex            ->push_back( -99 );
		}
			    
			    
	    }					 
			
	  isPF                       ->push_back( it->isPFMuon()       );
	  trackLayersWithMeasurement ->push_back( it->track()->hitPattern().trackerLayersWithMeasurement() );
			
	  energy->push_back( it->energy() );
	  trkIso         ->push_back( it->trackIso()           );
	  trackerIsoSumPT->push_back( it->isolationR03().sumPt );
	  ecalIso        ->push_back( it->isolationR03().emEt  );
	  hcalIso        ->push_back( it->isolationR03().hadEt );
	  hoIso          ->push_back( it->isolationR03().hoEt  );
	  
	  ecalVetoIso    ->push_back( it->isolationR03().emVetoEt  );
	  hcalVetoIso    ->push_back( it->isolationR03().hadVetoEt );
	 pfisor03chargedhadron  ->push_back( it->pfIsolationR03().sumChargedHadronPt              );
	  pfisor03chargedparticle->push_back( it->pfIsolationR03().sumChargedParticlePt            );
	  pfisor03neutralhadron  ->push_back( it->pfIsolationR03().sumNeutralHadronEt              );
	  pfisor03photon         ->push_back( it->pfIsolationR03().sumPhotonEt                     );
	  pfisor03neutralhadronht->push_back( it->pfIsolationR03().sumNeutralHadronEtHighThreshold );
	  pfisor03photonht       ->push_back( it->pfIsolationR03().sumPhotonEtHighThreshold        );
	  pfisor03pu             ->push_back( it->pfIsolationR03().sumPUPt                         );
	  pfisor04chargedhadron  ->push_back( it->pfIsolationR04().sumChargedHadronPt              );
	  pfisor04chargedparticle->push_back( it->pfIsolationR04().sumChargedParticlePt            );
	  pfisor04neutralhadron  ->push_back( it->pfIsolationR04().sumNeutralHadronEt              );
	  pfisor04photon         ->push_back( it->pfIsolationR04().sumPhotonEt                     );
	  pfisor04neutralhadronht->push_back( it->pfIsolationR04().sumNeutralHadronEtHighThreshold );
	  pfisor04photonht       ->push_back( it->pfIsolationR04().sumPhotonEtHighThreshold        );
	  pfisor04pu             ->push_back( it->pfIsolationR04().sumPUPt                         );

	  passID                 ->push_back( (it->muonID(muonID)) ?  1 : 0 );
	  IsGlobal               ->push_back( (it->isGlobalMuon()) ?  1 : 0 );
	  IsTracker              ->push_back( (it->isTrackerMuon()) ? 1 : 0 );
	  vtxIndex               ->push_back( vtxIndex_                     );
	  vtxDistXY              ->push_back( vtxDistXY_                    );
	  vtxDistZ               ->push_back( vtxDistZ_                     );
	  bestTrackVtxIndex      ->push_back( bt_vtxIndex_                  );
	  bestTrackVtxDistXY     ->push_back( bt_vtxDistXY_                 );
	  bestTrackVtxDistZ      ->push_back( bt_vtxDistZ_                  );
	  primaryVertexDXY       ->push_back( it->dB()                      );
	  primaryVertexDXYError  ->push_back( it->edB()                     );
	  beamspotDXY            ->push_back( it->dB(pat::Muon::BS2D)       );
	  beamspotDXYError       ->push_back( it->edB(pat::Muon::BS2D)      );
  

   }//end of loop over muons

}//for loop

  else
    {
      edm::LogError("RootTupleMakerV2_MuonsError") << "Error! Can't get the muons";
    }

/*
      iEvent.put(Eta , "Eta");
      iEvent.put(mCharge , "mCharge");
      iEvent.put(mPt , "mPt");
      iEvent.put(mPhi , "mPhi");

      iEvent.put(tEta , "tEta");
      iEvent.put(tPt , "tPt");
      iEvent.put(tPhi , "tPhi");
*/

  iEvent.put( isLooseMuon,                 "MuonisLooseMuon"                );
  iEvent.put( isMediumMuon,                "MuonisMediumMuon"               );
  iEvent.put( isTightMuon,                 "MuonisTightMuon"                );
  iEvent.put( isHighPtMuon,                "MuonisHighPtMuon"               );
  iEvent.put( eta,                         "MuonEta"                        );
  iEvent.put( phi,                         "MuonPhi"                        );
  iEvent.put( pt,                          "MuonPt"                         );
  iEvent.put( etaError,                    "MuonEtaError"                   );
  iEvent.put( phiError,                    "MuonPhiError"                   );
  iEvent.put( ptError,                     "MuonPtError"                    );
  iEvent.put( trkEta,                      "MuonTrkEta"                     );
  iEvent.put( trkPhi,                      "MuonTrkPhi"                     );
  iEvent.put( trkPt,                       "MuonTrkPt"                      );
  iEvent.put( trkEtaError,                 "MuonTrkEtaError"                );
  iEvent.put( trkPhiError,                 "MuonTrkPhiError"                );
  iEvent.put( trkPtError,                  "MuonTrkPtError"                 );
  iEvent.put( qoverpError,                 "MuonQOverPError"                );
  iEvent.put( p,                           "MuonP"                          );
  iEvent.put( energy,                      "MuonEnergy"                     );
  iEvent.put( charge,                      "MuonCharge"                     );
  iEvent.put( trkHits,                     "MuonTrkHits"                    );
  iEvent.put( trkHitsTrackerOnly,          "MuonTrkHitsTrackerOnly"         );
  iEvent.put( GlobaltrkValidHits,          "MuonGlobalTrkValidHits"         );
  iEvent.put( pixelHits,                   "MuonPixelHits"                  );
  iEvent.put( trkPixelHits,                "MuonTrkPixelHits"               );
  iEvent.put( segmentMatches,              "MuonSegmentMatches"             );
  iEvent.put( stationMatches,              "MuonStationMatches"             );
  iEvent.put( trkValidFractionOfHits,      "MuonTrkValidFractionOfHits"     );
  iEvent.put( trkD0,                       "MuonTrkD0"                      );
  iEvent.put( trkD0Error,                  "MuonTrkD0Error"                 );
  iEvent.put( trkDz,                       "MuonTrkDz"                      );
  iEvent.put( trkDzError,                  "MuonTrkDzError"                 );
  iEvent.put( trkVx,                       "MuonTrkVx"                      );
  iEvent.put( trkVy,                       "MuonTrkVy"                      );
  iEvent.put( trkVz,                       "MuonTrkVz"                      );
  iEvent.put( trackChi2,                   "MuonTrackChi2"                  );
  iEvent.put( globalChi2,                  "MuonGlobalChi2"                 );
  iEvent.put( trkIso,                      "MuonTrkIso"                     );
  iEvent.put( trackerIsoSumPT,             "MuonTrackerIsoSumPT"            );
  iEvent.put( ecalIso,                     "MuonEcalIso"                    );
  iEvent.put( hcalIso,                     "MuonHcalIso"                    );
  iEvent.put( hoIso,                       "MuonHOIso"                      );
  iEvent.put( ecalVetoIso,                 "MuonEcalVetoIso"                );
  iEvent.put( hcalVetoIso,                 "MuonHcalVetoIso"                );
  iEvent.put( pfisor03chargedhadron,       "MuonPFIsoR03ChargedHadron"      );
  iEvent.put( pfisor03chargedparticle,     "MuonPFIsoR03ChargedParticle"    );
  iEvent.put( pfisor03neutralhadron,       "MuonPFIsoR03NeutralHadron"      );
  iEvent.put( pfisor03photon,              "MuonPFIsoR03Photon"             );
  iEvent.put( pfisor03neutralhadronht,     "MuonPFIsoR03NeutralHadronHT"    );
  iEvent.put( pfisor03photonht,            "MuonPFIsoR03PhotonHT"           );
  iEvent.put( pfisor03pu,                  "MuonPFIsoR03PU"                 );
  iEvent.put( pfisor04chargedhadron,       "MuonPFIsoR04ChargedHadron"      );
  iEvent.put( pfisor04chargedparticle,     "MuonPFIsoR04ChargedParticle"    );
  iEvent.put( pfisor04neutralhadron,       "MuonPFIsoR04NeutralHadron"      );
  iEvent.put( pfisor04photon,              "MuonPFIsoR04Photon"             );
  iEvent.put( pfisor04neutralhadronht,     "MuonPFIsoR04NeutralHadronHT"    );
  iEvent.put( pfisor04photonht,            "MuonPFIsoR04PhotonHT"           );
  iEvent.put( pfisor04pu,                  "MuonPFIsoR04PU"                 );
  iEvent.put( passID,                      "MuonPassID"                     );
  iEvent.put( IsGlobal,                    "MuonIsGlobal"                   );
  iEvent.put( IsTracker,                   "MuonIsTracker"                  );
  iEvent.put( vtxIndex,                    "MuonVtxIndex"                   );
  iEvent.put( vtxDistXY,                   "MuonVtxDistXY"                  );
  iEvent.put( vtxDistZ,                    "MuonVtxDistZ"                   );
  iEvent.put( bestTrackVtxIndex,           "MuonBestTrackVtxIndex"          );
  iEvent.put( bestTrackVtxDistXY,          "MuonBestTrackVtxDistXY"         );
  iEvent.put( bestTrackVtxDistZ,           "MuonBestTrackVtxDistZ"          );
  iEvent.put( primaryVertexDXY,            "MuonPrimaryVertexDXY"           );
  iEvent.put( primaryVertexDXYError,       "MuonPrimaryVertexDXYError"      );
  iEvent.put( beamspotDXY,                 "MuonBeamSpotDXY"                );
  iEvent.put( beamspotDXYError,            "MuonBeamSpotDXYError"           );
  iEvent.put( matchedgenparticlept,        "MuonMatchedGenParticlePt"       );
  iEvent.put( matchedgenparticleeta,       "MuonMatchedGenParticleEta"      );
  iEvent.put( matchedgenparticlephi,       "MuonMatchedGenParticlePhi"      );
  iEvent.put( isPF,                        "MuonIsPF"                       );
  iEvent.put( trackLayersWithMeasurement,  "MuonTrackLayersWithMeasurement" );
  

  if ( useCocktailRefits )
    {
      iEvent.put( ctRefitID                ,  "CocktailRefitID"                ) ;
      iEvent.put( ctEta                    ,  "CocktailEta"                    ) ;
      iEvent.put( ctPhi                    ,  "CocktailPhi"                    ) ;
      iEvent.put( ctPt                     ,  "CocktailPt"                     ) ;
      iEvent.put( ctEtaError               ,  "CocktailEtaError"               ) ;
      iEvent.put( ctPhiError               ,  "CocktailPhiError"               ) ;
      iEvent.put( ctPtError                ,  "CocktailPtError"                ) ;
      iEvent.put( ctQoverpError            ,  "CocktailQOverPError"            ) ;
      iEvent.put( ctP                      ,  "CocktailP"                      ) ;
      iEvent.put( ctCharge                 ,  "CocktailCharge"                 ) ;
      iEvent.put( ctTrkHits                ,  "CocktailTrkHits"                ) ;
      iEvent.put( ctTrkValidFractionOfHits ,  "CocktailTrkValidFractionOfHits" ) ;
      iEvent.put( ctTrkD0                  ,  "CocktailTrkD0"                  ) ;
      iEvent.put( ctTrkD0Error             ,  "CocktailTrkD0Error"             ) ;
      iEvent.put( ctTrkDz                  ,  "CocktailTrkDz"                  ) ;
      iEvent.put( ctTrkDzError             ,  "CocktailTrkDzError"             ) ;
      iEvent.put( ctGlobalChi2             ,  "CocktailGlobalChi2"             ) ;

      iEvent.put( ctTrkvtxDistXY           ,  "CocktailTrkVtxDXY"              ) ;
      iEvent.put( ctTrkvtxDistZ            ,  "CocktailTrkVtxDZ"               ) ;
      iEvent.put( ctTrkvtxIndex            ,  "CocktailTrkVtxIndex"               ) ;


    }

  iEvent.put( HLTSingleMuonMatched     , "HLTSingleMuonMatched"       );
  iEvent.put( HLTSingleMuonMatchPt     , "HLTSingleMuonMatchPt"       );
  iEvent.put( HLTSingleMuonMatchEta    , "HLTSingleMuonMatchEta"      );
  iEvent.put( HLTSingleMuonMatchPhi    , "HLTSingleMuonMatchPhi"      );
  iEvent.put( HLTSingleIsoMuonMatched  , "HLTSingleIsoMuonMatched"    );
  iEvent.put( HLTSingleIsoMuonMatchPt  , "HLTSingleIsoMuonMatchPt"    );
  iEvent.put( HLTSingleIsoMuonMatchEta , "HLTSingleIsoMuonMatchEta"   );
  iEvent.put( HLTSingleIsoMuonMatchPhi , "HLTSingleIsoMuonMatchPhi"   );


}
void
MuonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
//
//
void
MuonProducer::endJob() {
}



void
MuonProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}



void
MuonProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}



void
MuonProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}



void
MuonProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

void
MuonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {


  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}



DEFINE_FWK_MODULE(MuonProducer);





