#!/bin/bash
EXP_NAME=synthiaSeq_csSeq_hrda_video_disrim
python ./tools/train.py configs/mic/synthiaSeqHR2csHR_mic_hrda_deeplab.py --launcher=slurm --no-masking True --l-warp-lambda=0.0 --l-mix-lambda=1.0 --adv-scale 1e-1 --seed 1 --deterministic --work-dir=./work_dirs/synthia/$EXP_NAME --auto-resume True --wandbid $EXP_NAME01-25-18-13-35
