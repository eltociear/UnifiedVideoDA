#!/bin/bash
EXP_NAME=viper_csSeq_hrda_dlv2_accel_consis_mixup_warp_frame
python ./tools/train.py configs/mic/viperHR2csHR_mic_hrda_deeplab.py --no-masking True --launcher=slurm --l-warp-lambda=1.0 --l-warp-begin=1500 --l-mix-lambda=0.0 --warp-cutmix True --bottom-pl-fill True --TPS-warp-pl-confidence True --TPS-warp-pl-confidence-thresh 0.0 -accel True --seed 1 --deterministic --work-dir=./work_dirs/viper/$EXP_NAME --auto-resume True --wandbid $EXP_NAME$T