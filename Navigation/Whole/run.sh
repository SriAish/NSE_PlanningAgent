#!/bin/bash
#SBATCH -A Research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:2
#SBATCH --mem-per-cpu=80G
#SBATCH -t 2-00:00:00
#SBATCH --output=result.txt
module add cuda/11.6
module add cudnn/8.4.0-cuda-11.6
source ~/keras/bin/activate

# echo "running agent"
echo "Checking Accuracy of learned FSAs"
# # python3.7 test.py data/Nav_15_15_30_150 4 > Nav_150_4.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_150 4 20 0 0 Nav_pol_150_4 >> Nav_150_4.txt
# echo "--------------------"
# # python3.7 test.py data/Nav_15_15_30_150 5 > Nav_150_5.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_150 5 20 0 0 Nav_pol_150_5 >> Nav_150_5.txt
# echo "--------------------"
# # python3.7 test.py data/Nav_15_15_30_150 6 > Nav_150_6.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_150 6 20 0 0 Nav_pol_150_6 >> Nav_150_6.txt
# echo "--------------------"
# # python3.7 test.py data/Nav_15_15_30_195 4 > Nav_195_4.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_195 4 20 0 0 Nav_pol_195_4 >> Nav_195_4.txt
# echo "--------------------"
# # python3.7 test.py data/Nav_15_15_30_195 5 > Nav_195_5.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_195 5 20 0 0 Nav_pol_195_5 >> Nav_195_5.txt
# echo "--------------------"
# # python3.7 test.py data/Nav_15_15_30_195 6 > Nav_195_6.txt
# python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_195 6 20 0 0 Nav_pol_195_6 >> Nav_195_6.txt
# echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 7 > Nav_300_7.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 7 20 0 0 Nav_pol_300_7 >> Nav_300_7.txt
echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 6 > Nav_300_6.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 6 20 0 0 Nav_pol_300_6 >> Nav_300_6.txt
echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 5 > Nav_300_5.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 5 20 0 0 Nav_pol_300_5 >> Nav_300_5.txt
echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 4 > Nav_300_4.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 4 20 0 0 Nav_pol_300_4 >> Nav_300_4.txt
echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 3 > Nav_300_3.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 3 20 0 0 Nav_pol_300_3 >> Nav_300_3.txt
echo "--------------------"
python3.7 test.py data/Nav_15_15_30_300 2 > Nav_300_2.txt
python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_300 2 20 0 0 Nav_pol_300_2 >> Nav_300_2.txt
echo "--------------------"