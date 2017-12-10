# coding=utf-8
import sys
import urllib
import urllib2
import cookielib
import base64
import re
import json
import rsa
import binascii


# import requests
# from bs4 import BeautifulSoup

class weiboLogin:
    def enableCookies(self):
        cj = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def getServerData(self):
        url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=ZW5nbGFuZHNldSU0MDE2My5jb20%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1442991685270'
        data = urllib2.urlopen(url).read()
        p = re.compile('\((.*)\)')
        try:
            json_data = p.search(data).group(1)
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakv = data['rsakv']
            return servertime, nonce, pubkey, rsakv
        except:
            print 'Get severtime error!'
            return None

    def getPassword(self, password, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537)
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
        passwd = rsa.encrypt(message, key)
        passwd = binascii.b2a_hex(passwd)
        return passwd

    def getUsername(self, username):
        username_ = urllib.quote(username)
        username = base64.encodestring(username_)[:-1]
        return username


    def getFormData(self, userName, password, servertime, nonce, pubkey, rsakv):
        userName = self.getUsername(userName)
        psw = self.getPassword(password, servertime, nonce, pubkey)

        form_data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'useticket': '1',
            'pagerefer': 'http://weibo.com/p/1005052679342531/home?from=page_100505&mod=TAB&pids=plc_main',
            'vsnf': '1',
            'su': userName,
            'service': 'miniblog',
            'servertime': servertime,
            'nonce': nonce,
            'pwencode': 'rsa2',
            'rsakv': rsakv,
            'sp': psw,
            'sr': '1366*768',
            'encoding': 'UTF-8',
            'prelt': '115',
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        formData = urllib.urlencode(form_data)
        return formData

    def login(self, username, psw):
        self.enableCookies()
        url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        servertime, nonce, pubkey, rsakv = self.getServerData()
        formData = self.getFormData(username, psw, servertime, nonce, pubkey, rsakv)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
        req = urllib2.Request(
            url=url,
            data=formData,
            headers=headers
        )
        result = urllib2.urlopen(req)
        text = result.read()
        print 'text:',text
        p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
        try:
            login_url = p.search(text).group(1)
            print login_url
            urllib2.urlopen(login_url)
            print "Login success!"
        except:
            print 'Login error!'
            return 0

        url = 'http://weibo.com/u/2679342531/home?topnav=1&wvr=6'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        text = response.read()
        print text
        fp_raw = open("/Users/mac/weibo.html", "w+")
        print 'write success!'
        fp_raw.write(text)
        fp_raw.close()


wblogin = weiboLogin()
print '登录:'
# username = raw_input(u'nam:')
# password = raw_input(u'pwd:')
wblogin.login('15984512792', '753951299')
