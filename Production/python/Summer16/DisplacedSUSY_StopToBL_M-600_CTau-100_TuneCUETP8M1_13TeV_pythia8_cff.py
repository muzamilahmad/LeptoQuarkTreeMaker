import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/06E9A6A7-4CC9-E611-9115-001E67504B25.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1EEFE3CF-4BC9-E611-A32C-FA163E4F1D1E.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/54867246-4CC9-E611-AC7D-001E67A402C1.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/66A05A9B-4CC9-E611-A695-B083FED16468.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/76F42B66-4CC9-E611-A2C1-70106F4A91E8.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/980BBBD0-4BC9-E611-A964-842B2B173478.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A4A7DD50-4CC9-E611-A4EE-002590E7DE70.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BCC35E5F-4CC9-E611-8877-0090FAA56994.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BEABEDD7-4BC9-E611-A48E-008CFA197904.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D6A1EFE0-4BC9-E611-822A-0CC47A6C115C.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E26AF0F6-4BC9-E611-80A6-02163E019A6D.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-600_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F618E0F9-4BC9-E611-ADCA-A0000420FE80.root' ] );


secFiles.extend( [
               ] )
