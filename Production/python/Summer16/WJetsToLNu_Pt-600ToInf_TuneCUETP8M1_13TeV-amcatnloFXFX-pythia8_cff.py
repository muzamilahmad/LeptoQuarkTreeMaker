import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/164C4540-86D1-E611-A62A-1418774126FB.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/185FF0C9-87D1-E611-AFDC-B083FED4263D.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/2A375061-88D1-E611-AC75-1418774126FB.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6059F8CA-87D1-E611-B347-B083FED40671.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6C69D364-88D1-E611-A70A-C81F66B7ED49.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8CA189A5-84D1-E611-8082-B083FECFF297.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A4C37912-93D1-E611-B49D-C81F66B782DD.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AE6BF4C8-87D1-E611-85F2-B083FED429D6.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AEF1B8E9-85D1-E611-9259-B083FED429D6.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B024F4FA-8BD1-E611-96C7-B083FED429D6.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B20E079F-84D1-E611-8741-B083FECF83AB.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B45CE3D3-87D1-E611-B343-C81F66B782DD.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EC71D7E0-8ED1-E611-88B8-B083FECFF297.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/FE8B12A7-89D1-E611-900A-90B11C0BB9CF.root' ] );


secFiles.extend( [
               ] )
