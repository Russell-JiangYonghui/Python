# coding=utf8
from datetime import datetime, timedelta
import  urllib2
import  MySQLdb
import sys
import  time
import  string
import re
import chardet
from BeautifulSoup import BeautifulSoup
type = sys.getfilesystemencoding()
reload(sys)
sys.setdefaultencoding("UTF-8")
from Tweet import *
conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'Weibo',
    charset = 'UTF8'
)

def getHtml(url,user_agent="wswp",num_retries=2):       #下载网页，如果下载失败重新下载两次
    print '开始下载网页：',url
    headers = {"User-agent": user_agent, "Cookie": "ALF=1517823886;"
                                                   "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWbLdpMbVsJ5dMk9R7IWnev5JpX5K-hUgL.FoqXShM71h5X1hM2dJLoIpWbds8bds8bds8bds8bds8b;"
                                                   "SUHB=0cSnpl44eppAQk;"
                                                   "_T_WM=9c1eb8a8b2847f1ee9327e0a22b57987;"
                                                   "SUB=_2A253VOqDDeRhGeBK71UR-C7IwzuIHXVUtvbLrDV6PUJbktBeLWXlkW1NR60m9UfyyLtCPb5Y8v7jOqLVj61SXHK0;"
                                                   "SCF=AtCwKsAwnK2G89SnkDwG7F--IgYr6UYaE_TiVP3hyzWTZ0hHPR7vkxaIYP7CK3BHDhrczD3ARyNCzysT9afBm9U.;"
                                                   "SSOLoginState=1515231955"}
    request = urllib2.Request(url,headers=headers)      #request请求包
    try:
        html = urllib2.urlopen(request).read()        #GET请求
        # typeEncode = sys.getfilesystemencoding()  ##系统默认编码
        # infoencode = chardet.detect(html).get('encoding', "GBK")  ##通过第3方模块来自动提取网页的编码
        # html1 = html.decode(infoencode, 'ignore').encode(typeEncode)  ##先转换成unicode编
        # print html1
    except urllib2.URLError as e:
        print "下载失败：",e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                # return getHtml(url,num_retries-1)
                return getHtml(url)
    return html

def normalizetime(time1):
    print '======================time to normalize:',time1
    if '分钟前' in time1:#几分钟前
        d = datetime.now()
        nPos = time1.index('分')
        m = time1[:nPos]
        return d + timedelta(minutes=-int(m))
    elif '今天' in time1:#今天几点
        t = time1[3:8]
        d = datetime.now().strftime('%Y-%m-%d')
        date = d+' '+t+':00'
        return datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
    elif '月' in time1:#x月x号
        d = datetime.now().strftime('%Y')
        m = time1[:2]
        da = time1[3:5]
        mi = time1[7:12]+':00'
        print d+'-'+m+'-'+da+' '+mi
        return datetime.strptime(d+'-'+m+'-'+da+' '+mi,'%Y-%m-%d %H:%M:%S')
    else:
        print 'time1:',time1[:18]
        return datetime.strptime(time1[:18],'%Y-%m-%d %H:%M:%S')
    # return bool(0)
def save(tweet):
    sql = ''
    try:
        print '++++++++++++++++++++'
        print tweet.user.strip()
        print tweet.id
        print tweet.t
        print tweet.content
        print '++++++++++++++++++++'
        try:
            sql = ('insert into tweets(id,user,time,content) values(\'{id}\',\'{user}\',\'{time}\',\'{content}\')').format(id=tweet.id,user = tweet.user.strip(), time = tweet.t, content = tweet.content)
        except:
            print '3333'
        print sql
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except Exception,e:
        # save(sql)
        print 'insert failed！！！',str(e)
        if(e.message.split(",")[0].__eq__("1062")):
            print "i know catch over!"

def conmments(id,oldtime):
    newid = id
    URL = ('https://weibo.cn/comment/{id}?rl=1&page={index}').format(id=id, index=1)
    html = getHtml(URL)
    soup = BeautifulSoup(html)
    mp = soup.findAll('input',{'name':'mp'})
    print 'mp',mp
    if len(mp) is 0:#if there is no conmments,the get the first one directly
        max = '1'
    else:
        max = mp[0]['value']
    print max
    for i in range(1, string.atoi(max)+1):
        time.sleep(1)
        URL = ('https://weibo.cn/comment/{id}?rl=1&page={index}').format(id=newid, index=i+4)
        html = getHtml(URL)
        soup = BeautifulSoup(html)
        #get the conmments content
        list = soup.findAll('span', {'class': 'ctt'})#find all the content:include weibo content and conmments
        for c in list:
            time.sleep(1)
            conmment = c.text
            cont = ''
            if '回复@' in conmment:
                pos = conmment.index(':')
                cont = c.text[(pos + 1):]
            else:
                cont = c.text

            user = c.findPreviousSibling('a').string

            getid = c.findParent('div',{'class':'c'}).attrs[1][1]
            if(getid.__eq__('M_')):#id is M_ means this is the weibo content,and not conmments
                d = 'M_'+id
                t = normalizetime(oldtime)
                print "deadLine:",deadline()
                print 't',t
                print islater(t,deadline())
                if islater(t,deadline()):
                    tweet = Tweet(user,d,t,cont[1:])
                    save(tweet)
                # else:
                    # exit(0)
            #
            else:
                d = getid
                t = normalizetime(c.findNextSibling('span', {'class': 'ct'}).text)
                if islater(t,deadline()):
                    tweet = Tweet(user, d, t, cont)
                    save(tweet)
                # else:
                    # exit(0)
def deadline():
    d = datetime.now()
    d2 = d + timedelta(hours=-d.hour)
    d2 = d2 + timedelta(minutes=-d.minute)
    d2 = d2 + timedelta(seconds=-d.second - 1)
    return d2
def islater(t,deadtime):
    print 't',t
    print 'dead:',deadtime
    if t > deadtime:
        return True
    else:
        return False

# Fuzk1ji1Z
if __name__ == '__main__':
    with open('sources/conf.txt', 'r') as f:
        list =  f.read().split(' ')
        for l in list:
            isFirst = True
            for i in range(1,101):
                print '-------------------------------------------------------------------------------------------------------------------------'
                URL = ('https://weibo.cn/search/mblog?hideSearchFrame=&keyword={key}&page={index}').format(key = l,index = i)
                print "url:",URL
                html = getHtml(URL)
                print html
                soup = BeautifulSoup(html)
                list = soup.findAll('div',attrs={'id': True})
                for a in list:
                    if isFirst:
                        isFirst = False
                        continue
                    if a.attrs[1][1] .__eq__('pagelist'):
                        continue
                    time2 = a.findAll('span',{'class':'ct'})
                    print 'text:',time2[0].text
                    d = deadline()
                    print d
                    conmments(a.attrs[1][1][2:],time2[0].text)
                    print '-------------------------------------------------------------------------------------------------------------------------'

                time.sleep(20)
                if normalizetime(time2[0].text) < deadline():
                    print '抓取完毕'
                    break

