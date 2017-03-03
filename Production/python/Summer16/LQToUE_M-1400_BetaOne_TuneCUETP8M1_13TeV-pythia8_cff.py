import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/4AB97C92-56F9-E611-966C-001E674FAF23.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7011E9F9-54F9-E611-8E22-FA163EFDD41D.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1400_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/D26E0929-55F9-E611-BCD8-001E674FB063.root' ] );


secFiles.extend( [
               ] )
