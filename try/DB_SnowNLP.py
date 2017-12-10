# coding=utf8
from snownlp import SnowNLP
import  jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf8
import jieba
import MySQLdb
# 这是读取数据库数据
# 进行情感分析结果
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'Weibo',
    charset = 'UTF8'
)

def query():
    cur = conn.cursor()
    sql = 'select content from tweets  where time >\'2017-11-21 22:08:10.351800 \' '
    try:
        aa = cur.execute(sql)
        info = cur.fetchmany(aa)
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print e.message
    cur.close()
    return  info
def selectAndCut():
    cnt = 0
    c = 0
    info = query()
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
    print "消极占比%f%"%(cnt / c)
if __name__ == '__main__':
    selectAndCut()

