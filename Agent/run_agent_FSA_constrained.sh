#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=resul3.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate

# start=`date +%s`
# python3.7 Agent.py 3 1 1 1 1 2 2 3_3_ogt 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 Agent.py 7 3 3 2 2 3 6 7_7_ogt 3
end=`date +%s`
runtime=$((end-start))
echo $runtime