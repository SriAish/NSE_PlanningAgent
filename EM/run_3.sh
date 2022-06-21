#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result3.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

# python3 EM3.py data_set/BP_15_15_10 7
# python3 test3.py data_set/BP_15_15_10 7
# echo "--------------------"
python3 EM3.py data_set/BP_15_15_10 8
python3 test3.py data_set/BP_15_15_10 8
echo "--------------------"
python3 EM3.py data_set/BP_15_15_10 9
python3 test3.py data_set/BP_15_15_10 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3 EM3.py data_set/BP_15_15_20 7
python3 test3.py data_set/BP_15_15_20 7
echo "--------------------"
python3 EM3.py data_set/BP_15_15_20 8
python3 test3.py data_set/BP_15_15_20 8
echo "--------------------"
python3 EM3.py data_set/BP_15_15_20 9
python3 test3.py data_set/BP_15_15_20 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3 EM3.py data_set/BP_15_15_28 7
python3 test3.py data_set/BP_15_15_28 7
echo "--------------------"
python3 EM3.py data_set/BP_15_15_28 8
python3 test3.py data_set/BP_15_15_28 8
echo "--------------------"
python3 EM3.py data_set/BP_15_15_28 9
python3 test3.py data_set/BP_15_15_28 9
echo "--------------------"
echo "--------------------"
echo "--------------------"