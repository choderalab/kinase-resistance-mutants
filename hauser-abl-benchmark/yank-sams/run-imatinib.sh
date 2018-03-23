#!/bin/bash

#BSUB -W 168:00
#BSUB -e %J.err
#BSUB -o %J.out
#BSUB -q gpuqueue
#BSUB -n 20 -R "rusage[mem=8]"
#BSUB -gpu "num=1:mode=shared:mps=no:j_exclusive=yes"
#BSUB -m 'lt-gpu'
#BSUB -J "imatinib-test"

source activate yank-sams
build_mpirun_configfile "yank script --yaml=sams-twostage.yaml"
mpiexec -f hostfile -configfile configfile
