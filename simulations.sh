#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=100G
#SBATCH -t 2-00:00:00
#SBATCH --output=temp
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
python3.7 PolicySimulation.py VI/policy_values/VIp_3_3.pkl
python3.7 PolicySimulation.py 'Convex Policy e_version/policy/C_Agent_Policy_ni_3_3_3.pkl'
python3.7 PolicySimulation.py 'Convex Policy e_version/policy/C_Agent_Policy_ni_1_3_3.pkl'
python3.7 PolicySimulation.py 'Non-Convex Policy e_version/policy/C_Agent_Policy_ni_1_3_3.pkl'
python3.7 PolicySimulation.py 'Non-Convex Policy e_version/policy/C_Agent_Policy_ni_1_3_3.pkl'
python3.7 PolicySimulation.py 'Non-Convex Policy/policy/C_Agent_Policy_nor_1_3_3.pkl'
python3.7 PolicySimulation.py 'Non-Convex Policy/policy/C_Agent_Policy_nor_3_3_3.pkl'