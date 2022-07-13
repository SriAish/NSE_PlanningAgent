#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 4-00:00:00
#SBATCH --output=result5.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

python3 EM2.py data_set/BP_7_7_35_15 4
python3 test2.py data_set/BP_7_7_35_15 4
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_15 5
python3 test2.py data_set/BP_7_7_35_15 5
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_15 6
python3 test2.py data_set/BP_7_7_35_15 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_20 4
python3 test2.py data_set/BP_7_7_35_20 4
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_20 5
python3 test2.py data_set/BP_7_7_35_20 5
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_20 6
python3 test2.py data_set/BP_7_7_35_20 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_25 4
python3 test2.py data_set/BP_7_7_35_25 4
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_25 5
python3 test2.py data_set/BP_7_7_35_25 5
echo "--------------------"
python3 EM2.py data_set/BP_7_7_35_25 6
python3 test2.py data_set/BP_7_7_35_25 6