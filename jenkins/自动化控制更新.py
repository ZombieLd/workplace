import requests,json
import paramiko
import time
from lxml import etree

# 登录Jenkins并触发任务
def startJenkinsTask(url, taskName, userinfo):
    s = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    if url.endswith('/'):loginUrl = url+'j_acegi_security_check'
    else:loginUrl = url+'/j_acegi_security_check'
    res = s.post(loginUrl,data=userinfo,headers = headers)
    # print(res.content)
    cookies = res.cookies

    if url.endswith('/'):taskurl = url+f'view/%E7%89%88%E6%9C%AC/job/{taskName}/build'
    else:taskurl = url+f'/view/%E7%89%88%E6%9C%AC/job/{taskName}/build'
    s.post(taskurl,cookies = cookies)
    s.close()

# 检查最新打包的是否成功
def checkJenkinsTask(url,taskName):
    s = requests.session()
    userinfo = {"j_username": 'liukai', "j_password": 'liukai', "from": "", "Submit": "%E7%99%BB%E5%BD%95",
                "remember_me": "on"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    if url.endswith('/'):
        loginUrl = url + 'j_acegi_security_check'
    else:
        loginUrl = url + '/j_acegi_security_check'
    res = s.post(loginUrl, data=userinfo, headers=headers)
    # print(res.content)
    cookies = res.cookies

    if url.endswith('/'):
        taskurl = url + f'view/%E7%89%88%E6%9C%AC/job/{taskName}'
    else:
        taskurl = url + f'/view/%E7%89%88%E6%9C%AC/job/{taskName}'
    pageinfo = s.post(taskurl, cookies=cookies)
    html = pageinfo.content.decode(encoding='utf-8')
    selector = etree.HTML(html)
    ele = selector.xpath('//tr/td/div/a/@href')
    num = ele[0].split('/')[-2]
    print(num)

    # 获取是否成功
    temp_url = f'{url}/view/%E7%89%88%E6%9C%AC/job/{taskName}/{num}/console'
    print(temp_url)
    pageinfo2 = s.post(temp_url,cookies = cookies)
    html2 = pageinfo2.content.decode(encoding='utf-8')
    s.close()
    if 'Finished: SUCCESS' in html2:
        print('打包成功')
        return True
    else:
        print('失败')
        return False


#重启服务
def updateControl(severInfo, path, shFile):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(severInfo['ip'],severInfo['port'], severInfo['username'], severInfo['password'], timeout=5)
    sentence = "cd %s;ls" % path
    info  = client.exec_command(sentence)
    files = bytes.decode(info[1].read())
    # print(files.split('\n'))
    if 'eUrbanGIS1' in files.split('\n'):
        updatesentence= r"cd %s;./%s" % (path,shFile)
        client.exec_command(updatesentence)
    else:
        print("等待3分钟后再执行")
        time.sleep(180)
        updateControl(severInfo, path, shFile)

#tomcat服务检查，判断是否重启成功


if __name__ == '__main__':
    severInfo = {'ip':'47.93.224.52','port':22,'username':'root','password':'egovaCS@2020'}
    path = r'/egova/20200601/'
    shFile = 'updateGIS.sh'
    # now = time.strftime("%H:%M:%S")
    # checkJenkinsTask(r'http://192.168.101.19:8085','pack-hotfix-3.2.2(20200501)')
    url = r'http://192.168.101.19:8087'
    taskName = 'gis_47.93.224.52'
    userinfo = {"j_username": 'zhaoxin', "j_password": 'zhaoxin', "from": "", "Submit": "%E7%99%BB%E5%BD%95",
                "remember_me": "on"}


    startJenkinsTask(url,taskName,userinfo)
    while True:
        res = checkJenkinsTask(url,taskName)
        if res == True:
            updateControl(severInfo,path,shFile)
            break
        else:
            time.sleep(30)
            continue