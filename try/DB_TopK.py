# coding=utf8
# this file try to delete the stop words from the words list
# but the question is that the stop words dic is not fat to this data
# so i will build a new stop words Dic by myself according to the data set
from snownlp import SnowNLP
import global_v
import Sort as s
import FileUtils as f
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf8
import jieba
import MySQLdb
import DBUtils as dbu
# 这是读取数据库数据
# 选取topK词语
def qselect(A,k):
    if len(A)<k:
        return A
    pivot = A[-1]
    right = [pivot] + [x for x in A[:-1] if x>=pivot]
    rlen = len(right)
    if rlen==k:
        return right
    if rlen>k:
        return qselect(right, k)
    else:
        left = [x for x in A[:-1] if x<pivot]
        return qselect(left, k-rlen) + right
def List2Dic(list):
    wordsDic = {}
    for i in list:
        if i not in wordsDic:
           wordsDic[i] = 0;
        wordsDic[i] +=1
    return wordsDic
def selectAndCut():
    sql = 'select content from tweets  where time >\'2017-12-01 09:48:14\' '
    info = dbu.query(sql)
    list1 = []
    list2 = []
    stops = f.readLine("sources/stop.txt")
    for ii in info:
        list = jieba.cut(ii[0])
        for i in list:
            global_v.GLOBAL_LIST.append(i.strip())
    words = s.stopwordsDel(stops,global_v.GLOBAL_LIST)
    dic =  s.Sort(words,100)
    for d in dic:
        print d,dic[d]



if __name__ == '__main__':
    selectAndCut()

