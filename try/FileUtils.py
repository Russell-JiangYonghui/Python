#coding=utf-8
import chardet
def readfile(filename):
    file = open(filename)
    list = []
    while 1:
        line = file.readline().strip()
        if not line:
            break
        list.append(line)
    return list