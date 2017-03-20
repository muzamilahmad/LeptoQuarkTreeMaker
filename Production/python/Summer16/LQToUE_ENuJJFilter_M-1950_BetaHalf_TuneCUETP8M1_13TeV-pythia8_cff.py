import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1950_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/16FA9B98-08CA-E611-872F-0025904B1FC0.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1950_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2863DB1A-08CA-E611-9C96-00269E95B124.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1950_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/48C4E28C-08CA-E611-9B0C-02163E013CF6.root' ] );


secFiles.extend( [
               ] )
