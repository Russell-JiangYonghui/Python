# coding=utf8
from snownlp import SnowNLP
import  jieba
import sys
import chardet
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

def readline(filename):
    file = open('sources/'+filename)
    list = []
    # while 1:
    line = file.readline()
    return line
    #     if not line:
    #         break
    #     list.append(line)
    # return list
def readfile(filename):
    list = []
    with open(filename, "r") as f:
        text = f.read()
    type = chardet.detect(text)
    text1 = text.decode(type["encoding"])
    # print text
    list.append(text1)
    for i in list:
        print i,
    print len(list)
    return list
def query():
    cur = conn.cursor()
    sql = 'select content from tweets  where time >\'2017-11-19 22:08:10.351800 \' '
    aa = cur.execute(sql)
    info = cur.fetchmany(aa)
    cur.execute(sql)
    conn.commit()
    cur.close()
    return  info
def scoreSent(senWord, notWord, degreeWord, segResult):
    W = 1
    score = 0
    # 存所有情感词的位置的列表
    senLoc = senWord.keys()
    notLoc = notWord.keys()
    degreeLoc = degreeWord.keys()
    senloc = 0
    notloc = -1
    degreeloc = -1

    # 遍历句中所有单词segResult，i为单词绝对位置
    for i in range(0, len(segResult)):
        # 如果该词为情感词
        try:
            if segResult[i] in senWord:
                if senloc < len(senLoc) - 1:
                    for j in range(senloc, i+1):#i为当前词语所处的位置，senloc是前一个情感词所在的位置
                        if segResult[j] in notLoc:
                            print "否定词",segResult[j]
                            W *= -1
                        elif segResult[j] in degreeLoc:
                            W *= float(degreeWord[j])
                score += W * float(senWord[segResult[i]])
            if senloc < i:
                senloc = i
        except Exception as e:
            print e.message
    print 'score:',score

def classifyWords(words):
    # (1) 情感词
    senList = []
    try:
        senList = readfile('sources／BosonNLP_sentiment_score.txt')#获取情感词典中的情感词
    except Exception as e:
        print e.message
    cnt = 0
    senDict = {}
    try:
        for s in senList:
            name = s.split(" ")[0]
            val = s.split(" ")[1]
            if len(senDict) >= len(senList):
                break
            senDict[name.strip()] = val.strip()
    except Exception as e:
        print e.message,"class"
    # (2) 否定词
    notList = []
    degreeList = []
    try:
        notList = readfile('sources／notwords.txt')
        # (3) 程度副词
        degreeList = readfile('sources／degree.txt')
    except Exception as e:
        print e.message
    degreeDict = {}
    try:
        for d in degreeList:
            name = d.split(" ")[0]
            val = d.split(" ")[1]
            degreeDict[name.strip()] = val.strip
    except Exception as e:
        print e.message,"ES"

    senWord = {}
    notWord = {}
    degreeWord = {}
    notL = []
    for i in notList:
        notL.append(i.strip())
    try:
        for word in words:
            if word in senDict.keys() and word not in notL and word not in degreeDict.keys():
                w = word.encode("utf8")
                senWord[word] = senDict[w]
            elif word in notL and word not in degreeDict.keys():
                notWord[word] = -1
            elif word in degreeDict.keys():
                w = word.encode("utf8")
                degreeWord[word] = degreeDict[w]
    except Exception as e:
        print( "exception",e.message)
    try:
        scoreSent(senWord, notWord, degreeWord,words)
    except Exception as e:
        print e.message,"scoreSent"
def selectAndCut():
    li1 = []
    l = []
    for i in range(0,5):
        try:
            name = ("/Users/mac/Desktop/svm/yuliao/ChnSentiCorp_htl_ba_2000/neg/neg.{index}.txt").format(index = i)
            li1 = jieba.cut(readfile(name)[0])
            for i in li1:
                l.append(i)
                print i,
            print "1"
        except Exception as e:
            print e.message
        try:
            classifyWords(l)
        except:
            print 'select failed!'
        print "++++++++++++++++++++++++++++++++++++++++++++++++++"

if __name__ == '__main__':
    selectAndCut()

