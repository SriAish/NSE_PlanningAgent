#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 4-00:00:00
#SBATCH --output=result2.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

python3.5 EM2.py data_set/BP_wh_10 4
python3.5 test2.py data_set/BP_wh_10 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_10 5
python3.5 test2.py data_set/BP_wh_10 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_10 6
python3.5 test2.py data_set/BP_wh_10 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_20 4
python3.5 test2.py data_set/BP_wh_20 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_20 5
python3.5 test2.py data_set/BP_wh_20 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_20 6
python3.5 test2.py data_set/BP_wh_20 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_30 4
python3.5 test2.py data_set/BP_wh_30 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_30 5
python3.5 test2.py data_set/BP_wh_30 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_30 6
python3.5 test2.py data_set/BP_wh_30 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_40 4
python3.5 test2.py data_set/BP_wh_40 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_40 5
python3.5 test2.py data_set/BP_wh_40 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_40 6
python3.5 test2.py data_set/BP_wh_40 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_50 4
python3.5 test2.py data_set/BP_wh_50 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_50 5
python3.5 test2.py data_set/BP_wh_50 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_50 6
python3.5 test2.py data_set/BP_wh_50 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_60 4
python3.5 test2.py data_set/BP_wh_60 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_60 5
python3.5 test2.py data_set/BP_wh_60 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_60 6
python3.5 test2.py data_set/BP_wh_60 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_70 4
python3.5 test2.py data_set/BP_wh_70 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_70 5
python3.5 test2.py data_set/BP_wh_70 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_70 6
python3.5 test2.py data_set/BP_wh_70 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_80 4
python3.5 test2.py data_set/BP_wh_80 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_80 5
python3.5 test2.py data_set/BP_wh_80 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_80 6
python3.5 test2.py data_set/BP_wh_80 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_90 4
python3.5 test2.py data_set/BP_wh_90 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_90 5
python3.5 test2.py data_set/BP_wh_90 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_90 6
python3.5 test2.py data_set/BP_wh_00 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_100 4
python3.5 test2.py data_set/BP_wh_100 4
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_100 5
python3.5 test2.py data_set/BP_wh_100 5
echo "--------------------"
python3.5 EM2.py data_set/BP_wh_100 6
python3.5 test2.py data_set/BP_wh_100 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
