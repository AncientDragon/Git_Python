#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/23/2018 11:04 AM
# @Author  : Apy
# @File    : rename.py


###rename
import os

#print "E partion include: %s "%os.listdir('E:/')
#os.rename('E:/12345', 'E:/123456')
#print "哈哈哈"


###re.findall
import re

dir_path='E:/a/'
#print os.listdir(dir_path)
for file in os.listdir(dir_path):
    #print file
    newfile=re.findall(r"\d+",file)
#    newfile=re.sub(r'\s+','.',file)
    a=newfile[0]
    print (dir_path+file,dir_path+a+".mp4")
    os.rename (dir_path+file,dir_path+a+".mp4")
    #print type(a)
os.listdir('E:/')