import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1300_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5AB2D7FE-15CE-E611-8CDF-0025907276DA.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1300_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/645EBCD7-15CE-E611-8CA4-0CC47A1E046E.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1300_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8488B3D2-15CE-E611-AF1A-001E67580724.root' ] );


secFiles.extend( [
               ] )
