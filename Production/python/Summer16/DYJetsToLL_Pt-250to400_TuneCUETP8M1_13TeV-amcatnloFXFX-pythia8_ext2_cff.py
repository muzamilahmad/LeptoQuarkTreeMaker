import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/14761573-20CB-E611-BD76-02163E019B79.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/4A4461F0-16CB-E611-90ED-02163E019CE8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/804A8C50-1DCB-E611-902B-02163E019C6D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/969C9D28-1CCB-E611-A856-02163E019D5C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/CAD40FC0-28CB-E611-AF01-02163E019B2A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/327F4F6D-59C8-E611-8933-02163E019B9F.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/6054E84A-85C8-E611-9E03-02163E019BE6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/A4EA1664-6DC8-E611-92FB-02163E019CA1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/A8032E85-8BC8-E611-AD4D-02163E019BAC.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/D4269753-64C8-E611-A64C-02163E019D5A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/80000/D682A04D-80C8-E611-9EA7-02163E014509.root' ] );


secFiles.extend( [
               ] )
