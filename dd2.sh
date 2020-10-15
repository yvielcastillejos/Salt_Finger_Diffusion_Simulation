#!/bin/bash
#BATCH --nodes 1
#SBATCH --ntasks-per-node=32
#SBATCH --time=24:00:00
#SBATCH --job-name=dd
#SBATCH --output=output/dd_%j.txt
#SBATCH --mail-type=ALL

cd ~/scratch/Nek5000

module load python/3.7.4
module load scipy-stack
module load intel
module load openmpi

/cvmfs/soft.computecanada.ca/easybuild/software/2017/Core/python/3.7.4/bin/python run.py
