import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26A905AA-D7D4-E611-987A-FA163E3985E4.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C451F80-D7D4-E611-9D33-0025901D08BA.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/807DE55F-D7D4-E611-A46A-00259029E670.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/80A236B3-68D4-E611-8C5B-A4BADB1C0EF3.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A254DE62-D8D4-E611-BE36-008CFA1111AC.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A874EF82-63D4-E611-9C6C-C81F66B7C6E1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B203715D-D7D4-E611-BFB8-A4BF01013D12.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C23BBEAE-D7D4-E611-AF55-FA163EA2BDE9.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D6CDE8CD-D3D4-E611-923B-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D810E07C-2FD4-E611-882D-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D82FF4C7-D3D4-E611-B8A6-02163E012F65.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FCC09568-D7D4-E611-96A2-1866DAEA6CF0.root' ] );


secFiles.extend( [
               ] )
