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

SCENARIO=Spring16

#### Spring16 rare backgrounds - diboson
SAMPLES=(
Spring16.WW_TuneCUETP8M1_13TeV_pythia8 \
Spring16.WZ_TuneCUETP8M1_13TeV_pythia8 \
Spring16.ZZ_TuneCUETP8M1_13TeV_pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
