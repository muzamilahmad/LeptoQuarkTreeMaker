import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/0AB3CF15-24C9-E611-A258-00266CFCC68C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/4EE11559-23C9-E611-A7BC-FA163EFECD88.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/5693105E-23C9-E611-921A-0090FAA58D24.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/7E9CCF6E-C3C8-E611-837F-3417EBE4E7D2.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/DA2EEE6E-24C9-E611-8851-6CC2173BBD70.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/DEB28172-23C9-E611-B176-70106F4D6AE8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/120000/E6437607-24C9-E611-849F-02163E013EA7.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/0A69A384-03C9-E611-93AE-00259074AE40.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/22404EA1-CFC8-E611-AD77-549F35AD8B6E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/52DEF08C-31C9-E611-AC9C-FA163EC29096.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/6E438B81-3FC9-E611-9F2E-7845C4F932B1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/761F4F04-DEC8-E611-BC97-FA163E32DCDF.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/A0D65912-3EC9-E611-B6ED-00259073E3D2.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/B29CA633-3EC9-E611-AAD2-008CFA0A5738.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/B8CEE606-3EC9-E611-A26D-FA163EDBDA55.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/C0A7B99D-3EC9-E611-98FE-6CC2173BBAA0.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/D6B66EA0-3EC9-E611-9426-70106F4A9248.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/F64D1E33-0EC9-E611-80B7-0025907DCA4A.root' ] );


secFiles.extend( [
               ] )
