#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=40G
#SBATCH -t 2-00:00:00
#SBATCH --output=result.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
echo "--------------------"
start=`date +%s`
python3.7 NCAgent_2.py 7 3 3 2 2 3 6 7_7_NSE_12_0 3 1 2 0
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 NCAgent_2.py 7 3 3 2 2 3 6 7_7_NSE_12_1 3 1 2 0.1
end=`date +%s`
runtime=$((end-start))
echo $runtime
