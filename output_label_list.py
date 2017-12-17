# -*- coding: utf-8 -*-
import os, csv, time
import glob

listFile = 'image_list.txt'

f = open(listFile, 'w')
for filename in glob.glob("/home/hoge/images/*.jpg"):
    print(filename)
    f.write(filename+"\n")
f.close()