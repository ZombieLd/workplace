import os, requests
import re
from lxml import html

etree = html.etree


def getIssueUrl():
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

    urls = []
    # 未验证案件入口
    startUrl = r'http://faq.egova.com.cn:7777/projects/proj/issues?query_id=1244'
    res3 = session.get(startUrl)
    html3 = etree.HTML(res3.content.decode('utf-8'))
    eles = html3.xpath('//div[@class="autoscroll"]/table/tbody/tr')
    flag = 0
    for ele in eles:
        flag += 1
        if 'id' not in ele.attrib.keys():
            loc = '//div[@class="autoscroll"]/table/tbody/tr['+str(flag)+']'+'/td/span[2]'
            typeinfo = html3.xpath(loc)[0]
            urls.append(typeinfo.text)
        else:
            loc = '//div[@class="autoscroll"]/table/tbody/tr['+str(flag)+']'+'/td[2]/a/@href'
            url = html3.xpath(loc)[0]
            urls.append(url)

    for i in range(2,30):
        href = "http://faq.egova.com.cn:7777/projects/proj/issues?page="+str(i)+"&query_id=1244"
        res4 = session.get(href)
        if '没有任何数据可供显示' in res4.content.decode('utf-8'):
            break
        else:
            print('开始获取：'+href)
            html4 = etree.HTML(res4.content.decode('utf-8'))
            eles = html4.xpath('//div[@class="autoscroll"]/table/tbody/tr')
            flag2 = 0
            for ele in eles:
                flag2 += 1
                if 'id' not in ele.attrib.keys():
                    loc = '//div[@class="autoscroll"]/table/tbody/tr[' + str(flag2) + ']' + '/td/span[2]'
                    typeinfo = html4.xpath(loc)[0]
                    urls.append(typeinfo.text)
                else:
                    loc = '//div[@class="autoscroll"]/table/tbody/tr[' + str(flag2) + ']' + '/td[2]/a/@href'
                    url = html4.xpath(loc)[0]
                    urls.append(url)

    session.close()

    typeindex = 0
    dictype = {}
    for i in range(len(urls)):
        if 'issues' not in urls[i]:
            typeindex = i
            continue
        if urls[typeindex] not in dictype.keys():
            dictype[urls[typeindex]] = []
        dictype[urls[typeindex]].append(r'http://faq.egova.com.cn:7777'+urls[i])
    return dictype

def getIssueInfo():
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

    startUrl = r'http://faq.egova.com.cn:7777/issues/66166'
    res2 = session.get(startUrl)
    html2 = etree.HTML(res2.content.decode('utf-8'))

    # 标题
    title = html2.xpath('//*[@id="content"]/div[2]/div[1]/div/div/h3')[0].text
    print(title)

    #描述
    desloc = html2.xpath('//*[@id="content"]/div[2]/div[3]/div[2]/p')
    des = ''
    for i in desloc:
        if i.text:
            des = des+i.text+'\n'

    # 历史记录





if __name__ == '__main__':
    # getIssueUrl()
    getIssueInfo()
    # for i in range(30000):
    #     url = ''
    #     res = requests.get(url)
    #     data = res.content.decode('utf-8')
    #     print("第 %s 请求数据 %s "%(i, data[:10]))





