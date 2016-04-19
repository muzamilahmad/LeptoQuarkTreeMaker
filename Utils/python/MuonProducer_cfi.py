import FWCore.ParameterSet.Config as cms

MuonProducer = cms.EDProducer('MuonProducer',
muontag = cms.InputTag('slimmedMuons'),
#rhotag = cms.InputTag('fixedGridRhoFastjetAll')
#jettag = cms.InputTag( "slimmedJets")
tautag = cms.InputTag('slimmedTaus')


)

