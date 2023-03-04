## Installation

step 1. prepare enviroment
```shell
conda create -n open-mmlab python=3.7 pytorch==1.7.0 cudatoolkit=10.1 torchvision -c pytorch -y
conda activate open-mmlab
pip install openmim
mim install mmcv-full
mim install mmdet
```

```shell
conda create -n openmmlab python=3.8 -y
conda activate openmmlab
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
pip install openmim
mim install mmcv-full
mim install mmdet
```

```shell
pip install opencv-python
```

step 2. make
```shell
git clone https://github.com/open-mmlab/mmrotate.git
cd mmrotate
pip install -r requirements/build.txt
pip install -v -e .
```


## Verify the installation

Step 1. We need to download config and checkpoint files.
```shell
mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .
```
Step 2. Verify the inference demo.
```shell
python demo/image_demo.py demo/demo.jpg yolov3_mobilenetv2_320_300e_coco.py yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth --device cpu --out-file result.jpg
```
You will see a new image result.jpg on your c urrent folder

## Download Dataset

```shell
python tools/misc/download_dataset.py --dataset-name coco2017
```


## Test Model:
```shell
python demo/image_demo.py demo/demo.jpg \
    configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
    checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
    --device cpu
```
