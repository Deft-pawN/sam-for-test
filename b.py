# -*- coding: utf-8 -*-
import os 
import shutil
path = '/home/ubuntu/.ssh/'
path2 = '/home/ubuntu/workspace/'
def changefile():
    os.chdir(path2)
    shutil.copy("id_rsa.pub","/home/ubuntu/.ssh/") 
    shutil.copy("id_rsa","/home/ubuntu/.ssh/") 

changefile()