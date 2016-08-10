import FWCore.ParameterSet.Config as cms

HEEPProducer = cms.EDProducer('HEEPProducer',
eletag = cms.InputTag('slimmedElectrons'),
gentag = cms.InputTag('prunedGenParticles'),
vtxtag = cms.InputTag('offlineSlimmedPrimaryVertices')
#jettag = cms.InputTag( "slimmedJets")
)
