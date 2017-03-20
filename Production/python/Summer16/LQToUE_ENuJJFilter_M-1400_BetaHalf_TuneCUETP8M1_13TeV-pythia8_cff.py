import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1400_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4EF8E305-5ACE-E611-B859-001E674FBA1D.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1400_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/80A70658-00CD-E611-AE43-0CC47A546E5E.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-1400_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/98A2127D-D9CD-E611-8599-001E67457E36.root' ] );


secFiles.extend( [
               ] )
