import FWCore.ParameterSet.Config as cms

JetEnergyResolution = cms.EDProducer('JetEnergyResolution',
jettag = cms.InputTag( "slimmedJets")
)
