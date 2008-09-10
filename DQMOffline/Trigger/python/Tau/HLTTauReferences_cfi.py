import FWCore.ParameterSet.Config as cms

#Create Reference Lorentz Vectors

TauRefProducer = cms.EDFilter("HLTTauRefProducer",

                    PFTaus = cms.untracked.PSet(
                            PFTauDiscriminator = cms.untracked.InputTag("pfRecoTauDiscriminationByIsolation"),
                            doPFTaus = cms.untracked.bool(True),
                            ptMin = cms.untracked.double(10.0),
                            PFTauProducer = cms.untracked.InputTag("pfRecoTauProducer")
                            ),
                    CaloTaus = cms.untracked.PSet(
                            ptMinTau = cms.untracked.double(10.0),
                            doCaloTaus = cms.untracked.bool(True),
                            CaloTauProducer = cms.untracked.InputTag("caloRecoTauProducer"),
                            CaloTauDiscriminator = cms.untracked.InputTag("caloRecoTauDiscriminationByIsolation")
                            ),

                    Electrons = cms.untracked.PSet(
                            ElectronCollection = cms.untracked.InputTag("pixelMatchGsfElectrons"),
                            doID = cms.untracked.bool(False),
                            InnerConeDR = cms.untracked.double(0.02),
                            MaxIsoVar = cms.untracked.double(0.02),
                            doElectrons = cms.untracked.bool(True),
                            TrackCollection = cms.untracked.InputTag("generalTracks"),
                            OuterConeDR = cms.untracked.double(0.6),
                            ptMin = cms.untracked.double(10.0),
                            doTrackIso = cms.untracked.bool(True),
                            ptMinTrack = cms.untracked.double(1.5),
                            lipMinTrack = cms.untracked.double(0.2),
                            IdCollection = cms.untracked.InputTag("electronIdCutBasedRobust"),
                            doElecFromZ = cms.untracked.bool(False),
                            MinZwindow = cms.untracked.double(70.),
                            MaxZwindow = cms.untracked.double(110.),
                            ElecEtFromZcut = cms.untracked.double(15.)
                            ),
                   Jets = cms.untracked.PSet(
                            JetCollection = cms.untracked.InputTag("iterativeCone5CaloJets"),
                            etMin = cms.untracked.double(10.0),
                            doJets = cms.untracked.bool(True)
                            ),
                   Muons = cms.untracked.PSet(
                            doMuons = cms.untracked.bool(True),
                            MuonCollection = cms.untracked.InputTag("muons"),
                            ptMin = cms.untracked.double(5.0)
                            ),

                  EtaMax = cms.untracked.double(2.5)
                  )
