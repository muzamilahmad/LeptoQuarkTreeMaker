import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/100000/B683B625-CCD0-E611-9863-02163E019DBE.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/2EEABD64-1AD1-E611-AECB-02163E019D55.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/5ACF1AAB-0BD1-E611-931B-02163E019E00.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/A0D0337E-19D1-E611-AAC1-02163E019E8D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/D6E7D54B-1BD1-E611-94CD-02163E019BC2.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/E8E498B7-0AD1-E611-97E0-02163E019BA8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/50000/F665A47C-19D1-E611-9A15-02163E019DDA.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/087CC77F-A2D1-E611-BBAF-02163E019E6F.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/12CF9557-9FD1-E611-AB5E-02163E019B29.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/20CD709C-AAD1-E611-8535-02163E019E6D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/2826290F-A1D1-E611-9186-02163E019CBA.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/285ABDB9-B5D1-E611-AC60-02163E019B4D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/3231F9F5-C0D1-E611-9B37-02163E019D1D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/4078B384-B9D1-E611-A73D-02163E019E2D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/40A013EE-A4D1-E611-ACCB-02163E019C46.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/4E6037FC-9FD1-E611-AEE2-02163E019BCC.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/5EA2DA57-9FD1-E611-852F-02163E019CF3.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/6AFBED57-9FD1-E611-850B-02163E019C48.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/742D940C-B8D1-E611-9D5F-02163E019D9D.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/7AA8E180-A2D1-E611-B8AA-02163E019D02.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/96A65258-9FD1-E611-9136-02163E019BF8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/96B39003-C2D1-E611-8844-02163E019B54.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/9836554E-BAD1-E611-B3B1-02163E019CF6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/9C007E59-9FD1-E611-BC96-02163E019D1C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/A02F31A2-9DD1-E611-BE73-02163E019DB1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/DAEF560A-9DD1-E611-9825-02163E019CF6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/E03746D4-A4D1-E611-91A0-02163E019D50.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/E2205CFB-9FD1-E611-ABFC-02163E019E62.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/E63942B8-B2D1-E611-8E3B-02163E019DE4.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/E86976B1-A8D1-E611-9A11-02163E019C83.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/EA90473C-B0D1-E611-8ED9-02163E019CE0.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/EAE0CC5C-9CD1-E611-A584-02163E019C6E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/F409AEBA-ACD1-E611-8B2F-02163E019E2A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/70000/FE7806FB-9FD1-E611-B30D-02163E019E65.root' ] );


secFiles.extend( [
               ] )
