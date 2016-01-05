import FWCore.ParameterSet.Config as cms

HEEPProducer = cms.EDProducer('HEEPProducer',
eletag = cms.InputTag('slimmedElectrons'),
#rhotag = cms.InputTag('fixedGridRhoFastjetAll')
vtxtag = cms.InputTag('offlineSlimmedPrimaryVertices')
#jettag = cms.InputTag( "slimmedJets")
)
