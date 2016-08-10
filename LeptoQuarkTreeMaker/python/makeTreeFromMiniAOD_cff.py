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
numevents=1000,
geninfo=False,
tagname="RECO",
jsonfile="",
jecfile="",
residual=False,
jerfile="",
pufile="",
doPDFs=False,
fastsim=False,
signal=False
):

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Preamble
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
    process.GlobalTag.globaltag = globaltag

    # CMSSW version sniffing
    CMSSWVER = os.getenv("CMSSW_VERSION")
    CMSSWVER_parts = CMSSWVER.split("_")
    is74X = False
    if int(CMSSWVER_parts[1])==7 and int(CMSSWVER_parts[2])>=4:
        is74X = True
        print "Configuring for 74X"

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
    
    # sequence for baseline producers
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
        process.Baseline += process.WeightProducer
        VarsDouble.extend(['WeightProducer:weight(Weight)','WeightProducer:xsec(CrossSection)','WeightProducer:nevents(NumEvents)',
                           'WeightProducer:TrueNumInteractions','WeightProducer:PUweight(puWeight)','WeightProducer:PUSysUp(puSysUp)','WeightProducer:PUSysDown(puSysDown)'])
        VarsInt.extend(['WeightProducer:NumInteractions'])

    ## ----------------------------------------------------------------------------------------------
    ## PDF weights for PDF systematics
    ## ----------------------------------------------------------------------------------------------
    if geninfo and doPDFs:
        process.PDFWeights = cms.EDProducer('PDFWeightProducer')
        process.Baseline += process.PDFWeights
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
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])
    # also store total number of vertices without quality checks
    process.nAllVertices = primaryvertices.clone(
        VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    process.Baseline += process.nAllVertices
    VarsInt.extend(['nAllVertices'])

    ## ----------------------------------------------------------------------------------------------
    ## GenParticles
    ## ----------------------------------------------------------------------------------------------

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
        
        # all changed from 74X->80X
        if is74X:
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
            
            # also update the corrections for AK8 jets
            process.patJetCorrFactorsReapplyJECAK8 = patJetCorrFactorsUpdated.clone(
                src     = cms.InputTag("slimmedJetsAK8"),
                levels  = ['L1FastJet',
                          'L2Relative',
                          'L3Absolute'],
                payload = 'AK8PFchs' # Make sure to choose the appropriate levels and payload here!
            )
            if residual: process.patJetCorrFactorsReapplyJECAK8.levels.append('L2L3Residual')
            process.patJetsReapplyJECAK8 = patJetsUpdated.clone(
                jetSource = cms.InputTag("slimmedJetsAK8"),
                jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJECAK8"))
            )
            process.Baseline += process.patJetCorrFactorsReapplyJECAK8
            process.Baseline += process.patJetsReapplyJECAK8
            JetAK8Tag = cms.InputTag('patJetsReapplyJECAK8')
            
            # update the MET to account for the new JECs
            # ref: https://github.com/cms-met/cmssw/blob/METCorUnc74X/PhysicsTools/PatAlgos/test/corMETFromMiniAOD.py
            
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
        else:
            levels  = ['L1FastJet','L2Relative','L3Absolute']
            if residual: levels.append('L2L3Residual')
            
            from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
            
            updateJetCollection(
                process,
                jetSource = cms.InputTag('slimmedJets'),
                postfix = 'UpdatedJEC',
                jetCorrections = ('AK4PFchs', levels, 'None')
            )
            process.Baseline += process.patJetCorrFactorsUpdatedJEC
            process.Baseline += process.updatedPatJetsUpdatedJEC
            
            JetTag = cms.InputTag('updatedPatJetsUpdatedJEC')
            
            # also update the corrections for AK8 jets
            updateJetCollection(
                process,
                jetSource = cms.InputTag('slimmedJetsAK8'),
                labelName = 'AK8',
                postfix = 'UpdatedJEC',
                jetCorrections = ('AK8PFchs', levels, 'None')
            )
            process.Baseline += process.patJetCorrFactorsAK8UpdatedJEC
            process.Baseline += process.updatedPatJetsAK8UpdatedJEC
            
            JetAK8Tag = cms.InputTag('updatedPatJetsAK8UpdatedJEC')
            
            # update the MET to account for the new JECs
            from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
            runMetCorAndUncFromMiniAOD(
                process,
                isData=not geninfo, # controls gen met
            )
            METTag = cms.InputTag('slimmedMETs','',process.name_())
    elif not is74X:
        # pointless run of MET tool because it is barely functional
        from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
        runMetCorAndUncFromMiniAOD(
            process,
            isData=not geninfo, # controls gen met
        )

    # JEC uncertainty - after JECs are updated
    from LeptoQuarkTreeMaker.Utils.jetuncertainty_cfi import JetUncertaintyProducer
    process.jecUnc = JetUncertaintyProducer.clone(
        JetTag = JetTag,
        jecUncDir = cms.int32(0)
    )
    process.Baseline += process.jecUnc
    # add userfloat & update tag
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.addJetInfo import addJetInfo
    process, JetTag = addJetInfo(process, "Baseline", JetTag, is74X, ['jecUnc'], [])

    ## ----------------------------------------------------------------------------------------------
    ## IsoTracks
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## MET Filters
    ## ----------------------------------------------------------------------------------------------
    
    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree
    
    if not fastsim: # MET filters are not run for fastsim samples

        from LeptoQuarkTreeMaker.Utils.filterdecisionproducer_cfi import filterDecisionProducer
        
        if is74X:
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
        else: #~all changed for 80X
            process.CSCTightHaloFilter = filterDecisionProducer.clone(
                trigTagArg1 = cms.string('TriggerResults'),
                trigTagArg2 = cms.string(''),
                trigTagArg3 = cms.string(tagname),
                filterName  = cms.string("Flag_CSCTightHalo2015Filter"),
            )
            process.Baseline += process.CSCTightHaloFilter
            VarsInt.extend(['CSCTightHaloFilter'])
            
            process.globalTightHalo2016Filter = filterDecisionProducer.clone(
                trigTagArg1 = cms.string('TriggerResults'),
                trigTagArg2 = cms.string(''),
                trigTagArg3 = cms.string(tagname),
                filterName  = cms.string("Flag_globalTightHalo2016Filter"),
            )
            process.Baseline += process.globalTightHalo2016Filter
            VarsInt.extend(['globalTightHalo2016Filter'])
            
            process.HBHENoiseFilter = filterDecisionProducer.clone(
                trigTagArg1 = cms.string('TriggerResults'),
                trigTagArg2 = cms.string(''),
                trigTagArg3 = cms.string(tagname),
                filterName  = cms.string("Flag_HBHENoiseFilter"),
            )
            process.Baseline += process.HBHENoiseFilter
            VarsInt.extend(['HBHENoiseFilter'])
            
            process.HBHEIsoNoiseFilter = filterDecisionProducer.clone(
                trigTagArg1 = cms.string('TriggerResults'),
                trigTagArg2 = cms.string(''),
                trigTagArg3 = cms.string(tagname),
                filterName  = cms.string("Flag_HBHENoiseIsoFilter"),
            )
            process.Baseline += process.HBHEIsoNoiseFilter
            VarsInt.extend(['HBHEIsoNoiseFilter'])
            
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
            
            # some filters need to be rerun
            process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
            process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
            process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
            process.BadChargedCandidateFilter.taggingMode = True
            process.Baseline += process.BadChargedCandidateFilter
            VarsBool.extend(['BadChargedCandidateFilter'])
            
            process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
            process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
            process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
            process.BadPFMuonFilter.taggingMode = True
            process.Baseline += process.BadPFMuonFilter
            VarsBool.extend(['BadPFMuonFilter'])

    
    
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
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1     = cms.string('TriggerResults'),
        trigTagArg2     = cms.string(''),
        trigTagArg3     = cms.string('HLT'),
        prescaleTagArg1  = cms.string('patTrigger'),
        prescaleTagArg2  = cms.string(''),
        prescaleTagArg3  = cms.string(''),
        triggerNameList = cms.vstring( # list of trigger names
            'HLT_PFMET90_PFMHT90_IDTight_v',
            'HLT_PFMET100_PFMHT100_IDTight_v',
            'HLT_PFMET110_PFMHT110_IDTight_v',
            'HLT_PFMET120_PFMHT120_IDTight_v',
            'HLT_Ele25_eta2p1_WPTight_v ',
            'HLT_Ele27_WPTight_v',
            'HLT_Ele27_eta2p1_WPLoose_v ',
            'HLT_Ele45_WPLoose_v',
            'HLT_Ele105_CaloIdVT_GsfTrkIdT_v',
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET50_v',
            'HLT_Ele15_IsoVVVL_PFHT600_v',
            'HLT_Ele15_IsoVVVL_PFHT350_v',
            'HLT_IsoMu24_v ',
            'HLT_IsoMu22_eta2p1_v',
            'HLT_Mu50_v',
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET50_v',
            'HLT_Mu15_IsoVVVL_PFHT600_v',
            'HLT_Mu15_IsoVVVL_PFHT350_v',
            'HLT_Photon90_CaloIdL_PFHT500_v',
            'HLT_Photon165_HE10_v',
            'HLT_PFHT300_PFMET100_v',
            'HLT_PFHT300_PFMET110_v',
            'HLT_PFHT800_v',
            'HLT_PFHT900_v',
            'HLT_DoubleMu8_Mass8_PFHT300_v',
            'HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v',
            'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v',
            'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
            'HLT_Mu15_IsoVVVL_PFHT400_v',
            'HLT_TkMu50_v',
            'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v',
            'HLT_Ele15_IsoVVVL_PFHT400_v',
            'HLT_IsoMu22_v',
            'HLT_IsoTkMu22_v',
            'HLT_Mu50_IsoVVVL_PFHT400_v',
            'HLT_Ele50_IsoVVVL_PFHT400_v',
            'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v',
            'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v',
            'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v',
            'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
            'HLT_PFHT200_v',
            'HLT_PFHT250_v',
            'HLT_PFHT300_v',
            'HLT_PFHT350_v',
            'HLT_PFHT400_v',
            'HLT_PFHT475_v',
            'HLT_PFHT600_v',
            'HLT_PFHT650_v',
            'HLT_IsoMu16_eta2p1_MET30_v',
            'HLT_Mu45_eta2p1_v',
            'HLT_CaloJet500_NoJetID_v'
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

       )
    )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:TriggerPass','TriggerProducer:TriggerPrescales'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    VectorDouble.extend(['TriggerProducer:objectPt'])
    VectorDouble.extend(['TriggerProducer:objecteta'])
    VectorDouble.extend(['TriggerProducer:objectphi'])
    VectorDouble.extend(['TriggerProducer:objectE'])


    ## ----------------------------------------------------------------------------------------------
    ## JER smearing, various uncertainties
    ## ----------------------------------------------------------------------------------------------
    
    # list of clean tags - ignore jet ID for jets matching these objects
    '''
    SkipTag = cms.VInputTag(
        cms.InputTag('LeptonsNew:IdIsoMuon'),
        cms.InputTag('LeptonsNew:IdIsoElectron'),
        cms.InputTag('IsolatedElectronTracksVeto'),
        cms.InputTag('IsolatedMuonTracksVeto'),
        cms.InputTag('IsolatedPionTracksVeto'),
    )
    '''
    SkipTag = cms.VInputTag()
    # get the JERs (disabled by default)
    # this requires the user to download the .db file from this github
    # https://github.com/cms-jet/JRDatabase
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

    # skip all jet smearing for data and for 74X
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.JetDepot import JetDepot
    from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.makeJetVars import makeJetVars
    doJERsmearing = geninfo and not is74X
    
    # JEC unc up
    process, JetTagJECup = JetDepot(process,
        sequence="Baseline",
        JetTag=JetTag,
        jecUncDir=1,
        doSmear=doJERsmearing,
        jerUncDir=0
    )
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=JetTagJECup,
                          suff='JECup',
                          skipGoodJets=False,
                          storeProperties=1,
                          geninfo=geninfo,
                          SkipTag=SkipTag,
                          is74X=is74X
    )
    
    # JEC unc down
    process, JetTagJECdown = JetDepot(process,
        sequence="Baseline",
        JetTag=JetTag,
        jecUncDir=-1,
        doSmear=doJERsmearing,
        jerUncDir=0
    )
    process = makeJetVars(process,
                          sequence="Baseline",
                          JetTag=JetTagJECdown,
                          suff='JECdown',
                          skipGoodJets=False,
                          storeProperties=1,
                          geninfo=geninfo,
                          SkipTag=SkipTag,
                          is74X=is74X
    )
    
    if doJERsmearing:
        # JER unc up
        process, JetTagJERup = JetDepot(process,
            sequence="Baseline",
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=1
        )
        process = makeJetVars(process,
                              sequence="Baseline",
                              JetTag=JetTagJERup,
                              suff='JERup',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              SkipTag=SkipTag,
                              is74X=is74X
        )
        
        # JER unc down
        process, JetTagJERdown = JetDepot(process,
            sequence="Baseline",
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=-1
        )
        process = makeJetVars(process,
                              sequence="Baseline",
                              JetTag=JetTagJERdown,
                              suff='JERdown',
                              skipGoodJets=False,
                              storeProperties=1,
                              geninfo=geninfo,
                              SkipTag=SkipTag,
                              is74X=is74X
        )

        # finally, do central smearing and replace jet tag
        process, JetTag = JetDepot(process,
            sequence="Baseline",
            JetTag=JetTag,
            jecUncDir=0,
            doSmear=doJERsmearing,
            jerUncDir=0
        )
        
    ## ----------------------------------------------------------------------------------------------
    ## Jet variables
    ## ----------------------------------------------------------------------------------------------

    # QG tagging DB payload

    # get QG tagging discriminant
    
    # AK8 jet variables - separate instance of jet properties producer

    ## ----------------------------------------------------------------------------------------------
    ## GenJet variables
    ## ----------------------------------------------------------------------------------------------
    
    ## ----------------------------------------------------------------------------------------------
    ## Baseline filters
    ## ----------------------------------------------------------------------------------------------
    from LeptoQuarkTreeMaker.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('HT'),
        CutValue  = cms.double('500'),
    )
    process.MHTFilter = DoubleFilter.clone(
        DoubleTag = cms.InputTag('MHT:Pt'),
        CutValue  = cms.double('200'),
    )
    #if applybaseline:
     #   process.Baseline += process.HTFilter
        #process.Baseline += process.MHTFilter
    
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
    process.Baseline += process.MET
    VarsDouble.extend(['MET:Pt(MET)','MET:Phi(METPhi)','MET:CaloPt(CaloMET)','MET:CaloPhi(CaloMETPhi)','MET:PFCaloPtRatio(PFCaloMETRatio)'])
    if geninfo:
        VarsDouble.extend(['MET:GenPt(GenMET)','MET:GenPhi(GenMETPhi)'])
        VectorDouble.extend(['MET:PtUp(METUp)', 'MET:PtDown(METDown)', 'MET:PhiUp(METPhiUp)', 'MET:PhiDown(METPhiDown)'])

    
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Optional producers (background estimations, control regions)
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # sequence for optional producers
    process.AdditionalSequence = cms.Sequence()
    
    ## ----------------------------------------------------------------------------------------------
    ## Hadronic Tau Background
    ## ----------------------------------------------------------------------------------------------

    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------
    ## Final steps
    ## ----------------------------------------------------------------------------------------------
    ## ----------------------------------------------------------------------------------------------

    # create the process path
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.WriteTree = cms.Path(
        process.Baseline *
        process.AdditionalSequence *
#        process.dump *
        process.LQTreeMaker2
    )
    
    return process

