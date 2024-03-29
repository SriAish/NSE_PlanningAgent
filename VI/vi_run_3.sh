#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=100G
#SBATCH -t 2-00:00:00
#SBATCH --output=VI3.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
start=`date +%s`
python3.7 VIAgent.py 15 7 3 6 4 7 14 VIp_15_15 V_15_15
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 17 9 3 7 4 8 16 VIp_17_17 V_17_17
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 VIAgent.py 19 9 3 8 5 9 18 VIp_19_19 V_19_19
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
