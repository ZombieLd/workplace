# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from lxml import etree
import logging
import sys, time

def isExistEle(driver, loc, retry_num = 3):
    isExist = False
    while retry_num>0:
        try:
            WebDriverWait(driver, 0.5).until(
                EC.visibility_of_element_located((By.XPATH, loc)))
            logging.info('找到元素%s' % loc)
            isExist = True
            break
        except:
            errorType = sys.exc_info()[0]
            print('没有找到元素%s' % loc, ', 错误类型：', errorType, end='\n')
            retry_num -= 1
            continue
    return isExist


def work(version):
    option = webdriver.ChromeOptions()
    # option = webdriver.IeOptions
    option.add_argument('disable-infobars')
    option.add_argument('headless')
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(1)


    url = "http://192.168.177.251:8000"
    driver.get(url)
    driver.find_element_by_id("user_login").click()
    driver.find_element_by_id("user_login").clear()
    driver.find_element_by_id("user_login").send_keys("liukai@egova.com.cn")
    driver.find_element_by_id("user_password").click()
    driver.find_element_by_id("user_password").clear()
    driver.find_element_by_id("user_password").send_keys("asd123456")
    driver.find_element_by_name("commit").click()

    driver.get("http://192.168.177.251:8000/wizdom-urban/wizdom-urban-v14/settings/repository?page=1")

    driver.find_element_by_xpath("//div[@id='content-body']/section/div/button[1]").click()
    driver.find_element_by_link_text(u"Last »").click()
    driver.find_element_by_xpath("//div[@id='content-body']/section/div/button[1]").click()
    driver.find_element_by_xpath(
        "//span[text()='%s']/../../td[4]/div/button"%version).click()
    #print(isExistEle(driver,"//span[text()='%s']/../../td[4]/div/div/div/ul/li/a[text()='No one']"%version))
    driver.find_element_by_xpath(
        "//span[text()='%s']/../../td[4]/div/div/div/ul/li/a[text()='No one']"%version).click()
    # Developers + Masters

    driver.quit()
    print('%s权限关闭'%version)

def work_request():


    import requests

    session = requests.Session()
    url = "http://192.168.177.251:8000"
    a = session.get(url)



    import re
    temp = '<meta name="csrf-token" content="(.*)" />'
    token = re.findall(temp,a.content.decode('utf-8'))[0]
    print(token)
    #
    signurl = 'http://192.168.177.251:8000/users/sign_in'
    data1 = {
        "utf8": "✓",
        "authenticity_token": token,
        "user[login]": "liukai@egova.com.cn",
        "user[password]": "asd123456",
        "user[remember_me]": "0"
    }
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0"
    # }
    b = session.post(signurl,data=data1)

    #cookies = requests.utils.dict_from_cookiejar(session.cookies)
    cookies ={}
    cookies['sidebar_collapsed'] = 'false'
    print(cookies)
    updateurl = 'http://192.168.177.251:8000/wizdom-urban/wizdom-urban-v14/protected_branches/1916'
    #打开
    data2 = {"protected_branch":{"merge_access_levels_attributes":[{"id":1916,"access_level":"0"}],"push_access_levels_attributes":[{"id":1916,"access_level":"30"}]}}
    #关闭
    data3 = {"protected_branch":{"merge_access_levels_attributes":[{"id":1916,"access_level":"0"}],"push_access_levels_attributes":[{"id":1916,"access_level":"0"}]}}
    import json
    c = session.patch(updateurl, data=json.dumps(data3).encode('utf-8'),cookies = cookies)
    print(c.status_code)









if __name__ == "__main__":
    version = 'release-3.9.0-20201201'
    #work(version)
    work_request()
