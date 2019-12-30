import os
import re
from glob import glob

anno = glob('Annotations/*')
img = glob('JPEGImages/*')

list1 = []
dict1 = {}
for a in anno:
    aa = re.split('[/.]', a)[1] # Sp_D_NRN_A_cha0036_art0090_0465
    list1.append(aa)
    s = re.split('[/_.]', a)[1:-1]
    dict1[aa] = s

# data1_path = '/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/Annotations'
# data2_path = '/home/duxiaowey/my_ps/src/faster-rcnn/data/mycasia/JPEGImages'
# file1_list = os.listdir(data1_path)
# file2_list = os.listdir(data2_path)

list2 = []
dict2 = {}
for i in img:
    ii = re.split('[/.]', i)[1] # Sp_D_NRN_A_cha0036_art0090_0465
    list2.append(ii)
    s = re.split('[/_.]', i)[1:-1]
    dict2[ii] = s           #  ['Sp', 'S', 'NNN', 'A', 'arc0051', 'arc0029', '0018']

'''删除anno字典中与img相同的元素'''
for f in list1:
    if f in list2:
        del dict1[f]

'''删除img字典中与anno相同的元素'''
for f in list2:
    if f in list1:
        del dict2[f]

cha = set(list1).difference(set(list2))

print(cha)

print(len(dict2))
