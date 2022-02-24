#!/bin/bash
#SBATCH -A research
#SBATCH --cpus-per-gpu=2
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=40G
#SBATCH -t 2-00:00:00
#SBATCH --output=resul3.txt
module add cuda/9.0
module add cudnn/7-cuda-9.0
source ~/keras/bin/activate
# start=`date +%s`
# python3.7 NCAgent.py 3 0 0 1 1 2 2 3_3 1
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 3 0 0 1 1 2 2 3_3_og 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent.py 5 1 1 2 2 5 5 5_5 1
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 5 1 1 2 2 5 5 5_5_og 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent.py 7 3 3 2 2 3 6 7_7 1
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 7 3 3 2 2 3 6 7_7_og 3 5 4
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 7 3 3 2 2 3 6 7_7_og_63 3 6 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 7 3 3 2 2 3 6 7_7_og_03 3 0 3
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
# echo "--------------------"
# start=`date +%s`
# python3.7 NCAgent4.py 7 3 3 2 2 3 6 7_7_og_12 3 1 2
# end=`date +%s`
# runtime=$((end-start))
# echo $runtime
echo "--------------------"
start=`date +%s`
python3.7 NCAgent4.py 7 3 3 2 2 3 6 7_7_og_30 3 3 0
end=`date +%s`
runtime=$((end-start))
echo $runtime