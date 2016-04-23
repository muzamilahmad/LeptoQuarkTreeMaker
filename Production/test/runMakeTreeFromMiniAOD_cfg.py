# otherwise edmConfigHash fails

from LeptoQuarkTreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()
inputFilesConfig=parameters.value("inputFilesConfig","")
scenarioName=parameters.value("scenario","")
outfile=parameters.value("outfile","test_run")
dataset=parameters.value("dataset",[])
nstart = parameters.value("nstart",0)
nfiles = parameters.value("nfiles",-1)
numevents=parameters.value("numevents",-1)
reportfreq=parameters.value("reportfreq",10)
doPDFs=parameters.value("doPDFs", True)


from LeptoQuarkTreeMaker.Production.scenarios import Scenario
scenario = Scenario(scenarioName)
globaltag=parameters.value("globaltag",scenario.globaltag)
tagname=parameters.value("tagname",scenario.tagname)
geninfo=parameters.value("geninfo",scenario.geninfo)
fastsim=parameters.value("fastsim",scenario.fastsim)
signal=parameters.value("signal",scenario.signal)
jsonfile=parameters.value("jsonfile",scenario.jsonfile)
jecfile=parameters.value("jecfile",scenario.jecfile)
residual=parameters.value("residual",scenario.residual)
#jecfile=parameters.value("jecfile",scenario.jecfile)
#residual=parameters.value("residual",scenario.residual)
#geninfo=parameters.value("geninfo",scenario.geninfo)
#tagname=parameters.value("tagname",scenario.tagname)
#jsonfile=parameters.value("jsonfile",scenario.jsonfile)
#globaltag=parameters.value("globaltag",scenario.globaltag)


import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2EventSelection")

from Configuration.StandardSequences.Eras import eras
process = cms.Process("RA2EventSelection",eras.Run2_25ns)

# configure geometry & conditions
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

readFiles = cms.untracked.vstring()

if inputFilesConfig!="" :
    if nfiles==-1:
        process.load("LeptoQuarkTreeMaker.Production."+inputFilesConfig+"_cff")
        readFiles.extend( process.source.fileNames )
    else:
        readFilesImport = getattr(__import__("LeptoQuarkTreeMaker.Production."+inputFilesConfig+"_cff",fromlist=["readFiles"]),"readFiles")
        readFiles.extend( readFilesImport[nstart:(nstart+nfiles)] )

if dataset!=[] :
    readFiles.extend( [dataset] )

#temporary redirector fix
#if fastsim: redir="root://cmseos.fnal.gov/"
for f,val in enumerate(readFiles):
    if readFiles[f][0:6]=="/store":
        readFiles[f] = "root://cmsxrootd.fnal.gov/"+readFiles[f]


print "***** SETUP ************************************"
print " dataset: "+str(readFiles)
print " storing PDF weights: "+str(doPDFs)
if scenario.known: print " scenario: "+scenarioName
print " global tag: "+globaltag
print " Instance name of tag information: "+tagname
print " Including gen-level information: "+str(geninfo)
print " Running signal uncertainties: "+str(signal)
#print "length of json file is : "
print len(jsonfile) 
if len(jsonfile)>0: print " JSON file applied: "+jsonfile
if len(jecfile)>0: print " JECs applied: "+jecfile+(" (residuals)" if residual else "")
print "************************************************"


from LeptoQuarkTreeMaker.LeptoQuarkTreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
process = makeTreeFromMiniAOD(process,
    outfile=outfile,
    reportfreq=reportfreq ,
    dataset=readFiles ,
    globaltag=globaltag ,
    numevents=numevents ,
    geninfo=geninfo ,
    tagname=tagname ,
    jecfile=jecfile ,
    jsonfile=jsonfile ,
    residual=residual,
    fastsim=fastsim,
    doPDFs=doPDFs
)


#process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        'file:2AC9FDED-4319-E511-AAF9-02163E011C20.root'
#    )
#)


#process.p = cms.Path()


# final tweaks to process
process.options.SkipEvent = cms.untracked.vstring('ProductNotFound')
process.TFileService.closeFileFast = cms.untracked.bool(True)
