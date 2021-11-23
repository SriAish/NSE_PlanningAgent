#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=100G
#SBATCH -t 2-00:00:00
#SBATCH --output=VI2.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
start=`date +%s`
python3.7 VIAgent.py 9 5 3 3 2 4 8 VIp_9_9 V_9_9
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 11 5 3 4 3 5 10 VIp_11_11 V_11_11
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 13 7 3 5 3 6 12 VIp_13_13 V_13_13
end=`date +%s`
runtime=$((end-start))
echo $runtime