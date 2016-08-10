import FWCore.ParameterSet.Config as cms

MuonProducer = cms.EDProducer('MuonProducer',
muontag = cms.InputTag('slimmedMuons'),
#rhotag = cms.InputTag('fixedGridRhoFastjetAll')
#jettag = cms.InputTag( "slimmedJets")
    MaxSize = cms.uint32(10),
    MuonIso = cms.double(0.05),
    MuonID = cms.string('GlobalMuonPromptTight'),
    BeamSpotCorr = cms.bool(True),
    UseCocktailRefits = cms.bool(True),
    VertexInputTag = cms.InputTag('offlineSlimmedPrimaryVertices'),
    BeamSpotInputTag = cms.InputTag('offlineBeamSpot')

)

