#!/bin/bash
#SBATCH -A Research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 4-00:00:00
#SBATCH --output=result3.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

python3.7 EM2.py data_set/BP_15_15_35_15 7
python3.7 test3.py data_set/BP_15_15_35_15 7
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_15 8
python3.7 test3.py data_set/BP_15_15_35_15 8
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_15 9
python3.7 test3.py data_set/BP_15_15_35_15 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_20 7
python3.7 test3.py data_set/BP_15_15_35_20 7
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_20 8
python3.7 test3.py data_set/BP_15_15_35_20 8
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_20 9
python3.7 test3.py data_set/BP_15_15_35_20 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_25 7
python3.7 test3.py data_set/BP_15_15_35_25 7
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_25 8
python3.7 test3.py data_set/BP_15_15_35_25 8
echo "--------------------"
python3.7 EM2.py data_set/BP_15_15_35_25 9
python3.7 test3.py data_set/BP_15_15_35_25 9