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

start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.01 0.01 > sm_3_7_01.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.001 0.001 > sm_3_7_001.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.0001 0.0001 > sm_3_7_0001.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.1 0.1 > sm_3_7_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0 0 > sm_3_7_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.2 0.2 > sm_3_7_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.3 0.3 > sm_3_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.4 0.4 > sm_3_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"