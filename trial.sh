#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=115G
#SBATCH -t 2-00:00:00
#SBATCH --output=try3.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
echo "MOSEK"
python3.7 planningAgent.py
