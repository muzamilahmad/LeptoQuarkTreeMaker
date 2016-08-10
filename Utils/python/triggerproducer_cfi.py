import FWCore.ParameterSet.Config as cms

triggerProducer = cms.EDProducer('TriggerProducer',
trigTagArg1  = cms.string('TriggerResults'),
trigTagArg2  = cms.string(''),
trigTagArg3  = cms.string('HLT'),
prescaleTagArg1  = cms.string('patTrigger'),
prescaleTagArg2  = cms.string(''),
prescaleTagArg3  = cms.string(''),
#objecttag = cms.string('selectedPatTrigger'),
objecttag =  cms.InputTag('selectedPatTrigger'),
objecttag1 = cms.string(''),
objecttag2 = cms.string(''),
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
triggerNameList    =   cms.vstring()
)
