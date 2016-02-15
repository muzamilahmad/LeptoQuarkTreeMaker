# LeptoQuarkTreeMaker, informations Copied from RA2b SUSY TreeMaker

## Instructions

The following installation instructions assume the user wants to process Run2015 data or Spring15 MC (miniAOD v2 format).

```
cmsrel CMSSW_7_4_15
cd CMSSW_7_4_15/src/
cmsenv
git cms-merge-topic -u kpedro88:METfix7415
git clone https://github.com/bmahakud/LeptoQuarkTreeMaker
scram b -j 8
cd LeptoQuarkTreeMaker/Production/test
```

Several predefined scenarios are available for ease of production.
These scenarios define various sample-dependent parameters, including:  
global tag, collection tag name, generator info, fastsim, signal, JSON file, JEC file, residual JECs, era.  
The available scenarios are:  
1. `Spring15v2`: for Spring15 re-miniAOD (v2) 25ns MC  
2. `Spring15v2sig`: for Spring15 re-miniAOD (v2) 25ns MC (signal)  
3. `Spring15Fastv2`: for Spring15 re-miniAOD (v2) 25ns FastSim MC (signal scans)  
4. `re2015C`: for 2015C re-reco 25ns data  
5. `re2015D`: for 2015D re-miniAOD (v2) 2015D 25ns data (part 1)  
6. `2015Db`: for 2015D PromptReco 25ns data (part 2)  

## Interactive Runs

To run interactively:
```
cmsRun runMakeTreeFromMiniAOD_cfg.py \
scenario=Spring15v2 \
dataset="/store/mc/RunIISpring15MiniAODv2/..." \
outfile="test"
```

Note that all of the background estimation processes (and some processes necessary to estimate systematic uncertainties) are turned *ON* by default in [runMakeTreeFromMiniAOD_cfg.py](./Production/test/runMakeTreeFromMiniAOD_cfg.py).

## Submit Production to Condor (@ LPC)

To reduce the size of the CMSSW tarball sent to the Condor worker node, there are a few standard directories that can be marked as cached using the script [cache_all.sh](./Production/test/cache_all.sh):
```
./cache_all.sh
```

The [test/condorSub](./Production/test/condorSub/) directory contains all of the relevant scripts.
If you copy this to another directory and run the [looper.sh](./Production/test/condorSub/looper.sh) script, it will submit one job per file to condor for all of the relevant samples. Example:
```
cp -r condorSub myProduction
cd myProduction
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction
```

The jobs open the files over xrootd, so [looper.sh](./Production/test/condorSub/looper.sh) will check that you have a valid grid proxy. 
It will also make a tarball of the current CMSSW working directory to send to the worker node. 
If you want to reuse an existing CMSSW tarball (no important changes have been made since the last time you submitted jobs), there is an extra argument:
```
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction keep
```

When the python file list for a given sample is updated, it may be desirable to submit jobs only for the new files. [looper_data_update.sh](./Production/test/condorSub/looper_data_update.sh) shows an example of how to do this.
To get the number of the first new job, just use `len(readFiles)` from the python file list *before* updating it.

If the `-d` flag is used when submitting jobs, each data file will be checked to see if the run it contains is certified in the corresponding JSON file. The JSON file is taken by default from the scenario; an alternative can be specified with the `--json` option, e.g. if the JSON is updated and you want to submit jobs only for the newly certified runs. (Use [compareJSON.py](https://github.com/cms-sw/cmssw/blob/CMSSW_7_6_X/FWCore/PythonUtilities/scripts/compareJSON.py) to subtract one JSON list from another, following [this twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGoodLumiSectionsJSONFile#How_to_compare_Good_Luminosity_f).)

Because of the large number of events in the Spring15 MC, there are now a number of looper_*.sh scripts for signal, data, and various background categories.

Sometimes, a few jobs might fail, e.g. due to xrootd connectivity problems. The script [resubCondor.sh](./Production/test/condorSub/resubCondor.sh) can identify the failed jobs and prepare them for resubmission by checking the Condor logs.
```
./resubCondor.sh "YYYY-MM-DD HH:MM" myResub.sh
./myResub.sh
```
The first parameter, if used, tells the script to look at only the jobs which finished after the specified starting date/time (default=beginning of time, "1970-01-01 00:00"). The second parameter, if used, specifies the name of the output resubmission script (default="resub.sh"). The existing JDL files are resubmitted by the resubmission script. If the script finds a failed job, it automatically checks to see if any newer instances of that job were successful (to account for multiple rounds of job submission from the same production folder).

## Calculate Integrated Luminosity

Scripts are available to calculate the integrated luminosity from data ntuples (produced with LeptoQuarkTreeMaker):
```
python lumiSummary.py
python calcLumi.py
```

The script [lumiSummary.py](./Production/test/lumiSummary.py) loops over a list of data samples (by default, a list of Run2015C and Run2015D samples) and creates a JSON
file for each sample consisting of the lumisections which were actually processed. Run `python lumiSummaryTest.py --help` to see the available options.
(This script is based on the CRAB3 client job report scripts.)

The resulting JSON file can be run through [brilcalc](http://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html) using [calcLumi.py](./Production/test/calcLumi.py)
to determine the integrated luminosity for the dataset. (NB: this only works on lxplus with brilcalc installed.)

