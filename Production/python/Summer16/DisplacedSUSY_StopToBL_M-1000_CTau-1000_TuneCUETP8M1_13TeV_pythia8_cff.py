import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7A66C17C-35D2-E611-BB56-FA163EBB8CF4.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C4AFB554-35D2-E611-A6A2-FA163EBB8CF4.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1C531847-F3D2-E611-9775-0025905D1CB2.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2AA9A929-F3D2-E611-9EFD-02163E019CE0.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/48796B5B-F3D2-E611-B768-A0369FC52374.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9A8A3457-F3D2-E611-941C-002590E7DFE0.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/ACC8C557-F3D2-E611-94E8-0CC47A7EEE80.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BCA51741-F3D2-E611-A49F-001E67E33C6A.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CC201B4E-F3D2-E611-BB34-0CC47A7E6A56.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CCDEF749-F3D2-E611-A728-008CFA00210C.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CE2A8019-F3D2-E611-8A2D-00266CFFC6CC.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC1E6159-F3D2-E611-A484-00266CFCC214.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E4B5E35A-F3D2-E611-A1DE-D8D385FF1914.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-1000_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F8AF8F5A-F3D2-E611-83F4-0CC47AC08BF8.root' ] );


secFiles.extend( [
               ] )
