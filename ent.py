import sys
import csv

def coordinate(filename)
    f = open(filename, "r")
    if f==None:
        return
    reader = csv.reader(f, delimiter=' ', quotechar='|')
    data=[]
    for row in reader:
    for col in (3,5)
    data.append(row)
    data.append(col)
    for item in data
        print(item)

coordinate(034205GNSS.csv)
