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
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 10 > 7_100.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 1 > 7_10.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.9 > 7_9.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.8 > 7_8.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.7 > 7_7.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.6 > 7_6.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.5 > 7_5.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.4 > 7_4.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.3 > 7_3.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.2 > 7_2.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0.1 > 7_1.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 FSA_Agent.py 7 3 3 2 2 3 6 7_7 3 0 > 7_0.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime