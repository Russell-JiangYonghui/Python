#coding = utf-8
# import csv
# csv_reader = csv.reader(open("/Users/mac/Desktop/sh000001.csv"))
writer = open("/Users/mac/Desktop/sh000001_1.txt",'wr')
# for row in csv_reader:
#     r = row[5]+' 1:'+row[2]+' 2:'+row[3]+' 3:'+row[4]+' 4:'+row[6]+"\n"
#     writer.write(r)
#     print r,


import csv
import numpy as np
csvfile = file('/Users/mac/Desktop/sh000001_1.csv', 'rb')
reader = csv.reader(csvfile)
c = True
cnt = 0
r= ''
l = []
k = 1
w = ''
w1 = ''
for line in reader:
    cnt+=1
    if c:
        c = False
        continue
    if k == 1:
        w = ' 1:'+str( (float(line[2]) - 1935.52) / 1277.04) + ' 2:' +str( (float(line[5]) - 1959.16) / (3239.36 -1959.16))+' 3:' +str( (float(line[4])-1849.65) / 1307.61)+' 4:'+str(line[8] )
        k += 1
        continue
    else:
        w1 = str((float(line[3])-1950.01) / 1284.67) + w
        w = ' 1:'+str( (float(line[2]) - 1935.52) / 1277.04) + ' 2:' +str( (float(line[5]) - 1959.16) / (3239.36 -1959.16))+' 3:' +str( (float(line[4])-1849.65) / 1307.61)+' 4:'+str(line[8] )
        if line[5] == '2440.38':
            print line,"+++++++++++++++++++++++++"
        print r
        writer.write(w1)
        writer.write('\n')
        k += 1

    # l = [(float(line[3])-1950.01) / 1284.67 , 1: , (float(line[2]) - 1935.52) / 1277.04 , ' 2:]
    # print type(line[8])
    # r  = str(line[3])+' 1:'+str( (float(line[2]) - 1935.52) / 1277.04) + ' 2:' +str( (float(line[5]) - 1959.16) / 1280.80)+ ' 3:' +str( (float(line[4])-1849.65) / 1307.61)+' 4:'+str(line[8] )

    # r  = str((float(line[3])-1950.01) / 1284.67)+' 1:'+str( (float(line[2]) - 1935.52) / 1277.04) + ' 2:' +str( (float(line[5]) - 1959.16) / 1280.80)+ ' 3:' +str( (float(line[4])-1849.65) / 1307.61)

csvfile.close()