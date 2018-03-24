# -*- coding: utf-8 -*-
import os
import cv2
import glob
import numpy as np
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

#元の奴box 0 1 2 3
#xmin xmax ymin ymax
#学習データセット作成
#xmin ymin xmax ymax

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for name in glob.glob("/home/ubuntu/darknet/labels/*.txt"):
    for line in open(name, 'r'):
    print("label name is " + name)
    print("image name is " + name.replace("labels","images").replace(".txt",".jpg"))
    img = cv2.imread(name.replace("labels","images").replace(".txt",".jpg"))
        h, w = img.shape[:2]
    print(line)
    l = line.split(" ")
        print l[0]
    print l[1]
    print l[2]
    print l[3]
    print l[4]

    b = (float(l[1]), float(l[3]), float(l[2]), float(l[4]))
    bb = convert((w,h), b)
    print(str(l[0]) + " " + " ".join([str(a) for a in bb]))
    list_write_file = open(name.replace("labels", "labels_"), 'a')
    list_write_file.write(str(l[0]) + " " + " ".join([str(a) for a in bb]) + "\n")
    list_write_file.close()
    #break
