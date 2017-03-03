import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/14118739-8CD2-E611-8D91-24BE05C63681.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/24D66338-08D3-E611-A9AF-20CF3027A5CB.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3A024AE3-07D3-E611-8011-02163E011658.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/60966B16-08D3-E611-B25F-008CFA0016A4.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/704CCEC1-89D2-E611-B329-1866DAEA8218.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/86C942AF-07D3-E611-89D4-008CFA111334.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A877A2B1-07D3-E611-B362-0CC47A7C35D8.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C420EA12-08D3-E611-B44C-001E67E713C2.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DC81AB14-08D3-E611-A146-6CC2173BBF40.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FA5B6BED-08D3-E611-880C-001E67DDC4CF.root' ] );


secFiles.extend( [
               ] )
