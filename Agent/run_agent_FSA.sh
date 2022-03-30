#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=resul.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate

# start=`date +%s`
# python3.7 FSA_Agent.py 3 1 1 1 2 2 2 3_3_ogt 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.01 0.01 > sm_7_01.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.04 0.04 > sm_7_04.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.06 0.06 > sm_7_06.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 1 1 > sm_7_10.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.9 0.9 > sm_7_9.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.8 0.8 > sm_7_8.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.7 0.7 > sm_7_7.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.6 0.6 > sm_7_6.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.5 0.5 > sm_7_5.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.4 0.4 > sm_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.3 0.3 > sm_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 Agent.py 7 3 3 2 2 3 6 7_7_ogt 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 -1 0.4 > m_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 -1 0.3 > m_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.1 -1 > 7_1.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0 -1 > 7_0.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 -1 0 > m_7_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7 3 0.4 0.4 > nsm_7_4.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7 3 0.3 0.3 > nsm_7_3.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7 3 0.2 0.2 > nsm_7_2.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7 3 0.1 0.1 > nsm_7_1.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 FSA_Agent_2.py 7 3 3 2 2 3 6 7_7 3 0 0 > nsm_7_0.txt
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime