#!/bin/bash

#BSUB -W 168:00
#BSUB -e %J.err
#BSUB -o %J.out
#BSUB -q gpuqueue
#BSUB -n 1
#BSUB -R "rusage[mem=4]"
#BSUB -gpu "num=1:mode=shared:mps=no:j_exclusive=yes"
#BSUB -m "lt-gpu ls-gpu"
#BSUB -J "SAMPL-13"

JOBID=13
#JOBID=$LSB_JOBINDEX
NJOBS=29
echo "Job $JOBID/$NJOBS"

source activate sampl6

echo "LSB_HOSTS: $LSB_HOSTS"
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
echo "LSB_START_JOB_MPS: $LSB_START_JOB_MPS"
echo "LSB_START_MPS: $LSB_START_MPS"
echo "CUDA_MPS_PIPE_DIR: $CUDA_MPS_PIPE_DIRECTORY"
echo "LSB_GPU_NEW_SYNTAX: $LSB_GPU_NEW_SYNTAX"
bjobs -u all -q gpuqueue -m $LSB_HOSTS
module add cuda/9.0
nvcc --version
nvidia-smi

yank script -y SAMPL.yaml --jobid=$JOBID --njobs=$NJOBS

echo "LSB_HOSTS: $LSB_HOSTS"
echo "CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"
echo "LSB_START_JOB_MPS: $LSB_START_JOB_MPS"
echo "LSB_START_MPS: $LSB_START_MPS"
echo "CUDA_MPS_PIPE_DIR: $CUDA_MPS_PIPE_DIRECTORY"
echo "LSB_GPU_NEW_SYNTAX: $LSB_GPU_NEW_SYNTAX"
bjobs -u all -q gpuqueue -m $LSB_HOSTS
module add cuda/9.0
nvcc --version
nvidia-smi

