#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import codecs

def gngsv(input_filename):
    f = codecs.open(input_filename, "r", "utf-8")
    name = os.path.splitext(input_filename)[0]
    fw = codecs.open(name+"GN.txt", "w")
    fgp = codecs.open(name+"GP.csv", "w", "utf-8")
    fgp.write("星系,數目,編號,總數,PRN,高度,方位角,CN\n" .encode('utf-8')
    fgl = codecs.open(name+"GL.csv", "w", "utf-8")
    fgl.write("星系,數目,編號,總數,PRN,高度,方位角,CN\n" .encode('utf-8')
    fbd = codecs.ope(name+"BD.csv", "w", "utf-8")
    fbd.write("星系,數目,編號,總數,PRN,高度,方位角,CN\n".encode('utf-8')
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

