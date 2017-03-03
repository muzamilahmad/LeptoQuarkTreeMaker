import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/48137927-28CB-E611-B499-0CC47A4D7644.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/984AA334-28CB-E611-BAFA-0CC47AA98F9A.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A1F0F6D-2FCB-E611-8B71-001E67DFFB4F.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9ABD0DE2-27CB-E611-8874-24BE05C6E7E1.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E0EFFEC8-27CB-E611-AE61-0025907D250C.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/06C0870B-48CB-E611-8351-FA163E702259.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0C03A0FF-4CCB-E611-B79B-90B11C2801E1.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/48F1E595-82CB-E611-ABB7-003048C91B0E.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/864C997A-42CB-E611-966B-FA163E23DBD1.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A03B3C76-54CB-E611-A0CD-0025905B8562.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A2583F81-40CB-E611-B3A2-B083FED406AD.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BEA921BD-A0CB-E611-BDA5-90B11C08C1BA.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CEE07CB3-30CB-E611-91D3-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D69B135F-90CA-E611-B96E-008CFA197E58.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0C5CEB77-E1C9-E611-9471-02163E0176A9.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9C580777-1BCA-E611-BEF1-B083FED14CE0.root' ] );


secFiles.extend( [
               ] )
