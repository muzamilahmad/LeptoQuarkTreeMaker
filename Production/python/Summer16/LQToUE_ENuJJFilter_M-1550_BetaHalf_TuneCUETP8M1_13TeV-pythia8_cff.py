import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1550_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/58E82CC1-B3E9-E611-AE63-002590A831B4.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1550_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/949893DA-BAE9-E611-AEA4-24BE05CE2E91.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1550_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B4BCD2BB-37EA-E611-821E-00259029ED1A.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1550_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/DC659492-37EA-E611-BAD1-001CC47D8D40.root' ] );


secFiles.extend( [
               ] )
