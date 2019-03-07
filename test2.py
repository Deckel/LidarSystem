# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:17:54 2019

@author: Deckel
"""

import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(5)

ser.write('hello'.encode('utf-8'))
i = 0
while (i < 25):
    time.sleep(2)
    i=i+1
    print(ser.read(1))