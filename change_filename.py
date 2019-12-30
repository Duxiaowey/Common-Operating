import glob
import os
l = glob.glob('*/*/*.JPG')

for ll in l:
    os.rename(ll,ll.replace('JPG','jpg'))
