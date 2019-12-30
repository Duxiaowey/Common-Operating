import os

from libtiff import TIFF
from scipy import misc
import os
from PIL import Image

original_path = '/home/duxiaowey/my_ps/src/faster-rcnn/data/casia/CASIA2/Tp/'

saved_path = '/home/duxiaowey/my_ps/src/faster-rcnn/data/casia/CASIA2/Tp/'

files = os.listdir(original_path)

for file in files:
    if file.endswith('tif'):
        tif = TIFF.open(original_path+file,mode = 'r')
        im = tif.read_image()
        new_path = saved_path + file[:-3] + 'jpg'
        im = Image.fromarray(im)
        im = im.convert('RGB')
        misc.imsave(new_path,im)
        
        os.remove(original_path+file)

print('successfully saved')
