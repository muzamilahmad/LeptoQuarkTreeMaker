import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/0A341391-FFD5-E611-9BB7-0CC47A78A3E8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/1A9B1D28-14D6-E611-8010-0CC47A4C8F26.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/303A585B-FBD5-E611-8598-0CC47A4D7674.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/30E0A89B-05D6-E611-8675-0CC47A4D76B6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3A3C4F68-04D6-E611-BB35-0025905A609A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3C331910-FED5-E611-AE8B-0025905A60CA.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3C8D427A-06D6-E611-BB7A-0CC47A78A4B8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3E180F70-02D6-E611-9747-0CC47A78A3E8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/4E5EB9A8-0FD6-E611-A0F0-0025905B857E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/4EC285A9-10D6-E611-80DB-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/583058DA-F9D5-E611-AA15-0025905A612C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/585B5BEF-8DD6-E611-A673-008CFA197D74.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/5895F016-8DD6-E611-B290-02163E0176B6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/5CE2841E-0AD6-E611-BF31-0025905B85BC.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/5CE4F9DB-FDD5-E611-AED8-0CC47A78A3F4.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/62F0599D-8DD6-E611-9B36-0CC47AA992C8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/74DD2EDE-00D6-E611-AF62-0CC47A7C3408.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/761F838F-0CD6-E611-B3E2-0CC47A4D75F2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/809ACA45-0CD6-E611-89A1-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/8EB1B250-3AD6-E611-9B7A-0025905B85BA.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/920E5CE3-8DD6-E611-9BF6-0CC47A537688.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/946E8F3A-FCD5-E611-9931-0CC47A78A30E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A230A228-08D6-E611-A9F7-0025905A612C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A4DE849F-FED5-E611-9C69-0025905A6056.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A6198E33-1AD6-E611-BD61-FA163EABE67B.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A8E089CE-0AD6-E611-A847-0025905A6134.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/AE7C769A-05D6-E611-A14C-0025905A607E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/AEC93534-00D6-E611-958C-0025905B85DA.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/B88DCEBD-8CD6-E611-8224-0CC47A7C3444.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/C8FADA0F-07D6-E611-8E51-0025905A60F8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/D0A07CB9-08D6-E611-830A-0025905B857E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/D4ADA28C-FED5-E611-92F9-0CC47A4D7668.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/D83C6EF9-8CD6-E611-A045-FA163E0DBCEB.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/DC537BD6-8CD6-E611-BD7E-0CC47A7C34C8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E0C42EEA-00D6-E611-B861-0CC47A7C3604.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E25A35DC-8DD6-E611-A746-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E63448C9-8CD6-E611-8895-B083FED42B3B.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/F41D5E07-8DD6-E611-9771-002590FD5122.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/F817C6BE-8DD6-E611-BDDD-A4BF01013F8D.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/F81AAD39-FCD5-E611-BE97-0CC47A78A33E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/40134FC5-FCD5-E611-8E79-0CC47A78A41C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/B6606657-3AD6-E611-8E9C-0CC47A78A414.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/FE8AB856-3AD6-E611-9E21-0CC47A78A440.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/5C64F155-5CD6-E611-AE21-002481DE4938.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/888980ED-5CD6-E611-BFE6-24BE05C68671.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/986E4569-5ED6-E611-A56E-0025905A609E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/A6270E82-60D6-E611-97B2-02163E01476F.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/A8C61416-5CD6-E611-A567-001E67E6F503.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0206EFF8-28D6-E611-852A-FA163E2737AE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/02C9AE71-14D6-E611-A40A-02163E019D74.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0A9C198A-06D6-E611-B3C2-A4BADB18BC05.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0AC64F43-2ED6-E611-878D-02163E013559.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0AF6B790-DED6-E611-85CA-0CC47A4D76AC.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0C2AB9BD-25D6-E611-9273-02163E01462B.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/0EC38CC1-DAD6-E611-B26D-0CC47A4C8E34.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1216DCFE-1AD6-E611-B16D-02163E019C88.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/147D2DE1-00D6-E611-9118-782BCB50BA54.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/16422414-10D6-E611-89E8-0025905B85F6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/166D0F68-0AD6-E611-BD70-02163E0140E5.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1828864B-ABD7-E611-B1BB-0CC47A7EEF1A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/18399CBF-07D6-E611-A3E9-20CF3027A61A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1AA1C3B1-29D6-E611-BBC6-02163E01429F.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1C61B15F-17D6-E611-A56D-02163E019E74.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/1E429DB5-0BD6-E611-A7A9-008CFA1111A0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2827EF22-BBD7-E611-8EC9-001E673986B0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2A22CEFD-DCD6-E611-A645-842B2B766849.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2A536AA2-D4D6-E611-B2AF-0CC47AD98C8C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2E0677D3-D0D6-E611-AF50-00145E5521B9.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/2EB9CF09-08D6-E611-ADBA-A0369F7FC540.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/30C8FCED-F8D6-E611-9A52-02163E013998.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/32BEBB4B-0DD6-E611-8035-FA163E70C298.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/38131345-92D7-E611-AFBF-A4BF0101DBED.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3862AEDE-E6D6-E611-A8CD-002590A887F0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3893C175-16D6-E611-82FC-02163E013801.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/3ED1386D-18D6-E611-91DD-02163E019DB7.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4239D55F-09D6-E611-B4F1-008CFA1113F4.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/460008C3-ABD7-E611-98DD-008CFAF554FA.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/48AA97F1-33D6-E611-8E9D-0025907859B8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/48B78161-FAD5-E611-9D6E-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4A88D76B-12D6-E611-8F20-02163E011CF7.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4C2CF4A3-9DD7-E611-96F9-002590D9D984.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4CBA299B-20D6-E611-98C1-02163E0134F6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4E11AD85-04D6-E611-B384-0025901AC3F6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4E4C8212-03D6-E611-9BB1-008CFA152144.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/500B5356-05D6-E611-BCA1-0025905A609A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/501BA1AD-A3D7-E611-9249-7845C4FC3B8D.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/509F1D62-22D6-E611-964D-02163E011E2A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/543BE6EC-01D6-E611-A758-00259073E4DA.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/54587616-FED5-E611-BDE6-E0071B7A6890.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/54C4F6E3-07D6-E611-9B7D-02163E011749.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5890D316-D7D6-E611-84C4-008CFAF5592A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/58DDD7DE-F5D5-E611-B5C7-782BCB538FDF.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/5E330123-0ED6-E611-9EF2-1CB72C1B2D88.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/60545C0E-1DD6-E611-9240-02163E013497.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/6258CA00-11D6-E611-AF5C-02163E019C0C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7021EB93-E4D6-E611-BBD0-D8D385AF8AB2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/704197EB-D4D6-E611-AF6B-001EC94BA182.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/706445E5-FBD5-E611-B167-002481DE485A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/72F36B91-FCD5-E611-9038-A0000420FE80.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/740947B4-09D6-E611-86DC-002590E7DE20.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7AC01AED-21D6-E611-A8B7-02163E0134FF.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/7CA46F4F-C5D6-E611-8D80-00A0D1EE928C.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/80643CEA-FED5-E611-998A-A0369FC5E0A4.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8080F958-C5D6-E611-B2D2-3417EBE643DE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8090B0E0-FED5-E611-9162-B083FED429D6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/86922AD5-0AD6-E611-82A6-20CF300E9ED6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/86936A80-03D8-E611-926C-0023AEEEB208.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/86986E4F-EBD6-E611-A44C-02163E00B6BC.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/88677279-A3D9-E611-8BCA-90E2BACBAB00.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8ABA7C07-0AD6-E611-8FB4-02163E00ADA2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8C7B9030-14D6-E611-A27A-02163E011E28.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8CA830B5-0DD6-E611-9BC9-02163E019C45.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8E706A7E-04D6-E611-A795-0CC47AA98B8E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/8EBA191D-08D6-E611-B053-0CC47A78A440.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/949A5DCF-C6D6-E611-9834-90B11C06DD39.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/96353C99-DBD6-E611-AA41-008CFA197CA0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/9661F140-03D6-E611-BC39-B083FECF8ACE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/98935A18-E3D6-E611-923D-20CF3027A5CD.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/98D334F5-00D6-E611-8D47-90B11C27F101.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A4DCDE04-D2D6-E611-A059-008CFA197D98.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/A4FFF532-E2D6-E611-8E80-D067E5F914D3.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B0769C67-02D6-E611-986A-D485646A4C3A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B4C7EA85-04D6-E611-8212-008CFA1112A0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B4F5A89C-CED6-E611-9FE0-E0071B7A5540.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B8232488-18D6-E611-8D94-D8D385FF36D8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/B8D05E51-12D6-E611-957E-0026B95A45FB.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/BE52AD7D-19D6-E611-BD98-02163E01182A.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C0916629-EBD6-E611-B903-02163E0176A9.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C2B18861-06D6-E611-9665-00259048B754.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/C4ABE5DE-D4D6-E611-8432-0CC47A1E0486.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CA3EE60A-0BD6-E611-B8E7-B083FECF837B.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CADE4F95-0DD6-E611-BF0E-008CFA1113F8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CC092EAB-90D7-E611-BEA2-AC162DAB0B08.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CCB4DBC4-10D6-E611-9E68-008CFA111270.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CE7E9E20-FED5-E611-9797-001E67DDC2CC.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CECBCDF4-1BD6-E611-B893-FA163E67CBD7.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/CED1C91B-FDD5-E611-9309-782BCB53A3A6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D285A17D-1AD6-E611-86B9-0CC47A78A440.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/D43AEB1E-1ED6-E611-A02F-02163E019DE4.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/DCB501A5-08D6-E611-8CBD-0CC47A78A33E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E0CDC26C-04D6-E611-AA29-008CFA01E258.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2AE1CD6-F9D5-E611-9BDC-B083FED43141.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E2B9B670-95D7-E611-BB55-00259073E502.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E441F228-23D6-E611-9033-02163E012114.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E469998C-B2D7-E611-AF35-00269E95B1B8.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E4B935D5-01D6-E611-BF3C-0025905A607E.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/E8F3701B-0BD6-E611-8D27-0CC47AA989C6.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EA78BFEA-06D6-E611-A7D0-20CF3019DF10.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EA88C275-2CD6-E611-A9C2-02163E0128E4.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EADC0D23-0DD6-E611-9D7F-02163E011658.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EC27A3C3-97D7-E611-B6F3-008CFAFBE5CE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EC4FE097-0AD6-E611-A391-A0B3CCDFB624.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EC8FAE1D-03D6-E611-BA31-A0369F30FFD2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/ECE96A6D-10D6-E611-AC58-001E67E713FE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F0FE63F8-C2D6-E611-A095-6CC21739DBD0.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F2312A7D-FDD5-E611-A0E9-008CFA01E258.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/F2E4D9F3-14D6-E611-AD24-02163E00ADA2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FA3EE17A-D3D6-E611-81CE-0CC47A706CDE.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FCE4E007-18D6-E611-8900-001E67397CB5.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FE707F3F-09D6-E611-AB17-0CC47A7034D2.root',
'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FEFD166D-9CD7-E611-A5AD-002590DE6E8A.root' ] );


secFiles.extend( [
               ] )
