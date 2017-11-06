import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0489A527-10D0-E611-82BA-1418774121A1.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/56E6FAFF-0AD0-E611-9D2F-842B2B09CE7B.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5E2ED5E9-05D0-E611-820F-001C23C103EB.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66B7502C-07D0-E611-A2D8-B083FED3EE25.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7861ECC6-0AD0-E611-9E6A-D4AE526A0D2E.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9E4F2226-0CD0-E611-A7B3-842B2B766242.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A40770A2-1AD0-E611-AF94-A4BADB1C4493.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A868BB28-07D0-E611-9EBC-B083FED42488.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BA5B4323-07D0-E611-8BDD-842B2B7682C7.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D2123F22-10D0-E611-9864-D4AE526A0CFB.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E8242E30-09D0-E611-9461-141877411367.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EE0FF9B2-1AD0-E611-9B9C-0CC47A00A832.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F837B6FC-04D0-E611-945F-1866DAEEB0A8.root' ] );


secFiles.extend( [
               ] )
