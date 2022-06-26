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

echo "Start learning FSA"
python3 EM.py data_set/BP_n_10 5
echo "Checking Accuracy of learned FSAs"
python3 test.py data_set/BP_n_10 5
echo "running agent"
python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0 0 data_set/BP_n_10 5 > LP_sm_1_7_0.txt
echo "--------------------"
echo "--------------------"
echo "--------------------"
echo "Start learning FSA"
python3 EM.py data_set/BP_n_30 5
echo "Checking Accuracy of learned FSAs"
python3 test.py data_set/BP_n_30 5
echo "Create FSA in the expected format"
python3 makeFSA.py data_set/BP_n_30 5
echo "running agent"
python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0 0 data_set/BP_n_30 5 > LP_sm_1_7_0.txt
echo "--------------------"
echo "--------------------"
echo "--------------------"
echo "Start learning FSA"
python3 EM.py data_set/BP_n_40 5
echo "Checking Accuracy of learned FSAs"
python3 test.py data_set/BP_n_40 5
echo "Create FSA in the expected format"
python3 makeFSA.py data_set/BP_n_40 5
echo "running agent"
python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0 0 data_set/BP_n_40 5 > LP_sm_1_7_0.txt
