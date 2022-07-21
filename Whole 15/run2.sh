#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result3.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

start=`date +%s`
# echo "Start learning FSA"
# python3.7 EM.py data_set/BP_15_15_35_25 7
# echo "Checking Accuracy of learned FSAs"
# python3.7 test.py data_set/BP_15_15_35_25 7
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_0_15 1 0 0 data_set/BP_15_15_35_25 7 15 > LP_sm_1_15_0_10_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_0_20 1 0 0 data_set/BP_15_15_35_25 7 20 >> LP_sm_1_15_0_10_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
start=`date +%s`
echo "running agent"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_0_25 1 0 0 data_set/BP_15_15_35_25 7 25 > LP_sm_1_15_0_10_2.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.4 0.4 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 3 0.4 0.4 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.5 0.5 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.8 0.8 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 1 1 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 10 10 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# echo "--------------------"
# echo "--------------------"
# start=`date +%s`
# echo "Start learning FSA"
# python3 EM.py data_set/BP_7_7_35_25 5
# echo "Checking Accuracy of learned FSAs"
# python3.7 test.py data_set/BP_7_7_35_25 5
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0 0 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_30.txt
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.1 0.1 data_set/BP_7_7_35_20 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.4 0.4 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.5 0.5 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0.8 0.8 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 1 1 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 10 10 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# echo "--------------------"
# echo "--------------------"
# # start=`date +%s`
# # echo "Start learning FSA"
# # python3 EM.py data_set/BP_7_7_35_25 5
# # echo "Checking Accuracy of learned FSAs"
# # python3.7 test.py data_set/BP_7_7_35_25 5
# # echo "running agent"
# # python3.7 FSA_Agent_combVar.py 7 3 3 2 2 3 6 7_7_0_3_0 1 0 0 data_set/BP_7_7_35_25 5 > LP_sm_1_7_0_40.txt
# # runtime=$((end-start))
# echo $runtime