# coding=utf8
from snownlp import SnowNLP
import  jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf8
import DBUtils as dbu
import jieba
import MySQLdb
# 这是读取数据库数据
# 进行情感分析结果
def queryAndSenti():
    cnt = 0
    c = 0
    sql = 'select content from tweets  where time >\'2017-11-21 22:08:10.351800 \' '
    info = dbu.query(sql)
    list1 = []
    list2 = []
    for ii in info:
        c = c + 1
        list = SnowNLP(ii[0]).words
        for i in list:
            print i,
        s = SnowNLP(ii[0])
        print '\n'
        print s.sentiments
        if s.sentiments < 0.5:
            cnt +=1
        print "++++++++++++++++++++++++++++++++++++++++++++++++++"
    print "消极占比%f%" %(cnt / c)
if __name__ == '__main__':
    queryAndSenti()

