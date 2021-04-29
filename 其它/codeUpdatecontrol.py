 #-*- coding: utf-8 -*-
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


    while True:
        flag = input("请输入控制标识（1表示开放，2表示关闭）:\n")
        if flag == '1':
            driver.find_element_by_xpath(
                "//span[text()='%s']/../../td[4]/div/button" % version).click()
            driver.find_element_by_xpath(
                "//span[text()='%s']/../../td[4]/div/div/div/ul/li/a[text()='Developers + Masters']" % version).click()
            # Developers + Masters
            print('%s权限开放' % version)
        elif flag == '2':
            driver.find_element_by_xpath(
                "//span[text()='%s']/../../td[4]/div/button" % version).click()
            driver.find_element_by_xpath(
                "//span[text()='%s']/../../td[4]/div/div/div/ul/li/a[text()='No one']" % version).click()
            print('%s权限关闭' % version)

        else:
            driver.quit()
            print('输入错误，程序退出' % version)
            sys.exit()



if __name__ == "__main__":

    version = 'release-3.9.0-20201201'

    work(version)