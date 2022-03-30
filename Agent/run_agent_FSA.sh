#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=resul.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate



start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.001 0.001 > sm_7_001.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.0001 0.0001 > sm_7_0001.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.00001 0.00001 > sm_7_00001.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
