OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Run2015C Prompt RECO
SCENARIO=re2015C
SAMPLES=(
Run2015C_25ns-05Oct2015-v1.SingleElectron 
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2015D re-miniAOD (part 1)
SCENARIO=re2015D
SAMPLES=(
Run2015D-05Oct2015-v1.SingleElectron 
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2015D Prompt RECO (part 2)
SCENARIO=2015Db
SAMPLES=(
Run2015D-PromptReco-v4.SingleElectron 
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

