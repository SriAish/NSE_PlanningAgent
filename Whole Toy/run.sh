#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

start=`date +%s`
echo "Start learning FSA"
python3.7 EM.py data_set/Toy_train_data 2
echo "Checking Accuracy of learned FSAs"
python3.7 test.py data_set/Toy_train_data 2
echo "running agent"
python3.7 FSA_Agent_combVar.py 1 4 1 1 0 2 0 3 1_4 1 0 0 data_set/Toy_train_data 2 > LP_1_4.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
start=`date +%s`
echo "--------------------"
echo "--------------------"
start=`date +%s`
echo "Start learning FSA"
python3.7 EM.py data_set/Toy_train_data_2_4 2
echo "Checking Accuracy of learned FSAs"
python3.7 test2.py data_set/Toy_train_data_2_4 2
echo "running agent"
python3.7 FSA_Agent_combVar2.py 2 4 1 1 0 2 0 3 2_4 1 0 0 data_set/Toy_train_data_2_4 2 > LP_2_4.txt
end=`date +%s`
runtime=$((end-start))
echo $runtime
start=`date +%s`
echo "--------------------"