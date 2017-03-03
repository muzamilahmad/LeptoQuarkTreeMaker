import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/3CD3FC0F-F7D1-E611-B209-001E677926C0.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E65EF489-CDD1-E611-AA84-002590A4FFC6.root' ] );


secFiles.extend( [
               ] )
