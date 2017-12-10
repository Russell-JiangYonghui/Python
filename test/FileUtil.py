# coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def readFile(filename):
    file = open(filename,'r')
    list = []
    while 1:
        line = file.readline()
        print line.strip().encode('utf-8')
        if not line:
            break
        list.append(line)
    return list
if __name__ == '__main__':
    l = []
    for i in range(0,1000):
        name = ('files/neg.{index}.txt').format(index = i)
        l.append(readFile(name)[0])
        # print l
