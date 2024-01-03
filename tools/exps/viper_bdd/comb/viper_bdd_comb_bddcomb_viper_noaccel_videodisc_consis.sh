#!/bin/bash
#SBATCH --job-name=analysisPaper_bddcomb_viper_noaccel_videodisc_consis
#SBATCH --output=analysisPaper_bddcomb_viper_noaccel_videodisc_consis.out
#SBATCH --error=analysisPaper_bddcomb_viper_noaccel_videodisc_consis.err
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=15
#SBATCH --constraint="a40"
#SBATCH --partition=short
#SBATCH --requeue
#SBATCH --open-mode=append
#SBATCH --exclude="baymax"

export PYTHONUNBUFFERED=TRUE
export MASTER_PORT=30155
source ~/.bashrc
conda activate mic
cd ~/flash9/oldFlash/VideoDA/mmsegmentation

set -x
srun python tools/train.py configs/mic/viperHR2bddHR_mic_hrda_deeplab.py --launcher=slurm --l-warp-lambda=1.0 --l-warp-begin=1500 --l-mix-lambda=0.0 --warp-cutmix True --bottom-pl-fill True --consis-filter True --no-masking True --adv-scale 1e-1 --seed 1 --deterministic --work-dir=./work_dirs/viper_bdd/bddcomb_viper_noaccel_videodisc_consis11-01-12-06-55 --auto-resume True --wandbid bddcomb_viper_noaccel_videodisc_consis11-01-12-06-55