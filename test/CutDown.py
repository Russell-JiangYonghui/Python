# coding=utf8
import jieba
import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'Weibo',
    charset = 'UTF8'
)

def selectAndCut():
    stop_words = []
    file = open("/Users/mac/Desktop/stop_words.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        stop_words.append(line.strip())
    cur = conn.cursor()

    try:
        sql = ' select content from tweets where time > \'2017-11-19 09:44:00\' '
        print 'sql:',sql
        aa = cur.execute(sql)
        print aa
        # 打印表中的多少数据
        info = cur.fetchmany(aa)
        cur.execute(sql)
        conn.commit()
        cur.close()
        list1 = []
        list2 = []
        for t in stop_words:
            print t,
        for ii in info:
            print ii[0]
            list =  jieba.cut(ii[0])
            for t in list:
                list1.append(t)
                print t,
                if t.strip() in stop_words:
                    print 'zai zhe li mian ....',t
                list2.append(t)
        for t in list1:
            print t,
        print '+++++++++++++++++++++++++++++++++++++++++'
        for t in list2:
            print t,
    except:
        print 'select failed!'

if __name__ == '__main__':
    selectAndCut()