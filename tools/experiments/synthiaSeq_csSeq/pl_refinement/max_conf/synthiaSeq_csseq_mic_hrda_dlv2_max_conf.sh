#!/bin/bash
EXP_NAME=synthiaSeq_csSeq_mic_hrda_dlv2_pl_refinement_max_conf
python ./tools/train.py configs/mic/synthiaSeqHR2csHR_mic_hrda_deeplab.py --launcher=slurm --l-warp-lambda=1.0 --l-warp-begin=1500 --l-mix-lambda=0.0 --warp-cutmix True --bottom-pl-fill True --max-confidence True --seed 1 --deterministic --work-dir=./work_dirs/synthia/$EXP_NAME --auto-resume True --wandbid $EXP_NAME$T
