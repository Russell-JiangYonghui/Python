# coding=utf8
import requests, lxml
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image


class SimulationLogging:
    # 构造data
    def structure_data(self):
        data = {
            'remember': 'on',
            'backURL': 'http://weibo.cn/1786213845/fans?vt=4',
            'backTitle': '微博',
            'tryCount': '',
            'submit': '登录'
        }
        url = 'http://weibo.cn/1786213845/fans?vt=4'
        i = requests.get(url).text
        r = BeautifulSoup(i, "lxml")
        url_2 = 'http://login.weibo.cn/login/'
        url_login = url_2 + str(r.find('form', method="post").get('action'))
        password_name = r.find('input', type="password").get('name')
        username = input('请输入用户名:')
        data['mobile'] = username
        password = input('请输入密码')
        data[password_name] = password
        vks = r.find_all('input')
        data['vk'] = vks[7].get('value')
        data['capId'] = vks[8].get('value')
        # img = r.find('img', alt="请打开图片显示").get('src')
        # file = BytesIO(requests.get(img).content)
        # img = Image.open(file)
        # img.show()
        # code = input('请输入显示的验证码(不分大小写)')
        # data['code'] = code
        # img.close()
        self.get_content(url_login, data)
        # 获取网页内容

    def get_content(self, url_login, data):
        request = requests.post(url_login, data=data).text
        r = BeautifulSoup(request, "lxml")
        print(r)


if __name__ == '__main__':
    test = SimulationLogging()
    test.structure_data()