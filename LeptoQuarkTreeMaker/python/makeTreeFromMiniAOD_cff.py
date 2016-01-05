# $Id:things are being changed for LQ analysis 
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outfile,
#reportfreq=10,
dataset="",
globaltag="",
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False
):

    #process = cms.Process("RA2EventSelection")
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    process.GlobalTag.globaltag = globaltag    


    print "function starts running ...."
    # log output
    # log output
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = 1000
    process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
        wantSummary = cms.untracked.bool(True)
    )

    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
    )



    # files to process
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(dataset)
    )
    
    # output file

    process.TFileService = cms.Service("TFileService",
        fileName = cms.string(outfile+".root")
    )
    # branches for treemaker
    VectorRecoCand       = cms.vstring() 
    VarsDouble           = cms.vstring()
    VarsInt              = cms.vstring()
    VarsBool             = cms.vstring()
    VectorTLorentzVector = cms.vstring()
    VectorDouble         = cms.vstring()
    VectorString         = cms.vstring()
    VectorInt            = cms.vstring()
    VectorBool           = cms.vstring()
    
    # sequence for baseline producers
    process.Baseline = cms.Sequence()

    # configure treemaker
    
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.treeMaker import TreeMaker
    process.LQTreeMaker = TreeMaker.clone(
        TreeName             = cms.string("SimpleTree"),
        VectorRecoCand       = VectorRecoCand, 
        VarsDouble           = VarsDouble,
        VarsInt              = VarsInt,
        VarsBool             = VarsBool,
        VectorTLorentzVector = VectorTLorentzVector,
        VectorDouble         = VectorDouble,
        VectorInt            = VectorInt,
        VectorString         = VectorString,
        VectorBool           = VectorBool,
    )
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC    
    JetTag = cms.InputTag('slimmedJets')
    METTag = cms.InputTag('slimmedMETs')
    if len(jecfile)>0:
        #get name of JECs without any directories
        JECera = jecfile.split('/')[-1]
        JECPatch = cms.string('sqlite_file:'+jecfile+'.db')
        if os.getenv('GC_CONF'):
            JECPatch = cms.string('sqlite_file:../src/'+jecfile+'.db')

        process.load("CondCore.DBCommon.CondDBCommon_cfi")
        from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
        process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
            connect = JECPatch,
            toGet   = cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PFchs"),
                    label  = cms.untracked.string("AK4PFchs")
                ),
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK4PF"),
                    label  = cms.untracked.string("AK4PF")
                )
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
    
        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
        process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
            src     = cms.InputTag("slimmedJets"),
            levels  = ['L1FastJet',
                      'L2Relative',
                      'L3Absolute'],
            payload = 'AK4PFchs' # Make sure to choose the appropriate levels and payload here!
        )
        if residual: process.patJetCorrFactorsReapplyJEC.levels.append('L2L3Residual')

        from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
        process.patJetsReapplyJEC = patJetsUpdated.clone(
            jetSource = cms.InputTag("slimmedJets"),
            jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
        )

        process.Baseline += process.patJetCorrFactorsReapplyJEC
        process.Baseline += process.patJetsReapplyJEC

        JetTag = cms.InputTag('patJetsReapplyJEC')

        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
            jetCollUnskimmed=JetTag.value(),
            jetColl=JetTag.value(),
            postfix="Update"
        )
        if not residual: #skip residuals for data if not used
            process.patPFMetT1T2CorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT1T2SmearCorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2CorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.patPFMetT2SmearCorrUpdate.jetCorrLabelRes = cms.InputTag("L3Absolute")
            process.shiftedPatJetEnDownUpdate.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
            process.shiftedPatJetEnUpUpdate.jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3Corrector")
        if hasattr(process,"slimmedMETsUpdate"):
            delattr(getattr(process,"slimmedMETsUpdate"),"caloMET")
        METTag = cms.InputTag('slimmedMETsUpdate','',process.name_())



    from LeptoQuarkTreeMaker.Utils.HEEPProducer_cfi import HEEPProducer
    process.HEEPProducer = HEEPProducer.clone(
        eletag = cms.InputTag('slimmedElectrons')
   # rhotag = cms.InputTag('fixedGridRhoFastjetAll')
    )
    process.Baseline += process.HEEPProducer
    VectorDouble.extend(['HEEPProducer:trackiso(Electron_trackiso)'])
    VectorDouble.extend(['HEEPProducer:Eta(Electron_Eta)'])
    VectorDouble.extend(['HEEPProducer:Et(Electron_Et)'])
    VectorDouble.extend(['HEEPProducer:DeltaEtain(Electron_DeltaEtain)'])
    VectorDouble.extend(['HEEPProducer:DeltaPhiin(Electron_DeltaPhiin)'])
    VectorDouble.extend(['HEEPProducer:HbE(Electron_HOverE)'])
    VectorDouble.extend(['HEEPProducer:SiEtaiEta(Electron_SiEtaiEta)'])
    VectorDouble.extend(['HEEPProducer:Ecaliso(Electron_Ecaliso)'])
    VectorDouble.extend(['HEEPProducer:HD1iso(Electron_HD1iso)'])
    VectorDouble.extend(['HEEPProducer:HD2iso(Electron_HD2iso)'])
    VectorBool.extend(['HEEPProducer:ecalDriven(Electron_ecalDriven)'])
    VectorDouble.extend(['HEEPProducer:e25max(Electron_e25max)'])
    VectorDouble.extend(['HEEPProducer:e55(Electron_e55)'])
    VectorDouble.extend(['HEEPProducer:e25bye55(Electron_e25bye55)'])
    VectorDouble.extend(['HEEPProducer:DeltaEtaSeed(Electron_DeltaEtaSeed)'])
    VectorDouble.extend(['HEEPProducer:rho(rho)'])
    VectorInt.extend(['HEEPProducer:Charge(Electron_Charge)'])
    VectorDouble.extend(['HEEPProducer:ePt(Electron_Pt)'])
    VectorDouble.extend(['HEEPProducer:e15(Electron_e15)'])
    VectorDouble.extend(['HEEPProducer:ecalEnergy(Electron_ecalEnergy)'])
    VectorDouble.extend(['HEEPProducer:full55SiEtaiEta(Electron_full55SiEtaiEta)'])
    VectorDouble.extend(['HEEPProducer:sce25max(Electron_sce25max)'])
    VectorDouble.extend(['HEEPProducer:sce55(Electron_sce55)'])
    VectorDouble.extend(['HEEPProducer:sce25bye55(Electron_sce25bye55)'])
    VectorDouble.extend(['HEEPProducer:e15bye55(Electron_e15bye55)'])
    VectorDouble.extend(['HEEPProducer:DeltaEtaSeedscandTrack(Electron_DeltaEtaSeedscandTrack)'])
    VectorDouble.extend(['HEEPProducer:Phi(Electron_Phi)'])
    VectorDouble.extend(['HEEPProducer:eEnergy(Electron_Energy)'])
    VectorDouble.extend(['HEEPProducer:dxy(dxy)'])
    VectorInt.extend(['HEEPProducer:losthits(Electron_losthits)'])
    VectorDouble.extend(['HEEPProducer:ePz(Electron_Pz)'])
    VectorDouble.extend(['HEEPProducer:eTheta(Electron_Theta)'])
    VectorDouble.extend(['HEEPProducer:ePx(Electron_Px)'])
    VectorDouble.extend(['HEEPProducer:ePy(Electron_Py)'])
    VectorDouble.extend(['HEEPProducer:normalizedChi2(Electron_normalizedChi2)'])

    from LeptoQuarkTreeMaker.Utils.triggerproducer_cfi import triggerProducer
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = cms.vstring( # list of trigger names
            'HLT_PFHT350_v',
            'HLT_PFHT800_v',
            'HLT_PFHT900_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v',
            'HLT_Ele15_IsoVVVL_PFHT600_v',
            'HLT_Ele15_IsoVVVL_PFHT600_v',
            'HLT_Photon500_v',
            'HLT_Photon600_v',
            'HLT_Photon22_v',
            'HLT_Photon30_v',
            'HLT_Photon36_v',
            'HLT_Photon50_v',
            'HLT_Photon75_v',
            'HLT_Photon90_v',
            'HLT_Photon120_v',
            'HLT_Photon175_v',
            'HLT_Photon165_HE10_v',
            'HLT_Photon90_CaloIdL_PFHT500_v',
            'HLT_Ele27_eta2p1_WP85_Gsf_v',
            'HLT_Ele27_WP85_Gsf_v',
            'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
            'HLT_DoubleMu18NoFiltersNoVtx_v',
            'HLT_Ele15_IsoVVVL_PFHT350_v',
            'HLT_Mu15_IsoVVVL_PFHT350_v',
            'HLT_Ele23_WPLoose_Gsf_v',
            'HLT_DoubleMu8_Mass8_PFHT250_v',
            'HLT_PFHT750_4JetPt50_v',
        )
    )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    ''' 
    SkipTag = cms.VInputTag(
        cms.InputTag('LeptonsNew:IdIsoMuon'),
        cms.InputTag('LeptonsNew:IdIsoElectron')
    )
    '''
    SkipTag = cms.VInputTag()    


 

    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=JetTag,
                          suff='',
                          fastsim=False,
                          skipGoodJets=False,
                          storeProperties=2,
                          SkipTag=SkipTag
    )



    from LeptoQuarkTreeMaker.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = cms.InputTag('slimmedMETs'), #METTag,
        GenMETTag = cms.InputTag("slimmedMETs","",tagname), #original collection used deliberately here
        JetTag = cms.InputTag('slimmedJets'),
        geninfo = cms.untracked.bool(geninfo),
    )
    process.Baseline += process.MET
    VarsDouble.extend(['MET:Pt(METPt)','MET:Phi(METPhi)','MET:CaloPt(CaloMETPt)','MET:CaloPhi(CaloMETPhi)'])



 
    process.WriteTree = cms.Path(
        process.Baseline * 
     #   process.AdditionalSequence *
#        process.dump *
        process.LQTreeMaker
    )



 
    return process
