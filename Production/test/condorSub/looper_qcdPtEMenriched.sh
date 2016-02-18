#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15v2

#### Spring15 backgrounds - QCD
SAMPLES=(
Spring15v2.QCD_Pt_30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_300to470_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_470to600_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_600to800_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_800to1000_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1000to1400_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1400to1800_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1800to2400_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_2400to3200_EMEnriched_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_3200toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8 

)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
