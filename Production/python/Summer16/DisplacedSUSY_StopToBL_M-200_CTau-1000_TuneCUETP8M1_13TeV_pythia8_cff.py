import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8A0E64D7-27D5-E611-AE41-0CC47A7C3422.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/10A02BEE-2AD2-E611-A712-E41D2D08DE60.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2469A2AE-2AD2-E611-88CE-0025905A60B6.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/62B066FB-2AD2-E611-AC6E-02163E011584.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/68F9E30B-2BD2-E611-B707-0025902BD8CE.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9281A9FC-2BD2-E611-A48E-02163E00AFA7.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A8CD530A-2BD2-E611-88D7-24BE05BDBE61.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B04C2BE8-2AD2-E611-9E89-001E67396DEC.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D6DFB904-2BD2-E611-B584-0CC47AD99062.root',
'/store/mc/RunIISummer16MiniAODv2/DisplacedSUSY_StopToBL_M-200_CTau-1000_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F26694FF-2AD2-E611-8374-D4AE527EE013.root' ] );


secFiles.extend( [
               ] )
