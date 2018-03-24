#!/bin/bash
#    Begin PBS directives
#PBS -A chm126
#PBS -N yank-imatinib-setup
#PBS -j oe
#PBS -l walltime=1:00:00,nodes=1
#PBS -l gres=atlas1%atlas2
#PBS -l feature=gpudefault
#    End PBS directives and begin shell commands
# MANUAL STEP: Change the path to the output of your `pwd`
export HOME=/lustre/atlas/scratch/jchodera1/chm126
export MINICONDA="$HOME/miniconda3"
export PATH="$MINICONDA/bin:$PATH"
export LD_LIBRARY_PATH=$MINICONDA/lib:$LD_LIBRARY_PATH
cd /lustre/atlas/scratch/jchodera1/chm126/kinase-resistance-mutants/hauser-abl-benchmark/yank/
# Run only one job to set things up
export OE_LICENSE="/lustre/atlas/scratch/jchodera1/chm126/.openeye/oe_license.txt"
aprun -n $PBS_NUM_NODES yank script --yaml=imatinib.yaml