import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2CEFAACB-A3C8-E611-A800-0CC47AD99044.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7293D3DB-A3C8-E611-8B4B-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/86330FC9-A3C8-E611-B16E-001E67E6920C.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A338644-58C8-E611-8A14-02163E015265.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/98B22733-A4C8-E611-ADA3-0025905B85FC.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A4602167-A3C8-E611-B78A-0CC47A745284.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E8E20BC0-A3C8-E611-8CDC-008CFA111230.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_ENuJJFilter_M-200_BetaHalf_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EAB3D587-A3C8-E611-87A5-141877411936.root' ] );


secFiles.extend( [
               ] )
