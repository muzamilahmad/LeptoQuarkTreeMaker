import FWCore.ParameterSet.Config as cms

HEEPProducer = cms.EDProducer('HEEPProducer',
eletag = cms.InputTag('slimmedElectrons'),
gentag = cms.InputTag('prunedGenParticles'),
vtxtag = cms.InputTag('offlineSlimmedPrimaryVertices'),
heep70trkIsolMap = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso"),
eleHEEPIdCutFlowResultMap = cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV70"),
#jettag = cms.InputTag( "slimmedJets")
ElectronVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
ElectronLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
ElectronMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
ElectronTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
ElectronHEEPIdMap = cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV70"),
   # The map name for the full info is the same as the map name of the
    # corresponding simple pass/fail map above, they are distinguished by
    # the type of the content.
eleVetoIdCutFlowResultMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
eleLooseIdCutFlowResultMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
eleMediumIdCutFlowResultMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
eleTightIdCutFlowResultMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    # new HEEP 7.0 track isolation
#heep70trkIsolMap = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso"),
EBReducedRecHitsInputTag = cms.InputTag("reducedEgamma:reducedEBRecHits"),
EEReducedRecHitsInputTag = cms.InputTag("reducedEgamma:reducedEERecHits"),
vidBitmap=cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV70Bitmap")



#jettag = cms.InputTag( "slimmedJets")
)
