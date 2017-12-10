# coding=utf8
from datetime import datetime, timedelta
import  urllib2
import  MySQLdb
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

def getHtml(url,user_agent="wswp",num_retries=2):       #下载网页，如果下载失败重新下载两次
    print '开始下载网页：',url
    #   headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
    #SCF	AvVs2H008mxqslMB6uEFBk4hXXW2WtT0KFikNwExNMiovNaEuwvKtQCpjghkMMWzBuHCT8s_6ad4G_dRyxmj0LY.	.weibo.cn	/	2027/11/8 上午10:22:14	91 B	✓
    headers = {"User-agent":user_agent,"Cookie":"SUHB= 0ebtdCqmZJ0h0v ;_T_WM=ecef07e0e16a63a6d9d4b6424df18c93;SUB=_2A253DV5QDeRhGeVO7VAR9CbLyTmIHXVUDmIYrDV6PUJbkdANLVDzkW2NBIMTqkbX-_QovdeR9YceSb5ymw..;SCF = AiAHiwGDBPB3takCrA3dxrZklkyUgDkVHNPRPLqK4rqBDGODi4Whs36tOtTskI6ud_EWkj09KmQoDFHAinBRWDY.;SSOLoginState=1510551040"}
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

def normalizetime(time1):
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
        return datetime.strptime(time1[:18],'%Y-%m-%d %H:%M:%S')
    # return bool(0)
def save(tweet):
    sql = ''
    try:
        # print '++++++++++++++++++++'
        # print tweet.user.strip()
        # print tweet.id
        # print tweet.t
        # print tweet.content
        # print '++++++++++++++++++++'
        try:
            sql = ('insert into tweets(id,user,time,content) values(\'{id}\',\'{user}\',\'{time}\',\'{content}\')').format(id=tweet.id,user = tweet.user.strip(), time = tweet.t, content = tweet.content)
        except:
            print '3333'
        print sql
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except:
        # save(sql)
        print 'insert failed！！！'
def conmments(id,oldtime):
    newid = id
    print 'oldtime:',oldtime
    URL = ('https://weibo.cn/comment/{id}?rl=1&page={index}').format(id=id, index=1)
    html = getHtml(URL)
    soup = BeautifulSoup(html)
    mp = soup.findAll('input',{'name':'mp'})
    print 'mp',mp
    if len(mp) is 0:#if there is no conmments,the get the first one directly
        max = '1';
    else:
        max = mp[0]['value']
    print max
    for i in range(1, string.atoi(max)+1):
        URL = ('https://weibo.cn/comment/{id}?rl=1&page={index}').format(id=newid, index=i)
        html = getHtml(URL)
        # print URL
        # print html
        soup = BeautifulSoup(html)

        #get the conmments content
        list = soup.findAll('span', {'class': 'ctt'})#find all the content:include weibo content and conmments

        for c in list:
            t = ''
            getid = c.findParent('div',{'class':'c'}).attrs[1][1]

            if(getid is 'M_'):#id is M_ means this is the weibo content,and not conmments
                id = 'M_'+id
                t  = oldtime
                print t,'000000'
                continue
            else:
                id = getid

            conmment = c.text

            cont = ''
            if '回复@' in conmment:
                pos = conmment.index(':')
                cont = c.text[(pos+1):]
            else:
                cont = c.text

            user = c.findPreviousSibling('a').string

            t = c.findNextSibling('span',{'class':'ct'})
            print '1111',t
            if t is not None:
                print t.text
                t = normalizetime(t.text)
                tweet = Tweet(user,id,t,cont)
                save(tweet)

            else:
                print '======================'
                print 'None'
                print '======================'





if __name__ == '__main__':
    # conmments('FvaNMCxNE')
    keywords = ''
    keywords = raw_input('请输入密码')
    for i in range(1,101):
        URL = ('https://weibo.cn/search/mblog?hideSearchFrame=&keyword={key}&page={index}').format(key = keywords,index = i)
        print URL
        html = getHtml(URL)
        soup = BeautifulSoup(html)
        list = soup.findAll('div',attrs={'id': True})
        for a in list:
            if a.attrs[1][1] .__eq__('pagelist'):
                continue
            time = a.findAll('span',{'class':'ct'})
            print 'text:',time[0].text
            d = datetime.now()
            d2 = d+ timedelta(hours=-d.hour)
            d2 = d2 + timedelta(minutes=-d.minute )
            d2 = d2 + timedelta(seconds=-d.second - 1)
            print d2

            conmments(a.attrs[1][1][2:],time[0].text)

            if normalizetime(time[0].text) < d2:
                continue
