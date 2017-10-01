import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/120A7CFB-74C8-E611-B68B-24BE05C49891.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/168A3D42-7FC8-E611-8634-000101000026.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/3E1C1C2F-72C8-E611-8B93-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/481D38F0-75C8-E611-9EF3-5065F38172A1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/60CE5DF7-75C8-E611-A75F-24BE05C3DB21.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/8EA15B41-78C8-E611-80D2-00010100008B.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/A4B33A42-75C8-E611-98F4-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/BA843BA5-7FC8-E611-86A6-E0071B7A68F0.root' ] );


secFiles.extend( [
               ] )
