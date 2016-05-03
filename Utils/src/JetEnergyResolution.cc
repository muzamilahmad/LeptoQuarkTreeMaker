
//Calculates the Jet energy correction factors and then corrects the Jet pt accordingly
////        [Notes on implementation]
////        */
////        //JetEnergyResolution
////        //          Original Author:  Muzamil Ahmad Bhat
////        //          Created:  Thu, 26 April 2016 06:55:01 GMT

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include <Math/VectorUtil.h>
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "CondFormats/BTauObjects/interface/BTagCalibration.h"
#include "CondFormats/BTauObjects/interface/BTagCalibrationReader.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "TVector2.h"


#include "TFile.h"
#include "TTree.h"
#include "TMath.h"
#include <vector>

//using namespace pat;
using namespace edm;
using namespace reco;
using namespace std;

class JetEnergyResolution : public edm::EDProducer {
   public:
      explicit JetEnergyResolution(const edm::ParameterSet&);
  ~JetEnergyResolution();

   private:
   //   virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;



      double smear(double pt, double genpt, double eta, std::string syst);
      double resolSF(double eta, std::string syst);
      edm::InputTag jettag_;
       std::string syst;
      double energy, ptCorr,energyCorr,ptCorrup,energyCorrup,ptCorrdown,energyCorrdown,smearfact,pt,eta,genpt;
};


JetEnergyResolution::JetEnergyResolution(const edm::ParameterSet& iConfig)
{
    jettag_  = iConfig.getParameter<edm::InputTag>( "jettag" );
//std::cout<<"jettag_ is :    "<<jettag_<<std::endl;

    produces<std::vector<double>>( "JERPtCorr" );
    produces<std::vector<double>>( "JEREnergyCorr" );
    produces<std::vector<double>>( "JERPtCorrSysUP" );
    produces<std::vector<double>>( "JERPtCorrSysDown" );
    produces<std::vector<double>>( "JEREnergyCorrSysUP" );
    produces<std::vector<double>>( "JEREnergyCorrSysDown" );
    produces<std::vector<double>>( "JEREta");    
    produces<std::vector<double>>( "JERPhi");  

}

JetEnergyResolution::~JetEnergyResolution() {
}
void JetEnergyResolution::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
/*


  using namespace edm;
  using namespace reco;
  using namespace std;

*/
std::auto_ptr<std::vector<double > >JERPtCorr (new std::vector<double>());
std::auto_ptr<std::vector<double > >JEREnergyCorr (new std::vector<double>());
std::auto_ptr<std::vector<double > >JERPtCorrSysUP (new std::vector<double>());
std::auto_ptr<std::vector<double > >JERPtCorrSysDown (new std::vector<double>());
std::auto_ptr<std::vector<double > >JEREnergyCorrSysUP (new std::vector<double>());
std::auto_ptr<std::vector<double > >JEREnergyCorrSysDown (new std::vector<double>());
std::auto_ptr<std::vector<double > >JEREta (new std::vector<double>());
std::auto_ptr<std::vector<double > >JERPhi (new std::vector<double>());


edm::Handle< edm::View<pat::Jet> > jets;
iEvent.getByLabel(jettag_, jets);



for(edm::View<pat::Jet>::const_iterator jet=jets->begin(); jet!=jets->end(); ++jet){
    pt=jet->pt();
    eta=jet->eta();
    energy=jet->energy();
   const reco::GenJet* ref = jet->genJet();

    if (ref) {
       genpt = ref->pt();

//syst= "nominal";
     smearfact = smear(pt, genpt, eta, "nominal");
     ptCorr = pt * smearfact;
     energyCorr = energy * smearfact;
     JEREta->push_back(jet->eta());
     JERPhi->push_back(jet->phi());
     JERPtCorr->push_back(ptCorr);
     JEREnergyCorr->push_back(energyCorr);
//syst= "jer__up";
     smearfact = smear(pt, genpt, eta, "jer__up");
     ptCorrup = pt * smearfact;
     energyCorrup = energy * smearfact;
     JERPtCorrSysUP->push_back(ptCorrup);
     JEREnergyCorrSysUP->push_back(energyCorrup);
//syst= "jer__down";
     smearfact = smear(pt, genpt, eta,  "jer__down");
     ptCorrdown = pt * smearfact;
     energyCorrdown = energy * smearfact;

     JERPtCorrSysDown->push_back(ptCorrdown);
     JEREnergyCorrSysDown->push_back(energyCorrdown);
//std::cout<<ptCorr<<"        "<<pt<<"       "<<ptCorrup<<"                "<<ptCorrdown<<std::endl;
    }
}





iEvent.put(JERPtCorr, "JERPtCorr");
iEvent.put(JEREnergyCorr, "JEREnergyCorr");
iEvent.put(JERPtCorrSysUP, "JERPtCorrSysUP");
iEvent.put(JEREnergyCorrSysUP, "JEREnergyCorrSysUP");
iEvent.put(JERPtCorrSysDown, "JERPtCorrSysDown");
iEvent.put(JEREnergyCorrSysDown, "JEREnergyCorrSysDown");
iEvent.put(JEREta, "JEREta");
iEvent.put(JERPhi, "JERPhi");
}

void JetEnergyResolution::endJob() {
}

double JetEnergyResolution::smear(double pt, double genpt, double eta, std::string syst){
  double resolScale = resolSF(fabs(eta), syst);
  double smear =1.0;
  if(genpt>0) smear = std::max((double)(0.0), (double)(pt + (pt - genpt) * resolScale) / pt);
  return  smear;
}

double JetEnergyResolution::resolSF(double eta, std::string syst)
{
  double fac = 0.;
  if (syst == "nominal")fac = 0.;
  if (syst == "jer__up")fac = 1.;
  if (syst == "jer__down")fac = -1.;
  if (eta <= 0.8)                       return 1.061 + (0.023 * fac);
  else if ( eta > 0.8 && eta <= 1.3 )   return 1.088 + (0.029 * fac);
  else if ( eta > 1.3 && eta <= 1.9 )   return 1.106 + (0.030 * fac);
  else if ( eta > 1.9 && eta <= 2.5 )   return 1.126 + (0.094 * fac);
  else if ( eta > 2.5 && eta <= 3.0 )   return 1.343 + (0.123 * fac);
  else if ( eta > 3.0 && eta <= 3.2 )   return 1.303 + (0.111 * fac);
  else if ( eta > 3.2 && eta <= 5.0 )   return 1.320 + (0.286 * fac);
  return 0.1;
}


DEFINE_FWK_MODULE(JetEnergyResolution);

