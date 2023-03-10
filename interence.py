import os

from mmdet.apis import init_detector, inference_detector

# Specify the path to model config and checkpoint file
config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
# config_file = 'configs/reppoints/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck+head_2x_coco.py'
# checkpoint_file = 'checkpoints/reppoints_moment_x101_fpn_dconv_c3-c5_gn-neck+head_2x_coco_20200329-f87da1ea.pth'

imgs_path = 'data/coco/val2017'
work_path = os.path.join('D:/zqc2/1-code/mmdetection_dir', os.path.basename(config_file).split('.')[0])

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

if not os.path.exists(work_path):
    os.mkdir(work_path)

for file in os.listdir(imgs_path):
    img = os.path.join(imgs_path, file)
    result = inference_detector(model, img)
    # visualize the results in a new window
    model.show_result(img, result)
    # or save the visualization results to image files
    model.show_result(img, result, out_file=os.path.join(work_path, file))