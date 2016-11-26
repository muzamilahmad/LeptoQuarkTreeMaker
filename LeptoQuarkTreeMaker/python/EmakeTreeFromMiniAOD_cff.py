# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outfile,
reportfreq=10,
dataset="",
globaltag="",
numevents=-1,
lostlepton=False,
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False,
jerfile="",
pufile="",
doPDFs=False,
fastsim=False,
signal=False,
):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    process.GlobalTag.globaltag = globaltag

    # log output
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = reportfreq
    process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
#        wantSummary = cms.untracked.bool(True) # off by default
    )

    # files to process
    import FWCore.PythonUtilities.LumiList as LumiList
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numevents)
    )
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(dataset)
    )
    if len(jsonfile)>0: process.source.lumisToProcess = LumiList.LumiList(filename = jsonfile).getVLuminosityBlockRange()

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
    process.Baseline = cms.Sequence()
    # configure treemaker
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.treeMaker import TreeMaker
    process.LQTreeMaker2 = TreeMaker.clone(
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

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Standard producers
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## SUSY scan info
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## WeightProducer
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        from LeptoQuarkTreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
        process.WeightProducer = getWeightProducer(process.source.fileNames[0],fastsim and signal)
        process.WeightProducer.Lumi                       = cms.double(1) #default: 1 pb-1 (unit value)
        process.WeightProducer.FileNamePUDataDistribution = cms.string(pufile)
        VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if geninfo and doPDFs:
        process.PDFWeights = cms.EDProducer('PDFWeightProducer')
        VectorDouble.extend(['PDFWeights:PDFweights','PDFWeights:ScaleWeights'])
        VectorInt.extend(['PDFWeights:PDFids'])

    ## ----------------------------------------------------------------------------------------------
    ## GenHT for stitching together MC samples
    ## ----------------------------------------------------------------------------------------------
    
    ## ----------------------------------------------------------------------------------------------
    ## PrimaryVertices
    ## ----------------------------------------------------------------------------------------------
    process.goodVertices = cms.EDFilter("VertexSelector",
        src = cms.InputTag("offlineSlimmedPrimaryVertices"),
        cut = cms.string("!isFake && ndof > 4 && abs(z) < 24 && position.Rho < 2"),
        filter = cms.bool(False)
    )
    from LeptoQuarkTreeMaker.Utils.primaryvertices_cfi import primaryvertices
    process.NVtx = primaryvertices.clone(
        VertexCollection  = cms.InputTag('goodVertices'),
    )
    VarsInt.extend(['NVtx'])
    # also store total number of vertices without quality checks
    process.nAllVertices = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    VarsInt.extend(['nAllVertices'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------
    ## JECs
    ## ----------------------------------------------------------------------------------------------

    process.load("CondCore.DBCommon.CondDBCommon_cfi")
    from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
    
    # default miniAOD tags
    JetTag = cms.InputTag('slimmedJets')
    JetAK8Tag = cms.InputTag('slimmedJetsAK8')
    METTag = cms.InputTag('slimmedMETs')
    
    # get the JECs (disabled by default)
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    if len(jecfile)>0:
        #get name of JECs without any directories
        JECera = jecfile.split('/')[-1]
        JECPatch = cms.string('sqlite_file:'+jecfile+'.db')
        if os.getenv('GC_CONF'): 
            JECPatch = cms.string('sqlite_file:../src/'+jecfile+'.db')

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
                ),
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag    = cms.string("JetCorrectorParametersCollection_"+JECera+"_AK8PFchs"),
                    label  = cms.untracked.string("AK8PFchs")
                ),
            )
        )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
        
        levels  = ['L1FastJet','L2Relative','L3Absolute']
        if residual: levels.append('L2L3Residual')
        
        from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
        
        updateJetCollection(
            process,
            jetSource = cms.InputTag('slimmedJets'),
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK4PFchs', levels, 'None')
        )
        
        JetTag = cms.InputTag('updatedPatJetsUpdatedJEC')
        
        # also update the corrections for AK8 jets
        updateJetCollection(
            process,
            jetSource = cms.InputTag('slimmedJetsAK8'),
            labelName = 'AK8',
            postfix = 'UpdatedJEC',
            jetCorrections = ('AK8PFchs', levels, 'None')
        )
        
        JetAK8Tag = cms.InputTag('updatedPatJetsAK8UpdatedJEC')
        
        # update the MET to account for the new JECs
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )
        METTag = cms.InputTag('slimmedMETs','',process.name_())
    else:
        # pointless run of MET tool because it is barely functional
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )

    # keep jets before any further modifications for hadtau
    JetTagBeforeSmearing = JetTag
    # JEC uncertainty - after JECs are updated
    from LeptoQuarkTreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    process.jecUnc = JetUncertaintyProducer.clone(
        JetTag = JetTag,
        jecUncDir = cms.int32(0)
    )
    # JER factors - central, up, dow
    
    from LeptoQuarkTreeMaker.Utils.smearedpatjet_cfi import SmearedPATJetProducer
    process.jerFactor = SmearedPATJetProducer.clone(
        src = JetTag,
        variation = cms.int32(0),
        store_factor = cms.bool(True)
    )
    process.jerFactorUp = SmearedPATJetProducer.clone(
        src = JetTag,
        variation = cms.int32(1),
        store_factor = cms.bool(True)
    )
    process.jerFactorDown = SmearedPATJetProducer.clone(
        src = JetTag,
        variation = cms.int32(-1),
        store_factor = cms.bool(True)
    )
    
    # add userfloat & update tag
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.addJetInfo import addJetInfo
    process, JetTag = addJetInfo(process, JetTag, ['jecUnc','jerFactor','jerFactorUp','jerFactorDown'], [])

    ## ----------------------------------------------------------------------------------------------
    ## IsoTracks
    ## ----------------------------------------------------------------------------------------------
    
    ## ----------------------------------------------------------------------------------------------
    ## Electrons/Muons
    ## ----------------------------------------------------------------------------------------------
    # The decision was made to include the filter decision flags
    # as individual branches in the tree
    
    if not fastsim: # MET filters are not run for fastsim samples

        from LeptoQuarkTreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer
        
        process.CSCTightHaloFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_CSCTightHalo2015Filter"),
        )
        VarsInt.extend(['CSCTightHaloFilter'])
        
        process.globalTightHalo2016Filter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_globalTightHalo2016Filter"),
        )
        VarsInt.extend(['globalTightHalo2016Filter'])
        
        process.HBHENoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_HBHENoiseFilter"),
        )
        VarsInt.extend(['HBHENoiseFilter'])
        
        process.HBHEIsoNoiseFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_HBHENoiseIsoFilter"),
        )
        VarsInt.extend(['HBHEIsoNoiseFilter'])
        
        process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
            trigTagArg1 = cms.string('TriggerResults'),
            trigTagArg2 = cms.string(''),
            trigTagArg3 = cms.string(tagname),
            filterName  = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
        VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])
        
        process.eeBadScFilter = filterDecisionProducer.clone(
            trigTagArg1  = cms.string('TriggerResults'),
            trigTagArg2  = cms.string(''),
            trigTagArg3  = cms.string(tagname),
            filterName  =   cms.string("Flag_eeBadScFilter"),
        )
        VarsInt.extend(['eeBadScFilter'])
        
        # some filters need to be rerun
        process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
        process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
        process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadChargedCandidateFilter.taggingMode = True
        VarsBool.extend(['BadChargedCandidateFilter'])
        
        process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
        process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
        process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
        process.BadPFMuonFilter.taggingMode = True
        VarsBool.extend(['BadPFMuonFilter'])
    '''
    process.load('Configuration.StandardSequences.Services_cff')
    process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                   calibratedPatElectrons  = cms.PSet( 
                                                     initialSeed = cms.untracked.uint32(81),
                                                     engineName = cms.untracked.string('TRandom3'),
                                                     ),
                                                   calibratedPatPhotons  = cms.PSet( 
                                                     initialSeed = cms.untracked.uint32(81),
                                                     engineName = cms.untracked.string('TRandom3'),
                                                     ),
                                                   )
    process.load('EgammaAnalysis.ElectronTools.calibratedElectronsRun2_cfi')
    correctionType = "80Xapproval"
    
    calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducerRun2",
                                        
                                        # input collections
                                        electrons = cms.InputTag('slimmedElectrons'),
                                        gbrForestName = cms.string("gedelectron_p4combination_25ns"),
                                        
                                        # data or MC corrections
                                        # if isMC is false, data corrections are applied
                                        isMC = cms.bool(False),
                                        
                                        # set to True to get special "fake" smearing for synchronization. Use JUST in case of synchronization
                                        isSynchronization = cms.bool(False),

                                        correctionFile = cms.string("80Xapproval")
                                        )   
    process.Baseline += process.calibratedPatElectrons

    
    
    from LeptoQuarkTreeMaker.Utils.HEEPProducer_cfi import HEEPProducer
    process.HEEPProducer = HEEPProducer.clone(
        eletag = cms.InputTag('slimmedElectrons')
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
    VectorDouble.extend(['HEEPProducer:Fullsce25bye55(Electron_Fullsce25bye55)'])
    VectorDouble.extend(['HEEPProducer:Fulle15bye55(Electron_Fulle15bye55)'])
    VectorDouble.extend(['HEEPProducer:scEnergy(Electron_scEnergy)'])
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
    VectorDouble.extend(['HEEPProducer:PtHEEP(Electron_PtHEEP)'])
    VectorDouble.extend(['HEEPProducer:scEtaa(Electron_scEtaa)'])
    VectorDouble.extend(['HEEPProducer:scEta(Electron_scEta)'])
    



    ## ----------------------------------------------------------------------------------------------
    ## Muons
    ## ----------------------------------------------------------------------------------------------

    from LeptoQuarkTreeMaker.Utils.MuonProducer_cfi import MuonProducer
    process.MuonProducer = MuonProducer.clone(
        muontag = cms.InputTag('slimmedMuons')
    )
    process.Baseline += process.MuonProducer

    VectorBool.extend(['MuonProducer:MuonisTightMuon(MuonisTightMuon)'])
    VectorBool.extend(['MuonProducer:MuonisHighPtMuon(MuonisHighPtMuon)'])
    VectorDouble.extend(['MuonProducer:MuonEta(MuonEta)'])
    VectorDouble.extend(['MuonProducer:MuonPhi(MuonPhi)'])
    VectorDouble.extend(['MuonProducer:MuonPt(MuonPt)'])
    VectorDouble.extend(['MuonProducer:MuonEnergy(MuonEnergy)'])
    VectorDouble.extend(['MuonProducer:MuonPtError(MuonPtError)'])
    VectorDouble.extend(['MuonProducer:MuonGlobalChi2(MuonGlobalChi2)'])
    VectorDouble.extend(['MuonProducer:MuonTrkPtError(MuonTrkPtError)'])
    VectorInt.extend(['MuonProducer:MuonIsPF(MuonIsPF)'])
    VectorInt.extend(['MuonProducer:MuonCharge(MuonCharge)'])
    VectorInt.extend(['MuonProducer:MuonGlobalTrkValidHits(MuonGlobalTrkValidHits)'])
    VectorInt.extend(['MuonProducer:MuonTrkPixelHits(MuonTrkPixelHits)'])
    VectorInt.extend(['MuonProducer:MuonStationMatches(MuonStationMatches)'])
    VectorDouble.extend(['MuonProducer:MuonPFIsoR04Photon(MuonPFIsoR04Photon)'])
    VectorDouble.extend(['MuonProducer:MuonPFIsoR04NeutralHadron(MuonPFIsoR04NeutralHadron)'])
    VectorDouble.extend(['MuonProducer:MuonPFIsoR04PU(MuonPFIsoR04PU)'])
    VectorDouble.extend(['MuonProducer:MuonTrackerIsoSumPT(MuonTrackerIsoSumPT)'])
    VectorDouble.extend(['MuonProducer:MuonPFIsoR04ChargedHadron(MuonPFIsoR04ChargedHadron)'])
    VectorInt.extend(['MuonProducer:MuonPassID(MuonPassID)'])
    VectorInt.extend(['MuonProducer:MuonIsGlobal(MuonIsGlobal)'])
    VectorInt.extend(['MuonProducer:MuonTrackLayersWithMeasurement(MuonTrackLayersWithMeasurement)'])
    VectorDouble.extend(['MuonProducer:CocktailEta(CocktailPtError)'])
    VectorDouble.extend(['MuonProducer:CocktailPt(CocktailPt)'])
    VectorDouble.extend(['MuonProducer:MuonBestTrackVtxDistXY(MuonBestTrackVtxDistXY)'])
    VectorDouble.extend(['MuonProducer:MuonBestTrackVtxDistZ(MuonBestTrackVtxDistZ)'])

    ## ----------------------------------------------------------------------------------------------
    ## Taus
    ## ----------------------------------------------------------------------------------------------


    from LeptoQuarkTreeMaker.Utils.TauProducer_cfi import TauProducer
    process.TauProducer = TauProducer.clone(
        tautag = cms.InputTag('slimmedTaus')
    )
    process.Baseline += process.TauProducer
    VectorDouble.extend(['TauProducer:tEta(TauEta)'])
    VectorDouble.extend(['TauProducer:tPhi(TauPhi)'])
    VectorDouble.extend(['TauProducer:tPt(TauPt)'])

    '''


    
    ## ----------------------------------------------------------------------------------------------
    ## Triggers
    ## ----------------------------------------------------------------------------------------------

    # The trigger results are saved to the tree as a vector
    # Three vectors are saved:
    # 1) names of the triggers
    # 2) trigger results
    # 3) trigger prescales
    # the indexing of these vectors must match
    # If the version number of the input trigger name is omitted,
    # any matching trigger will be included (default behavior)

    from LeptoQuarkTreeMaker.Utils.triggerproducer_cfi import triggerProducer
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.triggerNameList import triggerNameList as _triggerNameList
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = _triggerNameList
    )
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    VectorDouble.extend(['TriggerProducer:objectPt'])
    VectorDouble.extend(['TriggerProducer:objecteta'])
    VectorDouble.extend(['TriggerProducer:objectphi'])
    VectorDouble.extend(['TriggerProducer:objectE'])


    '''
    if not geninfo:
        from LeptoQuarkTreeMaker.Utils.prescaleweightproducer_cfi import prescaleweightProducer
        process.PrescaleWeightProducer = prescaleweightProducer.clone()
        VarsDouble.extend(['PrescaleWeightProducer:weight(PrescaleWeightHT)'])
        VarsDouble.extend(['PrescaleWeightProducer:ht(HTOnline)'])
        VarsDouble.extend(['PrescaleWeightProducer:mht(MHTOnline)'])
    '''
    
    ## ----------------------------------------------------------------------------------------------
    ## JER smearing, various uncertainties
    ## ----------------------------------------------------------------------------------------------
    
    # list of clean tags - ignore jet ID for jets matching these objects
    SkipTag = cms.VInputTag(
       # cms.InputTag('LeptonsNew:IdIsoMuon'),
       # cms.InputTag('LeptonsNew:IdIsoElectron'),
       # cms.InputTag('IsolatedElectronTracksVeto'),
       # cms.InputTag('IsolatedMuonTracksVeto'),
       # cms.InputTag('IsolatedPionTracksVeto'),
    )
    
    # get the JERs (disabled by default)
    # this requires the user to download the .db file from this github
    # https://github.com/cms-jet/JRDatabase
    ''' 
    if len(jerfile)>0:
        #get name of JERs without any directories
        JERera = jerfile.split('/')[-1]
        JERPatch = cms.string('sqlite_file:'+jerfile+'.db')
        if os.getenv('GC_CONF'): 
            JERPatch = cms.string('sqlite_file:../src/'+jerfile+'.db')
    
        process.jer = cms.ESSource("PoolDBESSource",CondDBSetup,
            connect = JERPatch,
            toGet = cms.VPSet(
                cms.PSet(
                    record = cms.string('JetResolutionRcd'),
                    tag    = cms.string('JR_'+JERera+'_PtResolution_AK4PFchs'),
                    label  = cms.untracked.string('AK4PFchs_pt')
                ),
                cms.PSet(
                    record = cms.string('JetResolutionScaleFactorRcd'),
                    tag    = cms.string('JR_'+JERera+'_SF_AK4PFchs'),
                    label  = cms.untracked.string('AK4PFchs')
                ),
            ),
        )

        process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')
    '''
    # skip all jet smearing and uncertainties for data
#    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.JetDepot import JetDepot
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.makeJetVars import makeJetVars
    process = makeJetVars(process,
                          JetTag=JetTag,
                          suff='',
                          skipGoodJets=False,
                          storeProperties=2,
                          geninfo=geninfo,
                          fastsim=fastsim,
                          SkipTag=SkipTag
    )

 
    if geninfo:
        from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.JetDepot import JetDepot

        # JEC unc up
        process, JetTagJECup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVars(process,
                              JetTag=JetTagJECup,
                              suff='JECup',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              SkipTag=SkipTag
        )
        
        # JEC unc down
        process, JetTagJECdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=-1,
            doSmear=True,
            jerUncDir=0
        )
        process = makeJetVars(process,
                              JetTag=JetTagJECdown,
                              suff='JECdown',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              SkipTag=SkipTag
        )

        # JER unc up
        process, JetTagJERup = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=1
        )
        process = makeJetVars(process,
                              JetTag=JetTagJERup,
                              suff='JERup',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              SkipTag=SkipTag
        )
        
        # JER unc down
        process, JetTagJERdown = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=-1
        )
        process = makeJetVars(process,
                              JetTag=JetTagJERdown,
                              suff='JERdown',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              fastsim=fastsim,
                              SkipTag=SkipTag
        )

        # finally, do central smearing and replace jet tag
        process, JetTag = JetDepot(process,
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=True,
            jerUncDir=0
        )
        
    ## ----------------------------------------------------------------------------------------------
    ## Jet variables
    ## ----------------------------------------------------------------------------------------------
    '''
    # get updated QG training
    QGPatch = cms.string('sqlite_file:data/QGL_80X.db')
    if os.getenv('GC_CONF'): 
        QGPatch = cms.string('sqlite_file:../src/data/QGL_80X.db')

    process.qgdb = cms.ESSource("PoolDBESSource",CondDBSetup,
        connect = QGPatch,
        toGet   = cms.VPSet(
            cms.PSet(
                record = cms.string('QGLikelihoodRcd'),
                tag    = cms.string('QGLikelihoodObject_80X_AK4PFchs'),
                label  = cms.untracked.string('QGL_AK4PFchs')
            ),
            cms.PSet(
                record = cms.string('QGLikelihoodRcd'),
                tag    = cms.string('QGLikelihoodObject_80X_AK4PFchs_antib'),
                label  = cms.untracked.string('QGL_AK4PFchs_antib')
            ),
        )
    )
    process.es_prefer_qg = cms.ESPrefer("PoolDBESSource","qgdb")
    
    # get QG tagging discriminant
    process.QGTagger = cms.EDProducer('QGTagger',
        srcJets	            = JetTag,
        jetsLabel           = cms.string('QGL_AK4PFchs'),
        srcRho              = cms.InputTag('fixedGridRhoFastjetAll'),		
        srcVertexCollection	= cms.InputTag('offlinePrimaryVerticesWithBS'),
        useQualityCuts	    = cms.bool(False)
    )
    
    # add userfloats & update tag
    process, JetTag = addJetInfo(process, JetTag, ['QGTagger:qgLikelihood','QGTagger:ptD', 'QGTagger:axis2'], ['QGTagger:mult'])
    
    process = makeJetVars(process,
                          JetTag=JetTag,
                          suff='',
                          skipGoodJets=False,
                          storeProperties=2,
                          geninfo=geninfo,
                          fastsim=fastsim,
                          SkipTag=SkipTag
    )
    
    # get double b-tagger (w/ miniAOD customizations)
    process.load("RecoBTag.ImpactParameter.pfImpactParameterAK8TagInfos_cfi")
    process.pfImpactParameterAK8TagInfos.primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.pfImpactParameterAK8TagInfos.candidates = cms.InputTag("packedPFCandidates")
    process.pfImpactParameterAK8TagInfos.jets = JetAK8Tag
    process.load("RecoBTag.SecondaryVertex.pfInclusiveSecondaryVertexFinderAK8TagInfos_cfi")
    process.pfInclusiveSecondaryVertexFinderAK8TagInfos.extSVCollection = cms.InputTag("slimmedSecondaryVertices")
    process.pfInclusiveSecondaryVertexFinderAK8TagInfos.trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfos")
    process.load("RecoBTag.SecondaryVertex.pfBoostedDoubleSVAK8TagInfos_cfi")
    process.load("RecoBTag.SecondaryVertex.candidateBoostedDoubleSecondaryVertexAK8Computer_cfi")
    process.load("RecoBTag.SecondaryVertex.pfBoostedDoubleSecondaryVertexAK8BJetTags_cfi")
    
    # add discriminator and update tag
    process, JetAK8Tag = addJetInfo(process, JetAK8Tag, [], [], cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTags")))
    
    # apply jet ID
    process = makeJetVars(process,
                          JetTag=JetAK8Tag,
                          suff='AK8',
                          skipGoodJets=False,
                          storeProperties=1,
                          geninfo=geninfo,
                          fastsim=fastsim,
                          onlyGoodJets=True
    )
    
    # AK8 jet variables - separate instance of jet properties producer
    from LeptoQuarkTreeMaker.Utils.jetproperties_cfi import jetproperties
    process.JetsPropertiesAK8 = jetproperties.clone(
        JetTag       = JetAK8Tag,
        properties = cms.vstring(
            "prunedMass"           ,
            "NsubjettinessTau1"    ,
            "NsubjettinessTau2"    ,
            "NsubjettinessTau3"    ,
            "bDiscriminatorSubjet1",
            "bDiscriminatorSubjet2",
            "bDiscriminatorCSV"    ,
            "NumBhadrons"          ,
            "NumChadrons"          ,
        )
    )
    #specify userfloats
    process.JetsPropertiesAK8.prunedMass = cms.vstring('ak8PFJetsCHSPrunedMass')
    process.JetsPropertiesAK8.NsubjettinessTau1 = cms.vstring('NjettinessAK8:tau1')
    process.JetsPropertiesAK8.NsubjettinessTau2 = cms.vstring('NjettinessAK8:tau2')
    process.JetsPropertiesAK8.NsubjettinessTau3 = cms.vstring('NjettinessAK8:tau3')
    process.JetsPropertiesAK8.bDiscriminatorSubjet1 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8.bDiscriminatorSubjet2 = cms.vstring('SoftDrop','pfCombinedInclusiveSecondaryVertexV2BJetTags')
    process.JetsPropertiesAK8.bDiscriminatorCSV = cms.vstring('pfBoostedDoubleSecondaryVertexAK8BJetTags')
    #VectorRecoCand.extend([JetAK8Tag.value()+'(JetsAK8)'])
    #VectorDouble.extend(['JetsPropertiesAK8:prunedMass(JetsAK8_prunedMass)',
     #                    'JetsPropertiesAK8:bDiscriminatorSubjet1(JetsAK8_bDiscriminatorSubjet1CSV)',
      #                   'JetsPropertiesAK8:bDiscriminatorSubjet2(JetsAK8_bDiscriminatorSubjet2CSV)',
       #                  'JetsPropertiesAK8:bDiscriminatorCSV(JetsAK8_doubleBDiscriminator)',
        #                 'JetsPropertiesAK8:NsubjettinessTau1(JetsAK8_NsubjettinessTau1)',
         #                'JetsPropertiesAK8:NsubjettinessTau2(JetsAK8_NsubjettinessTau2)',
          #               'JetsPropertiesAK8:NsubjettinessTau3(JetsAK8_NsubjettinessTau3)'])
    #VectorInt.extend(['JetsPropertiesAK8:NumBhadrons(JetsAK8_NumBhadrons)',
           #           'JetsPropertiesAK8:NumChadrons(JetsAK8_NumChadrons)'])
    ''' 
    ## ----------------------------------------------------------------------------------------------
    ## GenJet variables
    ## ----------------------------------------------------------------------------------------------
    if geninfo:
        # store all genjets
        VectorRecoCand.extend ( [ 'slimmedGenJets(GenJets)' ] )
    
        from LeptoQuarkTreeMaker.Utils.subJetSelection_cfi import SubGenJetSelection
        
        process.GenHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(2.4),
        )
        #VectorBool.extend(['GenHTJets:SubJetMask(GenJets_HTMask)'])
        
        # make gen HT
        from LeptoQuarkTreeMaker.Utils.htdouble_cfi import htdouble
        process.GenHT = htdouble.clone(
            JetTag = cms.InputTag("GenHTJets"),
        )
        #VarsDouble.extend(['GenHT'])
        
        process.GenMHTJets = SubGenJetSelection.clone(
            JetTag = cms.InputTag('slimmedGenJets'),
            MinPt  = cms.double(30),
            MaxEta = cms.double(5.0),
        )
        #VectorBool.extend(['GenMHTJets:SubJetMask(GenJets_MHTMask)'])
        ''' 
        # make gen MHT
        from LeptoQuarkTreeMaker.Utils.mhtdouble_cfi import mhtdouble
        process.GenMHT = mhtdouble.clone(
            JetTag  = cms.InputTag('GenMHTJets'),
        )
        VarsDouble.extend(['GenMHT:Pt(GenMHT)','GenMHT:Phi(GenMHTPhi)'])
        '''
    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    # sequence for baseline filters
    process.Baseline = cms.Sequence()
    '''
    from LeptoQuarkTreeMaker.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('HT'),
        CutValue  = cms.double('500'),
    )
    process.MHTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('MHT:Pt'),
        CutValue  = cms.double('200'),
    )
    if applybaseline:
        process.Baseline += process.HTFilter
        #process.Baseline += process.MHTFilter
    '''
    ## ----------------------------------------------------------------------------------------------
    ## MET
    ## ----------------------------------------------------------------------------------------------
    from LeptoQuarkTreeMaker.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
        METTag = METTag,
        GenMETTag = cms.InputTag("slimmedMETs","",tagname), #original collection used deliberately here
        JetTag = cms.InputTag('HTJets'),
        geninfo = cms.untracked.bool(geninfo),
    )
    VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)'])
    if geninfo:
        VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])
    '''
    from LeptoQuarkTreeMaker.Utils.mt2producer_cfi import mt2Producer
    process.Mt2Producer = mt2Producer.clone(
                JetTag  = cms.InputTag('MHTJets'),
                METTag = METTag
        )
    VarsDouble.extend(['Mt2Producer:mt2(MT2)'])
    '''
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------
    '''
    if hadtau:
        from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.doHadTauBkg import doHadTauBkg
        dorecluster = False
        if hadtaurecluster==0: dorecluster = False
        elif hadtaurecluster==1: dorecluster = ("TTJets" in process.source.fileNames[0] or "WJets" in process.source.fileNames[0])
        elif hadtaurecluster==2: dorecluster = geninfo
        elif hadtaurecluster==3: dorecluster = True
        process = doHadTauBkg(process,geninfo,residual,JetTagBeforeSmearing,fastsim,dorecluster)

    ## ----------------------------------------------------------------------------------------------
    ## Lost Lepton Background
    ## ----------------------------------------------------------------------------------------------
    if lostlepton:
        from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.doLostLeptonBkg import doLostLeptonBkg
        process = doLostLeptonBkg(process,geninfo,METTag)

    ## ----------------------------------------------------------------------------------------------
    ## Zinv Background
    ## ----------------------------------------------------------------------------------------------
    if doZinv:
        from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.doZinvBkg import doZinvBkg
        process = doZinvBkg(process,tagname,geninfo,residual,fastsim)

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Final steps
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    '''
    # create the process path
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.WriteTree = cms.Path(
        process.Baseline *
        process.LQTreeMaker2
    )
    
    return process

