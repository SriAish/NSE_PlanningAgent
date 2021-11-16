#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=4G
#SBATCH -t 2-00:00:00
#SBATCH --output=VI.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
python3.7 VIAgent.py