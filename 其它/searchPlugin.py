import requests,json
from pprint import pprint

def getLists():
    url = r'http://faq.egova.com.cn:7788/license/login/validpassword?userName=liukai&password=YXNkMTIz&fromMobile=true'
    s = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        'Content-Type':'application/json',
    }
    res1 = s.post(url,headers=headers)
    res2 = s.get('http://faq.egova.com.cn:7788/license/home/license/getsubplugintree')
    data = json.loads(res2.content.decode('utf-8'))['data']['data'][0]["children"]

    alltype = []
    allplugins = {}
    for i in data:
        t = i['text']
        # print(i['children'])
        if i['children'] != []:
            alltype.append(t)
            for j in i['children']:
                #name = j['text']
                if j['children'] != []:
                    #alltype.append(j['text'])  #是否添加子系统
                    for m in j['children']:
                        name = m['text']
                        allplugins[name] = t+'-'+j['text']
                else:
                    name = j['text']
                    allplugins[name] = t

    s.close()

    return allplugins,alltype

def get_res(allplugins,alltype,flag,info=''):
    temp1 = []
    xxx = ''
    if flag == '1': #查找类别下所有插件
        if info!= ''or info!=None :
            for i in allplugins.keys():
                if info in allplugins[i]:
                    temp1.append(i)
            return temp1
    elif flag == '2': #查找插件名
        if info!= '' or info!=None:
            str1 = info+'('
            for j in allplugins.keys():
                if j.startswith(str1):
                    xxx = '类别：'+allplugins[j]+'；'+'名称：'+j
            return xxx
    else:
        return "输入不正确，请重新输入"


if __name__ == '__main__':
    allplugins,alltype=getLists()
    print('插件类型有：\n%s' % alltype)
    #print(allplugins)
    flag = input("按照插件名查找（输入2）或者查询类型所有插件（输入1）：\n")
    info = input('请输入信息：\n')
    res = get_res(allplugins,alltype,flag,info)
    print('查询结果：\n%s'%res)
    str2 = ''
    for i in res:
        name = i.split('(')[0]
        str2 = str2+name+','
    print(str2)


