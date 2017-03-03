import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/0CAA0415-38EC-E611-AF7F-0025907277BE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/0CB052CE-3EEC-E611-B5E5-0CC47A4DED62.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/26A4768D-58EB-E611-B46F-0090FAA572C0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/2E1DF27E-37EC-E611-A696-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/326BF8CE-3EEC-E611-8D37-00259073E3FC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/48B8CA8A-58EB-E611-BFFC-0090FAA57750.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/4ECA2359-28EB-E611-AC6A-00259073E34A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/68148CCF-3EEC-E611-B460-00259073E38A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/6EEAF7F1-29EC-E611-8115-002590747E14.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/9A8FBA56-28EB-E611-9782-0CC47A4DEED6.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/A282F536-21EB-E611-A98B-0090FAA573E0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/B057FEF0-29EC-E611-9A15-0025907B4FC0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/100000/B48D07A8-48EC-E611-BD40-00259073E50A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/004F7170-E8EE-E611-9E6C-0CC47A4DEF50.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/4430462E-E5EE-E611-BB3F-00259073E502.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/84A82A09-F0EE-E611-BC69-00259073E382.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/AA92CF31-E5EE-E611-965F-0090FAA58134.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/C6703D2E-E5EE-E611-8AC5-00259073E382.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/110000/E20F772F-E5EE-E611-BC5F-00259073E516.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/00041030-DDEB-E611-B827-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/000A3F9C-7DEB-E611-BBFB-00259073E3D2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/005EF0BD-A6EB-E611-BCEB-0090FAA56994.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/00F91CE3-D7EB-E611-867B-00259073E3A8.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/02041C0E-92EB-E611-AD7A-0090FAA57AE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/020BFC7B-DDEB-E611-8BEF-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/020DC9BB-A6EB-E611-B9F9-0090FAA57C74.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/02225438-D0EB-E611-BD8D-0025907B4FC0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0256CC30-9AEB-E611-ABA3-0090FAA58D64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/084312BE-A6EB-E611-B6B2-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0865A898-7DEB-E611-B1C9-20CF3019DF17.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/08AA386B-BCEB-E611-A74D-20CF3019DF0C.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/08BEAC38-D0EB-E611-96E3-0025907277BE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0ABD0C66-E7EB-E611-B5B4-00259073E510.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0CBB037A-8CEB-E611-A84D-00259074AE3E.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0CCBC9E2-84EB-E611-B09F-0090FAA59124.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/0E462936-A0EB-E611-A107-0090FAA58BF4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/18344FF5-E5EB-E611-82F3-20CF305B04E3.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/186CE203-99EB-E611-B651-0090FAA56994.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/18A0A2C5-DDEB-E611-80E9-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/1A0CE7E4-84EB-E611-957D-0CC47A4DEF68.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/1A21059F-C9EB-E611-8BBA-00259073E398.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/1C3964E3-DEEB-E611-9F8A-20CF305B04E3.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/20B3D898-7DEB-E611-B522-0090FAA57BA0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2859EFA7-E5EB-E611-BC2C-00259074AE7A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2878F48D-C2EB-E611-9DD7-0025907B4F6C.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2A836EE2-D7EB-E611-9265-0025907B5038.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2AA3C79B-7DEB-E611-B31B-00259073E3D2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2AEDA26E-ADEB-E611-896C-0090FAA597B4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2C0CF8D9-DFEB-E611-A3A6-00259073E3A8.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2CB59237-D0EB-E611-B6F6-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2CD5069C-7DEB-E611-AC0C-00259073E3D2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2E6F6366-E7EB-E611-8B81-00259073E38A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/2ED8A703-DEEB-E611-B600-00259073E4BC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3044C6D5-75EB-E611-83AB-0090FAA58544.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/32FB57A9-BBEB-E611-9E89-0090FAA584B4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3404B1D4-D6EB-E611-BF5D-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/34CBD796-8BEB-E611-BCB7-485B3989725B.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/364D6F65-E7EB-E611-8762-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/36EAE16C-ADEB-E611-A012-0025907B4FA4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3834A738-D0EB-E611-B546-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/383E884C-E5EB-E611-A4EC-00259073E510.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/38B5E2EA-CFEB-E611-A6DC-0025907B4F6C.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3A943836-D0EB-E611-A35E-0090FAA578E0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3AAF7527-EBEB-E611-8E0B-0090FA9DFD5A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3CED99E0-D7EB-E611-9E75-0090FAA58274.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3E290DC1-B4EB-E611-BDE0-0090FAA57690.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/3E88CAE0-D7EB-E611-BF3E-0090FAA58D24.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/420A6519-93EB-E611-930C-0090FAA585D4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/42B8039B-C9EB-E611-B751-0090FAA58D84.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/444C06C2-B4EB-E611-AD04-0090FAA57D64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/44C8048F-C2EB-E611-9CEA-00259073E3FC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/48502DBF-A6EB-E611-BC7A-0090FAA57BE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4852308A-C2EB-E611-B507-0090FAA57310.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/48D766BD-A6EB-E611-8DA5-0090FAA57350.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4A055D36-D0EB-E611-8DB8-0090FAA59D74.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4A0A2415-E4EB-E611-A8F3-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4A5E4AC0-B4EB-E611-B714-0090FAA57AE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4AD1531D-EAEB-E611-A48A-0090FAA1ACF4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4C63CE8B-C2EB-E611-8FB4-00259073E398.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4CC54B93-8BEB-E611-A7F0-0090FAA57C00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4E4C48A2-C9EB-E611-A652-00259073E42E.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/4EBCD57F-E4EB-E611-9A70-0090FAA58924.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5205AFC0-B4EB-E611-948B-0090FAA58274.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/52C4A639-D0EB-E611-B9E2-00259073E4BC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5429DDD8-75EB-E611-95B3-20CF30561726.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5440BCE2-84EB-E611-959E-0090FAA58544.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/54D17E5F-D7EB-E611-8CDA-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/54FC2CE0-D7EB-E611-A7D8-0090FAA57630.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/58F685A2-8CEB-E611-AF9A-0090FAA57E94.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5A962FA2-8CEB-E611-A45D-0090FAA58204.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5A9EC084-DEEB-E611-9F68-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5CCE31C5-D7EB-E611-BFB7-0025907277BE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5CE2BC35-A0EB-E611-B120-0090FAA57AE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5E1C89D8-D6EB-E611-8E47-0090FAA57E34.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/5E9BE864-DFEB-E611-82F8-0090FAA57400.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/60567F92-8BEB-E611-991A-0090FAA584D4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/62039F9E-C9EB-E611-9EE0-00259073E3A8.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/62087BBD-A6EB-E611-B3A6-0090FAA57C74.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/6218CCA3-8CEB-E611-B588-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/62B5AA1D-92EB-E611-928E-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/649E8136-D0EB-E611-BE65-0025907B5038.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/64E81805-99EB-E611-BC7B-0090FAA58D04.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/662552A3-8CEB-E611-BECB-0090FAA57AE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/6663871A-93EB-E611-800D-002590D0B090.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/66FFEB68-BCEB-E611-AD1E-0090FAA57E94.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/68AD69BF-A6EB-E611-9F6A-0090FAA57C00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/6ABC049B-C9EB-E611-8824-0090FAA57310.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/6C0A1497-7DEB-E611-91D6-0090FAA572B0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/6C5A8569-BCEB-E611-9E2B-0090FAA59124.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/70239F35-A0EB-E611-AC21-0090FAA57660.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/72D05836-A0EB-E611-B7B7-0090FAA57410.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/741267D5-D6EB-E611-A158-00259073E50A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/7458A336-D0EB-E611-ABD1-0090FAA572C0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/74F20D7D-E9EB-E611-852E-0090FAA58134.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/766FF735-A0EB-E611-B736-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/76742DAD-BBEB-E611-8703-002590D0B008.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/76774914-E0EB-E611-A6FB-00259073E510.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/78D7DB77-DDEB-E611-8F8D-0090FAA57C00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/7A4F104B-DEEB-E611-8091-0025907277BE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/7A8F3EED-D7EB-E611-A173-00259074AE7A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/7E84A468-BCEB-E611-A102-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/7EDF256E-ADEB-E611-8073-0090FAA58D64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8015D81B-93EB-E611-87EB-20CF305B04D2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8059E2A9-BBEB-E611-88CD-0090FAA57690.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/80E3A236-D0EB-E611-A286-0CC47A4D99B0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/80F442A9-BBEB-E611-B5D7-0090FAA1ACF4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/80F6481F-DEEB-E611-82E0-0025907B5038.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/821BC235-A0EB-E611-B4A1-0090FAA57A60.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/82762DDB-DEEB-E611-951C-00259074AEDE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/84378C36-D0EB-E611-9F7E-0090FAA57FC4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/88FE951C-93EB-E611-9301-485B3989725B.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8A0E9EA4-8CEB-E611-AD18-0090FAA57A50.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8A98EAE4-84EB-E611-8EF0-0090FAA58924.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8AA63835-C9EB-E611-A97C-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8AF57D14-F1EB-E611-9858-0CC47A4DED62.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8C40A173-EAEB-E611-AD7F-0090FAA575E0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8CE2156D-ADEB-E611-BAF9-20CF305B04E3.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/8EB83A39-D0EB-E611-81DA-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/901B766B-ADEB-E611-B7E6-0090FAA57410.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/92307136-D0EB-E611-B846-0090FAA57B20.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/94307A8A-99EB-E611-90D6-002590D0AF64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/964067C0-B4EB-E611-A41B-0090FAA58824.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/9662E0CE-D8EB-E611-9E00-00259073E3A8.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/96934E17-F1EB-E611-9F35-002590D0AF64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/96F5FC6D-ADEB-E611-83A5-0090FAA578E0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/98E685C2-B4EB-E611-B8DB-0090FAA581A4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/9A2F727D-E0EB-E611-B1D3-00259073E370.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/9AA27F89-C2EB-E611-A0D8-0090FAA57770.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/9CD6F635-A0EB-E611-A7DC-0090FAA57A60.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/A0D5111B-93EB-E611-8130-0090FAA59124.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/A22FE7E8-DEEB-E611-9A4D-00259074AE7A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/A2D1476C-84ED-E611-8DA4-02163E019E21.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/A4FCCF03-99EB-E611-8236-0090FAA572B0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/A85968E4-D7EB-E611-80B6-00259074AEDE.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AA3A84E3-84EB-E611-9605-0090FAA569C4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AAE83939-D0EB-E611-83E8-0025907B4F46.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AC1B6704-99EB-E611-A0D6-0090FAA57600.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AC897E36-A0EB-E611-AEFE-0090FAA588B4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AC9D4F18-93EB-E611-B4A3-0090FAA57D04.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AE18D270-EAEB-E611-92D4-00259073E30E.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/AE9266D8-D8EB-E611-8E5D-0090FAA58134.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B0182D40-85ED-E611-8A7F-0090FAA58BF4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B0CD650A-DEEB-E611-931C-00259073E50A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B286D56F-ADEB-E611-A77C-20CF3027A62F.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B2CCCB47-D0EB-E611-8735-0090FAA57400.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B4200608-99EB-E611-B7D1-002590D0B086.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B432309B-C9EB-E611-9421-0090FAA57C74.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B4DA2A36-A0EB-E611-8380-0090FA9DFD5A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B6EE4659-D7EB-E611-AA3C-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B83424D0-D6EB-E611-9B14-0090FAA57EA4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B83B9F36-D0EB-E611-8D23-0090FAA57630.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/B87F971B-E6EB-E611-AAA2-00259073E32A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BA765E35-D0EB-E611-86FE-0090FAA58224.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BA883FAC-E8EB-E611-B49D-002590D0AF74.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BADC4578-D6EB-E611-B6DA-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BADD09AB-BBEB-E611-9D92-0090FAA57430.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BEC5C096-7DEB-E611-BDA5-0090FAA57FC4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/BEFC921F-D7EB-E611-8FB7-00259073E4BC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C01FB3DA-8BEB-E611-A1B4-00259073E50A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C073C562-E8EB-E611-A079-0090FAA57E34.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C22844E1-DEEB-E611-A9B6-0090FAA58924.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C2D800C1-A6EB-E611-A608-20CF3019DF17.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C4AA3D36-D0EB-E611-9321-0090FAA57960.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C4E9389E-C9EB-E611-8D2C-485B39897219.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C64C2F9D-C9EB-E611-A7A9-0025907B4F6C.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C6DA266B-E9EB-E611-83FC-0090FAA58924.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C8114D94-75EB-E611-8537-0CC47A4DED2A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C82D25DE-C8EB-E611-B3C9-0025907B4F6C.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/C8AE912C-92EB-E611-BA0B-0090FAA57A50.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CA62471A-93EB-E611-9EC1-002590D0AF64.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CAF1CCF9-F8EB-E611-A5CF-002590D0AFEC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CC9EDF9E-C9EB-E611-BCB9-00259073E4BC.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CCBE24A4-8CEB-E611-A1AA-0090FAA57A00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CE9F6035-A0EB-E611-AB85-0090FAA57470.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/CED1FBE2-84EB-E611-85C9-0090FAA57F34.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D01586E9-ADEB-E611-9FAE-0090FAA59124.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D07B7B84-E9EB-E611-8D78-0090FAA57400.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D2420F17-EBEB-E611-82B9-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D469F3E0-DCEB-E611-B559-0090FAA58274.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D6824D6E-ADEB-E611-AE8A-0090FAA57AF0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D80F33B2-4EEC-E611-A9B4-0025907B5038.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/D8292EBE-A6EB-E611-8C5E-0090FAA58824.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/DC227B90-DFEB-E611-BF5B-0090FAA57E34.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/DC7CCF99-7DEB-E611-9745-0090FAA57C00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/DCD7588E-C2EB-E611-9D3C-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/DE205319-93EB-E611-94A6-0090FAA56994.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/DE2EDB34-A0EB-E611-B95E-0090FAA58754.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E0A8AA68-BCEB-E611-B06E-0090FAA57430.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E0C47FE1-DEEB-E611-AC9A-0090FA9DFD5A.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E2556B89-C2EB-E611-B5F8-0090FAA588A4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E268A68B-C2EB-E611-9C1A-00259073E3F2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E28D7737-D0EB-E611-A311-0090FAA583F4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E463CDE1-84EB-E611-9673-0090FAA57630.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E47AC47C-E0EB-E611-8332-0CC47A4DEF00.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E4DDB889-C2EB-E611-B2DE-0090FAA58D84.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/E8619AA4-E8EB-E611-96E8-00259073E4EA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/ECCEB029-EBEB-E611-9228-00259073E4CA.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/EEB1A7C0-B4EB-E611-85B5-0090FAA58274.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F03950E6-84EB-E611-94E1-00259074AE3E.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F07366AA-BBEB-E611-89A3-0090FAA57AE0.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F2CE4C47-E5EB-E611-812C-0090FAA1ACF4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F2EC7CC5-B4EB-E611-96B8-00259073E3F2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F48A8E92-8BEB-E611-B652-0090FAA57420.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F4AD6C6E-EAEB-E611-9029-0090FAA57E44.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F4D37F04-99EB-E611-B865-0090FAA57ED4.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F4E0FACD-D8EB-E611-9226-00259073E510.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F6184A0A-84EE-E611-BFE1-02163E019CA7.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F81629D6-D6EB-E611-BB0E-00259073E4E2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/F8D2F36E-ADEB-E611-B28B-002590D0B008.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/FC0F429C-7DEB-E611-95C1-00259073E3D2.root',
       '/store/data/Run2016G/MET/MINIAOD/03Feb2017-v1/80000/FCCEE48B-C2EB-E611-BE3F-20CF305B0512.root',
] )
