#-*-coding:utf8-*-
# coding=utf8
import requests

from lxml import etree

import re

import sys

reload(sys)

sys.setdefaultencoding('utf-8')

#防止编码错误

url_login = 'https://passport.weibo.cn/signin/login'

html = requests.get(url_login).content

selector = etree.HTML(html)

print  selector.xpath('//*[@id="loginPassword"]')[0]

password = selector.xpath('//input[@type="password"]/@name')[0]

vk = selector.xpath('//input[@name="vk"]/@value')[0]

action = selector.xpath('//form[@method="post"]/@action')[0]

print action

print password

print vk

print" ************* "

newurl = url_login + action

data={

   'mobile' : '登陆账号',

   password : '登陆密码',

   'remember' : 'on',

   'backURL' : 'http://weibo.cn/',

   'backTitle' : u'手机新浪网',

   'tryCount' : '',

   'vk' : vk,

   'submit' : u'登录'

}



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}

cookie=requests.session().post(newurl,data=data,headers=headers).cookies

print cookie



page = []

for i in range(1,21):

   newpage = 'http://weibo.cn/greatanny?page=' + str(i)

   page.append(newpage)

for url in page:

   html = requests.get(url,cookies = cookie,headers=headers).content

   selector = etree.HTML(html)

   content = selector.xpath('//span[@class="ctt"]')

   for each in content:

       text = each.xpath('string(.)')

       print text