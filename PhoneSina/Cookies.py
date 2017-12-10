# coding=utf8
import  urllib2
import  MySQLdb
import sys
from BeautifulSoup import BeautifulSoup
type = sys.getfilesystemencoding()

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
if __name__ == '__main__':
    keywords = ''
    keywords = raw_input('请输入密码')
    for i in range(1,101):
        URL = ('https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%E8%82%A1%E7%A5%A8&page={index}').format(index = i)
        html = getHtml(URL)
        soup = BeautifulSoup(html)
        for weibo in soup.findAll('div',{'class':'c'}):
            print weibo.attrs('id')
        # for i in  soup.findAll('a',{'class':'nk'}):
        #     cur = conn.cursor()
        #     user = i.text
        #     contents = i.findNextSiblings('span')
        #     # contents = i.findNextSiblings('span',{'class':'ctt'}).text
        #     print contents
            # time   =  i.findNextSibling('span',{'class':'ct'})
            # print 'time:',time
            # for c in contents:

            # print user,'++++++++',contents
            # T = ((user, content))
            # # cur.execute("insert into stu_info (name, age, sex) values (%s,%s,%s)", ("Tony", 25, "man"))
            #
            # # sql = "insert into tweets (user,time,content) values (%s,%s)"
            # # print sql
            # cur.execute("insert into tweets (user,time,content) values (%s,%s,%s)",(user,"2017-11-1",content))
            # conn.commit()
            # print 'insert successfully!'
            # cur.close()