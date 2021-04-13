# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:44:00 2020

@author: nikhi
"""


import os
import json
from os import listdir, getcwd
from os.path import join
from tqdm import tqdm
classes = ["table"]

#box form[x,y,w,h]

def convert(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    w = box[2]
    h = box[3]
    x = box[0] + box[2]/2.0
    y = box[1] + box[3]/2.0
    x = round(x*dw, 6)
    w = round(w*dw, 6)
    y = round(y*dh, 6)
    h = round(h*dh, 6)
    return (x,y,w,h)

def convert_annotation():
    with open('/home/le.minh.chien/Downloads/TableBank/Detection/annotations/tablebank_latex_test.json','r') as f:
        data = json.load(f)
    for idx in tqdm(range(len(data['images']))):
    # for item in data['images']:
        item = data['images'][idx]
        image_id = item['id']      
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open('/home/le.minh.chien/Downloads/TableBank/Detection/annotations/yolo_annotations/latex_test/%s.txt'%(file_name[:-4]), 'a+')
        for item2 in value:
    	    category_id = item2['category_id']
    	    value1 = list(filter(lambda item3: item3['id'] == category_id,data['categories']))
    	    name = value1[0]['name']
    	    class_id = classes.index(name)
    	    box = item2['bbox']
    	    bb = convert((width,height),box)
    	    outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()
			
if __name__ == '__main__':
    convert_annotation()
