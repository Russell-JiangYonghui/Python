# coding=utf8

from snownlp import SnowNLP
import  global_v
import chardet
import jieba
import FileUtils as fu
# 这是通过SnowNLP实现文本数据读取并进行情感分析，
# 但是准确率很低，主要是情感词不是很准确

def readfile(filename):
    file = open(filename)
    list = []
    while 1:
        line = file.readline()
        if not line:
            break
        # type = chardet.detect(line)
        # text1 = line.decode(type["encoding"])
        list.append(line)
        #  #print line,
    return list
def selectAndCut():
    senList = fu.readLine('/Users/mac/Desktop/svm/BosonNLP_sentiment_score.txt')  # 获取情感词典中的情感词

    for j in range(0,100):
        li1 = []
        l = []
        try:
            name = ("/Users/mac/Desktop/svm/yuliao/ChnSentiCorp_htl_ba_2000/pos/pos.{index}.txt").format(index =j)
        except Exception as e:
            print e.message
            continue
        l2 = fu.readLine(name)
        s = SnowNLP(l2[0])
        # print l2[0]
        print s.sentiments
        if s.sentiments < 0.5:
            print l2[0]
            global_v.GLOBAL_CNT += 1
        print "第(%r) 个数据，有(%r)个错误"%(int(j+1),int(global_v.GLOBAL_CNT))
        print "++++++++++++++++++++++++++++++++++++++++++++++++++"
    print  "错了%d个"%(global_v.GLOBAL_CNT)
    print "错误率：%d"%(global_v.GLOBAL_CNT / 1000 * 100)


if __name__ == '__main__':
    selectAndCut()

