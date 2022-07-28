#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result4.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_3_15_corr 1 0 0 data_set/BP_15_15_35_25 3 20 >>LP_sm_1_15_0_10_3.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_4_15_corr 1 0 0 data_set/BP_15_15_35_25 4 20 >> LP_sm_1_15_0_10_4.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_5_15_corr 1 0 0 data_set/BP_15_15_35_25 5 20 >> LP_sm_1_15_0_10_5.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_corr 1 0 0 data_set/BP_15_15_35_25 6 20 >> LP_sm_1_15_0_10_6.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_corr 1 0 0 data_set/BP_15_15_35_25 7 20 >> LP_sm_1_15_0_10_7.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_corr 1 0 0 data_set/BP_15_15_35_25 8 20 >> LP_sm_1_15_0_10_8_trial.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_9_15_corr 1 0 0 data_set/BP_15_15_35_25 9 20 >> LP_sm_1_15_0_10_9_trial.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"