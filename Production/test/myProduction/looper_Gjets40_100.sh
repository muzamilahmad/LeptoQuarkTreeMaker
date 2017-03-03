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

#### Summer16 backgrounds - zjets
SAMPLES=(
Summer16.GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Summer16.GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Summer16.GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Summer16.GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Summer16.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
