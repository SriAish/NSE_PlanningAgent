#!/bin/bash
#SBATCH -A MLL
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:2
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result2.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

# echo "running agent"
echo "Checking Accuracy of learned FSAs"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 15 0.1 0.1 Nav_pol_300_7_15_1_1 > Nav_300_7_15_1_1.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300_3 5 15 1 1 Nav_pol_300_3_5_15_1_1 > Nav_300_3_5_15_1_1.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300_3 5 15 0 0 Nav_pol_300_3_5_15_0_0 > Nav_300_3_5_15_0_0.txt
# echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 15 0.1 0.1 Nav_pol_300_2_5_15_1_1 > Nav_300_2_5_15_1_1.txt
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 15 0.1 0.1 Nav_pol_300_3_15_1_1 > Nav_300_3_15_1_1.txt
echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 15 0.1 0.2 Nav_pol_300_7_15_1_2 > Nav_300_7_15_1_2.txt
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 15 0.1 0.2 Nav_pol_300_5_15_1_2 > Nav_300_5_15_1_2.txt
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 15 0.1 0.2 Nav_pol_300_3_15_1_2 > Nav_300_3_15_1_2.txt
echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 15 0.2 0.3 Nav_pol_300_7_15_2_3 > Nav_300_7_15_2_3.txt
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 15 0.2 0.3 Nav_pol_300_5_15_2_3 > Nav_300_5_15_2_3.txt
echo "--------------------"
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 15 0.2 0.3 Nav_pol_300_3_15_2_3 > Nav_300_3_15_2_3.txt
echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 20 1 1 Nav_pol_300_7_20_1_1 > Nav_300_7_20_1_1.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 20 1 1 Nav_pol_300_5_20_1_1 > Nav_300_5_20_1_1.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 20 1 1 Nav_pol_300_3_20_1_1 > Nav_300_3_20_1_1.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 20 1 2 Nav_pol_300_7_20_1_2 > Nav_300_7_20_1_2.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 20 1 2 Nav_pol_300_5_20_1_2 > Nav_300_5_20_1_2.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 20 1 2 Nav_pol_300_3_20_1_2 > Nav_300_3_20_1_2.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 20 2 3 Nav_pol_300_7_20_2_3 > Nav_300_7_20_2_3.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 20 2 3 Nav_pol_300_5_20_2_3 > Nav_300_5_20_2_3.txt
# echo "--------------------"
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 20 2 3 Nav_pol_300_3_20_2_3 > Nav_300_3_20_2_3.txt
# echo "--------------------"