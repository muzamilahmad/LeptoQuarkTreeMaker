import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/1E84F2B0-63C8-E611-972E-F04DA27540BB.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/42261DC2-8FC7-E611-B190-848F69FD4442.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/4EABD302-C2C6-E611-8632-02163E0130AE.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/6AC771D2-D0C6-E611-AB46-FA163EDE6201.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/6EAF8E1A-D0C6-E611-AB28-FA163EF78F0E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/7E664CAA-8DC7-E611-A77B-000E1E878860.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/90F51456-18C8-E611-9C1C-0025905C42A6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/9E4AD769-BDC6-E611-AB38-02163E01533A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/A8EDE72C-A0C7-E611-B211-02163E015EA1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/B26C7374-D1C6-E611-AFEB-02163E012E6C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/B4756D77-9DCA-E611-A87A-02163E019B64.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/B657D904-C9C6-E611-9552-02163E00BC01.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/C01C0D3D-88C7-E611-B9D7-FA163E027819.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/C4F547FC-D4C6-E611-9199-FA163EC9C922.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/E4EC6989-67C8-E611-B19E-FA163E7E2869.root' ] );


secFiles.extend( [
               ] )
