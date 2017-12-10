# coding=utf8
from snownlp import SnowNLP
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# str = unicode('学而时习之，不亦说乎',encoding='utf-8')
# print str
# print type((SnowNLP(str).words)[0])
# print (SnowNLP(str).words)[0]


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

def readline(filename):
    file = open('sources/'+filename)
    list = []
    while 1:
        line = file.readline()
        return line;
        if not line:
            break
        list.append(line)
    return list
def query():
    cur = conn.cursor()
    sql = 'select content from tweets  where time >\'2017-11-19 22:08:10.351800 \' '
    print 'sql:', sql
    aa = cur.execute(sql)
    print aa
    # 打印表中的多少数据
    info = cur.fetchmany(aa)
    cur.execute(sql)
    conn.commit()
    cur.close()
    return  info
def scoreSent(senWord, notWord, degreeWord, segResult):
    # print senWord.get('还有')
    # for d, x in senWord.items():
    #     print "key:" + d + ",value:" + str(x)
    # print '++++++++++++++++++++++++++++++'
    # for i in notWord:
    #     print i,
    # print '++++++++++++++++++++++++++++++'
    # for i in degreeWord:
    #     print i,
    # print '++++++++++++++++++++++++++++++'
    # for i in segResult:
    #     print i,
    # print '++++++++++++++++++++++++++++++'
    W = 1
    score = 0
    # 存所有情感词的位置的列表
    senLoc = senWord.keys()
    for i in senLoc:
        print i,
    notLoc = notWord.keys()
    degreeLoc = degreeWord.keys()
    senloc = 0
    notloc = -1
    degreeloc = -1

    # 遍历句中所有单词segResult，i为单词绝对位置
    for i in range(0, len(segResult)):
        # 如果该词为情感词
        try:
            print segResult[i],',',i
            if segResult[i] in senWord:
                # loc为情感词位置列表的序号
                # 直接添加该情感词分数
                # wo = segResult[i].encode('utf8')
                print "i:",float(senWord[segResult[i]]),' words:',segResult[i]
                score += W * float(senWord[segResult[i]])
                print "score = %f",score
                if senloc < len(senLoc) - 1:
                    # 判断该情感词与前一情感词之间是否有否定词或程度副词
                    # j为绝对位置
                    for j in range(senloc, i):
                        # 如果有否定词
                        if segResult[j] in notLoc:
                            print '否定词：',j
                            W *= -1
                        # 如果有程度副词
                        elif segResult[j] in degreeLoc:
                            W *= float(degreeWord[j])
            # i定位至下一个情感词
            if senloc < len(senLoc) :
                i = i;
        except Exception as e:
            print e.message
    print 'score:',score
def classifyWords(words):
    # (1) 情感词
    senList = readline('BosonNLP_sentiment_score.txt')
    cnt = 0
    senDict = {}
    try:
        for s in senList:
            name = s.split(" ")[0]
            val = s.split(" ")[1]
            # if len(senDict) ==   95633:
            #     break
            senDict[name.strip()] = val.strip()
    except Exception as e:
        print e.message
    # for d, x in senDict.items():
    #     print "key:" + d + ",value:" + str(x)
    # print '++++++++++++++++++++++++++++++'
    # (2) 否定词
    notList = readline('notwords.txt')
    print "not list:",len(notList)
    # (3) 程度副词
    degreeList = readline('degree.txt')
    print len(degreeList)
    degreeDict = {}
    for d in degreeList:
        name = d.split(" ")[0]
        val = d.split(" ")[1]
        if len(degreeDict) == 110:
            break
        degreeDict[name.strip()] = val.strip
    print "degreedic:",len(degreeDict)

    senWord = {}
    notWord = {}
    degreeWord = {}
    notL = []
    for i in notList:
        notL.append(i.strip())
        # print i.strip(),

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
    scoreSent(senWord, notWord, degreeWord,words)
def selectAndCut():
    # stop_words = readline('stop.txt')
    # info = query()
    # list1 = []
    # list2 = []
    # l = []
    # for t in stop_words:
    #     l.append(t.strip())
    # for ii in info:
    #     list =  SnowNLP(ii[0]).words
    #     for t in list:
    #         list1.append(t)
    #         if t.strip() in l:
    #             list.remove(t)
    #             continue
    #         list2.append(t)
    # doc = u"""
    # 有车一族都用了这个宝贝，后果很严重哦[偷笑][偷笑][偷笑]1，交警工资估计会打5折，没有超速罚款了[呲牙][呲牙][呲牙]2，移动联通公司大幅度裁员，电话费少了[呲牙][呲牙][呲牙]3，中石化中石油裁员2成，路痴不再迷路，省油[悠闲][悠闲][悠闲]5，保险公司裁员2成，保费折上折2成，全国通用[憨笑][憨笑][憨笑]买不买你自己看着办吧[调皮][调皮][调皮]2980元轩辕魔镜带回家，推广还有返利[得意]
    # """
    # list2 = SnowNLP(doc).words
    l1 = SnowNLP('标准间太差,房间还不如3星的,而且设施非常陈旧.建议酒店把老的标准间从新改善.'.encode('utf-8')).words
    for i in l1:
        print i,


    for i in range(0,4):
        name = ('neg.{index}.txt').format(index = i)
        try:
            # print readline(name)
            # print SnowNLP(readline(name)).words
            list2 = SnowNLP(readline(name)).words
        except Exception as e:
            print e.message
        # print 'list2:',len(list2)
        # for i in list2:
        #     print i,
        try:
            classifyWords(list2)
        except:
            print 'select failed!'

if __name__ == '__main__':
    selectAndCut()

