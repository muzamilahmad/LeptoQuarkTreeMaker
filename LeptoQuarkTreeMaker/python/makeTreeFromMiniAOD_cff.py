# $Id:things are being changed for LQ analysis 
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outfile,
dataset="",
globaltag="",
geninfo=False,
tagname="PAT",
jsonfile="",
jecfile="",
doPDFs=False,
residual=False,
fastsim=False
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
    if geninfo:
       from LeptoQuarkTreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
       process.WeightProducer = getWeightProducer(process.source.fileNames[0])
       process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
       process.WeightProducer.FileNamePUDataDistribution = cms.string("LeptoQuarkTreeMaker/Production/test/data/PileupHistograms_1117.root")
       process.Baseline += process.WeightProducer
       VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                          'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
       VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if doPDFs:
       process.PDFWeights = cms.EDProducer('PDFWeightProducer')
       process.Baseline += process.PDFWeights
       VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights'])
       VectorInt.extend(['PDFWeights:PDFids'])
   
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

    


    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
        photonCollection       = cms.untracked.InputTag("slimmedPhotons"),
        electronCollection     = cms.untracked.InputTag("slimmedElectrons"),
        conversionCollection   = cms.untracked.InputTag("reducedEgamma","reducedConversions",tagname),
        beamspotCollection     = cms.untracked.InputTag("offlineBeamSpot"),
        ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
        ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
        rhoCollection          = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
        genParCollection = cms.untracked.InputTag("prunedGenParticles"),
        debug                  = cms.untracked.bool(False)
    )
    process.Baseline += process.goodPhotons
    # good photon tag is InputTag('goodPhotons','bestPhoton')
    VectorRecoCand.append("goodPhotons:bestPhoton")
    #VectorRecoCand.append("goodPhotons:bestPhotonLoose")
    VectorRecoCand.append("goodPhotons:SimplePhoton")
 
    VarsInt.append("goodPhotons:NumPhotons")




    if not fastsim: # MET filters are not run for fastsim samples

        from LeptoQuarkTreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer
        process.METFilters = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_METFilters"),
        )
        process.Baseline += process.METFilters
        VarsInt.extend(['METFilters'])
        
        #process.CSCTightHaloFilter = filterDecisionProducer.clone(
        #    trigTagArg1 = cms.string('TriggerResults'),
        #    trigTagArg2 = cms.string(''),
        #    trigTagArg3 = cms.string(tagname),
        #    filterName  = cms.string("Flag_CSCTightHaloFilter"),
        #)
        #process.Baseline += process.CSCTightHaloFilter
        #VarsInt.extend(['CSCTightHaloFilter'])
        
        #run beam halo filter from text list of events
        from LeptoQuarkTreeMaker.Utils.getEventListFilter_cff import getEventListFilter
        process.CSCTightHaloFilter = getEventListFilter(process.source.fileNames[0],"Dec01","csc2015")
        process.Baseline += process.CSCTightHaloFilter
        VarsBool.extend(['CSCTightHaloFilter'])
        
        #process.HBHENoiseFilter = filterDecisionProducer.clone(
        #    trigTagArg1 = cms.string('TriggerResults'),
        #    trigTagArg2 = cms.string(''),
        #    trigTagArg3 = cms.string(tagname),
        #    filterName  = cms.string("Flag_HBHENoiseFilter"),
        #)
        #process.Baseline += process.HBHENoiseFilter
        #VarsInt.extend(['HBHENoiseFilter'])
        
        #rerun HBHE noise filter manually
        process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
        process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
        process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(False) 
        process.HBHENoiseFilterResultProducer.defaultDecision = cms.string("HBHENoiseFilterResultRun2Loose")
        process.Baseline += process.HBHENoiseFilterResultProducer
        VarsBool.extend(['HBHENoiseFilterResultProducer:HBHENoiseFilterResult(HBHENoiseFilter)'])
        #add HBHE iso noise filter
        VarsBool.extend(['HBHENoiseFilterResultProducer:HBHEIsoNoiseFilterResult(HBHEIsoNoiseFilter)'])

        process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
        process.Baseline += process.EcalDeadCellTriggerPrimitiveFilter
        VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])
        
        process.eeBadScFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(tagname),
            filterName  =   cms.string("Flag_eeBadScFilter"),
            )
        process.Baseline += process.eeBadScFilter
        VarsInt.extend(['eeBadScFilter'])
        
        #run eeBadSc4 filter from text list of events
        process.eeBadSc4Filter = getEventListFilter(process.source.fileNames[0],"Dec01","ecalscn1043093")
        process.Baseline += process.eeBadSc4Filter
        VarsBool.extend(['eeBadSc4Filter'])





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
    VectorInt.extend(['HEEPProducer:PDGID(PDGID)'])
    VectorInt.extend(['HEEPProducer:gencharge(gencharge)'])
    VectorDouble.extend(['HEEPProducer:genPt(genPt)'])
    VectorDouble.extend(['HEEPProducer:genEta(genEta)'])
    VectorDouble.extend(['HEEPProducer:genPhi(genPhi)'])
    VectorDouble.extend(['HEEPProducer:genEnergy(genEnergy)'])
    VectorInt.extend(['HEEPProducer:motherPDGID(motherPDGID)'])
    VectorInt.extend(['HEEPProducer:elstatus(elstatus)'])

    from LeptoQuarkTreeMaker.Utils.triggerproducer_cfi import triggerProducer
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = cms.vstring( # list of trigger names
            'HLT_Photon22_v',
            'HLT_Photon30_v',
            'HLT_Photon36_v',
            'HLT_Photon50_v',
            'HLT_Photon75_v',
            'HLT_Photon90_v',
            'HLT_Photon120_v',
            'HLT_Photon175_v',
            'HLT_Ele22_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele22_eta2p1_WPTight_Gsf_v',
            'HLT_Ele23_WPLoose_Gsf_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele27_eta2p1_WPTight_Gsf_v',
            'HLT_Ele32_eta2p1_WPTight_Gsf_v',
            'HLT_Ele35_CaloIdVT_GsfTrkIdT_PFJet150_PFJet50_v',
            'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v',
            'HLT_Ele105_CaloIdVT_GsfTrkIdT_v',
            'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v',
            'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v',
            'HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v',
            'HLT_Ele12_CaloIdM_TrackIdM_PFJet30_v',
            'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v',
            'HLT_Ele33_CaloIdM_TrackIdM_PFJet30_v',
            'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',
            'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v'
        )
    )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    VectorDouble.extend(['TriggerProducer:objectPt'])
    VectorDouble.extend(['TriggerProducer:objecteta'])
    VectorDouble.extend(['TriggerProducer:objectphi'])
    VectorDouble.extend(['TriggerProducer:objectE'])
     
   
   
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
