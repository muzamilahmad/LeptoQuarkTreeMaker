import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/007EF3DD-79D5-E611-871C-02163E013AFC.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/04E5B501-D9D4-E611-8387-008CFA197D2C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/24FE921C-1FD6-E611-8818-00266CFFBC38.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/56C898DF-B0D4-E611-95B9-FA163E34D56A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/602E8609-92D5-E611-9314-20CF3019DF17.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/C681EC39-D4D4-E611-B7A3-00266CFCC43C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/C6B31B71-A9D5-E611-801A-A0369FC5E22C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/E2205AF1-7FD5-E611-96EC-02163E01306F.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/E8731FCD-AED4-E611-A81B-FA163EF9B667.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/EA50A9F7-1ED6-E611-99EB-002590A8312A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/100000/F0D87C65-E7D4-E611-8DB4-549F35AD8BFD.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/062266C9-12D5-E611-A7C8-008CFA1983E0.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/0C36EF08-C1D5-E611-8BAB-FA163E9ED082.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/1CA4BD23-77D6-E611-AD7F-549F358EB796.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/48125A51-77D6-E611-8F91-02163E011557.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/50D1B849-77D6-E611-9324-001E67F33631.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/7AAD1E19-78D6-E611-81E4-02163E00C8C3.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/A024285C-08D5-E611-BAE4-008CFA1CBA7C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/A4F1100F-77D6-E611-A163-02163E019DDA.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/AE660C4E-77D6-E611-96DD-001E67E71B96.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/CE28D1FB-0AD5-E611-A631-00266CFCC9F8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/D89B0AB2-1BD5-E611-9B42-008CFA0A58F8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/50000/E855E244-0FD5-E611-9300-00266CFCC364.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/0E6E9838-7BD6-E611-9E64-02163E0145B5.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/3A414035-29D5-E611-BFB7-008CFA1CB740.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/6E3B2AE5-5FD6-E611-8437-02163E017659.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/6E530898-02D6-E611-B896-02163E0131CB.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/8E98D061-88D6-E611-901B-02163E013A71.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/901D701D-7FD5-E611-8F44-02163E00B2D9.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/BEC44028-0AD6-E611-A3C9-001E67E6F8F5.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/C2E52753-92D5-E611-92E2-FA163EB20BDE.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/E217ECFF-8CD6-E611-BAFA-00266CFFBF68.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/E833CEB9-88D6-E611-B244-00266CFBE88C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/E8AC868D-88D6-E611-A3C1-02163E011C0E.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/60000/EEE52E14-80D5-E611-A537-008CFA197C38.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/0897CE60-AFD5-E611-A95B-02163E019D28.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/26A80B5A-4BD4-E611-A409-008CFA1C6458.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/30D61947-4AD4-E611-8A87-FA163EBAEAC1.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/503A6990-1DD5-E611-8157-02163E017650.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/72731DEF-5AD4-E611-BF1B-002590494DA0.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/72FC8CCA-1CD5-E611-B1F7-002590494FE6.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/9083B9A2-46D4-E611-9D56-A0369FC5B85C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/A46B8EF8-51D4-E611-8C29-02163E01761A.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/E43087AB-18D5-E611-B599-549F35AD8BFD.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/E47A3729-42D4-E611-8372-549F358EB721.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/FC287B38-AFD5-E611-A0E1-002590747E14.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/1864FFCF-28D5-E611-AC05-FA163ED6397C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/1A957EB9-28D5-E611-B658-001E6779239C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/667ED40F-29D5-E611-A7BC-008CFA0A5684.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/A824B6DC-28D5-E611-A8E9-02163E0176A8.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/B8919F96-EAD4-E611-89F3-008CFA197D8C.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/E00EFF99-D3D4-E611-9DCF-FA163E00DC23.root',
'/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/80000/F49C0876-28D5-E611-BDC4-02163E019B9F.root' ] );


secFiles.extend( [
               ] )
