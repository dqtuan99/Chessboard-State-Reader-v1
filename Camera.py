#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 01:53:00 2019

@author: tuan
"""

import urllib
import cv2
import numpy as np
import time
import imutils

def adjust_image_gamma_lookuptable(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    table = np.array([((i / 255.0) ** gamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

class Camera:
    '''
    Open new connection to IP Camera webcam
    '''
    def __init__(self, url):
        self.url = url

    def takePicture(self):
        imgResponse = urllib.request.urlopen(self.url)
        imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
        img = imutils.resize(img, width=800)
        img = adjust_image_gamma_lookuptable(img, gamma=0.7)
        time.sleep(0.5)

        return img
