# dataset settings
FRAME_OFFSET = -2
dataset_type = 'ViperSeqDataset'
viper_data_root = '/coc/testnvme/datasets/VideoDA/VIPER'
bdd_data_root = '/coc/flash9/datasets/bdd100k/videoda-subset'

viper_train_flow_dir = "/coc/testnvme/datasets/VideoDA/VIPER_gen_flow/frame_dist_1/forward/train/img"

# Backward
bdd_train_flow_dir= "/coc/flash9/datasets/bdd100k_flow/t_t-1/frame_dist_2/backward/train/images"
bdd_val_flow_dir = "/coc/flash9/datasets/bdd100k_flow/t_t-1/frame_dist_2/backward/val/images"

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

crop_size = (1024, 1024)
ignore_index = [5, 3, 16, 12, 201, 255]

gta_train_pipeline = {
    "im_load_pipeline": [
        dict(type='LoadImageFromFile'),
        dict(type='LoadAnnotations'),
    ],
    "load_no_ann_pipeline": [
        dict(type='LoadImageFromFile'),
    ],
    "load_flow_pipeline": [
        dict(type='LoadFlowFromFile'),
    ],
    "shared_pipeline": [
        dict(type='Resize', img_scale=(2560, 1440)),
        dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
        dict(type='RandomFlip', prob=0.5),
    ],
    "im_pipeline": [
        # dict(type='PhotoMetricDistortion'),
        dict(type='Normalize', **img_norm_cfg),
        dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        # dict(type='DefaultFormatBundle'), #I'm not sure why I had to comment it for im, but not for flow.
        dict(type='ImageToTensor', keys=['img']),
        dict(type='Collect', keys=['img', 'gt_semantic_seg']),
    ],
    "flow_pipeline": [
        dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        dict(type='DefaultFormatBundle'), #I don't know what this is
        dict(type='Collect', keys=['img', 'gt_semantic_seg']),
    ]
}

bdd_train_pipeline = {
    "im_load_pipeline": [
        dict(type='LoadImageFromFile'),
        dict(type='LoadAnnotations'),
    ],
    "load_no_ann_pipeline": [
        dict(type='LoadImageFromFile'),
    ],
    "load_flow_pipeline": [
        dict(type='LoadFlowFromFile'),
    ],
    "shared_pipeline": [
        dict(type='Resize', img_scale=(2048, 1024)), # not sure since bdd is 720 x 1280
        dict(type='RandomCrop', crop_size=crop_size),
        dict(type='RandomFlip', prob=0.5),
    ],
    "im_pipeline": [
        # dict(type='PhotoMetricDistortion'),
        dict(type='Normalize', **img_norm_cfg),
        dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        # dict(type='DefaultFormatBundle'), 
        dict(type='ImageToTensor', keys=['img']),
        dict(type='Collect', keys=['img', 'gt_semantic_seg']),
    ],
    "flow_pipeline": [
        dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        dict(type='DefaultFormatBundle'),
        dict(type='Collect', keys=['img', 'gt_semantic_seg']),
    ]
}

test_pipeline = {
    "im_load_pipeline": [
        dict(type='LoadImageFromFile'),
        dict(type='LoadAnnotations'),
    ],
    "load_no_ann_pipeline": [
        dict(type='LoadImageFromFile'),
    ],
    "load_flow_pipeline": [
        dict(type='LoadFlowFromFile'),
    ],
    "shared_pipeline": [
        dict(type='Resize', keep_ratio=True, img_scale=(2048, 1024)),
        # dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
        dict(type='RandomFlip', prob=0.0),
    ],
    "im_pipeline": [
        # dict(type='PhotoMetricDistortion'),
        dict(type='Normalize', **img_norm_cfg),
        # dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        # dict(type='DefaultFormatBundle'),
        dict(type='ImageToTensor', keys=['img']),
        dict(type='Collect', keys=['img', 'gt_semantic_seg'])#, meta_keys=[]),
    ],
    "flow_pipeline": [
        # dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
        dict(type='DefaultFormatBundle'), #I don't know what this is
        dict(type='Collect', keys=['img', 'gt_semantic_seg'])#, meta_keys=[]),
    ]
}


data = dict(
    train=dict(
        type='UDADataset',
        source=dict(
            type='ViperSeqDataset',
            data_root=viper_data_root,
            img_dir='train/img',
            ann_dir='train/cls',
            split='splits/train.txt',
            pipeline=gta_train_pipeline,
            frame_offset=FRAME_OFFSET,
            flow_dir=viper_train_flow_dir,
        ),
        target=dict(
            type='BDDSeqDataset',
            data_root=bdd_data_root,
            img_dir='train/images',
            ann_dir='train/labels',
            split='splits/valid_imgs_train.txt',
            pipeline=bdd_train_pipeline,
            frame_offset=FRAME_OFFSET,
            flow_dir=bdd_train_flow_dir,
            ignore_index=ignore_index,
        )
    ),
    val=dict(
        type='BDDSeqDataset',
        data_root=bdd_data_root,
        img_dir='val/images',
        ann_dir='val/labels',
        split='splits/valid_imgs_val.txt',
        pipeline=test_pipeline,
        frame_offset=FRAME_OFFSET,
        flow_dir=bdd_val_flow_dir,
        ignore_index=ignore_index
    ),
    test=dict(
        type='BDDSeqDataset',
        data_root=bdd_data_root,
        img_dir='val/images',
        ann_dir='val/labels',
        split='splits/valid_imgs_val.txt',
        pipeline=test_pipeline,
        frame_offset=FRAME_OFFSET,
        flow_dir=bdd_val_flow_dir,
        ignore_index=ignore_index
    )
)