# coding=utf8
import base64
import binascii
import cookielib
import json
import os
import random
import re
import rsa
import time
import urllib
import urllib2
import urlparse
from pprint import pprint
import  math
import  time
import  sys

__client_js_ver__ = 'ssologin.js(v1.4.18)'


class Weibo(object):
    """"Login assist for Sina weibo."""

    def __init__(self, username, password,callback = ''):
        self.username = self.__encode_username(username).rstrip()
        self.password = password
        self.callback = 'jsonpcallback',id


        cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    @staticmethod
    def __encode_username(username):
        return base64.encodestring(urllib2.quote(username))

    @staticmethod
    def _encode_callback():
        id =  time.time()+ math.floor(random.random() * 100000);
        print 'jsonpcallback',id
        return 'jsonpcallback',id

    @staticmethod
    def __encode_password(password, info):
        key = rsa.PublicKey(int(info['pubkey'], 16), 65537)
        msg = ''.join([
            str(info['servertime']),
            '\t',
            str(info['nonce']),
            '\n',
            str(password)
        ])
        return binascii.b2a_hex(rsa.encrypt(msg, key))

    # https://login.sina.com.cn/sso/prelogin.php?entry=account&callback=sinaSSOController.preloginCallBack&su=MTU5ODQ1MTI3OTI%3D&rsakt=mod&client=ssologin.js(v1.4.15)&_=1510536650960
    # https: // login.sina.com.cn / sso / prelogin.php?checkpin = 1 & entry = mweibo & su = MTU5ODQ1MTI3OTI = & callback = jsonpcallback1510536619472
    def __prelogin(self):
        url = ('http://login.sina.com.cn/sso/prelogin.php?'
               'entry=mweibo&callback={callback}&checkpin=1&'
               'su={username}'
               ).format(callback = self.callback,username=self.username)
        print url

        resp = urllib2.urlopen(url).read()
        print 'resp:',resp

        return self.__prelogin_parse(resp)

    @staticmethod
    def __prelogin_parse(resp):
        p = re.compile('jsonpcallback\d+\((.+)\)')
        data = json.loads(p.search(resp).group(1))
        print 'date:',data
        return data

    def login(self):
        info = self.__prelogin()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

        login_data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'useticket': '1',
            'pagerefer': '',
            'pcid': '',
            'door': '',
            'vsnf': '1',
            'su': '',
            'service': 'miniblog',
            'servertime': '',
            'nonce': '',
            'pwencode': 'rsa2',
            'rsakv': '',
            'sp': '',
            'sr': '',
            'encoding': 'UTF-8',
            'prelt': '115',
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        # if 'showpin' in info and info['showpin']:  # need to input verify code
        #     login_data.update(self.__process_verify_code(info['pcid']))
        login_data['servertime'] = info['servertime']
        login_data['nonce'] = info['nonce']
        login_data['rsakv'] = info['rsakv']
        login_data['su'] = self.username
        # login_data['sp'] = self.__encode_password(self.password, info)
        login_data['password'] = self.password
        return self.__do_login(login_data)

    def __do_login(self, data):
        url = 'http://login.sina.com.cn/sso/login.php?client=%s' % __client_js_ver__
        headers = { 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
        req = urllib2.Request(
            url=url, data=urllib.urlencode(data), headers=headers)
        print "URL:",url
        resp = urllib2.urlopen(req).read()

        return self.__parse_real_login_and_do(resp)

    def __parse_real_login_and_do(self, resp):
        p = re.compile('replace\(["\'](.+)["\']\)')
        url = p.search(resp).group(1)

        # parse url to check whether login successfully
        query = urlparse.parse_qs(urlparse.urlparse(url).query)
        if int(query['retcode'][0]) == 0:  # successful
            self.opener.open(url)  # log in and get cookies
            print u'登录成功!'
            return True
        else:  # fail
            print u'错误代码:', query['retcode'][0]
            print u'错误提示:', query['reason'][0].decode('gbk')
            return False

    def urlopen(self, url):
        return self.opener.open(url)


if __name__ == '__main__':
    weibo = Weibo('15984512792', '753951299')
    if weibo.login():
        print weibo.urlopen('http://weibo.com').read()