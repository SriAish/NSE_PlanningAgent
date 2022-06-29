#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result6.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

# python3.5 EM3.py data_set/BP_15_15_35_13 7
# python3.5 test3.py data_set/BP_15_15_35_13 7
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_13 8
python3.5 test3.py data_set/BP_15_15_35_13 8
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_13 9
python3.5 test3.py data_set/BP_15_15_35_13 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_26 7
python3.5 test3.py data_set/BP_15_15_35_26 7
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_26 8
python3.5 test3.py data_set/BP_15_15_35_26 8
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_26 9
python3.5 test3.py data_set/BP_15_15_35_26 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_39 7
python3.5 test3.py data_set/BP_15_15_35_39 7
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_39 8
python3.5 test3.py data_set/BP_15_15_35_39 8
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_39 9
python3.5 test3.py data_set/BP_15_15_35_39 9
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_52 7
python3.5 test3.py data_set/BP_15_15_35_52 7
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_52 8
python3.5 test3.py data_set/BP_15_15_35_52 8
echo "--------------------"
python3.5 EM3.py data_set/BP_15_15_35_52 9
python3.5 test3.py data_set/BP_15_15_35_52 9
echo "--------------------"
echo "--------------------"
echo "--------------------"