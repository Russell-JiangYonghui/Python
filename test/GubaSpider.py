# coding=utf8
from datetime import datetime, timedelta
import  urllib2
import  MySQLdb
import urllib
import sys
import  time
import  string
import re
from BeautifulSoup import BeautifulSoup
type = sys.getfilesystemencoding()
reload(sys)
from Tweet import *
sys.setdefaultencoding('utf8')

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'Weibo',
    charset = 'UTF8'
)
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

def getHtml(url,num_retries=2):       #下载网页，如果下载失败重新下载两次
    print '开始下载网页：',url
    #   headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
    #SCF	AvVs2H008mxqslMB6uEFBk4hXXW2WtT0KFikNwExNMiovNaEuwvKtQCpjghkMMWzBuHCT8s_6ad4G_dRyxmj0LY.	.weibo.cn	/	2027/11/8 上午10:22:14	91 B	✓
    headers = {"User-agent":'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    request = urllib2.Request(url,headers=headers)      #request请求包
    try:
        html = urllib2.urlopen(request).read()          #GET请求
    except urllib2.URLError as e:
        print "下载失败：",e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return getHtml(url,num_retries-1)
    return html

def getDetails(html):
    soup = BeautifulSoup(html)
    div = soup.findAll('div',{'id':'zwconttbn'})
    user = div[0].findChild('strong').findChild("a").string
    print user
    id = div[0].findChild('strong').findChild("a").get("data-popper")
    print id

    ctd = soup.findAll("div",{"class":"zwfbtime"})[0].text.split(" ")
    ct = ctd[1]+" "+ctd[2]

    content = soup.findAll("div",{"class":"stockcodec"})[0].text

    tweet = Tweet(user,id,ct,content)
    try:
        save(tweet)
    except Exception as e:
        print e.message

def htmlAnalysis(html):
    soup = BeautifulSoup(html)
    list = soup.findAll("span",{'class':'searchlititlet'})#获取当夜所有的内容
    for l in list:
        a = soup.findAll(name='a', attrs={"href": re.compile(r'^http:')})
        deatil_url = l.findAll('a',attrs={"href":re.compile(r"^/news,+")})
        print deatil_url[0].get("href")
        new_url = ('http://guba.eastmoney.com{detail}').format(detail = deatil_url[0].get("href"))
        try:
            getDetails(getHtml(new_url))
        except Exception as e:
            print e.message
            continue

if __name__ == "__main__":
    with open('sources/conf1.txt', 'r') as f:
        list =  f.read().split(' ')
        for key in list:
            quoted_query = urllib.quote(key)
            for i in range(1,21):
                print i
                url = ("http://guba.eastmoney.com/search.aspx?t={keyword}&page={pages}").format(keyword = quoted_query,pages = i)
                htmlAnalysis(getHtml(url))
                print '++================================page%d'%i
