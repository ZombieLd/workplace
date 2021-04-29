# -*- coding: utf-8 -*-
import random
import pymysql
import datetime
import requests
from bs4 import BeautifulSoup
import time
import json

mysqlConnectInfo = {'host': '47.93.224.52', "port": 3306, 'user': 'root', 'password': '123456',
                        'database': 'cgdb20210401'}
with open('county.txt') as f:
    text = f.read()
    county = json.loads(text)

with open('areainfo.txt') as f:
    text2  = f.read()
    areainfo = {}
    temp = json.loads(text2)
    #for


class Administrative(object):
    def __init__(self):
        self.main()

    def main(self):
        # 年份
        year = 2020
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/%s/' % year
        trs = self.get_response(base_url, 'provincetr')
        with open('county.txt','w') as f:
            county = {}
            for tr in trs:  # 循环每一行
                for td in tr:  # 循环每个省
                    if td.a is None:
                        continue
                    href_url = td.a.get('href')
                    province_name = td.a.get_text()
                    province_code = str(href_url.split(".")[0]) + "0000000000"
                    province_url = base_url + href_url

                    # print(province_code)
                    # print(province_name)
                    # print(province_url)

                    # 插入省份数据并获取主键
                    province_data = [province_code, province_name, '0', 0, 1]

                    trs = self.get_response(province_url, None)
                    for tr in trs[1:]:  # 循环每个市
                        city_code = tr.find_all('td')[0].string
                        city_name = tr.find_all('td')[1].string

                        # 插入城市数据并获取主键
                        city_data = [city_code, city_name, province_code, province_code, 2]

                        city_url = base_url + tr.find_all('td')[1].a.get('href')
                        trs = self.get_response(city_url, None)
                        for tr in trs[1:]:  # 循环每个区县
                            county_code = tr.find_all('td')[0].string
                            county_name = tr.find_all('td')[1].string

                            # 插入区县数据并获取主键
                            county_data = [county_code, county_name, city_code, city_code, 3]
                            county[city_code[:6]] = county_name
                    time.sleep(1)
                time.sleep(1)
            f.write(json.dumps(county))

    @staticmethod
    def get_response(url, attr):
        response = requests.get(url)
        response.encoding = 'gb2312'  # 编码转换
        soup = BeautifulSoup(response.text, features="html.parser")
        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs



class IdNumber(str):
    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number

    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else "X"

    @classmethod
    def generate_myid(cls,birth_day,area_code):
        generate_ids = []
        # 随机生成一个区域码(6位数)
        # # 限定出生日期范围(8位数)
        # birth_day = "19610420"

        # 顺序码(2位数)
        for i in range(100):
            sort_no = f"{i:02d}"
            for j in [x for x in range(10) if x % 2 != 0]:
                sex = j
                prefix = f"{area_code}{birth_day}{sort_no}{sex}"
                valid_bit = str(cls(prefix).get_check_digit())
                generate_ids.append(f"{prefix}{valid_bit}")
        return generate_ids

def temp(pid):
    if pid == None:
        return 0
    else:
        return int(pid)

def getIdcard(startDay,num,area_code):
    res = []
    start = datetime.datetime.strptime(startDay,'%Y%m%d')
    step = datetime.timedelta(days=1)
    while True:
        tempday = start.strftime('%Y%m%d')
        tempIds = IdNumber.generate_myid(tempday,area_code)
        for i in tempIds:
            res.append(i)
        if len(res)<num:
            start += step
        else:
            break
    return res[:num]

def getMaxPid(tableName):
    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()
    mysql_curs.execute('select MAX(PID) from %s' % tableName)
    maxpid = mysql_curs.fetchone()[0]
    mysql_curs.close()
    mysql_conn.close()
    return maxpid

def get_sex(idno):
    # 男生：1 女生：0
    num = int(idno[16:17])
    if num % 2 == 0:
        return 0
    else:
        return 1

def get_age(idno):
    # 获取年龄
    birth_year = int(idno[6:10])
    birth_month = int(idno[10:12])
    birth_day = int(idno[12:14])
    now = (datetime.datetime.now() + datetime.timedelta(days=1))
    year = now.year
    month = now.month
    day = now.day

    if year == birth_year:
        return 0
    else:
        if birth_month > month or (birth_month == month and birth_day > day):
            return year - birth_year - 1
        else:
            return year - birth_year

def getTel():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

def getAreaInfo():
    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()
    sql = 'select region_id,region_code,region_name,'
    # mysql_curs.execute(sqls)
    # mysql_conn.commit()
    mysql_curs.close()
    mysql_conn.close()


def getSqls(res):
    maxpid = getMaxPid('tccmresident')
    maxHJpid = getMaxPid('tcCMHouseholdPerson')
    maxLDpid = getMaxPid('tcCMFloatingPerson')
    maxJWpid = getMaxPid('tcCMSeasPerson')
    persontype = {'0': 'tcCMHouseholdPerson', '1': 'tcCMFloatingPerson', '2': 'tcCMSeasPerson'}
    sqls = []
    for i in range(len(res)):

        sql = 'insert tccmresident set pid = %s,IdentityNo="%s",name="%s",LivingType=%s,PatrolID=100433,deleteflag=0;'
        typesql = 'insert %s set pid = %s,IdentityNo="%s",name="%s",PatrolID=100433,deleteflag=0;'

        pid = temp(maxpid)+1+i
        HJpid = temp(maxHJpid)+1+i
        LDpid = temp(maxLDpid)+1+i
        JWpid = temp(maxJWpid)+1+i

        identity_no = res[i] #2
        name = '人员%s' % (i+1) #3
        USEDNAME = '曾用名%s' % name
        gender = get_sex(identity_no)
        birthday = '%s-%s-%s'%(identity_no[6:10],identity_no[10:12],identity_no[12:14])
        livingtype = "%s" % random.choice(['0','1'])
        nationcode = '01'
        NATIVEPLACECODE = identity_no[:6]
        DOMICILE = NATIVEPLACECODE
        CONTACT = getTel()

        tempsql = sql % (pid, identity_no, name, livingtype)

        sqls.append(tempsql)
        if livingtype == '0':
            temptypesql = typesql%(persontype[livingtype],HJpid,identity_no,name)
            sqls.append(temptypesql)
        elif livingtype == '1':
            temptypesql = typesql % (persontype[livingtype], LDpid, identity_no, name)
            sqls.append(temptypesql)
    return sqls

def workmain(startDay,endDay,num):
    area_code = random.choice(county.keys())
    res = getIdcard(startDay,endDay,area_code)

    # 生成插入sql
    sqls = getSqls(res)
    print(len(sqls))

    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()
    # mysql_curs.execute(sqls)
    # mysql_conn.commit()
    mysql_curs.close()
    mysql_conn.close()

if __name__ == "__main__":
    a = getIdcard('19940103',2,'420111')
    print(a)





