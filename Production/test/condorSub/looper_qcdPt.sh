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
Spring15v2.QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8 \
Spring15v2.QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8 

)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
