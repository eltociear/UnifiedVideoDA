#!/bin/bash
EXP_NAME=synthiaSeq_csSeq_hrda_dlv2_pl_refinement_max_conf
python ./tools/train.py configs/mic/synthiaSeqHR2csHR_mic_hrda_deeplab.py --no-masking True --launcher=slurm --l-warp-lambda=0.0 --l-mix-lambda=1.0 --warp-cutmix True --bottom-pl-fill True --max-confidence True --seed 1 --deterministic --work-dir=./work_dirs/synthia/$EXP_NAME --auto-resume True --wandbid $EXP_NAME$T
