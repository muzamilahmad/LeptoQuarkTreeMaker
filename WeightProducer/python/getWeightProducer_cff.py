# $Id: getWeightProducer_cff.py,v 1.7 2012/11/05 14:58:14 mschrode Exp $
#
# Returns a WeightProducer module that knows at runtime
# which data sample is produced and thus, what weights
# are required. The function can be used as follows:
#
#    from RA2Classic.WeightProducer.getWeightProducer_cff import getWeightProducer
#    process.WeightProducer = getWeightProducer(process.source.fileNames[0])

import FWCore.ParameterSet.Config as cms

class MCSample:
    def __init__(self, name, production, mcVersion, Method, XS, NumberEvts):
        self.name = name
        self.production = production
        self.mcVersion = mcVersion
        self.Method = Method
        self.XS = XS
        self.NumberEvts = NumberEvts

def getWeightProducer(fileName,fastsim=False, pmssm=False):

    applyWeight = False
    
    ## --- Setup default WeightProducer ------------------------------------
    
    # Import weightProducer
    from LeptoQuarkTreeMaker.WeightProducer.weightProducer_cfi import weightProducer
    
    # Set default values to produce an event weight of 1
    weightProducer.weight = cms.double(1.0)
    weightProducer.Method = cms.string("Constant")
    weightProducer.FileNamePUDataDistribution = cms.string("NONE")

    # assign cross sections for fastsim
    # assume privately-produced samples do not have mixed mass points
    if fastsim and "SusyRA2Analysis2015" not in fileName:
        weightProducer.weight = cms.double(-1.)
        weightProducer.Method = cms.string("FastSim")
        weightProducer.NumberEvts = cms.double(1.0)
        if pmssm: weightProducer.modelIdentifier = cms.InputTag("Pmssm:PmssmId")
        else: weightProducer.modelIdentifier = cms.InputTag("SusyScan:SusyMotherMass")
        if "SMS-T1" in fileName or "SMS-T5" in fileName: weightProducer.XsecFile = cms.string("LeptoQuarkTreeMaker/Production/test/data/dict_xsec_T1.txt")
        elif "SMS-T2tt" in fileName or "SMS-T2bb" in fileName: weightProducer.XsecFile = cms.string("LeptoQuarkTreeMaker/Production/test/data/dict_xsec_T2.txt")
        elif "SMS-T2qq" in fileName: weightProducer.XsecFile = cms.string("LeptoQuarkTreeMaker/Production/test/data/dict_xsec_T2qq.txt")
        elif "SMS-TChiHH" in fileName: weightProducer.XsecFile = cms.string("LeptoQuarkTreeMaker/Production/test/data/dict_xsec_TChiHH.txt")
        elif "pMSSM_MCMC1" in fileName: weightProducer.XsecFile = cms.string("LeptoQuarkTreeMaker/Production/test/data/pmssm-xsecs-scan1.txt")
        print "Setup WeightProducer for '"+fileName+"'"
        return weightProducer
    
    # list of samples
    samples = [
        # 13 TeV miniAODv2 samples - Summer16
        # backgrounds
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        # missing: TTJets inclusive
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 61973977), # subtotal = 11957043
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 61973977), # subtotal = 50016934
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 60210394), # subtotal = 11944041
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 60210394), # subtotal = 48266353
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 88.34, 30444678), # subtotal = 6094476
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 88.34, 30444678), # subtotal = 24350202
        MCSample("TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5.979, 17363624),
        # missing: TTJets_SingleLeptFromTbar_genMET-150
        MCSample("TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.666, 9890329),
        # HT jets: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.6562
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2.7343862, 14277035),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1.12075054, 10403610),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.1979159, 2932983),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.002368366, 1519815),
        # WJets: k-factor of 1.21 applied, extensions included
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1627.45, 29503700),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 435.24, 19766301), # subtotal = 4950373
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 435.24, 19766301), # subtotal = 14815928
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 59.18, 7759701), # subtotal = 1963464
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 59.18, 7759701), # subtotal = 5796237
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14.58, 18687480), # subtotal = 3779141
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14.58, 18687480), # subtotal = 14908339
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6.66, 7745467), # subtotal = 1544513
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6.66, 7745467), # subtotal = 6200954
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.608, 6872441), # subtotal = 244532
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1.608, 6872441), # subtotal = 6627909
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.03891, 2637821), # subtotal = 253561
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.03891, 2637821), # subtotal = 2384260
        MCSample("WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 61526.7, 29705748),
        # QCD: extensions included
        MCSample("QCD_HT50to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",1, 4097049),
        MCSample("QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2","Constant", 27540000, 80684349),
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1717000, 57580393), # subtotal = 18722416
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1717000, 57580393), # subtotal = 38857977
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 351300, 54537903), # subtotal = 17035891
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 351300, 54537903), # subtotal = 37502012
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 31630, 62271343), # subtotal = 18929951
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 31630, 62271343), # subtotal = 43341392
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6802, 45412780), # subtotal = 15629253
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6802, 45412780), # subtotal = 29783527
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1206, 15127293), # subtotal = 4767100
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1206, 15127293), # subtotal = 10360193
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 120.4, 11826702), # subtotal = 3970819
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 120.4, 11826702), # subtotal = 7855883
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 25.24, 6039005), # subtotal = 1991645
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 25.24, 6039005), # subtotal = 4047360
        # DY/Z: k-factor of 1.23 applied, available extensions included
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 181.302, 10607207), # subtotal = 2751187
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 181.302, 10607207), # subtotal = 7856020
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 50.4177, 9653731), # subtotal = 962195
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 50.4177, 9653731), # subtotal = 8691536
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6.98394, 10008776), # subtotal = 1070454
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6.98394, 10008776), # subtotal = 8938322
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 831.76, 10139950),
        MCSample("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 831.76,77081156),

        MCSample("TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 831.76, 43561608),
        MCSample("DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 1.68141, 8292957),
        MCSample("DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.775392, 2668730),
        MCSample("DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.186222, 596079),
        MCSample("DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.00438495, 399492),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 6025.2, 49144274),
        #MCSample("DYJetsToLL_Pt-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 18610.0, 40381391),
        MCSample("DYJetsToLL_Zpt-0To50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 349.7256,32734121),
        MCSample("DYJetsToLL_Pt-50to100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2",  "Constant", 349.7256, 108692157),


        MCSample("DYJetsToLL_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 83.12, 2950812),
        MCSample("DYJetsToLL_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 590806),
        MCSample("DYJetsToLL_Pt-400to650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 0.3921, 589842),
        MCSample("DYJetsToLL_Pt-650toInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 0.03636, 599665),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2",  "Constant", 5765.4, 122055388),

        MCSample("DYJetsToLL_Pt-50to100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2",  "Constant", 349.7256, 108692157),
        MCSample("DYJetsToLL_Pt-50to100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2",  "Constant", 349.7256, 108692157),

        MCSample("DYJetsToLL_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2",  "Constant", 83.12, 2950812),
        MCSample("DYJetsToLL_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2",  "Constant", 83.12, 2950812),
        MCSample("DYJetsToLL_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext5-v1", "RunIISummer16MiniAODv2",  "Constant", 83.12, 2950812),

        MCSample("DYJetsToLL_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 590806),
        MCSample("DYJetsToLL_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 590806),
        MCSample("DYJetsToLL_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext5-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 590806),

        MCSample("DYJetsToLL_Pt-400to650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 0.3921, 589842),
        MCSample("DYJetsToLL_Pt-400to650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2",  "Constant", 0.3921, 589842),

        MCSample("DYJetsToLL_Pt-650toInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 0.03636, 599665),
        MCSample("DYJetsToLL_Pt-650toInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2",  "Constant", 0.03636, 599665),












        MCSample("WJetsToLNu_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 83.12,10089661),
        MCSample("WJetsToLNu_Pt-100to250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext4-v1", "RunIISummer16MiniAODv2",  "Constant", 83.12,99945850),
        MCSample("WJetsToLNu_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 1001250),
        MCSample("WJetsToLNu_Pt-250to400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext4-v1", "RunIISummer16MiniAODv2",  "Constant", 3.047, 10021205),
        MCSample("WJetsToLNu_Pt-400to600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 0.3921, 951713),
        MCSample("WJetsToLNu_Pt-600toInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8","PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant", 0.03636, 989482),

        MCSample("WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2",  "Constant",61256.7, 24120319),
        MCSample("WJetsToLNu_Wpt-0To50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2","Constant",630.6,99983076),
        MCSample("WJetsToLNu_Wpt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2","Constant",630.6,67082709),
        MCSample("WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 630.6, 10088599),
        MCSample("WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 22.1, 1000132),
        MCSample("WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 2.67, 988234),
        MCSample("WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2",  "Constant", 0.4168, 985127),



        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 344.8305, 24272858), # subtotal = 5246318
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 344.8305, 24272858), # subtotal = 19026540
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 95.5341, 24744916), # subtotal = 5132650
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 95.5341, 24744916), # subtotal = 19612266
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 13.1979, 9862869), # subtotal = 1020309
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 13.1979, 9862869), # subtotal = 8842560
        MCSample("ZJetsToNuNu_HT-600To800_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.14757, 5763506),
        MCSample("ZJetsToNuNu_HT-800To1200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.450908, 2170137),
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.3546459, 513471), # subtotal = 369514
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.3546459, 513471), # subtotal = 143957
        MCSample("ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.00854235, 405030),
        MCSample("GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 20790, 4858154),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9226, 10182407), # subtotal = 5131873
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 9226, 10182407), # subtotal = 5050534
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2300, 20387336), # subtotal = 10036487
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2300, 20387336), # subtotal = 10350849
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 277.4, 5060070), # subtotal = 2529729
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 277.4, 5060070), # subtotal = 2530341
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 93.38, 5080857), # subtotal = 2463946
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 93.38, 5080857), # subtotal = 2616911
        MCSample("GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5000, 14758163),
        MCSample("GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1079, 49572400),
        MCSample("GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 125.9, 11680386),
        MCSample("GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 43.36, 11639826),
        # single top: NoFullyHadronicDecays xsec scaled by BF for non-fully-hadronic (1-(1-3*0.108)^2
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.34, 622990), # straight total = 1000000
        MCSample("ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 136.02, 67240808),
        MCSample("ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 80.95, 38811017),
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 5425134
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 5425134
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 2726603
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 5372991
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 3256650
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 2715978
        # rare backgrounds
        MCSample("WWTo2L2Nu_13TeV-powheg", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 12.178, 1999000),
        MCSample("WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 12.7, 5077680),
        MCSample("WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.834, 502190),
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 49.997, 3223676), # straight total = 5176114
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 10.71, 14017474), # straight total = 24152376
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.058, 942046), # straight total = 1703772
        MCSample("ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 32.3, 1268806), # straight total = 2009042
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.22, 9688612), # straight total = 15345572
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 4.04, 18470622), # straight total = 30082038
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.2529, 927976), # straight total = 1992438
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.5297, 351164), # straight total = 749400
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3", "RunIISummer16MiniAODv2", "Constant", 0.2043, 2716249), # subtotal = 1112722, straight subtotal = 2160168
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 0.2043, 2716249), # subtotal = 1603527, straight subtotal = 3120397
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.4026, 430310), # straight total = 833298
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.697, 4777013), # subtotal = 1577833, straight subtotal = 4870911
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 3.697, 4777013), # subtotal = 3199180, straight subtotal = 9885348
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.009103, 104640), # straight total = 250000
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.1651, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.05565, 216366), # straight total = 246800
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.01398, 213197), # straight total = 249237
        # signal
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.325388, 142671),
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0141903, 142671),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0856418, 146849),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0141903, 105415),
        MCSample("SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.000981077, 51352),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.325388, 92094),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0252977, 51260),
        MCSample("SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.31169, 156847),
        MCSample("SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.51848, 397678),
        MCSample("SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0189612, 235029),
        MCSample("SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 36.3818, 949417),
        MCSample("SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 21.5949, 905836),
        MCSample("SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 21.5949, 899982),
        MCSample("SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249.409, 400314),
        MCSample("SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249.409, 291078),
        MCSample("SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.107045, 100070),
        MCSample("WW_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1","RunIISummer16MiniAODv2", "Constant", 118.7, 6987124),
        MCSample("WZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1","RunIISummer16MiniAODv2", "Constant", 45.01, 2995828),
        MCSample("ZZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1","RunIISummer16MiniAODv2", "Constant", 16.91, 998034),
        MCSample("LQToUE_M-200_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 60.6, 50000),
        MCSample("LQToUE_M-250_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 20.3, 50000),
        MCSample("LQToUE_M-300_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 8.04, 50000),
        MCSample("LQToUE_M-350_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 3.59, 50000),
        MCSample("LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 1.74, 50000),
        MCSample("LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.906, 49721),
        MCSample("LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.496, 50000),
        MCSample("LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.284, 50000),
        MCSample("LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.169, 50000),
        MCSample("LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.103, 49815),
        MCSample("LQToUE_M-700_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0648, 50000),
        MCSample("LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0416, 50000),
        MCSample("LQToUE_M-800_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0273, 50000),
        MCSample("LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0182, 48242),
        MCSample("LQToUE_M-900_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0123, 50000),
        MCSample("LQToUE_M-950_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00845, 49834),
        MCSample("LQToUE_M-1000_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00586, 49716),
        MCSample("LQToUE_M-1050_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00411, 49782),
        MCSample("LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00291, 50000),
        MCSample("LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00208, 49909),
        MCSample("LQToUE_M-1200_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00150, 50000),
        MCSample("LQToUE_M-1250_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00109, 49841),
        MCSample("LQToUE_M-1300_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000795, 50000),
        MCSample("LQToUE_M-1350_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000585, 49808),
        MCSample("LQToUE_M-1400_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000433, 49835),
        MCSample("LQToUE_M-1450_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000321, 50000),
        MCSample("LQToUE_M-1500_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000240, 50000),
        MCSample("LQToUE_M-1550_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000180, 50000),
        MCSample("LQToUE_M-1600_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000135, 50000),
        MCSample("LQToUE_M-1650_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000102, 50000),
        MCSample("LQToUE_M-1700_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000774, 50000),
        MCSample("LQToUE_M-1750_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000588, 49416),
        MCSample("LQToUE_M-1800_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000448, 50000),
        MCSample("LQToUE_M-1850_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000343, 50000),
        MCSample("LQToUE_M-1900_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000262, 49111),
        MCSample("LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00000201, 50000),
        MCSample("LQToUE_M-2000_BetaOne_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00000155, 49881),
        MCSample("LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 60.6, 49745),
        MCSample("LQToUE_ENuJJFilter_M-250_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 20.3, 49183),
        MCSample("LQToUE_ENuJJFilter_M-300_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 8.04, 49889),
        MCSample("LQToUE_ENuJJFilter_M-350_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 3.59, 50009),
        MCSample("LQToUE_ENuJJFilter_M-400_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 1.74, 49578),
        MCSample("LQToUE_ENuJJFilter_M-450_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.906, 50244),
        MCSample("LQToUE_ENuJJFilter_M-500_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.496, 49908),
        MCSample("LQToUE_ENuJJFilter_M-550_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.284, 49850),
        MCSample("LQToUE_ENuJJFilter_M-600_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.169, 49793),
        MCSample("LQToUE_ENuJJFilter_M-650_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.103, 50059),
        MCSample("LQToUE_ENuJJFilter_M-700_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0648, 49876),
        MCSample("LQToUE_ENuJJFilter_M-750_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0416, 49865),
        MCSample("LQToUE_ENuJJFilter_M-800_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0273, 50059),
        MCSample("LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0182, 50003),
        MCSample("LQToUE_ENuJJFilter_M-900_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0123, 50099),
        MCSample("LQToUE_ENuJJFilter_M-950_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00845, 49556),
        MCSample("LQToUE_ENuJJFilter_M-1000_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00586, 49574),
        MCSample("LQToUE_ENuJJFilter_M-1050_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00411, 50222),
        MCSample("LQToUE_ENuJJFilter_M-1100_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00291, 49579),
        MCSample("LQToUE_ENuJJFilter_M-1150_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00208, 49369),
        MCSample("LQToUE_ENuJJFilter_M-1200_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00150, 50229),
        MCSample("LQToUE_ENuJJFilter_M-1250_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00109, 50017),
        MCSample("LQToUE_ENuJJFilter_M-1300_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000795, 49807),
        MCSample("LQToUE_ENuJJFilter_M-1350_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000585, 49806),
        MCSample("LQToUE_ENuJJFilter_M-1400_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000433, 49315),
        MCSample("LQToUE_ENuJJFilter_M-1450_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000321, 48988),
        MCSample("LQToUE_ENuJJFilter_M-1500_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000240, 49730),
        MCSample("LQToUE_ENuJJFilter_M-1550_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000180, 48783),
        MCSample("LQToUE_ENuJJFilter_M-1600_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000135, 49900),
        MCSample("LQToUE_ENuJJFilter_M-1650_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.000102, 49891),
        MCSample("LQToUE_ENuJJFilter_M-1700_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000774, 48730),
        MCSample("LQToUE_ENuJJFilter_M-1750_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000588, 49619),
        MCSample("LQToUE_ENuJJFilter_M-1800_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000448, 49694),
        MCSample("LQToUE_ENuJJFilter_M-1850_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000343, 48965),
        MCSample("LQToUE_ENuJJFilter_M-1900_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.0000262, 50003),
        MCSample("LQToUE_ENuJJFilter_M-1950_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00000201, 49843),
        MCSample("LQToUE_ENuJJFilter_M-2000_BetaHalf_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1","RunIISummer16MiniAODv2", "Constant", 0.00000155, 49284),


        MCSample("QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 557600000, 9218954),
        MCSample("QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2","Constant", 136000000, 6768384),
        MCSample("QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2","Constant", 19800000, 23474171),
        MCSample("QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2","Constant", 2800000, 41853504),
        MCSample("QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2","Constant", 477000, 41954035),
        MCSample("QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2","Constant", 114000, 11540163),
        MCSample("QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2","Constant", 9000, 7373633),


        MCSample("DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00615134, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-1200_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00159844, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-1200_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00159844, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-1200_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00159844, 89836),
        MCSample("DisplacedSUSY_StopToBL_M-1200_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00159844, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",64.5085, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-200_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",64.5085, 88848),
        MCSample("DisplacedSUSY_StopToBL_M-200_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",64.5085, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-200_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",64.5085, 89056),
        MCSample("DisplacedSUSY_StopToBL_M-300_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",8.51615, 88821),
        MCSample("DisplacedSUSY_StopToBL_M-300_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",8.51615, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-300_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",8.51615, 89692),
        MCSample("DisplacedSUSY_StopToBL_M-300_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",8.51615, 88779),
        MCSample("DisplacedSUSY_StopToBL_M-400_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",1.83537, 89798),
        MCSample("DisplacedSUSY_StopToBL_M-400_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",1.83537, 88752),
        MCSample("DisplacedSUSY_StopToBL_M-400_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",1.83537, 89875),
        MCSample("DisplacedSUSY_StopToBL_M-400_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",1.83537, 89568),
        MCSample("DisplacedSUSY_StopToBL_M-500_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.51848, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-500_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.51848, 89451),
        MCSample("DisplacedSUSY_StopToBL_M-500_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.51848, 88630),
        MCSample("DisplacedSUSY_StopToBL_M-500_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.51848, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-600_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.174599, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.174599, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-600_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.174599, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-600_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.174599, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-700_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0670476, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-700_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0670476, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-700_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0670476, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-700_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0670476, 89614),
        MCSample("DisplacedSUSY_StopToBL_M-800_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0283338, 89730),
        MCSample("DisplacedSUSY_StopToBL_M-800_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0283338, 89809),
        MCSample("DisplacedSUSY_StopToBL_M-800_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0283338, 89494),
        MCSample("DisplacedSUSY_StopToBL_M-800_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0283338, 89780),
        MCSample("DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0128895, 89719),
        MCSample("DisplacedSUSY_StopToBL_M-900_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0128895, 88936),
        MCSample("DisplacedSUSY_StopToBL_M-900_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0128895, 89637),
        MCSample("DisplacedSUSY_StopToBL_M-900_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.0128895, 89878),
        MCSample("DisplacedSUSY_StopToBL_M-1000_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00615134, 89771),
        MCSample("DisplacedSUSY_StopToBL_M-1000_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00615134, 89724),
        MCSample("DisplacedSUSY_StopToBL_M-1000_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00615134, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-1100_CTau-1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00307413, 89742),
        MCSample("DisplacedSUSY_StopToBL_M-1100_CTau-100_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00307413, 88992),
        MCSample("DisplacedSUSY_StopToBL_M-1100_CTau-10_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00307413, 90000),
        MCSample("DisplacedSUSY_StopToBL_M-1100_CTau-1_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant",0.00307413, 89863),





    ]
    
    # loop over all samples until we find a match
    for sample in samples:
        if sample.name in fileName and sample.production in fileName:
            weightProducer.Method     = cms.string(sample.Method)
            weightProducer.XS         = cms.double(sample.XS)
            weightProducer.NumberEvts = cms.double(sample.NumberEvts)
            print sample.name+", "+sample.production+" : '"+fileName+"'"
            applyWeight = True
            weightProducer.weight = cms.double(-1.)
            break
	
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer
