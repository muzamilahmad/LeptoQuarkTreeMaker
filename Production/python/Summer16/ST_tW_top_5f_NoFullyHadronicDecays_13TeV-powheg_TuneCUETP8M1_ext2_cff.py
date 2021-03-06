import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/004B97C5-B8D4-E611-B069-0CC47A4D7600.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/0A4FE142-C5D4-E611-ACA4-ECF4BBE1CE08.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/18BB5022-D9D4-E611-BFDB-0CC47A4C8E1E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/1AC89805-F4D4-E611-BF1A-0CC47A4D76D2.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/20B68427-06D5-E611-9C56-001E67792496.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/227CDF9C-4AD5-E611-A12C-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/2ABB59FD-E2D4-E611-A7F4-0CC47A745250.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/30564211-91D4-E611-9275-B083FECFF52E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/367B0B86-4AD5-E611-B394-02163E00C933.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/3C2555F4-ECD4-E611-9C71-0025905A60E0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/42ACA19D-F1D4-E611-A8DF-0025905A4964.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/4A35D63D-4AD5-E611-A158-001E67E6F869.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/4AB877BF-B8D4-E611-BFCD-0CC47A4D7694.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/6052DC54-4AD5-E611-8736-0025905A612C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/662F755C-C7D4-E611-99BC-0CC47A4D7670.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/6AA364E2-A2D4-E611-B8AC-0CC47A4C8E34.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/7A5470A4-4AD5-E611-BA61-0025907793F4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/7AC036FF-CCD4-E611-BC26-0CC47A546E5E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/7C4C4DFE-CED4-E611-A440-0CC47A4C8E1C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/80FDDDCA-A8D4-E611-BFBB-0CC47A7C356A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/8829F612-BFD4-E611-A0AD-0CC47A7C361E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/8C171F9D-F1D4-E611-8D5F-0025905A6080.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/8C60D2F2-F9D4-E611-9722-0CC47A4D7650.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/90932C9D-4AD5-E611-BC87-B083FED00118.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/926E0340-FED4-E611-9C74-0CC47A4D762A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/946C3175-4AD5-E611-97CB-001E67348055.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/98E8C124-3FD5-E611-878B-02163E01772E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/B67D9D52-DDD4-E611-9CB6-0CC47A7C361E.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/B8E8EDA4-A0D4-E611-BD82-0CC47A4D7654.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/B8F46148-4AD5-E611-97D5-0090FAA57FE4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/C61BE221-ADD4-E611-AF93-0CC47A7C357A.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/D41BABC1-E5D4-E611-88B1-0CC47A4D75F4.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/D6687CFA-0ED5-E611-83E6-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/DE1E8A0D-F4D4-E611-B028-0025905A60BC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/E41A1BE5-D4D4-E611-9EC0-B083FED045ED.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/E4F7B2B3-4AD5-E611-AB4B-0CC47A4C8E64.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/ECEB13BF-C9D4-E611-871F-0CC47A4C8E20.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/F05F9D97-90D4-E611-ADEF-FA163E45D381.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/F2CC4645-29D5-E611-9FC4-FA163E94FF67.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/F2F80F00-B6D4-E611-8D00-0CC47A57D086.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/100000/F6098550-9AD4-E611-BE91-0CC47A4C8E1C.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/04EEC768-F7D4-E611-98C6-0025905B85DE.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/06C3BD5A-F7D4-E611-A46E-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/22A8C862-F7D4-E611-BD9B-0CC47A4D7668.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/2ABB957A-F7D4-E611-B0F6-002590D9D9FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/30FC0FA0-F2D4-E611-BBEF-0CC47A4D7678.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/5E7B3450-F8D4-E611-97CB-02163E0115F6.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/6E4AFE9D-F7D4-E611-8E1B-FA163E70C298.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/A472118C-F7D4-E611-B34B-001E674FCAE9.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/C24CA455-C6D4-E611-AA2A-0025905A60A0.root',
       '/store/mc/RunIISummer16MiniAODv2/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/MINIAODSIM/80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/50000/CA20DD87-F7D4-E611-8117-C81F66B78749.root',
] )
