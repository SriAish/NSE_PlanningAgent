#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=100G
#SBATCH -t 2-00:00:00
#SBATCH --output=VI.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
start=`date +%s`
python3.7 VIAgent.py 3 0 0 1 1 2 2 VIp_3_3 V_3_3
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 5 1 1 2 2 4 4 VIp_5_5 V_5_5
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 7 3 3 2 2 3 6 VIp_7_7 V_7_7
end=`date +%s`
runtime=$((end-start))
echo $runtime