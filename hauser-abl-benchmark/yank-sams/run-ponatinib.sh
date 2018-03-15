#!/bin/bash

#BSUB -W 168:00
#BSUB -e %J.err
#BSUB -o %J.out
#BSUB -q gpuqueue
#BSUB -n 2 -R "rusage[mem=8]"
#BSUB -gpu "num=1:mode=shared:mps=no:j_exclusive=yes"
#BSUB -m 'ls-gpu lt-gpu'
#BSUB -J "ponatinib"

source activate py3.6
build_mpirun_configfile "yank script --yaml=ponatinib.yaml"
mpiexec -f hostfile -configfile configfile
