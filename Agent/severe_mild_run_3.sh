#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=resul.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate

# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_0_3_0 3 0 0 > osm_3_7_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_1_3_0 3 0.1 0.1 > osm_3_7_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_2_3_0 3 0.2 0.2 > osm_3_7_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_3_3_0 3 0.3 0.3 > osm_3_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_4_3_0 3 0.4 0.4 > osm_3_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_10_3_0 3 10 10 > osm_3_7_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_0_3_3 3 0 0 > sm_3_7_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_1_3_3 3 0.1 0.1 > sm_3_7_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_2_3_3 3 0.2 0.2 > sm_3_7_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_3_3_3 3 0.3 0.3 > sm_3_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_4_3_3 3 0.4 0.4 > sm_3_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7_10_0_3 3 10 10 > sm_3_7_0_3_10.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7_10_6_3 3 10 10 > sm_3_7_6_3_10.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"