# The new config inherits a base config to highlight the necessary modification
_base_ = '../ssd/ssd512_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(
        num_classes=4,
    ))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('aircraft', 'oiltank', 'overpass', 'playground')
data = dict(
    train=dict(
        img_prefix='data/RSOD/',
        classes=classes,
        ann_file='data/RSOD/RSOD_train.json'),
    val=dict(
        img_prefix='data/RSOD/',
        classes=classes,
        ann_file='data/RSOD/RSOD_val.json'),
    test=dict(
        img_prefix='data/RSOD/',
        classes=classes,
        ann_file='data/RSOD/RSOD_val.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/ssd512_coco_20210803_022849-0a47a1ca.pth'