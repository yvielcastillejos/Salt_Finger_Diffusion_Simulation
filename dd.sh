#!/bin/bash
#BATCH --nodes 8
#SBATCH --ntasks-per-node=32
#SBATCH --time=24:00:00
#SBATCH --job-name=dd
#SBATCH --output=dd_%j.txt
#SBATCH --mail-type=ALL

cd ~/Nek5000/run/dd

module load intel
module load openmpi

~/Nek5000/bin/nekmpi dd 8
