#Walltime
#BSUB -W 16:00
#
# Set Output file
#BSUB -o  resistance-setup.%J.log
#
# Specify node group
#BSUB -m "ls-gpu lt-gpu"
#BSUB -q gpuqueue
#
# nodes: number of nodes and GPU request
# 12 GPU's spread over 3 nodes
##BSUB -n 8 -R "rusage[mem=12] span[ptile=4]"
#BSUB -n 4 -R "rusage[mem=12]"
#BSUB -gpu "num=1:j_exclusive=yes:mode=shared"
#
# job name (default = name of script file)
#BSUB -J "resistance-setup"

build_mpirun_configfile "yank script --yaml=allmuts-sams.yaml"
mpiexec.hydra -f hostfile -configfile configfile
