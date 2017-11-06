import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/16FBBA48-6AD4-E611-BE22-0CC47AA9906E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1C1F35B1-D0D4-E611-9F5E-0025907E343C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1ED03346-D0D4-E611-9B29-001E675A6D10.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/22FD03D3-79D4-E611-8BDA-001E67C7AF3F.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/28305311-D1D4-E611-B3E0-02163E017630.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/54F88D60-D0D4-E611-8610-1866DAEB4284.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6EBC386E-D0D4-E611-97A6-0CC47AD98BEE.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8A49B96B-72D4-E611-A274-FA163EB792F6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/ACFE6B60-D0D4-E611-B31D-02163E011463.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/CA3A9B63-D0D4-E611-BF5A-001E674FB2D4.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EC973DBA-D0D4-E611-A24A-008CFA111230.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/02327B3A-CCD4-E611-8982-FA163E48F90A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/16399FFF-CCD4-E611-A4D3-001E674FC800.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/30776F28-CCD4-E611-8373-0CC47A4C8E16.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3842A348-CDD4-E611-A622-02163E01494B.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5252CC19-CCD4-E611-B30E-0CC47A57CC42.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8CBD9C85-CCD4-E611-BF5F-0CC47A13CC7E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/92E44F4B-CCD4-E611-A705-0025905A60F2.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/94FF7F21-CCD4-E611-8EB5-E0071B7A45D0.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C2894049-CCD4-E611-A1E4-001E675A5244.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE42781A-CCD4-E611-93AC-1866DAEA6CC4.root' ] );


secFiles.extend( [
               ] )
