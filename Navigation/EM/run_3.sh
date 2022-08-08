#!/bin/bash
#SBATCH -A Research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=80G
#SBATCH -t 4-00:00:00
#SBATCH --output=result3.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

echo "--------------------"
echo "--------------------"
echo "--------------------"
# python3.7 EM2.py data/Nav_15_15_30_165 4
# python3.7 test3.py data/Nav_15_15_30_165 4
# echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_165 5 > result_run3
python3.7 test3.py data/Nav_15_15_30_165 5 >> result_run3
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_165 6 >> result_run3
python3.7 test3.py data/Nav_15_15_30_165 6 >> result_run3
echo "--------------------"
echo "--------------------"
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_180 4 >> result_run3
python3.7 test3.py data/Nav_15_15_30_180 4 >> result_run3
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_180 5 >> result_run3
python3.7 test3.py data/Nav_15_15_30_180 5 >> result_run3
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_180 6 >> result_run3
python3.7 test3.py data/Nav_15_15_30_180 6 >> result_run3