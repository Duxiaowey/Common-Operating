import os
import os.path
import xml.dom.minidom
 
path="/home/duxiaowey/my_ps/src/faster-rcnn/data/CASIA/CASIA1/Annotations"
files=os.listdir(path)  #得到文件夹下所有文件名称

for xmlFile in files: #遍历文件夹
	# 将获取的xml文件名送入到dom解析
    dom=xml.dom.minidom.parse(os.path.join(path,xmlFile)) #输入xml文件具体路径
    root=dom.documentElement
    # 获取标签<folder>的值
    # name=root.getElementsByTagName('name')
    folder = root.getElementsByTagName('folder')
    database = root.getElementsByTagName('database')
    filename = root.getElementsByTagName('filename')

    #对每个xml文件的多个同样的属性值进行修改。此处将每一个<folder>属性修改为CASIA1,每一个<folder>属性修改为CASIA1
    for i in range(len(folder)):  
        # print (folder[i].firstChild.data)
        folder[i].firstChild.data='CASIA1'
        # print (folder[i].firstChild.data)
    for i in range(len(database)):
        database[i].firstChild.data = 'CASIA1'

    for i in range(len(filename)):
        filename[i].firstChild.data = filename[i].firstChild.data.replace('_gt.png', '.jpg')

    # 将属性存储至xml文件中
    with open(os.path.join(path,xmlFile),'w') as fh:
        dom.writexml(fh)
