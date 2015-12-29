#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import codecs

def gngsv(input_filename):
    f = codecs.open(input_filename, "r", "utf-8")
    if f == None:
        return
    name = os.path.splitext(input_filename)[0]
    fw = codecs.open(name+"GN.txt", "w", "utf-8")
    fgp = codecs.open(name+"GP.csv", "w", "utf-8")
    fgp.write(u"星系,數目,編號,總數,PRN,高度,方位角,CN\n")
    fgl = codecs.open(name+"GL.csv", "w", "utf-8")
    fgl.write(u"星系,數目,編號,總數,PRN,高度,方位角,CN\n")
    fbd = codecs.open(name+"BD.csv", "w", "utf-8")
    fbd.write(u"星系,數目,編號,總數,PRN,高度,方位角,CN\n")
    lines = f.readlines()
    for line in lines:
        if "GPGSV" in line:
            #print line,
            fw.write(line)
            fgp.write(line),
        if "GLGSV" in line:
            #print line,
            fw.write(line)
            fgl.write(line),
        if "BDGSV" in line:
            #print line,
            fw.write(line)
            fbd.write(line),
    f.close()
    fw.close()
    
if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " input_filename output_filename")
else:
    gngsv(sys.argv[1])


#gngsv("1109.txt")

