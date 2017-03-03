import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/036/00000/5ECB61E4-539F-E611-A682-02163E0144AB.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/036/00000/8AEA1CCB-529F-E611-88EF-FA163E8FA971.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/036/00000/BC271AE0-539F-E611-BA5C-FA163E04D38B.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/036/00000/E4CB16DB-539F-E611-A672-FA163E0212AF.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/037/00000/127935A9-639F-E611-B116-02163E0135A0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/037/00000/3E41F8A6-639F-E611-9F27-02163E011C40.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/037/00000/F20F54BE-639F-E611-B542-02163E012562.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/038/00000/9A2913F6-969F-E611-88B9-02163E012336.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/039/00000/462362CF-8C9F-E611-B476-02163E0137FC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/040/00000/6C0B2C30-9F9F-E611-AF8E-02163E0145B7.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/041/00000/E67C7228-8E9F-E611-BEF9-02163E0126DD.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/042/00000/8A5C879C-959F-E611-8528-02163E013541.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/043/00000/0C2D5E02-B69F-E611-BFEE-FA163E7B4B8B.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/043/00000/8E546048-BA9F-E611-830D-FA163E8481D3.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/044/00000/508927A7-B19F-E611-9E4B-02163E01413D.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/02806786-BC9F-E611-86E6-02163E01387A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/06866C39-BE9F-E611-9B7D-FA163E5A1368.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/16F50422-C39F-E611-AB59-02163E0119E0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/2086D7CA-C09F-E611-9E8C-FA163EE4FD49.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/280741FA-AD9F-E611-94FF-02163E011AA7.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/3414E4EC-B39F-E611-A013-02163E0145D7.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/568E029C-A99F-E611-B381-FA163E5E6E2D.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/5C8BBC62-D59F-E611-910C-FA163EB2CA3A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/8E3B4988-AF9F-E611-91E9-02163E011E16.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/96C0AE44-BA9F-E611-B177-FA163EB04E29.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/9A54205D-B19F-E611-921A-02163E011C9A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/A8BF5B87-CD9F-E611-BD70-02163E01463E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/B29522E9-B59F-E611-8584-02163E0142DE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/C0A57C7F-D99F-E611-94BE-02163E0140E6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/C8AF306C-C79F-E611-B9F2-02163E011D00.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v3/000/284/068/00000/E6E8BCE5-A69F-E611-8DF7-02163E014725.root',
] )
