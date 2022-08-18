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

# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_00 1 0 0 data_set/BP_15_15_35_25 6 15 > LP_sm_1_15_1_2_6_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_00 1 0 0 data_set/BP_15_15_35_25 8 15 > LP_sm_1_15_1_2_8_0_0.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 6 15 > LP_sm_1_15_1_2_6_1_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 7 15 > LP_sm_1_15_1_2_7_1_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 8 15 > LP_sm_1_15_1_2_8_1_2.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 6 15 > LP_sm_1_15_1_2_6_1_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 7 15 > LP_sm_1_15_1_2_7_1_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 8 15 > LP_sm_1_15_1_2_8_1_1.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 6 15 > LP_sm_1_15_1_2_6_2_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 7 15 > LP_sm_1_15_1_2_7_2_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 8 15 > LP_sm_1_15_1_2_8_2_3.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_5_15_00 1 0 0 data_set/BP_15_15_35_25 5 15 > LP_sm_1_15_1_2_5_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_5_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 5 15 > LP_sm_1_15_1_2_5_1_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_5_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 5 15 > LP_sm_1_15_1_2_5_1_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_5_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 5 15 > LP_sm_1_15_1_2_5_2_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_2_15_00 1 0 0 data_set/BP_15_15_35_25 2 15 > LP_sm_1_15_1_2_2_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_2_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 2 15 > LP_sm_1_15_1_2_2_1_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_2_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 2 15 > LP_sm_1_15_1_2_2_1_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_2_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 2 15 > LP_sm_1_15_1_2_2_2_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_4_15_00 1 0 0 data_set/BP_15_15_35_25 4 15 > LP_sm_1_15_1_2_4_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_4_15_12 1 0.1 0.2 data_set/BP_15_15_35_25 4 15 > LP_sm_1_15_1_2_4_1_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_4_15_11 1 0.1 0.1 data_set/BP_15_15_35_25 4 15 > LP_sm_1_15_1_2_4_1_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_4_15_23 1 0.2 0.3 data_set/BP_15_15_35_25 4 15 > LP_sm_1_15_1_2_4_2_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# echo "--------------------"
# echo "--------------------"
# echo "--------------------"
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_00 1 0 0 data_set/BP_15_15_35_25 6 0 > LP_sm_1_0_1_2_6_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_00 1 0 0 data_set/BP_15_15_35_25 7 0 > LP_sm_1_0_1_2_7_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_00 1 0 0 data_set/BP_15_15_35_25 8 0 > LP_sm_1_0_1_2_8_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# # start=`date +%s`
# # echo "running agent"
# # python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_00 1 0 0 data_set/BP_15_15_35_25 6 15 > LP_sm_1_15_1_2_6_0_0.txt
# # end=`date +%s`
# # runtime=$((end-start))
# # echo $runtime
# # echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_00 1 0 0 data_set/BP_15_15_35_25 7 15 > LP_sm_1_15_1_2_7_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# # start=`date +%s`
# # echo "--------------------"
# # python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_00 1 0 0 data_set/BP_15_15_35_25 8 15 > LP_sm_1_15_1_2_8_0_0.txt
# # end=`date +%s`
# # runtime=$((end-start))
# # echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_00 1 0 0 data_set/BP_15_15_35_25 6 20 > LP_sm_1_20_1_2_6_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_00 1 0 0 data_set/BP_15_15_35_25 7 20 > LP_sm_1_20_1_2_7_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
# echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_00 1 0 0 data_set/BP_15_15_35_25 8 20 > LP_sm_1_20_1_2_8_0_0.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_6_15_00 1 0 0 data_set/BP_15_15_35_25 6 25 > LP_sm_1_25_1_2_6_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# echo "running agent"
# python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_7_15_00 1 0 0 data_set/BP_15_15_35_25 7 25 > LP_sm_1_25_1_2_7_0_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# start=`date +%s`
# echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_0_1_8_15_00 1 0 0 data_set/BP_15_15_35_25 8 25 > LP_sm_1_25_1_2_8_0_0.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"