import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/322C633E-B5D0-E611-92AD-001E67444EAC.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-900_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/60C7BA8B-8DD0-E611-AB71-D067E5F9156C.root' ] );


secFiles.extend( [
               ] )
