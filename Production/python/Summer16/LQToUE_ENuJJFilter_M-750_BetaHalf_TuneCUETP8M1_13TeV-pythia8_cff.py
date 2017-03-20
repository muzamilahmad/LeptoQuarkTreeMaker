import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-750_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/64553FF0-2DC9-E611-9015-901B0E542962.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-750_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6EEC91BB-2DC9-E611-BF5C-44A84225CFF0.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-750_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8E925239-2EC9-E611-A312-002590E7DFEE.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-750_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E46716C3-2DC9-E611-BDBD-20CF3019DF17.root' ] );


secFiles.extend( [
               ] )
