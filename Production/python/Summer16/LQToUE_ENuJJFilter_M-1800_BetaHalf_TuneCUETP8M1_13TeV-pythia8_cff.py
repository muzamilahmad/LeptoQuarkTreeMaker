import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8248B467-7FCA-E611-B2B8-008CFA1979A0.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E06309DC-44C7-E611-B39F-008CFA110AEC.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1800_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E01EBD46-C0C7-E611-AE7E-008CFA111334.root' ] );


secFiles.extend( [
               ] )
