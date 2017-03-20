import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/92472A66-8AD2-E611-9E91-0CC47A4D767C.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96BA5282-8DD2-E611-B3AE-0CC47A4D7694.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F2665131-0ED3-E611-B1F5-0CC47A4C8F08.root' ] );


secFiles.extend( [
               ] )
