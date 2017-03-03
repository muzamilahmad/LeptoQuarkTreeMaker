import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/04698E34-0FC9-E611-B074-141877641875.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/36462502-0FC9-E611-8B55-1866DAEB296C.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4C2AD41C-0FC9-E611-B525-0CC47A13CC7A.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/68618A67-3EC8-E611-A1BA-00259048B754.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94A6885D-0FC9-E611-8E57-20CF3027A5F9.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9ABE7539-0FC9-E611-B504-002590E7DFEE.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DAD7465A-0FC9-E611-84C3-24BE05CE3C91.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE618DF3-0FC9-E611-B2FA-02163E012D8D.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DEFDE75C-0FC9-E611-BBD7-001E67DFFB31.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E412B76D-0FC9-E611-83DB-008CFA197D74.root',
'/store/mc/RunIISummer16MiniAODv2/LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F87A6B2E-0FC9-E611-A08C-FA163E46FBAD.root' ] );


secFiles.extend( [
               ] )
