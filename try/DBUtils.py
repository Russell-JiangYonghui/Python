# coding=utf8
from snownlp import SnowNLP
import  jieba
import sys
import chardet
import jieba
import MySQLdb
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'Weibo',
    charset = 'UTF8')
def query(sql):
    cur = conn.cursor()
    # sql = 'select content from tweets  where time >\'2017-11-19 22:08:10.351800 \' '
    aa = cur.execute(sql)
    info = cur.fetchmany(aa)
    cur.execute(sql)
    conn.commit()
    cur.close()
    return  info


