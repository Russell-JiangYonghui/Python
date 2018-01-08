#coding=utf-8
import chardet
# this is a test to readfile content from txt file
def readLine(filename):
    file = open(filename)
    list = []
    while 1:
        line = file.readline()
        if not line:
            break
        type = chardet.detect(line)
        try:
            text1 = line.decode(type["encoding"])
        except Exception as e:
            print e.message
            continue
        list.append(text1)
    return list