# -*- coding: utf-8 -*-
#example
#python output_label_list.py /home/ubuntu/darknet/001/bf664c27-a4e3-4684-aced-dc0b5a805bc7/images image_list_dog.txt
import os, csv, time
import glob
import os.path

import sys
args = sys.argv

print(len(args))
if os.path.exists(args[1]) == False:
    print("not exists path")
    sys.exit()

print("arg1:full path", args[1])
print("arg2:output filename",args[2])
image_path = args[1]
file_name = args[2]
label_path = image_path.replace("images", "labels")

image_base_list = glob.glob(os.path.join(image_path, "*.png"))
label_base_list = glob.glob(os.path.join(label_path, "*.txt"))
image_list = [os.path.basename(o).replace(".png", "") for o in image_base_list]
label_list = [os.path.basename(o).replace(".txt", "") for o in label_base_list]

image_cleaned_list = []
for i, l, ib in zip (image_list, label_list, image_base_list):
    if i in label_list:
        image_cleaned_list.append(ib)

f = open("train_"+file_name, 'w')
[f.write(i+"\n") for i in image_cleaned_list[:int(len(image_cleaned_list)*0.8)]]
f.close()

f = open("test_"+file_name, 'w')
[f.write(i+"\n") for i in image_cleaned_list[int(len(image_cleaned_list)*0.8):]]
f.close()

