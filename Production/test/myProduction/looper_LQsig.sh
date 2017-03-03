#!/bin/bash

CHECKARGS=""
OUTPUTDIR=""

#check arguments
while getopts "kd:" opt; do
  case "$opt" in
  k) CHECKARGS="${CHECKARGS} -k"
    ;;
  d) OUTPUTDIR=$OPTARG
    ;;
  esac
done

if [ -z "$OUTPUTDIR" ]; then
  echo "Need to specify output directory with -d"
  exit  
fi

./FScheck.sh ${CHECKARGS}

SCENARIO=Summer16

#### Summer16 gluino
SAMPLES=(
Summer16.LQToUE_M-200_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-250_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-300_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-350_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-400_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-450_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-500_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-550_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-600_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-650_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-700_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-750_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-800_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-850_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-900_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-950_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1000_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1050_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1100_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1150_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1200_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1250_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1300_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1350_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1400_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1450_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1500_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1550_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1600_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1650_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1700_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1750_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1800_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1850_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1900_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-1950_BetaOne_TuneCUETP8M1_13TeV-pythia8 \
Summer16.LQToUE_M-2000_BetaOne_TuneCUETP8M1_13TeV-pythia8 \


)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
