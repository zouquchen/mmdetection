## generate RSOD dataset with COCO format
# python tools/dataset_converters/my_pascal_voc.py --devkit_path "D:/zqc2/1-code/mmdetection/data/RSOD" --out-dir "D:/zqc2/1-code/mmdetection/data/RSOD" --out-format "coco"


## Train RSOD
# python tools/train.py "configs/_mine/reppoints_moment_r50_fpn_gn-neck+head_1x_RSOD.py"
# python tools/train.py "configs/_mine/reppoints_moment_r50_fpn_gn-neck+head_2x_RSOD.py"
# python tools/train.py "configs/_mine/reppoints_moment_r101_fpn_gn-neck+head_2x_RSOD.py"
# python tools/train.py "configs/_mine/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck+head_2x_RSOD.py"                # mAP is to low
# python tools/train.py "configs/_mine/reppoints_moment_r101_fpn_dconv_c3-c5_gn-neck+head_2x_RSOD.py"

python tools/train.py "configs/_mine/cascade_rcnn_r50_fpn_1x_RSOD.py"  # encounter bug
python tools/train.py "configs/_mine/cascade_rcnn_r101_fpn_1x_RSOD.py"  # encounter bug

python tools/train.py "configs/_mine/centernet_resnet18_140e_RSOD.py"   # encounter bug

# python tools/train.py "configs/_mine/cornernet_hourglass104_mstest_10x5_210e_RSOD.py"

# python tools/train.py "configs/_mine/faster_rcnn_r50_fpn_1x_RSOD.py"
# python tools/train.py "configs/_mine/faster_rcnn_r101_fpn_1x_RSOD.py"

# python tools/train.py "configs/_mine/grid_rcnn_r50_fpn_gn-head_2x_RSOD.py"
# python tools/train.py "configs/_mine/grid_rcnn_r101_fpn_gn-head_2x_RSOD.py"

# python tools/train.py "configs/_mine/retinanet_r50_fpn_1x_RSOD.py"
# python tools/train.py "configs/_mine/retinanet_r101_fpn_1x_RSOD.py"

# python tools/train.py "configs/_mine/ssd512_RSOD.py"  # encounter bug

python tools/train.py "configs/_mine/yolov3_d53_mstrain-608_273e_RSOD.py" # encounter bug









## Inference RSOD
# python tools/test.py "configs/_mine/reppoints_moment_r50_fpn_gn-neck+head_2x_RSOD.py" "work_dirs/reppoints_moment_r50_fpn_gn-neck+head_2x_RSOD/latest.pth" --show-dir "show_dirs/reppoints_moment_r50_fpn_gn-neck+head_2x_RSOD"
python tools/test.py "configs/_mine/reppoints_moment_r101_fpn_dconv_c3-c5_gn-neck+head_2x_RSOD.py" "work_dirs/reppoints_moment_r101_fpn_dconv_c3-c5_gn-neck+head_2x_RSOD/latest.pth" --show-dir "show_dirs/reppoints_moment_r101_fpn_dconv_c3-c5_gn-neck+head_2x_RSOD"
python tools/test.py "configs/_mine/faster_rcnn_r50_fpn_1x_RSOD.py" "work_dirs/faster_rcnn_r50_fpn_1x_RSOD/latest.pth" --show-dir "show_dirs/faster_rcnn_r50_fpn_1x_RSOD"