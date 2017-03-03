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

#### global ReReco scenario
SCENARIO=2016ReMiniAOD03Feb

#### Run2016B ReReco
SAMPLES=(
Run2016B-03Feb2017_ver2-v2.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done


#### Run2016C ReReco
SAMPLES=(

Run2016C-03Feb2017-v1.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016D ReReco
SAMPLES=(

Run2016D-03Feb2017-v1.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016E ReReco
SAMPLES=(
Run2016E-03Feb2017-v1.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016F ReReco
SAMPLES=(
Run2016F-03Feb2017-v1.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016G ReReco
SAMPLES=(
Run2016G-03Feb2017-v1.SingleElectron \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016H Prompt RECO
SCENARIO=2016H
SAMPLES=(
Run2016H-03Feb2017_ver2-v1.SingleElectron  \
Run2016H-03Feb2017_ver3-v1.SingleElectron  \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done
