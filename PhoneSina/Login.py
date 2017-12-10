#-*-coding:utf8-*-

import requests
from lxml import etree
import urllib
import cookielib
import urllib2


s = requests.Session()#记住cookies

url = 'https://weibo.cn/?rand=691293' #此处请修改为微博地址
html_you = s.get(url).content
selector_you = etree.HTML(html_you)
url_login = selector_you.xpath('//a[@id="top"]/@href')[0]

html = s.get(url_login).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]#//*[@id="loginName"]
vk = selector.xpath('//input[@name="vk"]/@value')[0]#//*[@id="loginPassword"]
action = selector.xpath('//form[@method="post"]/@action')[0]
capId = selector.xpath('//input[@name="capId"]/@value')[0]
url_1 = 'http://weibo.cn/interface/f/ttt/captcha/show.php?cpt='+capId
path = "d://downloads//1.GIF"
data = urllib.urlretrieve(url_1,path)
print'Pic Saved!'
print capId
print action
print password
print vk
code = raw_input('please input the:')
new_url = url_login + action
print new_url
data = {
    'backTitle' : u'手机新浪网',
    'backURL' : 'http://weibo.cn/u/1906257933', #此处请填写微博地址
    'capId' : capId,
    'code': code,
    'mobile' : '登录名',
    'password' : '密码',
    'remember' : 'on',
    'tryCount' : '',
    'vk' : vk,
    'submit' : u'登录'
    }

newhtml = s.post(new_url,data=data).content
new_selector = etree.HTML(newhtml, parser=etree.HTMLParser(encoding='UTF-8'))
page = new_selector.xpath('//input[@type="hidden"]/@value')[0]
print page
for i in range(1,int(page)+1):
    url_page = 'http://weibo.cn/u/1906257933?page=%s'%i
    url_page_1 = s.get(url_page).content
    new_selector_1 = etree.HTML(url_page_1, parser=etree.HTMLParser(encoding='UTF-8'))
    content = new_selector_1.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        print text