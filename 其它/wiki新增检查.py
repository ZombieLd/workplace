import os, requests
import re
from lxml import etree

def getWikiInfo():
    session = requests.session()

    headers = {
        'Referer': 'http://faq.egova.com.cn:7777',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'
    }

    URL = r'http://faq.egova.com.cn:7777/login'
    res1 = session.get(URL)
    html = etree.HTML(res1.content.decode('utf-8'))
    token = html.xpath('//meta[@name="csrf-token"]/@content')[0]
    # print(token)

    data = {'username': 'liukai', 'password': 'asd123',
            'authenticity_token': token,
            'utf8': '✓',
            'back_url': 'http://faq.egova.com.cn:7777/',
            'login': '登录 »'}
    session.post(URL, data=data, headers=headers)

    startUrl = r'http://faq.egova.com.cn:7777/projects/redmine/wiki/20200601%E6%96%B0%E5%A2%9E%E5%8F%8A%E5%AE%8C%E5%96%84%E7%9A%84%E5%8A%9F%E8%83%BD'
    res2 = session.get(startUrl)
    html2 = etree.HTML(res2.content.decode('utf-8'))

    # 标题
    title = html2.xpath('//*[@id="content"]/div[2]/div[1]/div/div/h3')[0].text
    print(title)


if __name__ == '__main__':
    getWikiInfo()