#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=100G
#SBATCH -t 2-00:00:00
#SBATCH --output=try_SCS_7_7.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
start=`date +%s`
echo "SCS"
echo "full DCP"
python3.7 planningAgent.py
end=`date +%s`
runtime=$((end-start))
echo $runtime