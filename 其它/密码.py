import requests,json
import hashlib

def MD5_demo(a):
    md= hashlib.md5()# 创建md5对象
    md.update(a.encode(encoding='utf-8'))
    return md.hexdigest()

def work(p):
    session = requests.Session()
    ps = '607'+p
    md_ps = MD5_demo(ps)
    url = f"http://192.168.177.153:8181/htglchrome/caservice.htm?action=verifyPWD&from=logon&humanID=607&securityConfig=0&applicationID=3&password={md_ps}&dynPwd="
    a = session.post(url)
    #print(a.status_code)
    res = json.loads(a.content.decode('utf-8'))
    if res['ResultInfo']['success'] == 'false':
        print('密码错误！')
    else:
        print("密码是："+ps)

if __name__ == '__main__':
    work('egova@2021')

