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

#### Summer16 rare backgrounds - diboson
SAMPLES=(
Summer16.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \  
Summer16.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \  
Summer16.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 \
Summer16.ZZTo4L_13TeV-amcatnloFXFX-pythia8 \
Summer16.ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Summer16.VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8 \

)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
