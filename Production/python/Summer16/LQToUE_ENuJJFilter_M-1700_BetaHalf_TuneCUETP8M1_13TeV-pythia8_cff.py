import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1700_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/54E06A31-20CC-E611-8580-0CC47A78A42E.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1700_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A0053D9D-E9CB-E611-AB1F-0CC47A4D7634.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1700_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC45C09B-E9CB-E611-834C-0CC47A78A426.root' ] );


secFiles.extend( [
               ] )
