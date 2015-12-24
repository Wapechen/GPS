#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import csv

def gngsv(input_filename):
    f = open(input_filename, "r")
    name = os.path.splitext(input_filename)[0]
    fw = open(name+"GN.txt", "w")
    fgp = open(name+"GP.csv", "w")
    writer = csv.writer(fgp)
    writer.writerow(['星系', '數目', '編號', '總數', 'PRN', '高度', '方位角', 'CN'])
    fgl = open(name+"GL.csv", "w")
    writer = csv.writer(fgl)
    writer.writerow(['星系', '數目', '編號', '總數', 'PRN', '高度', '方位角', 'CN'])
    fbd = open(name+"BD.csv", "w")
    writer = csv.writer(fbd)
    writer.writerow(['星系', '數目', '編號', '總數', 'PRN', '高度', '方位角', 'CN'])
    if f == None:
        return
    lines = f.readlines()
    for line in lines:
        if "GPGSV" in line:
            #print line,
            fw.write(line)
            fgp.write(line)
        if "GLGSV" in line:
            #print line,
            fw.write(line)
            fgl.write(line)
        if "BDGSV" in line:
            #print line,
            fw.write(line)
            fbd.write(line)
    f.close()
    fw.close()
    
if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " input_filename output_filename")
else:
    gngsv(sys.argv[1])


#gngsv("1109.txt")

