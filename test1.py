import sys
import os
import csv
def gngsv(filename):
    f = open(filename, "r")
    name = os.path.splitext(filename)[0]
    fw = open(name+"GNSS.csv", "w")
    writer = csv.writer(fw)
    writer.writerow(['�P�t', '�ƥ�', '�s��', '�`��', 'PRN', '����', '��쨤', 'CN'])
    if f == None:
        return
    lines = f.readlines()
    for line in lines:
        if "GPGSV" in line:
            #print line,
            fw.write(line)
        if "GLGSV" in line:
            #print line,
            fw.write(line)
        if "BDGSV" in line:
            #print line,
            fw.write(line)
    f.close()
    fw.close()
    
#if len(sys.argv) != 2:
#    print("Usage: python " + sys.argv[0] + " file_name")
#else:
#    gngsv(sys.argv[1])


gngsv("1109.txt")

