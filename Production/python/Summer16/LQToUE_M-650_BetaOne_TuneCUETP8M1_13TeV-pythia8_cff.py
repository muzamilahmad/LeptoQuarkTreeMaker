import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A2EB60D-6FC9-E611-8388-001E67E6A206.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/44CD7336-6FC9-E611-B47E-0090FAA59114.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A0E61EE4-6EC9-E611-9087-A0369FC5B4F4.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C2BC43BC-6FC9-E611-81EA-FA163EFE1563.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D68C156F-70C9-E611-9864-0CC47A7E6A3E.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA750A89-73C9-E611-8D4D-02163E013833.root' ] );


secFiles.extend( [
               ] )
