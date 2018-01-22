import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/10A5A1D9-A5BE-E611-9A4D-0025904A8ED2.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/10B50674-A0BE-E611-BBFD-0CC47AD98F6A.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1222AA5D-A4BE-E611-A8DF-0CC47AD98BEE.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/16A3A62A-A1BE-E611-B2E8-0025901D1668.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1C8392F1-B2BE-E611-B811-047D7BD6DD58.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/26F14B11-A3BE-E611-85E7-90B11C2CB7A9.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4296A8A5-AFBE-E611-A678-0CC47AA98F92.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/54CF1198-AEBE-E611-AA1D-0CC47AD98BEE.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58A056AF-AFBE-E611-82FA-00238BCE45E0.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5CD614B1-A1BE-E611-A426-0CC47AD98F78.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62C35220-B1BE-E611-B2BB-0CC47AD99176.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/76A5676B-B0BE-E611-BFE2-0CC47AD990C4.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/828ED7B2-A9BE-E611-B56A-0CC47AD98BEE.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8C805B1A-B3BE-E611-ABEB-0CC47A13D2A4.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/989168F5-A8BE-E611-B62F-0CC47AD98D26.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A0344378-A0BE-E611-AB2C-0CC47A13CC7E.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4F97052-ACBE-E611-B90F-002590490020.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A8870262-ABBE-E611-AA66-90B11C2801E1.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B25F41FE-9DBE-E611-BFD0-0CC47AD98F78.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B4A2474B-9CBE-E611-A9B3-002590491B1E.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BC9CF1A9-AFBE-E611-B341-0CC47AD98D10.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C03254F4-A4BE-E611-BB26-0CC47AA992B0.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C4AD016E-9ABE-E611-88CC-0CC47A7DFC98.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CEC99E7A-A7BE-E611-8B08-0CC47AA992D0.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DEDFAF56-ADBE-E611-B49C-90B11C27E14D.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E6351E2F-AEBE-E611-AA03-0025904A8ED2.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EEAF06CA-A8BE-E611-BBD7-90B11C27F8B2.root',
'/store/mc/RunIISummer16MiniAODv2/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F0DC66F5-B1BE-E611-9E6D-0025901D08B8.root' ] );


secFiles.extend( [
               ] )
