#!/bin/bash

#BSUB -W 168:00
#BSUB -e %J.err
#BSUB -o %J.out
#BSUB -q gpuqueue
#BSUB -n 1
#BSUB -R "rusage[mem=4]"
#BSUB -gpu "num=1:mode=shared:mps=no:j_exclusive=yes"
#BSUB -m "lt-gpu ls-gpu"
#BSUB -J "imatinib-test"

JOBID=5
NJOBS=5
echo "Job $JOBID/$NJOBS"
source activate py3.6
yank script --yaml=imatinib-test.yaml --jobid=$JOBID --njobs=$NJOBS
 
