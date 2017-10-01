import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/16C2AEB8-90C9-E611-9BC8-002590E7DF2A.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/16CCCBD7-44CA-E611-BD95-0CC47ABD6C6C.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/402B6E27-42CA-E611-B90A-0CC47ABD6C6C.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/681FA02E-38CA-E611-B627-002590E7D7D0.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/84B72F17-02CA-E611-BCDE-002590E7E050.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AC9A1BC1-52C9-E611-83C3-0CC47ABD6C6C.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/C86C745A-D1C9-E611-9759-002590E7D7EA.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/DA06F6D8-2AC9-E611-BDA8-002590E7DE20.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/00170222-86C9-E611-B0E3-141877641875.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/0C99DA27-0ACA-E611-9F69-0CC47ABB518A.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/3E95193D-ACC8-E611-88F3-00259074AE8C.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/50D19345-B8C8-E611-B167-20CF3027A5CD.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/6EF77005-AFC8-E611-B68B-002590D600B6.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/8A7DBE13-B1C8-E611-AE71-001E67580BAC.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/8C195595-AFC8-E611-B987-0090FAA57490.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/8E510FBA-77C9-E611-A381-002590E7E004.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/9A153063-74C9-E611-91E0-20CF3019DEF5.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/B4AE0F0F-7CC9-E611-BD62-0090FAA57E54.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/C6086E0A-0BCA-E611-AC5D-B083FED16468.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/162B87F0-45C8-E611-AA87-D48564593FD8.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/42F31714-CEC9-E611-A9A8-20CF300E9ECA.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4C84E5D1-3AC8-E611-BC06-20CF307C9940.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9803DADD-CCC9-E611-8BC0-00259073E516.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A6BF7471-F2C9-E611-B995-002590E7DE70.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B8B9AA5A-D1C9-E611-8B9D-D48564592B02.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/BC44F088-5CC8-E611-9466-002590E7E02E.root',
'/store/mc/RunIISummer16MiniAODv2/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E8913023-2BC9-E611-904B-0CC47ABB517C.root' ] );


secFiles.extend( [
               ] )
