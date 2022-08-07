#!/bin/bash
#SBATCH -A MLL
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
python3.7 EM2.py data/Nav_15_15_30_165 4
python3.7 test3.py data/Nav_15_15_30_165 4
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_165 5
python3.7 test3.py data/Nav_15_15_30_165 5
echo "--------------------"
python3.7 EM2.py data/Nav_15_15_30_165 6
python3.7 test3.py data/Nav_15_15_30_165 6