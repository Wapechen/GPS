import sys
def gngsv(input_filename, output_filename):
    if input_filename == output_filename:
        print("input and output should not be the same!")
        return
    f = open(input_filename, "r")
    fw = open(output_filename, "w")
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
    
if len(sys.argv) != 3:
    print("Usage: python " + sys.argv[0] + " input_filename output_filename")
else:
    gngsv(sys.argv[1], sys.argv[2])


#gngsv("1109.txt")

