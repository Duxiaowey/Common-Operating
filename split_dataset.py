import os
import random


def split_trainval():
    trainval_percent = 0.8
    train_percent = 0.9
    xmlfilepath = 'Annotations'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open('/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/ImagesSets/Main/trainval.txt', 'w')
    ftest = open('/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/ImagesSets/Main/test.txt', 'w')
    ftrain = open('/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/ImagesSets/Main/train.txt', 'w')
    fval = open('/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/ImagesSets/Main/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()


if __name__ == '__main__':
    split_trainval()
