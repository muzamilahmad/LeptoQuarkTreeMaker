import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02407367-3705-E611-953F-0090FAA57720.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/02C565A5-9A05-E611-BA32-0090FAA57750.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/04BB75B6-4B04-E611-BF97-3417EBE6471D.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/167D66B5-4B04-E611-A7DC-00266CF9AD34.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/18604F64-3705-E611-BC36-00259073E470.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2AF0AE1E-DB04-E611-944F-00266CFAEBF8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/2E257265-7405-E611-B7B7-02163E01767A.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/3EBE9B01-9705-E611-95AE-842B2B768127.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/46FB4B22-EB04-E611-BFA6-00266CFAE740.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/4A385BEE-9605-E611-BBFC-02163E01306F.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/50A827D5-3C04-E611-A60E-00266CF9AFF0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/52303AA0-9705-E611-A12A-002590A8880A.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/5ADBB4B4-D804-E611-A6E6-008CFA001DB8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6431FB60-7204-E611-B6DE-008CFA0079C4.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/6C42BB3C-3F05-E611-BB56-02163E0177EB.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/704EAED5-DA04-E611-A61C-00266CFAE7E8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7A664BCA-EA04-E611-A78E-00266CFAE844.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7CDA0F63-1205-E611-8032-02163E01795C.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7E00F5A7-E304-E611-B7AF-3417EBE527EF.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/7E6BD2B6-4B04-E611-8445-3417EBE6471D.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/8C0206CF-4B04-E611-B430-00266CFAE764.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/903C15D2-4B04-E611-A857-008CFA002028.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/98662B7B-DC04-E611-A1D3-00266CF9B1C4.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/9A114DD6-DA04-E611-AE11-00266CF9B1C4.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/A470C3C7-4B04-E611-BC45-3417EBE64C51.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/BC9A153B-D504-E611-8C47-00266CF2679C.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/CC50E183-DC04-E611-94AE-00266CFAC6D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/CE08264C-D904-E611-89A0-00266CF9B2D4.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D038E760-7204-E611-8717-00266CFAE4C8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/D4D0D958-EB04-E611-9793-00266CFAE7D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/E4DC4AC0-9605-E611-B847-3417EBE64BAF.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/E84A669B-E304-E611-999E-00266CFAC6D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/EC220560-1205-E611-9156-001F2965648A.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/F02D3120-7204-E611-A055-00266CF268B8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/F4FB7D39-D504-E611-BC67-001D09FDD831.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/F6D5324A-3D05-E611-AFD5-02163E00EA36.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/FCCEA9CC-EA04-E611-A191-3417EBE6456D.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/0C5AF6D9-0A04-E611-87E1-02163E00C1DA.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/12489AB4-CF03-E611-B63E-7845C4FC3AB8.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/22EAB9BA-CF03-E611-A494-02163E00F8B7.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/30246111-D003-E611-9F1F-02163E015E66.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/3A5BA455-1005-E611-BAFB-00266CFAE8D0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/60080B6C-FD03-E611-BA93-02163E00EA8D.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/6266DA6F-0A05-E611-8F3E-44A84224053C.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/64B03B92-BE03-E611-B4FC-02163E012F46.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/9215CBBA-AE04-E611-B767-02163E015182.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/A024F64A-0404-E611-93A9-02163E016521.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/AA3E2AB4-3705-E611-8AB8-02163E01321A.root',
       '/store/mc/RunIISpring16MiniAODv1/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/DEEB9D12-1105-E611-9290-00259073E3C8.root',
] )
