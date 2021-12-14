import torch
import random
import shutil
import numpy as np
import os
import sys
import shutil 
import os
import random
import pandas as pd
from glob import glob
import cv2
import csv
from skimage import io
import ipywidgets as widgets
from datetime import datetime
from skimage import img_as_float32
from tifffile import imread, imsave
from skimage.util import img_as_uint
from skimage.util import img_as_ubyte
from urllib.parse import urlparse
from cellpose import models
from ipywidgets import interact, interact_manual
from zipfile import ZIP_DEFLATED
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
from cellpose import plot
from skimage import exposure
from os import environ

#This function mooves images based on channel to channel folders 
#and extracts image metadata from img filename and renames imgs.
def move_to_chan_folder(src, nr_of_channels):
    if nr_of_channels == 1:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
    if nr_of_channels == 2:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
    if nr_of_channels == 3:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
    if nr_of_channels == 4:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
    if nr_of_channels == 5:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
        if os.path.exists(src+'/'+'chan_5') is False:         
            os.mkdir(src+'/chan_5')
    if nr_of_channels == 6:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
        if os.path.exists(src+'/'+'chan_5') is False:         
            os.mkdir(src+'/chan_5')
        if os.path.exists(src+'/'+'chan_6') is False:         
            os.mkdir(src+'/chan_6')
    if nr_of_channels == 7:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
        if os.path.exists(src+'/'+'chan_5') is False:         
            os.mkdir(src+'/chan_5')
        if os.path.exists(src+'/'+'chan_6') is False:         
            os.mkdir(src+'/chan_6')
        if os.path.exists(src+'/'+'chan_7') is False:         
            os.mkdir(src+'/chan_7')
    if nr_of_channels == 8:
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
        if os.path.exists(src+'/'+'chan_5') is False:         
            os.mkdir(src+'/chan_5')
        if os.path.exists(src+'/'+'chan_6') is False:         
            os.mkdir(src+'/chan_6')
        if os.path.exists(src+'/'+'chan_7') is False:         
            os.mkdir(src+'/chan_7')
        if os.path.exists(src+'/'+'chan_8') is False:         
            os.mkdir(src+'/chan_8')
    if nr_of_channels == 9:                     
        if os.path.exists(src+'/'+'chan_1') is False:         
            os.mkdir(src+'/chan_1')
        if os.path.exists(src+'/'+'chan_2') is False:         
            os.mkdir(src+'/chan_2')
        if os.path.exists(src+'/'+'chan_3') is False:         
            os.mkdir(src+'/chan_3')
        if os.path.exists(src+'/'+'chan_4') is False:         
            os.mkdir(src+'/chan_4')
        if os.path.exists(src+'/'+'chan_5') is False:         
            os.mkdir(src+'/chan_5')
        if os.path.exists(src+'/'+'chan_6') is False:         
            os.mkdir(src+'/chan_6')
        if os.path.exists(src+'/'+'chan_7') is False:         
            os.mkdir(src+'/chan_7')
        if os.path.exists(src+'/'+'chan_8') is False:         
            os.mkdir(src+'/chan_8')
        if os.path.exists(src+'/'+'chan_9') is False:         
            os.mkdir(src+'/chan_9')
    for root, _, files in os.walk(src):
        for file in files:
            path = os.path.join(src, file)
            if os.path.exists(path) == False:
                print(file, ': is in subfolder')
            else:
                print(file, ': is in ', src)
                if os.path.exists(src+'/'+file) == True:
                    metadata=os.path.splitext(file)[0]
                    extension=os.path.splitext(file)[1]
                    if extension == '.tif':
                        img_path=os.path.join(src, file)
                        plateid = os.path.basename(src)
                        wellid=metadata[0:3]
                        fieldid=metadata[10:13]
                        chanid=metadata[22:25]
                        newname=plateid+'_'+wellid+'_'+fieldid
                        new_path=os.path.join(src, newname+extension)
                        print(metadata, plateid, wellid, fieldid, chanid)
                        if chanid == 'C01' or 'C1':
                            move=src+'/'+'chan_1'
                        if chanid == 'C02' or 'C2':
                            move=src+'/'+'chan_2'
                        if chanid == 'C03' or 'C3':
                            move=src+'/'+'chan_3'
                        if chanid == 'C04' or 'C4':
                            move=src+'/'+'chan_4'
                        if chanid == 'C05' or 'C5':
                            move=src+'/'+'chan_5'
                        if chanid == 'C06' or 'C6':
                            move=src+'/'+'chan_6'
                        if chanid == 'C07' or 'C7':
                            move=src+'/'+'chan_7'
                        if chanid == 'C08' or 'C8':
                            move=src+'/'+'chan_8'
                        if chanid == 'C09' or 'C9':
                            move=src+'/'+'chan_9'
                        if chanid != 'C01' or 'C02' or 'C03' or 'C04' or 'C05' or 'C06' or 'C07' or 'C08' or 'C09':
                            print('chanid metadata not found')
                            pass
                        new_path=os.path.join(move, newname+extension)
                        shutil.move(img_path, new_path)

# in case you want something like mean over this H slices:
#Function that colects 4 or 3 grayscale images from a folder and outputs renamed 16 bit PNGs.
#this function also colects low and high quantile intensity values for each chanel, which are used in the next function.
def gray_to_color(src, nr_of_channels, mode):
    if mode == 'gray':
        if os.path.exists(src+'/'+'gray') is False:
            os.mkdir(src+'/'+'gray')
        if os.path.exists(src+'/'+'gray/img_intensity.csv') is False:         
            with open(src+'/'+'gray/img_intensity.csv', 'w') as csvfile:
                img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99'])
        for root, _, files in os.walk(src+'/chan_1'):
            for file in files:
                gray_path=os.path.join(src+'/'+'gray', file)
                if os.path.exists(gray_path) == True:
                    print('Gray '+file+' exists')
                    pass
                else:
                    gray = cv2.imread(chan_1_path, -1)
                    
                    chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                    chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                    if chan_1_ratio_1 < 10:
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                        chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_2 >= 10:
                            print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                        if chan_1_ratio_2 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                            chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                            print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)

                    print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99')
                    print([file, chan_1_int_Q01, chan_1_int_Q99])
                    new_row = [gray_path, chan_1_int_Q01, chan_1_int_Q99]
                    img_intensity_csv = src+'/gray/img_intensity.csv'
                    with open(img_intensity_csv, 'a+', newline='') as write_obj:
                        csv_writer = csv.writer(write_obj)
                        csv_writer.writerow(new_row)
                    print('Gray dtype: '+str(gray.dtype), 'Gray dimensions : '+str(gray.shape))
                    cv2.imwrite(gray_path, gray.astype(bitdepth))

    if mode == 'rgb':
        if os.path.exists(src+'/'+'rgb') is False:
            os.mkdir(src+'/'+'rgb')
        if nr_of_channels == 2:
            if os.path.exists(src+'/'+'rgb/img_intensity.csv') is False:         
                with open(src+'/'+'rgb/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/chan_1', file)
                    chan_2_path=os.path.join(src+'/chan_2', file)
                    rgb_path=os.path.join(src+'/'+'rgb', file)
                    if os.path.exists(rgb_path) == True:
                        print('rgb '+file+' exists')
                        pass
                    else:
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)

                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        
                        rgb = cv2.merge((chan_1, chan_2),-1)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99])
                        new_row = [rgb_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99]
                        img_intensity_csv = src+'/rgb/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('RGB dtype: '+ str(rgb.dtype), 'RGB dimensions : '+str(rgb.shape))
                        cv2.imwrite(rgb_path, rgb.astype(bitdepth))                    
                    
        if nr_of_channels == 3:
            if os.path.exists(src+'/'+'rgb/img_intensity.csv') is False:         
                with open(src+'/'+'rgb/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/chan_1', file)
                    chan_2_path=os.path.join(src+'/chan_2', file)
                    chan_3_path=os.path.join(src+'/chan_3', file)
                    chan_4_path=os.path.join(src+'/chan_4', file)
                    rgb_path=os.path.join(src+'/'+'rgb', file)
                    if os.path.exists(rgb_path) == True:
                        print('rgb '+file+' exists')
                        pass
                    else:
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)

                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)

                        
                        rgb = cv2.merge((chan_1, chan_2, chan_3),-1)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99])
                        new_row = [rgb_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99]
                        img_intensity_csv = src+'/rgb/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('RGB dtype: '+ str(rgb.dtype), 'RGB dimensions : '+str(rgb.shape))
                        cv2.imwrite(rgb_path, rgb.astype(bitdepth))
                        
    if mode == 'rgba': 
        if nr_of_channels == 4:
            if os.path.exists(src+'/'+'rgba') is False:
                os.mkdir(src+'/'+'rgba')
            if os.path.exists(src+'/rgba/img_intensity.csv') is False:         
                with open(src+'/rgba/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99'])

            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/chan_1', file)
                    chan_2_path=os.path.join(src+'/chan_2', file)
                    chan_3_path=os.path.join(src+'/chan_3', file)
                    chan_4_path=os.path.join(src+'/chan_4', file)
                    rgba_path=os.path.join(src+'/'+'rgba', file)
                    if os.path.exists(rgba_path) == True:
                        print('rgba '+file+' exists')
                        pass
                    else:
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        
                        rgba = cv2.merge((chan_1, chan_2, chan_3, chan_4),-1)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99])
                        new_row = [rgba_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99]
                        img_intensity_csv = src+'/rgba/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('RGBA dtype: '+ str(rgba.dtype), 'RGBA dimensions : '+str(rgba.shape))
                        cv2.imwrite(rgba_path, rgba.astype(bitdepth))
    
    if mode == 'stack':
        if os.path.exists(src+'/'+'stack') is False:
            os.mkdir(src+'/'+'stack')
        
        if nr_of_channels == 1:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:
                        chan_1 = cv2.imread(chan_1_path, -1)
                        stack = np.stack([chan_1], axis=-1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99])
                        new_row = [rgb_path, chan_1_int_Q01, chan_1_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)                    
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))

                                            
        if nr_of_channels == 2:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        stack = np.stack([chan_1, chan_2], axis=-1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                                                    
        if nr_of_channels == 3:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        stack = np.stack([chan_1, chan_2, chan_3], axis=-1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                                                    
        if nr_of_channels == 4:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99'])
                    print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99')
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    name=os.path.splitext(file)[0]
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    stack_path=os.path.join(src+'/'+'stack', name+'.npy')
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4], axis=2)
                        print(stack.shape)
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))

        if nr_of_channels == 5:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    chan_5_path=os.path.join(src+'/'+'chan_5', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        chan_5 = cv2.imread(chan_5_path, -1)
                        
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.99))
                        chan_5_ratio_1 = int(chan_5_int_Q99/chan_5_int_Q01)
                        if chan_5_ratio_1 < 10:
                            chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.999))
                            chan_5_ratio_2 = int(chan_5_int_Q99/chan_5_int_Q01)
                            if chan_5_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2)
                            if chan_5_ratio_2 <10:
                                chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.001, 0.9999))
                                chan_5_ratio_3 = int(chan_5_int_Q99/chan_5_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2, chan_5_ratio_3)
                        
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5], axis=-1)
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                                                    
        if nr_of_channels == 6:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    chan_5_path=os.path.join(src+'/'+'chan_5', file)
                    chan_6_path=os.path.join(src+'/'+'chan_6', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        chan_5 = cv2.imread(chan_5_path, -1)
                        chan_6 = cv2.imread(chan_6_path, -1)
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6], axis=-1)
                                                
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.99))
                        chan_5_ratio_1 = int(chan_5_int_Q99/chan_5_int_Q01)
                        if chan_5_ratio_1 < 10:
                            chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.999))
                            chan_5_ratio_2 = int(chan_5_int_Q99/chan_5_int_Q01)
                            if chan_5_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2)
                            if chan_5_ratio_2 <10:
                                chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.001, 0.9999))
                                chan_5_ratio_3 = int(chan_5_int_Q99/chan_5_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2, chan_5_ratio_3)
                        chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.99))
                        chan_6_ratio_1 = int(chan_6_int_Q99/chan_6_int_Q01)
                        if chan_6_ratio_1 < 10:
                            chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.999))
                            chan_6_ratio_2 = int(chan_6_int_Q99/chan_6_int_Q01)
                            if chan_6_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2)
                            if chan_6_ratio_2 <10:
                                chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.001, 0.9999))
                                chan_6_ratio_3 = int(chan_6_int_Q99/chan_6_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2, chan_6_ratio_3)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                                                    
        if nr_of_channels == 7:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    chan_5_path=os.path.join(src+'/'+'chan_5', file)
                    chan_6_path=os.path.join(src+'/'+'chan_6', file)
                    chan_7_path=os.path.join(src+'/'+'chan_7', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        chan_5 = cv2.imread(chan_5_path, -1)
                        chan_6 = cv2.imread(chan_6_path, -1)
                        chan_7 = cv2.imread(chan_7_path, -1)
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7], axis=-1)
                                                
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.99))
                        chan_5_ratio_1 = int(chan_5_int_Q99/chan_5_int_Q01)
                        if chan_5_ratio_1 < 10:
                            chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.999))
                            chan_5_ratio_2 = int(chan_5_int_Q99/chan_5_int_Q01)
                            if chan_5_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2)
                            if chan_5_ratio_2 <10:
                                chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.001, 0.9999))
                                chan_5_ratio_3 = int(chan_5_int_Q99/chan_5_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2, chan_5_ratio_3)
                        chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.99))
                        chan_6_ratio_1 = int(chan_6_int_Q99/chan_6_int_Q01)
                        if chan_6_ratio_1 < 10:
                            chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.999))
                            chan_6_ratio_2 = int(chan_6_int_Q99/chan_6_int_Q01)
                            if chan_6_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2)
                            if chan_6_ratio_2 <10:
                                chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.001, 0.9999))
                                chan_6_ratio_3 = int(chan_6_int_Q99/chan_6_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2, chan_6_ratio_3)
                        chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.99))
                        chan_7_ratio_1 = int(chan_7_int_Q99/chan_7_int_Q01)
                        if chan_7_ratio_1 < 10:
                            chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.999))
                            chan_7_ratio_2 = int(chan_7_int_Q99/chan_7_int_Q01)
                            if chan_7_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2)
                            if chan_7_ratio_2 <10:
                                chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.001, 0.9999))
                                chan_7_ratio_3 = int(chan_7_int_Q99/chan_7_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2, chan_7_ratio_3)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                                                    
        if nr_of_channels == 8:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99', 'chan_8_int_Q01', 'chan_8_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    chan_5_path=os.path.join(src+'/'+'chan_5', file)
                    chan_6_path=os.path.join(src+'/'+'chan_6', file)
                    chan_7_path=os.path.join(src+'/'+'chan_7', file)
                    chan_8_path=os.path.join(src+'/'+'chan_8', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:                    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        chan_5 = cv2.imread(chan_5_path, -1)
                        chan_6 = cv2.imread(chan_6_path, -1)
                        chan_7 = cv2.imread(chan_7_path, -1)
                        chan_8 = cv2.imread(chan_8_path, -1)
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8], axis=-1)
                                                
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.99))
                        chan_5_ratio_1 = int(chan_5_int_Q99/chan_5_int_Q01)
                        if chan_5_ratio_1 < 10:
                            chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.999))
                            chan_5_ratio_2 = int(chan_5_int_Q99/chan_5_int_Q01)
                            if chan_5_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2)
                            if chan_5_ratio_2 <10:
                                chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.001, 0.9999))
                                chan_5_ratio_3 = int(chan_5_int_Q99/chan_5_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2, chan_5_ratio_3)
                        chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.99))
                        chan_6_ratio_1 = int(chan_6_int_Q99/chan_6_int_Q01)
                        if chan_6_ratio_1 < 10:
                            chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.999))
                            chan_6_ratio_2 = int(chan_6_int_Q99/chan_6_int_Q01)
                            if chan_6_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2)
                            if chan_6_ratio_2 <10:
                                chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.001, 0.9999))
                                chan_6_ratio_3 = int(chan_6_int_Q99/chan_6_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2, chan_6_ratio_3)
                        chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.99))
                        chan_7_ratio_1 = int(chan_7_int_Q99/chan_7_int_Q01)
                        if chan_7_ratio_1 < 10:
                            chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.999))
                            chan_7_ratio_2 = int(chan_7_int_Q99/chan_7_int_Q01)
                            if chan_7_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2)
                            if chan_7_ratio_2 <10:
                                chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.001, 0.9999))
                                chan_7_ratio_3 = int(chan_7_int_Q99/chan_7_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2, chan_7_ratio_3)
                        chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.01, 0.99))
                        chan_8_ratio_1 = int(chan_8_int_Q99/chan_8_int_Q01)
                        if chan_8_ratio_1 < 10:
                            chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.01, 0.999))
                            chan_8_ratio_2 = int(chan_8_int_Q99/chan_8_int_Q01)
                            if chan_8_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_8 Q01/Q99', chan_8_ratio_1, chan_8_ratio_2)
                            if chan_8_ratio_2 <10:
                                chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.001, 0.9999))
                                chan_8_ratio_3 = int(chan_8_int_Q99/chan_8_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_8 Q01/Q99', chan_8_ratio_1, chan_8_ratio_2, chan_8_ratio_3)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99', 'chan_8_int_Q01', 'chan_8_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99, chan_8_int_Q01, chan_8_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99, chan_8_int_Q01, chan_8_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        np.save(stack_path, stack.astype(bitdepth))
                        
        if nr_of_channels == 9:
            if os.path.exists(src+'/'+'stack/img_intensity.csv') is False:         
                with open(src+'/'+'stack/img_intensity.csv', 'w') as csvfile:
                    img_intensity = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    img_intensity.writerow(['chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99', 'chan_8_int_Q01', 'chan_8_int_Q99', 'chan_9_int_Q01', 'chan_9_int_Q99'])
            for root, _, files in os.walk(src+'/chan_1'):
                for file in files:
                    chan_1_path=os.path.join(src+'/'+'chan_1', file)
                    chan_2_path=os.path.join(src+'/'+'chan_2', file)
                    chan_3_path=os.path.join(src+'/'+'chan_3', file)
                    chan_4_path=os.path.join(src+'/'+'chan_4', file)
                    chan_5_path=os.path.join(src+'/'+'chan_5', file)
                    chan_6_path=os.path.join(src+'/'+'chan_6', file)
                    chan_7_path=os.path.join(src+'/'+'chan_7', file)
                    chan_8_path=os.path.join(src+'/'+'chan_8', file)
                    chan_9_path=os.path.join(src+'/'+'chan_9', file)
                    stack_path=os.path.join(src+'/'+'stack', file)
                    if os.path.exists(stack_path) == True:
                        print('stack '+file+' exists')
                        pass     
                    else:    
                        chan_1 = cv2.imread(chan_1_path, -1)
                        chan_2 = cv2.imread(chan_2_path, -1)
                        chan_3 = cv2.imread(chan_3_path, -1)
                        chan_4 = cv2.imread(chan_4_path, -1)
                        chan_5 = cv2.imread(chan_5_path, -1)
                        chan_6 = cv2.imread(chan_6_path, -1)
                        chan_7 = cv2.imread(chan_7_path, -1)
                        chan_8 = cv2.imread(chan_8_path, -1)
                        chan_9 = cv2.imread(chan_9_path, -1)
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8, chan_9], axis=-1)
                                                
                        chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.99))
                        chan_1_ratio_1 = int(chan_1_int_Q99/chan_1_int_Q01)
                        if chan_1_ratio_1 < 10:
                            chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.01, 0.999))
                            chan_1_ratio_2 = int(chan_1_int_Q99/chan_1_int_Q01)
                            if chan_1_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2)
                            if chan_1_ratio_2 < 10:
                                chan_1_int_Q01, chan_1_int_Q99 = np.quantile(chan_1, (.001, 0.9999))
                                chan_1_ratio_3 = int(chan_1_int_Q99/chan_1_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_1 Q01/Q99', chan_1_ratio_1, chan_1_ratio_2, chan_1_ratio_3)
                        chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.99))
                        chan_2_ratio_1 = int(chan_2_int_Q99/chan_2_int_Q01)
                        if chan_2_ratio_1 < 10:
                            chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.01, 0.999))
                            chan_2_ratio_2 = int(chan_2_int_Q99/chan_2_int_Q01)
                            if chan_2_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2)
                            if chan_2_ratio_2 < 10:
                                chan_2_int_Q01, chan_2_int_Q99 = np.quantile(chan_2, (.001, 0.9999))
                                chan_2_ratio_3 = int(chan_2_int_Q99/chan_2_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_2 Q01/Q99', chan_2_ratio_1, chan_2_ratio_2, chan_2_ratio_3)
                        chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.99))
                        chan_3_ratio_1 = int(chan_3_int_Q99/chan_3_int_Q01)
                        if chan_3_ratio_1 < 10:
                            chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.01, 0.999))
                            chan_3_ratio_2 = int(chan_3_int_Q99/chan_3_int_Q01)
                            if chan_3_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2)
                            if chan_3_ratio_2 < 10:
                                chan_3_int_Q01, chan_3_int_Q99 = np.quantile(chan_3, (.001, 0.9999))
                                chan_3_ratio_3 = int(chan_3_int_Q99/chan_3_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_3 Q01/Q99', chan_3_ratio_1, chan_3_ratio_2, chan_3_ratio_3)
                        chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.99))
                        chan_4_ratio_1 = int(chan_4_int_Q99/chan_4_int_Q01)
                        if chan_4_ratio_1 < 10:
                            chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.01, 0.999))
                            chan_4_ratio_2 = int(chan_4_int_Q99/chan_4_int_Q01)
                            if chan_4_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2)
                            if chan_4_ratio_2 <10:
                                chan_4_int_Q01, chan_4_int_Q99 = np.quantile(chan_4, (.001, 0.9999))
                                chan_4_ratio_3 = int(chan_4_int_Q99/chan_4_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_4 Q01/Q99', chan_4_ratio_1, chan_4_ratio_2, chan_4_ratio_3)
                        chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.99))
                        chan_5_ratio_1 = int(chan_5_int_Q99/chan_5_int_Q01)
                        if chan_5_ratio_1 < 10:
                            chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.01, 0.999))
                            chan_5_ratio_2 = int(chan_5_int_Q99/chan_5_int_Q01)
                            if chan_5_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2)
                            if chan_5_ratio_2 <10:
                                chan_5_int_Q01, chan_5_int_Q99 = np.quantile(chan_5, (.001, 0.9999))
                                chan_5_ratio_3 = int(chan_5_int_Q99/chan_5_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_5 Q01/Q99', chan_5_ratio_1, chan_5_ratio_2, chan_5_ratio_3)
                        chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.99))
                        chan_6_ratio_1 = int(chan_6_int_Q99/chan_6_int_Q01)
                        if chan_6_ratio_1 < 10:
                            chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.01, 0.999))
                            chan_6_ratio_2 = int(chan_6_int_Q99/chan_6_int_Q01)
                            if chan_6_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2)
                            if chan_6_ratio_2 <10:
                                chan_6_int_Q01, chan_6_int_Q99 = np.quantile(chan_6, (.001, 0.9999))
                                chan_6_ratio_3 = int(chan_6_int_Q99/chan_6_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_6 Q01/Q99', chan_6_ratio_1, chan_6_ratio_2, chan_6_ratio_3)
                        chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.99))
                        chan_7_ratio_1 = int(chan_7_int_Q99/chan_7_int_Q01)
                        if chan_7_ratio_1 < 10:
                            chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.01, 0.999))
                            chan_7_ratio_2 = int(chan_7_int_Q99/chan_7_int_Q01)
                            if chan_7_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2)
                            if chan_7_ratio_2 <10:
                                chan_7_int_Q01, chan_7_int_Q99 = np.quantile(chan_7, (.001, 0.9999))
                                chan_7_ratio_3 = int(chan_7_int_Q99/chan_7_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_7 Q01/Q99', chan_7_ratio_1, chan_7_ratio_2, chan_7_ratio_3)
                        chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.01, 0.99))
                        chan_8_ratio_1 = int(chan_8_int_Q99/chan_8_int_Q01)
                        if chan_8_ratio_1 < 10:
                            chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.01, 0.999))
                            chan_8_ratio_2 = int(chan_8_int_Q99/chan_8_int_Q01)
                            if chan_8_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_8 Q01/Q99', chan_8_ratio_1, chan_8_ratio_2)
                            if chan_8_ratio_2 <10:
                                chan_8_int_Q01, chan_8_int_Q99 = np.quantile(chan_8, (.001, 0.9999))
                                chan_8_ratio_3 = int(chan_8_int_Q99/chan_8_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_8 Q01/Q99', chan_8_ratio_1, chan_8_ratio_2, chan_8_ratio_3)
                        chan_9_int_Q01, chan_9_int_Q99 = np.quantile(chan_9, (.01, 0.99))
                        chan_9_ratio_1 = int(chan_9_int_Q99/chan_9_int_Q01)
                        if chan_9_ratio_1 < 10:
                            chan_9_int_Q01, chan_9_int_Q99 = np.quantile(chan_9, (.01, 0.999))
                            chan_9_ratio_2 = int(chan_9_int_Q99/chan_9_int_Q01)
                            if chan_9_ratio_2 >= 10:
                                print('WARNING: Q99 set to 0.999 for: chan_9 Q01/Q99', chan_9_ratio_1, chan_9_ratio_2)
                            if chan_9_ratio_2 <10:
                                chan_9_int_Q01, chan_9_int_Q99 = np.quantile(chan_9, (.001, 0.9999))
                                chan_9_ratio_3 = int(chan_9_int_Q99/chan_9_int_Q01)
                                print('WARNING: Q01 set to 0.001 Q99 set to 0.9999 for: chan_9 Q01/Q99', chan_9_ratio_1, chan_9_ratio_2, chan_9_ratio_3)
                        
                        print('file name', 'chan_1_int_Q01', 'chan_1_int_Q99', 'chan_2_int_Q01', 'chan_2_int_Q99', 'chan_3_int_Q01', 'chan_3_int_Q99', 'chan_4_int_Q01', 'chan_4_int_Q99', 'chan_5_int_Q01', 'chan_5_int_Q99', 'chan_6_int_Q01', 'chan_6_int_Q99', 'chan_7_int_Q01', 'chan_7_int_Q99', 'chan_8_int_Q01', 'chan_8_int_Q99', 'chan_9_int_Q01', 'chan_9_int_Q99')
                        print([file, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99, chan_8_int_Q01, chan_8_int_Q99, chan_9_int_Q01, chan_9_int_Q99])
                        new_row = [stack_path, chan_1_int_Q01, chan_1_int_Q99, chan_2_int_Q01, chan_2_int_Q99, chan_3_int_Q01, chan_3_int_Q99, chan_4_int_Q01, chan_4_int_Q99, chan_5_int_Q01, chan_5_int_Q99, chan_6_int_Q01, chan_6_int_Q99, chan_7_int_Q01, chan_7_int_Q99, chan_8_int_Q01, chan_8_int_Q99, chan_9_int_Q01, chan_9_int_Q99]
                        img_intensity_csv = src+'/stack/img_intensity.csv'
                        with open(img_intensity_csv, 'a+', newline='') as write_obj:
                            csv_writer = csv.writer(write_obj)
                            csv_writer.writerow(new_row)               
                        print('Stack dtype: '+str(stack.dtype), 'Stack dimensions : '+str(stack.shape))
                        cv2.imwrite(stack_path, stack.astype(bitdepth))


#This Function prinsts each image and channel in a stack.                 
def plot_arrays_in_stack(stack):
    stack_dim = stack.shape
    channel = stack_dim[2]
    image_dim = stack_dim[3]
    if len(stack_dim)==4:
        a, b, c = np.split(stack, 3, axis=3)
        if a.shape == b.shape == c.shape:
            n_dim=len(a.shape)
        
            dim=a.shape #dimensions of image
            channel_position=dim.index(channel)
            
            print('Stack dimensions: ', stack_dim)
            print('Image index: ', image_dim)
            print('Channel index: ', channel_position)
            print("img has "+str(n_dim)+" dimensions")
            channel_image_a=a.shape[2]
            channel_image_b=b.shape[2]
            channel_image_c=c.shape[2]
            
            fig, axs = plt.subplots(1, channel_image_a,figsize=(20,20))
            
            for channel in range(channel_image_a):
                axs[channel].imshow(a[:,:,channel])
                axs[channel].set_title('Slice '+str(channel+1),size=18)
                axs[channel].axis('off')
            fig, axs = plt.subplots(1, channel_image_b,figsize=(20,20))
            for channel in range(channel_image_b):
                axs[channel].imshow(b[:,:,channel])
                axs[channel].set_title('Slice '+str(channel+3),size=18)
                axs[channel].axis('off')
            fig, axs = plt.subplots(1, channel_image_c,figsize=(20,20))
            for channel in range(channel_image_c):
                axs[channel].imshow(c[:,:,channel])
                axs[channel].set_title('Slice '+str(channel+6),size=18)
                axs[channel].axis('off')
                
# explicit function to normalize array
def normalize_array(arr, chan):
    norm_arr = []
    diff = 10000 - 1
    if chan == '1':
        diff_arr = chan_1_int_Q99 - chan_1_int_Q5
        Q5 = chan_1_int_Q5
    if chan == '2':
        diff_arr = chan_2_int_Q99 - chan_2_int_Q5
        Q5 = chan_2_int_Q5
    if chan == '3':
        diff_arr = chan_3_int_Q99 - chan_3_int_Q5
        Q5 = chan_3_int_Q5
    if chan == '4':
        diff_arr = chan_4_int_Q99 - chan_4_int_Q5
        Q5 = chan_4_int_Q5
    if chan == '5':
        diff_arr = chan_5_int_Q99 - chan_5_int_Q5
        Q5 = chan_5_int_Q5
    if chan == '6':
        diff_arr = chan_6_int_Q99 - chan_6_int_Q5
        Q5 = chan_6_int_Q5
    if chan == '7':
        diff_arr = chan_7_int_Q99 - chan_7_int_Q5
        Q5 = chan_7_int_Q5
    if chan == '8':
        diff_arr = chan_8_int_Q99 - chan_8_int_Q5
        Q5 = chan_8_int_Q5
    if chan == '9':
        diff_arr = chan_9_int_Q99 - chan_9_int_Q5
        Q5 = chan_9_int_Q5
    if environ.get('Q5') is not None: 
        for i in arr:
            temp = (((i - Q5)*diff)/diff_arr) + Q5
            norm_arr.append(temp)
    #return norm_arr
    
#This Function uses the intensity quantiles colected in 'gray_to_color' and normalizes
#images on a per plate and per channel bases to the respective quantiles. 
def rescal_intensity(src, nr_of_channels, mode):
    if environ.get('chan_1_upperQnr2') is None:
        chan_1_upperQnr2 = 0.99
    if environ.get('chan_2_upperQnr2') is None:
        chan_2_upperQnr2 = 0.99
    if environ.get('chan_3_upperQnr2') is None:
        chan_3_upperQnr2 = 0.99
    if environ.get('chan_4_upperQnr2') is None:
        chan_4_upperQnr2 = 0.99
    if environ.get('chan_5_upperQnr2') is None:
        chan_5_upperQnr2 = 0.99
    if environ.get('chan_6_upperQnr2') is None:
        chan_6_upperQnr2 = 0.99
    if environ.get('chan_7_upperQnr2') is None:
        chan_7_upperQnr2 = 0.99
    if environ.get('chan_8_upperQnr2') is None:
        chan_8_upperQnr2 = 0.99
    if environ.get('chan_9_upperQnr2') is None:
        chan_9_upperQnr2 = 0.99
    
    if os.path.exists(src+'/'+'gray') is True:
        mode = 'gray'
        img_intensity_csv = src+'/gray/img_intensity.csv'
        if os.path.exists(src+'/'+'gray_orig') is False:         
            os.mkdir(src+'/'+'gray_orig')
                                          
    if os.path.exists(src+'/'+'rgb') is True:
        mode = 'rgb'
        img_intensity_csv = src+'/rgb/img_intensity.csv'
        if os.path.exists(src+'/'+'rgb_orig') is False:         
            os.mkdir(src+'/'+'rgb_orig')
                                       
    if os.path.exists(src+'/'+'rgba') is True:
        mode = 'rgba'
        img_intensity_csv = src+'/rgba/img_intensity.csv'
        if os.path.exists(src+'/'+'rgba_orig') is False:         
            os.mkdir(src+'/'+'rgba_orig')
                       
    if os.path.exists(src+'/'+'stack') is True: 
        mode = 'stack'
        img_intensity_csv = src+'/stack/img_intensity.csv'
        if os.path.exists(src+'/'+'stack_orig') is False:         
            os.mkdir(src+'/'+'stack_orig')
        
    df = pd.read_csv (img_intensity_csv)
                                          
    if nr_of_channels == 1:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        print('file name', 'chan_1_int_Q5', 'chan_1_int_Q99')
    if nr_of_channels == 2:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        print('file name', 'chan_1_int_Q5', 'chan_1_int_Q99', 'chan_2_int_Q5', 'chan_2_int_Q99')
    if nr_of_channels == 3:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        print('file name', 'chan_1_int_Q5', 'chan_1_int_Q99', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99')                                          
    if nr_of_channels == 4:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        
        chan_1_signal_to_nois = chan_1_int_Q99/chan_1_int_Q5
        if chan_1_signal_to_nois < 10:
            print('WARNING: Increasing upper intensity quantile to 0.999')
            chan_1_upperQnr2=0.999
            chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        
        chan_2_signal_to_nois = chan_2_int_Q99/chan_2_int_Q5
        if chan_2_signal_to_nois < 10:
            print('WARNING: Increasing upper intensity quantile to 0.999')
            chan_2_upperQnr2=0.999
            chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        
        chan_3_signal_to_nois = chan_3_int_Q99/chan_3_int_Q5
        if chan_3_signal_to_nois < 10:
            print('WARNING: Increasing upper intensity quantile to 0.999')
            chan_3_upperQnr2=0.999
            chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        
        chan_4_signal_to_nois = chan_4_int_Q99/chan_4_int_Q5
        if chan_4_signal_to_nois < 10:
            print('WARNING: Increasing upper intensity quantile to 0.999')
            chan_4_upperQnr2=0.999
            chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        
        chan_1_signal_to_nois = chan_1_int_Q99/chan_1_int_Q5
        if chan_1_signal_to_nois < 10:
            print('WARNING: forground/background < 10: chan_1')
            
        chan_2_signal_to_nois = chan_2_int_Q99/chan_2_int_Q5
        if chan_1_signal_to_nois < 10:
            print('WARNING: forground/background < 10: chan_2')
            
        chan_3_signal_to_nois = chan_3_int_Q99/chan_3_int_Q5
        if chan_1_signal_to_nois < 10:
            print('WARNING: forground/background < 10: chan_3')
            
        chan_4_signal_to_nois = chan_4_int_Q99/chan_4_int_Q5
        if chan_1_signal_to_nois < 10:
            print('WARNING: forground/background < 10: chan_4')
            
        print(chan_1_upperQnr2, chan_2_upperQnr2, chan_3_upperQnr2, chan_4_upperQnr2)
        print('file name', 'chan_1_int_Q5', 'chan_1_int_Q99', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99')                                          
    if nr_of_channels == 5:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        chan_5_int_Q5 = df['chan_5_int_Q01'].quantile(0.5)
        chan_5_int_Q99 = df['chan_5_int_Q99'].quantile(chan_5_upperQnr2)
        print('file name', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99', 'chan_5_int_Q5', 'chan_5_int_Q99')
    if nr_of_channels == 6:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        chan_5_int_Q5 = df['chan_5_int_Q01'].quantile(0.5)
        chan_5_int_Q99 = df['chan_5_int_Q99'].quantile(chan_5_upperQnr2)
        chan_6_int_Q5 = df['chan_6_int_Q01'].quantile(0.5)
        chan_6_int_Q99 = df['chan_6_int_Q99'].quantile(chan_6_upperQnr2)
        print('file name', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99', 'chan_5_int_Q5', 'chan_5_int_Q99', 'chan_6_int_Q5', 'chan_6_int_Q99')                                          
    if nr_of_channels == 7:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        chan_5_int_Q5 = df['chan_5_int_Q01'].quantile(0.5)
        chan_5_int_Q99 = df['chan_5_int_Q99'].quantile(chan_5_upperQnr2)
        chan_6_int_Q5 = df['chan_6_int_Q01'].quantile(0.5)
        chan_6_int_Q99 = df['chan_6_int_Q99'].quantile(chan_6_upperQnr2)
        chan_7_int_Q5 = df['chan_7_int_Q01'].quantile(0.5)
        chan_7_int_Q99 = df['chan_7_int_Q99'].quantile(chan_7_upperQnr2)
        print('file name', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99', 'chan_5_int_Q5', 'chan_5_int_Q99', 'chan_6_int_Q5', 'chan_6_int_Q99', 'chan_7_int_Q5', 'chan_7_int_Q99')                                          
    if nr_of_channels == 8:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        chan_5_int_Q5 = df['chan_5_int_Q01'].quantile(0.5)
        chan_5_int_Q99 = df['chan_5_int_Q99'].quantile(chan_5_upperQnr2)
        chan_6_int_Q5 = df['chan_6_int_Q01'].quantile(0.5)
        chan_6_int_Q99 = df['chan_6_int_Q99'].quantile(chan_6_upperQnr2)
        chan_7_int_Q5 = df['chan_7_int_Q01'].quantile(0.5)
        chan_7_int_Q99 = df['chan_7_int_Q99'].quantile(chan_7_upperQnr2)
        chan_8_int_Q5 = df['chan_8_int_Q01'].quantile(0.5)
        chan_8_int_Q99 = df['chan_8_int_Q99'].quantile(chan_8_upperQnr2)
        print('file name', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99', 'chan_5_int_Q5', 'chan_5_int_Q99', 'chan_6_int_Q5', 'chan_6_int_Q99', 'chan_7_int_Q5', 'chan_7_int_Q99', 'chan_8_int_Q5', 'chan_8_int_Q99')
    if nr_of_channels == 9:
        chan_1_int_Q5 = df['chan_1_int_Q01'].quantile(0.5)
        chan_1_int_Q99 = df['chan_1_int_Q99'].quantile(chan_1_upperQnr2)
        chan_2_int_Q5 = df['chan_2_int_Q01'].quantile(0.5)
        chan_2_int_Q99 = df['chan_2_int_Q99'].quantile(chan_2_upperQnr2)
        chan_3_int_Q5 = df['chan_3_int_Q01'].quantile(0.5)
        chan_3_int_Q99 = df['chan_3_int_Q99'].quantile(chan_3_upperQnr2)
        chan_4_int_Q5 = df['chan_4_int_Q01'].quantile(0.5)
        chan_4_int_Q99 = df['chan_4_int_Q99'].quantile(chan_4_upperQnr2)
        chan_5_int_Q5 = df['chan_5_int_Q01'].quantile(0.5)
        chan_5_int_Q99 = df['chan_5_int_Q99'].quantile(chan_5_upperQnr2)
        chan_6_int_Q5 = df['chan_6_int_Q01'].quantile(0.5)
        chan_6_int_Q99 = df['chan_6_int_Q99'].quantile(chan_6_upperQnr2)
        chan_7_int_Q5 = df['chan_7_int_Q01'].quantile(0.5)
        chan_7_int_Q99 = df['chan_7_int_Q99'].quantile(chan_7_upperQnr2)
        chan_8_int_Q5 = df['chan_8_int_Q01'].quantile(0.5)
        chan_8_int_Q99 = df['chan_8_int_Q99'].quantile(chan_8_upperQnr2)
        chan_9_int_Q5 = df['chan_9_int_Q01'].quantile(0.5)
        chan_9_int_Q99 = df['chan_9_int_Q99'].quantile(chan_9_upperQnr2)
        print('file name', 'chan_2_int_Q5', 'chan_2_int_Q99', 'chan_3_int_Q5', 'chan_3_Q99', 'chan_4_int_Q5', 'chan_4_int_Q99', 'chan_5_int_Q5', 'chan_5_int_Q99', 'chan_6_int_Q5', 'chan_6_int_Q99', 'chan_7_int_Q5', 'chan_7_int_Q99', 'chan_8_int_Q5', 'chan_8_int_Q99', 'chan_9_int_Q5', 'chan_9_int_Q99')                                  
    
    if mode == 'gray':
        for root, _, files in os.walk(src+'/gray'):
            for file in files:
                name = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                if extension == '.tif': 
                    gray_png = os.path.join(src+'/gray',name+'.png')
                    gray_orig = os.path.join(src+'/gray',file)
                    gray_orig_new = os.path.join(src+'/gray_orig',file)
                    gray = cv2.imread(gray_orig, -1)
                    
                    gray = exposure.rescale_intensity(gray, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                    shutil.move(gray_orig, gray_orig_new)
                    cv2.imwrite(gray_png, gray.astype(bitdepth))
                    print(file, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99)
                                          
    if mode == 'rgb':
        if nr_of_channels == 2:
            for root, _, files in os.walk(src+'/rgb'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.tif': 
                        rgb_png = os.path.join(src+'/rgb',name+'.png')
                        rgb_orig = os.path.join(src+'/rgb',file)
                        rgb_orig_new = os.path.join(src+'/rgb_orig',file)
                        img = cv2.imread(rgb_orig, -1)
                        b, g = cv2.split(img) 

                        b = exposure.rescale_intensity(b, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        g = exposure.rescale_intensity(g, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)

                        rgb = cv2.merge((b,g))
                        shutil.move(rgb_orig, rgb_orig_new)
                        cv2.imwrite(rgb_png, rgb.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99)
        if nr_of_channels == 3:
                    for root, _, files in os.walk(src+'/rgb'):
                        for file in files:
                            name = os.path.splitext(file)[0]
                            extension = os.path.splitext(file)[1]
                            if extension == '.tif': 
                                rgb_png = os.path.join(src+'/rgb',name+'.png')
                                rgb_orig = os.path.join(src+'/rgb',file)
                                rgb_orig_new = os.path.join(src+'/rgb_orig',file)
                                img = cv2.imread(rgb_orig, -1)
                                b, g, r = cv2.split(img) 

                                b = exposure.rescale_intensity(b, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                                g = exposure.rescale_intensity(g, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                                r = exposure.rescale_intensity(r, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)

                                rgb = cv2.merge((b,g,r))
                                shutil.move(rgb_orig, rgb_orig_new)
                                cv2.imwrite(rgb_png, rgb.astype(bitdepth))
                                print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99)
    
    if mode == 'rgba':
        for root, _, files in os.walk(src+'/rgba'):
            for file in files:
                name = os.path.splitext(file)[0]
                extension = os.path.splitext(file)[1]
                if extension == '.tif':
                    rgba_png = os.path.join(src+'/rgba',name+'.png')
                    rgba_orig = os.path.join(src+'/rgba',file)
                    rgba_orig_new = os.path.join(src+'/rgba_orig',file)
                    img = cv2.imread(rgba_orig, -1)
                    b, g, r, a = cv2.split(img)

                    b = exposure.rescale_intensity(b, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                    g = exposure.rescale_intensity(g, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                    r = exposure.rescale_intensity(r, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                    a = exposure.rescale_intensity(a, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)

                    rgba = cv2.merge((b,g,r,a))
                    shutil.move(rgba_orig, rgba_orig_new)
                    cv2.imwrite(rgba_png, rgba.astype(bitdepth))
                    print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99)

    if mode == 'stack':
        if nr_of_channels == 1:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)

                        array = exposure.rescale_intensity(array, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)               

                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99)
        if nr_of_channels == 2:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)

                        a, b = np.split(img, 2)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99)
        if nr_of_channels == 3:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_png = os.path.join(src+'/stack',name+'.png')
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c = np.split(img, 3)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b, c], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99)
        if nr_of_channels == 4:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig, allow_pickle=True)
                        print(array.shape)
                        array_index=array.shape[2]
                        print('Array index: '+str(array_index))

                        chan_1, chan_2, chan_3, chan_4 = np.split(array, array_index, axis=2)   
                        
                        chan_1 = exposure.rescale_intensity(chan_1, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
#chan_1_norm = normalize_array(chan_1, 1)
                        chan_2 = exposure.rescale_intensity(chan_2, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
#chan_2_norm = normalize_array(chan_2, 2)
                        chan_3 = exposure.rescale_intensity(chan_3, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
#chan_3_norm = normalize_array(chan_3, 3)
                        chan_4 = exposure.rescale_intensity(chan_4, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
#chan_4_norm = normalize_array(chan_4, 4)
#print(chan_4_norm.shape)
#stack = np.stack([chan_1_norm, chan_2_norm, chan_3_norm, chan_4_norm], axis=2)
                        stack = np.stack([chan_1, chan_2, chan_3, chan_4], axis=2)
                        stack = np.squeeze(stack, 3)
                        print(stack.shape)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99)
        if nr_of_channels == 5:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c, d, e = np.split(img, 5)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                        d = exposure.rescale_intensity(d, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
                        e = exposure.rescale_intensity(e, (chan_5_int_Q5, chan_5_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b, c, d, e], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99, chan_5_int_Q5, chan_5_int_Q99)
        if nr_of_channels == 6:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c, d, e, f = np.split(img, 6)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                        d = exposure.rescale_intensity(d, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
                        e = exposure.rescale_intensity(e, (chan_5_int_Q5, chan_5_int_Q99)).astype(bitdepth)
                        f = exposure.rescale_intensity(f, (chan_6_int_Q5, chan_6_int_Q99)).astype(bitdepth)

                        stack = np.stack([a, b, c, d, e, f], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99, chan_5_int_Q5, chan_5_int_Q99, chan_6_int_Q5, chan_6_int_Q99)
        if nr_of_channels == 7:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c, d, e, f, g = np.split(img, 7)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                        d = exposure.rescale_intensity(d, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
                        e = exposure.rescale_intensity(e, (chan_5_int_Q5, chan_5_int_Q99)).astype(bitdepth)
                        f = exposure.rescale_intensity(f, (chan_6_int_Q5, chan_6_int_Q99)).astype(bitdepth)
                        g = exposure.rescale_intensity(g, (chan_7_int_Q5, chan_7_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b, c, d, e, f, g], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99, chan_5_int_Q5, chan_5_int_Q99, chan_6_int_Q5, chan_6_int_Q99, chan_7_int_Q5, chan_7_int_Q99)
        if nr_of_channels == 8:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c, d, e, f, g, h = np.split(img, 8)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                        d = exposure.rescale_intensity(d, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
                        e = exposure.rescale_intensity(e, (chan_5_int_Q5, chan_5_int_Q99)).astype(bitdepth)
                        f = exposure.rescale_intensity(f, (chan_6_int_Q5, chan_6_int_Q99)).astype(bitdepth)
                        g = exposure.rescale_intensity(g, (chan_7_int_Q5, chan_7_int_Q99)).astype(bitdepth)
                        h = exposure.rescale_intensity(h, (chan_8_int_Q5, chan_8_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b, c, d, e, f, g, h], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99, chan_5_int_Q5, chan_5_int_Q99, chan_6_int_Q5, chan_6_int_Q99, chan_7_int_Q5, chan_7_int_Q99, chan_8_int_Q5, chan_8_int_Q99)
        if nr_of_channels == 9:
            for root, _, files in os.walk(src+'/stack'):
                for file in files:
                    name = os.path.splitext(file)[0]
                    extension = os.path.splitext(file)[1]
                    if extension == '.npy':
                        stack_orig = os.path.join(src+'/stack',file)
                        stack_orig_new = os.path.join(src+'/stack_orig',file)
                        array = np.load(stack_orig)
                        
                        a, b, c, d, e, f, g, h, i = np.split(img, 9)
                        a = exposure.rescale_intensity(a, (chan_1_int_Q5, chan_1_int_Q99)).astype(bitdepth)
                        b = exposure.rescale_intensity(b, (chan_2_int_Q5, chan_2_int_Q99)).astype(bitdepth)
                        c = exposure.rescale_intensity(c, (chan_3_int_Q5, chan_3_int_Q99)).astype(bitdepth)
                        d = exposure.rescale_intensity(d, (chan_4_int_Q5, chan_4_int_Q99)).astype(bitdepth)
                        e = exposure.rescale_intensity(e, (chan_5_int_Q5, chan_5_int_Q99)).astype(bitdepth)
                        f = exposure.rescale_intensity(f, (chan_6_int_Q5, chan_6_int_Q99)).astype(bitdepth)
                        g = exposure.rescale_intensity(g, (chan_7_int_Q5, chan_7_int_Q99)).astype(bitdepth)
                        h = exposure.rescale_intensity(h, (chan_8_int_Q5, chan_8_int_Q99)).astype(bitdepth)
                        i = exposure.rescale_intensity(i, (chan_9_int_Q5, chan_9_int_Q99)).astype(bitdepth)
              
                        stack = np.stack([a, b, c, d, e, f, g, h, i], axis=-1)
                        shutil.move(stack_orig, stack_orig_new)
                        np.save(stack_orig, stack.astype(bitdepth))
                        print(file, chan_1_int_Q5, chan_1_int_Q99, chan_2_int_Q5, chan_2_int_Q99, chan_3_int_Q5, chan_3_int_Q99, chan_4_int_Q5, chan_4_int_Q99, chan_5_int_Q5, chan_5_int_Q99, chan_6_int_Q5, chan_6_int_Q99, chan_7_int_Q5, chan_7_int_Q99, chan_8_int_Q5, chan_8_int_Q99, chan_9_int_Q5, chan_9_int_Q99)              

#Read images
def plot_array(src, mode):
    imgs = []
    src = src+'/'+mode
    for path, subfolders, files in os.walk(src):
        for file in files:
            path = os.path.join(src,file)
            ext = os.path.splitext(path)[1]
            if ext == '.tif' or ext == '.png':
                print(file, 'im an image')
                imgs.append(path)
            if ext == '.npy':
                print(file, 'im an array')
                imgs.append(path)
    nimg = len(imgs)
    random_idx = random.choice(range(len(imgs)))        
    file=imgs[random_idx]        
    
    path = os.path.join(src,file)
    file_name = os.path.splitext(path)[0]
    ext = os.path.splitext(path)[1]

    if ext == '.tif' or ext == '.png':
        x = cv2.imread(file, -1) # img for cellpose
        x = cv2.cvtColor(file, cv2.COLOR_BGR2RGB)
        n_dim=len(x.shape) #shape of image
        dim=x.shape #dimensions of image
        channel=min(dim) #channel will be dimension with min value usually
        channel_position=dim.index(channel)
    elif ext == '.npy':
        x = np.load(path)
        n_dim=len(x.shape) #shape of image
        dim=x.shape #dimensions of image
        channel=min(dim) #channel will be dimension with min value usually
        channel_position=dim.index(channel)
    print('Number of images: ', nimg)
    print('Number of dimensions: ', n_dim)
    print('Channel index: ', channel_position)
    print('Image dimensions: ', dim)

    if n_dim > 3:
        channel_image=x.shape[2]
        fig, axs = plt.subplots(1, channel_image,figsize=(50,50))
        print("Image: %s" %(file_name))
        for channel in range(channel_image):
            axs[channel].imshow(x[:,:,channel])
            axs[channel].set_title('Channel '+str(channel+1),size=18)
            axs[channel].axis('off')
        fig.tight_layout()
        print('NOTE: If mode = stack channel order is reversed in cellpose')
        print('NOTE: blue = low intensity, yellow = high intensity, red = saturated intensity')
    if n_dim==3:
        channel_image=x.shape[2]
        fig, axs = plt.subplots(1, channel_image,figsize=(50,50))
        print("Image: %s" %(file_name))
        for channel in range(channel_image):
            axs[channel].imshow(x[:,:,channel])
            axs[channel].set_title('Channel '+str(channel+1),size=18)
            axs[channel].axis('off')
        fig.tight_layout()
        print('NOTE: If mode = stack channel order is reversed')
        print('NOTE: blue = low intensity, yellow = high intensity, red = saturated intensity')
    elif n_dim==2:
        print("One Channel")
        plt.imshow(x)
    else:
        print("Channel number invalid or dimensions wrong. Image shape is: "+str(x.shape))

def create_test_folder(src, mode):
    if os.path.exists(src+'/test/'+mode) is False:  
        os.mkdir(src+'/test/')
        os.mkdir(src+'/test/'+mode)
    print('Test folder path: ', src+'/test')
    contents = os.listdir(src+'/'+mode) # get contents of folder
    random.shuffle(contents) # shuffle the contents list
    if len(contents) <= 1:
        split_point = 1
    if len(contents) <= 2:
        split_point = 2
    if len(contents) <= 3:
        split_point = 3
    if len(contents) <= 4:
        split_point = 4
    if len(contents) <= 5:
        split_point = 5
    if len(contents) <= 6:
        split_point = 6
    if len(contents) <= 7:
        split_point = 7
    if len(contents) <= 8:
        split_point = 8
    if len(contents) <= 9:
        split_point = 9
    if len(contents) > 9:
        split_point = 10
    for img in contents[: split_point]:
        img_path = os.path.join(src+'/'+mode, img)
        test_path = os.path.join(src+'/test/'+mode, img)
        if os.path.exists(test_path) is False:         
            shutil.copy(img_path, test_path)
        else:
            print(img, 'already in test folder')
            
            
def run_cellpose_segmentation(src, mode, number_of_objects):

    src_mask = src+'/masks'
    if os.path.exists(src_mask) is False:         
        os.mkdir(src_mask)
    
    if mode == 'grey':
        ch1 = [0, 0]
        if obj1 == 'nuclei':
            model1 = models.Cellpose(gpu=True, model_type='nuclei')
            print('Nuclei model enabled '+'for '+obj1+' Segmentation from grayscale image')

        if obj1 != 'cells':
            model1 = models.Cellpose(gpu=True, model_type='cyto')
            print('Cytoplasmic model enabled '+'for '+obj1+' Segmentation from grayscale image')
    
    if mode == 'rgb':
        if obj1 == 'nuclei':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='nuclei')
            print('Nuclei model enabled '+'for '+obj1+' Segmentation '+' in  channel: '+str(ch1))
        if obj1 != 'cells':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='cyto')
            print('Cytoplasmic model enabled '+'for '+obj1+' Segmentation')

    if mode == 'rgba':
        if obj1 == 'nuclei':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='nuclei')
            print('Nuclei model enabled '+'for '+obj1+' Segmentation '+' in  channel: '+str(ch1))
        if obj1 != 'cells':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='cyto')
            print('Cytoplasmic model enabled '+'for '+obj1+' Segmentation')
             
    if mode == 'stack':
        if obj1 == 'nuclei':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='nuclei')
            print('Nuclei model enabled '+'for '+obj1+' Segmentation '+' in  channel: '+str(ch1))
        if obj1 != 'cells':
            ch1 = [obj1_channel, 0]
            model1 = models.Cellpose(gpu=True, model_type='cyto')
            print('Cytoplasmic model enabled '+'for '+obj1+' Segmentation')

    path = src
    src = src+'/'+mode    
    for name in os.listdir(src):
        file = os.path.join(src, name)
        os.chdir(src_mask)
        mask_name=name.replace('.png', '.tif')
        if os.path.exists(src_mask+"/"+mask_name) is True:
            print("mask exists: "+name)
        else:
            extension=os.path.splitext(name)[1]
            if extension == '.csv':
                print(name, 'is a csv file')
            else:
                if mode == 'gray' and extension == '.png':
                    image = cv2.imread(file, -1) # img for cellpose
                    image_show = img_as_ubyte(image) # img for matplotlib
                    print(image.shape)
                if mode == 'gray' and extension != '.png':
                    print(file+': is not png')
                if mode == 'rgb' and extension == '.png':
                    image = cv2.imread(file, -1) # img for cellpose
                    image_show = img_as_ubyte(image) # img for matplotlib
                    print(image.shape)
                if mode == 'rgb' and extension != '.png':
                    print(file+': is not png')
                if mode == 'rgba' and extension == '.png':
                    image = cv2.imread(file, -1) # img for cellpose
                    image_show = img_as_ubyte(image) # img for matplotlib
                    print(image.shape)
                if mode == 'rgba' and extension != '.png':
                    print(file+': is not png')
                    pass
                if mode == 'stack' and extension == '.npy':
                    array = np.load(file)
                    array_index=array.shape[2]
                    print('Array index: '+str(array_index))
                    if array_index == 1:
                        image = cv2.merge((array), array_index) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 2:
                        chan_1, chan_2 = np.split(array, array_index, axis=2)
                        image = cv2.merge((chan_1, chan_2), array_index) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 3:
                        chan_1, chan_2, chan_3 = np.split(array, array_index, axis=2)
                        image = cv2.merge((chan_1, chan_2, chan_3), array_index) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 4:
                        chan_1, chan_2, chan_3, chan_4 = np.split(array, array_index, axis=2)
                        image = cv2.merge((chan_1, chan_2, chan_3), 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 5:
                        chan_1, chan_2, chan_3, chan_4, chan_5 = np.split(array, array_index, axis=2)
                        image = cv2.merge(merg_channels_index, 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 6:
                        chan_1, chan_2, chan_3, chan_4, chan_5, chan_6 = np.split(array, array_index, axis=2)
                        image = cv2.merge(merg_channels_index, 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 7:
                        chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7 = np.split(array, array_index, axis=2)
                        image = cv2.merge(merg_channels_index, 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 8:
                        chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8 = np.split(array, array_index, axis=2)
                        image = cv2.merge(merg_channels_index, 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image
                    if array_index == 9:
                        chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8, chan_9 = np.split(array, array_index, axis=2)
                        image = cv2.merge(merg_channels_index, 3) 
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # img for cellpose
                        image_show = img_as_ubyte(image) # img for matplotlib
                        image2 = image

                    os.chdir(src)
                try:
                    #find primary object
                    if gausian1 != 0:
                        kernel = np.ones((gausian1, gausian1),np.float32)/(gausian1*gausian1)
                        image = cv2.filter2D(image,-1, kernel)
                        image_show = img_as_ubyte(image)
                    short_name = os.path.splitext(name)
                    min1 = (dim1*dim1)/2
                    print(obj1+' minimum Nr. of px: '+str(min1)+' Mean diamiter (px): '+str(dim1))
                    masks, flows, styles, diams = model1.eval(image,
                                                              batch_size = batch_size, # (int (optional, default 8)) – number of 224x224 patches to run simultaneously on the GPU (can make smaller or bigger depending on GPU memory usage)
                                                              channels = ch1, # (list (optional, default None)) – list of channels, either of length 2 or of length number of images by 2. First element of list is the channel to segment (0=grayscale, 1=red, 2=green, 3=chan_4). Second element of list is the optional nuclear channel (0=none, 1=red, 2=green, 3=chan_4). For instance, to segment grayscale images, input [0,0]. To segment images with cells in green and nuclei in blue, input [2,3]. To segment one grayscale image and one image with cells in green and nuclei in blue, input [[0,0], [2,3]].
                                                              channel_axis = None, # (int (optional, default None)) – if None, channels dimension is attempted to be automatically determined
                                                              z_axis = None, # (int (optional, default None)) – if None, z dimension is attempted to be automatically determined
                                                              normalize = True, # (bool (default, True)) – normalize data so 0.0=1st percentile and 1.0=99th percentile of image intensities in each channel
                                                              invert = False, # (bool (optional, default False)) – invert image pixel intensity before running network
                                                              rescale = True, # (float (optional, default None)) – resize factor for each image, if None, set to 1.0
                                                              diameter = dim1, # (float (optional, default None)) – diameter for each image (only used if rescale is None), if diameter is None, set to diam_mean
                                                              do_3D = False, # (bool (optional, default False)) – set to True to run 3D segmentation on 4D image input
                                                              anisotropy = None, # (float (optional, default None)) – for 3D segmentation, optional rescaling factor (e.g. set to 2.0 if Z is sampled half as dense as X or Y)
                                                              net_avg = True, # (bool (optional, default True)) – runs the 4 built-in networks and averages them if True, runs one network if False
                                                              augment = True, # (bool (optional, default False)) – tiles image with overlapping tiles and flips overlapped regions to augment
                                                              tile = True, # (bool (optional, default True)) – tiles image to ensure GPU/CPU memory usage limited (recommended)
                                                              tile_overlap = 0.1, # (float (optional, default 0.1)) – fraction of overlap of tiles when computing flows
                                                              resample = True, # (bool (optional, default False)) – run dynamics at original image size (will be slower but create more accurate boundaries)
                                                              interp = True, # (bool (optional, default True)) – interpolate during 2D dynamics (not available in 3D) (in previous versions it was False)
                                                              flow_threshold = flow_threshold, # (float (optional, default 0.4)) – flow error threshold (all cells with errors below threshold are kept) (not used for 3D)
                                                              mask_threshold = mt1, # (float (optional, default 0.0)) – all pixels with value above threshold kept for masks, decrease to find more and larger masks
                                                              # DEPRECEATED: dist_threshold = None, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              # DEPRECEATED: cellprob_threshold = primary_ct, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              #compute_masks = False, # (bool (optional, default True)) – Whether or not to compute dynamics and return masks. This is set to False when retrieving the styles for the size model.
                                                              min_size = min1, # (int (optional, default 15)) – minimum number of pixels per mask, can turn off with -1
                                                              stitch_threshold = 0.0, # (float (optional, default 0.0)) – if stitch_threshold>0.0 and not do_3D, masks are stitched in 3D to return volume segmentation
                                                              progress = False, # (pyqt progress bar (optional, default None)) – to return progress bar status to GUI
                                                              omni = True, # (bool (optional, default False)) – use omnipose mask recontruction features
                                                              #calc_trace = False, # (bool (optional, default False)) – calculate pixel traces and return as part of the flow
                                                              verbose = True, # (bool (optional, default False)) – turn on additional output to logs for debugging
                                                              transparency = False) #(bool (optional, default False)) – modulate flow opacity by magnitude instead of brightness (can use flows on any color background) diameter=primary_dim
                    obj1_mask = masks
                    print(obj1_mask.shape)
                    if os.path.basename(path) == 'test':
                        print(obj1)
                        maski = masks
                        flowi = flows[0]
                        fig = plt.figure(figsize=(50,50))
                        plot.show_segmentation(fig, image_show, obj1_mask, flowi, channels=ch1)
                        plt.tight_layout()
                        plt.show()

                    if gausian1 != 0:
                        image = image2

                except:
                    print('WARNING: Segmentation of '+obj1+' for image: '+name+' FAILED')
                try:
                    if obj2 != 'off':
                        if obj1 == 'nuclei':
                            if obj2_model != 'cyto':
                                ch2 = [obj2_channel, obj1_channel]
                                model2 = models.Cellpose(gpu=True, model_type="cyto2")
                                print('Cytoplasmic model with nuclei enabled '+'for '+obj2+' Segmentation')
                            if obj2_model == 'cyto':
                                ch2 = [obj2_channel, 0]
                                model2 = models.Cellpose(gpu=True, model_type="cyto")
                                print('Cytoplasmic model '+'for '+obj2+' Segmentation')
                    if obj1 != 'nuclei':
                        ch2 = [obj2_channel, 0]
                        model2 = models.Cellpose(gpu=True, model_type="cyto")
                        print('Cytoplasmic model enabled '+'for '+obj2+' Segmentation')

                    #find secondary object
                    if gausian2 != 0:
                        kernel = np.ones((gausian2, gausian2),np.float32)/(gausian2*gausian2)
                        image = cv2.filter2D(image,-1, kernel)
                        image_show = img_as_ubyte(image)

                    min2 = (dim2*dim2)/2
                    print(obj2+' minimum Nr. of px: '+str(min2)+' Mean diamiter (px): '+str(dim2))
                    masks, flows, styles, diams = model2.eval(image,
                                                              batch_size = batch_size, # (int (optional, default 8)) – number of 224x224 patches to run simultaneously on the GPU (can make smaller or bigger depending on GPU memory usage)
                                                              channels = ch2, # (list (optional, default None)) – list of channels, either of length 2 or of length number of images by 2. First element of list is the channel to segment (0=grayscale, 1=red, 2=green, 3=blue). Second element of list is the optional nuclear channel (0=none, 1=red, 2=green, 3=blue). For instance, to segment grayscale images, input [0,0]. To segment images with cells in green and nuclei in blue, input [2,3]. To segment one grayscale image and one image with cells in green and nuclei in blue, input [[0,0], [2,3]].
                                                              channel_axis = None, # (int (optional, default None)) – if None, channels dimension is attempted to be automatically determined
                                                              z_axis = None, # (int (optional, default None)) – if None, z dimension is attempted to be automatically determined
                                                              normalize = True, # (bool (default, True)) – normalize data so 0.0=1st percentile and 1.0=99th percentile of image intensities in each channel
                                                              invert = False, # (bool (optional, default False)) – invert image pixel intensity before running network
                                                              rescale = True, # (float (optional, default None)) – resize factor for each image, if None, set to 1.0
                                                              diameter = dim2, # (float (optional, default None)) – diameter for each image (only used if rescale is None), if diameter is None, set to diam_mean
                                                              do_3D = False, # (bool (optional, default False)) – set to True to run 3D segmentation on 4D image input
                                                              anisotropy = None, # (float (optional, default None)) – for 3D segmentation, optional rescaling factor (e.g. set to 2.0 if Z is sampled half as dense as X or Y)
                                                              net_avg = True, # (bool (optional, default True)) – runs the 4 built-in networks and averages them if True, runs one network if False
                                                              augment = True, # (bool (optional, default False)) – tiles image with overlapping tiles and flips overlapped regions to augment
                                                              tile = True, # (bool (optional, default True)) – tiles image to ensure GPU/CPU memory usage limited (recommended)
                                                              tile_overlap = 0.1, # (float (optional, default 0.1)) – fraction of overlap of tiles when computing flows
                                                              resample = True, # (bool (optional, default False)) – run dynamics at original image size (will be slower but create more accurate boundaries)
                                                              interp = True, # (bool (optional, default True)) – interpolate during 2D dynamics (not available in 3D) (in previous versions it was False)
                                                              flow_threshold = flow_threshold, # (float (optional, default 0.4)) – flow error threshold (all cells with errors below threshold are kept) (not used for 3D)
                                                              mask_threshold = mt2, # (float (optional, default 0.0)) – all pixels with value above threshold kept for masks, decrease to find more and larger masks
                                                              # DEPRECEATED: dist_threshold = None, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              # DEPRECEATED: cellprob_threshold = secondary_ct, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              #compute_masks = True, # (bool (optional, default True)) – Whether or not to compute dynamics and return masks. This is set to False when retrieving the styles for the size model.
                                                              min_size = min2, # (int (optional, default 15)) – minimum number of pixels per mask, can turn off with -1
                                                              stitch_threshold = 0.0, # (float (optional, default 0.0)) – if stitch_threshold>0.0 and not do_3D, masks are stitched in 3D to return volume segmentation
                                                              progress = True, # (pyqt progress bar (optional, default None)) – to return progress bar status to GUI
                                                              omni = True, # (bool (optional, default False)) – use omnipose mask recontruction features
                                                              #calc_trace = False, # (bool (optional, default False)) – calculate pixel traces and return as part of the flow
                                                              verbose = True, # (bool (optional, default False)) – turn on additional output to logs for debugging
                                                              transparency = False) #(bool (optional, default False)) – modulate flow opacity by magnitude instead of brightness (can use flows on any color background)

                    obj2_mask = masks
                    print(obj2_mask.shape)
                    if os.path.basename(path) == 'test':
                        print(obj2)
                        maski = masks
                        flowi = flows[0]
                        fig = plt.figure(figsize=(50,50))
                        plot.show_segmentation(fig, image_show, obj2_mask, flowi, channels=ch2)
                        plt.tight_layout()
                        plt.show() #plt.subplot(122),plt.imshow(dst),plt.title('Averaging')

                    if gausian2 != 0:
                        image = image2

                except:
                    print('WARNING: Segmentation of '+obj2+' '+' for image: '+'name '+'FAILED')
                try:
                    if obj3 != 'off':
                        if obj3_model == 'cyto':
                            ch3 = [obj3_channel, 0]
                            model3 = models.Cellpose(gpu=True, model_type="cyto")
                            print('Cytoplasmic model '+'for '+obj3+' Segmentation')
                        if obj3_model == 'cyto2':
                            ch3 = [obj3_channel, obj1_channel]
                            model3 = models.Cellpose(gpu=True, model_type="cyto2")
                            print('Cytoplasmic model with nuclei '+'for '+obj3+' Segmentation')
                        if obj3_model == 'nuceli':
                            ch3 = [obj3_channel, 0]
                            model3 = models.Cellpose(gpu=True, model_type="nuclei")
                            print('Nuclei model '+'for '+obj3+' Segmentation')

                    #find secondary object
                    if gausian3 != 0:
                        kernel = np.ones((gausian3, gausian3),np.float32)/(gausian3*gausian3)
                        image = cv2.filter2D(image,-1, kernel)
                        image_show = img_as_ubyte(image)
                    min3 = (dim3*dim3)/2
                    print(obj3+' minimum Nr. of px: '+str(min3)+' Mean diamiter (px): '+str(dim3))
                    masks, flows, styles, diams = model3.eval(image,
                                                              batch_size = batch_size, # (int (optional, default 8)) – number of 224x224 patches to run simultaneously on the GPU (can make smaller or bigger depending on GPU memory usage)
                                                              channels = ch3, # (list (optional, default None)) – list of channels, either of length 2 or of length number of images by 2. First element of list is the channel to segment (0=grayscale, 1=red, 2=green, 3=blue). Second element of list is the optional nuclear channel (0=none, 1=red, 2=green, 3=blue). For instance, to segment grayscale images, input [0,0]. To segment images with cells in green and nuclei in blue, input [2,3]. To segment one grayscale image and one image with cells in green and nuclei in blue, input [[0,0], [2,3]].
                                                              channel_axis = None, # (int (optional, default None)) – if None, channels dimension is attempted to be automatically determined
                                                              z_axis = None, # (int (optional, default None)) – if None, z dimension is attempted to be automatically determined
                                                              normalize = True, # (bool (default, True)) – normalize data so 0.0=1st percentile and 1.0=99th percentile of image intensities in each channel
                                                              invert = False, # (bool (optional, default False)) – invert image pixel intensity before running network
                                                              rescale = True, # (float (optional, default None)) – resize factor for each image, if None, set to 1.0
                                                              diameter = dim3, # (float (optional, default None)) – diameter for each image (only used if rescale is None), if diameter is None, set to diam_mean
                                                              do_3D = False, # (bool (optional, default False)) – set to True to run 3D segmentation on 4D image input
                                                              anisotropy = None, # (float (optional, default None)) – for 3D segmentation, optional rescaling factor (e.g. set to 2.0 if Z is sampled half as dense as X or Y)
                                                              net_avg = True, # (bool (optional, default True)) – runs the 4 built-in networks and averages them if True, runs one network if False
                                                              augment = True, # (bool (optional, default False)) – tiles image with overlapping tiles and flips overlapped regions to augment
                                                              tile = True, # (bool (optional, default True)) – tiles image to ensure GPU/CPU memory usage limited (recommended)
                                                              tile_overlap = 0.1, # (float (optional, default 0.1)) – fraction of overlap of tiles when computing flows
                                                              resample = True, # (bool (optional, default False)) – run dynamics at original image size (will be slower but create more accurate boundaries)
                                                              interp = True, # (bool (optional, default True)) – interpolate during 2D dynamics (not available in 3D) (in previous versions it was False)
                                                              flow_threshold = flow_threshold, # (float (optional, default 0.4)) – flow error threshold (all cells with errors below threshold are kept) (not used for 3D)
                                                              mask_threshold = mt3, # (float (optional, default 0.0)) – all pixels with value above threshold kept for masks, decrease to find more and larger masks
                                                              # DEPRECEATED: dist_threshold = None, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              # DEPRECEATED: cellprob_threshold = secondary_ct, # (float (optional, default None) DEPRECATED) – use mask_threshold instead
                                                              #compute_masks = True, # (bool (optional, default True)) – Whether or not to compute dynamics and return masks. This is set to False when retrieving the styles for the size model.
                                                              min_size = min3, # (int (optional, default 15)) – minimum number of pixels per mask, can turn off with -1
                                                              stitch_threshold = 0.0, # (float (optional, default 0.0)) – if stitch_threshold>0.0 and not do_3D, masks are stitched in 3D to return volume segmentation
                                                              progress = True, # (pyqt progress bar (optional, default None)) – to return progress bar status to GUI
                                                              omni = True, # (bool (optional, default False)) – use omnipose mask recontruction features
                                                              #calc_trace = False, # (bool (optional, default False)) – calculate pixel traces and return as part of the flow
                                                              verbose = True, # (bool (optional, default False)) – turn on additional output to logs for debugging
                                                              transparency = False) #(bool (optional, default False)) – modulate flow opacity by magnitude instead of brightness (can use flows on any color background)

                    obj3_mask = masks
                    print(obj3_mask.shape)
                    if os.path.basename(path) == 'test':
                        print(obj3)
                        maski = masks
                        flowi = flows[0]
                        fig = plt.figure(figsize=(50,50))
                        plot.show_segmentation(fig, image_show, obj3_mask, flowi, channels=ch3)
                        plt.tight_layout()
                        plt.show() #plt.subplot(122),plt.imshow(dst),plt.title('Averaging')

                except:
                    print('WARNING: Segmentation of '+obj3+' '+' for image: '+'name '+'FAILED')
                
                if mode != stack:
                    if os.path.basename(path) != 'test':
                        if os.path.exists(src_mask+'/'+obj1) is False:
                            os.mkdir(src_mask+'/'+obj1)
                        os.chdir(src_mask+'/'+obj1)
                        imsave(str(short_name[0])+".tif", obj1_mask, compress=ZIP_DEFLATED)
                        print("Saved: "+name+' '+obj1)
                        
                if mode != stack:
                    if os.path.basename(path) != 'test':    
                        if os.path.exists(src_mask+'/'+obj2) is False:
                            os.mkdir(src_mask+'/'+obj2)
                        os.chdir(src_mask+'/'+obj2)
                        imsave(str(short_name[0])+".tif", obj2_mask, compress=ZIP_DEFLATED)
                        print("Saved: "+name+' '+obj2)
                
                if mode != stack:
                    if os.path.basename(path) != 'test':    
                        if os.path.exists(src_mask+'/'+obj3) is False:
                            os.mkdir(src_mask+'/'+obj3)
                        os.chdir(src_mask+'/'+obj3)
                        imsave(str(short_name[0])+".tif", obj3_mask, compress=ZIP_DEFLATED)
                        print("Saved: "+name+' '+obj3)
                
                if mode == 'stack':
                    if number_of_objects == 1:
                        if nr_of_channels == 1:
                            chan_1 = np.squeeze(chan_1, 2)
                            stack = np.stack([chan_1, obj1_mask], axis=2)

                        if nr_of_channels == 2:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            stack = np.stack([chan_1,chan_2, obj1_mask], axis=2)

                        if nr_of_channels == 3:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, obj1_mask], axis=2)

                        if nr_of_channels == 4:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, obj1_mask], axis=2)

                        if nr_of_channels == 5:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            stack = np.stack([chan_1, chan_2, chan_3,chan_4, chan_5, obj1_mask], axis=2)

                        if nr_of_channels == 6:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, obj1_mask], axis=2)

                        if nr_of_channels == 7:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, obj1_mask], axis=2)

                        if nr_of_channels == 8:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, chan_8, obj1_mask], axis=2)

                        if nr_of_channels == 9:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            chan_9 = np.squeeze(chan_9, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8, chan_9, obj1_mask], axis=2)
                        print(stack.shape)
                        print("Saved: "+name+' '+obj1)
                        np.save(file, stack.astype(bitdepth))
                    
                    if number_of_objects == 2:
                        if nr_of_channels == 1:
                            chan_1 = np.squeeze(chan_1, 2)
                            stack = np.stack([chan_1, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 2:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            stack = np.stack([chan_1,chan_2, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 3:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 4:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 5:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            stack = np.stack([chan_1, chan_2, chan_3,chan_4, chan_5, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 6:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 7:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 8:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, chan_8, obj1_mask, obj2_mask], axis=2)

                        if nr_of_channels == 9:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            chan_9 = np.squeeze(chan_9, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8, chan_9, obj1_mask, obj2_mask], axis=2)
                        print(stack.shape)
                        print("Saved: "+name+' '+obj1)
                        np.save(file, stack.astype(bitdepth))
                    if number_of_objects == 3:
                        if nr_of_channels == 1:
                            chan_1 = np.squeeze(chan_1, 2)
                            stack = np.stack([chan_1, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 2:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            stack = np.stack([chan_1,chan_2, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 3:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 4:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 5:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            stack = np.stack([chan_1, chan_2, chan_3,chan_4, chan_5, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 6:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 7:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            stack = np.stack([chan_1,chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 8:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            stack = np.stack([chan_1, chan_2,chan_3,chan_4, chan_5, chan_6, chan_7, chan_8, obj1_mask, obj2_mask, obj3_mask], axis=2)

                        if nr_of_channels == 9:
                            chan_1 = np.squeeze(chan_1, 2)
                            chan_2 = np.squeeze(chan_2, 2)
                            chan_3 = np.squeeze(chan_3, 2)
                            chan_4 = np.squeeze(chan_4, 2)
                            chan_5 = np.squeeze(chan_5, 2)
                            chan_6 = np.squeeze(chan_6, 2)
                            chan_7 = np.squeeze(chan_7, 2)
                            chan_8 = np.squeeze(chan_8, 2)
                            chan_9 = np.squeeze(chan_9, 2)
                            stack = np.stack([chan_1, chan_2, chan_3, chan_4, chan_5, chan_6, chan_7, chan_8, chan_9, obj1_mask, obj2_mask, obj3_mask], axis=2)
                        print(stack.shape)
                        print("Saved: "+name+' '+obj1)
                        np.save(stack_mask+'/'+file, stack.astype(bitdepth))