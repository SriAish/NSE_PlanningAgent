#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

python3.5 EM.py data_set/BP_n_10 4
python3.5 test.py data_set/BP_n_10 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_10 5
python3.5 test.py data_set/BP_n_10 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_10 6
python3.5 test.py data_set/BP_n_10 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_20 4
python3.5 test.py data_set/BP_n_20 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_20 5
python3.5 test.py data_set/BP_n_20 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_20 6
python3.5 test.py data_set/BP_n_20 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_30 4
python3.5 test.py data_set/BP_n_30 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_30 5
python3.5 test.py data_set/BP_n_30 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_30 6
python3.5 test.py data_set/BP_n_30 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_40 4
python3.5 test.py data_set/BP_n_40 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_40 5
python3.5 test.py data_set/BP_n_40 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_40 6
python3.5 test.py data_set/BP_n_40 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_50 4
python3.5 test.py data_set/BP_n_50 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_50 5
python3.5 test.py data_set/BP_n_50 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_50 6
python3.5 test.py data_set/BP_n_50 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_60 4
python3.5 test.py data_set/BP_n_60 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_60 5
python3.5 test.py data_set/BP_n_60 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_60 6
python3.5 test.py data_set/BP_n_60 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_70 4
python3.5 test.py data_set/BP_n_70 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_70 5
python3.5 test.py data_set/BP_n_70 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_70 6
python3.5 test.py data_set/BP_n_70 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_80 4
python3.5 test.py data_set/BP_n_80 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_80 5
python3.5 test.py data_set/BP_n_80 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_80 6
python3.5 test.py data_set/BP_n_80 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_90 4
python3.5 test.py data_set/BP_n_90 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_90 5
python3.5 test.py data_set/BP_n_90 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_90 6
python3.5 test.py data_set/BP_n_00 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.5 EM.py data_set/BP_n_100 4
python3.5 test.py data_set/BP_n_100 4
echo "--------------------"
python3.5 EM.py data_set/BP_n_100 5
python3.5 test.py data_set/BP_n_100 5
echo "--------------------"
python3.5 EM.py data_set/BP_n_100 6
python3.5 test.py data_set/BP_n_100 6
echo "--------------------"
echo "--------------------"
echo "--------------------"
