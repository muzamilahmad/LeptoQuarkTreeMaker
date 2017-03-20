import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10A2615D-DCC9-E611-8405-001E67E6F760.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E8E8658-DCC9-E611-BEF3-008CFA58074C.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/86EFB667-DCC9-E611-8127-047D7B881D26.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8C01D860-DCC9-E611-99C3-FA163E29B2CC.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/946B87DF-DCC9-E611-8C76-00266CFEFDE0.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-850_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DEA59C5F-DCC9-E611-B334-7845C4F932B1.root' ] );


secFiles.extend( [
               ] )
