# -*- coding:utf-8 -*-
import os
import random

train_percent = 0.9  # 训练集占数据的比例
val_percent = 0.1    # 验证集占数据的比例
test_percent = 0     # 测试集占数据集的比例

data_path = "/data/RSOD"
xmlfilepath = 'Annotations'

total_xml = os.listdir(data_path + "/" + xmlfilepath)

num = len(total_xml)        # 图片数量
list = range(num)

train_num = int(num * train_percent)  # train的数量
test_num = int(num * test_percent)    # test的数量
val_num = int(num * val_percent)      # val的数量

trainval = random.sample(list, train_num + val_num)
train = random.sample(trainval, train_num)

if not os.path.exists(os.path.join(data_path, 'ImageSets')):
    os.mkdir(os.path.join(data_path, 'ImageSets'))

ftest = open(data_path + '/ImageSets/test.txt', 'w')
ftrain = open(data_path + '/ImageSets/train.txt', 'w')
fval = open(data_path + '/ImageSets//val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)


ftrain.close()
ftest.close()
fval.close()
