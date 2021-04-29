from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from lxml import etree
import logging
import sys, time


logging.basicConfig(level=logging.INFO)

def login_mis(url, info, retrynum = 10):
    option = webdriver.ChromeOptions()
    #option = webdriver.IeOptions
    option.add_argument('disable-infobars')
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(1)

    driver.get(url)
    n = 3
    while n>0:
        html =driver.page_source
        if '登录' in html:
            break
        elif 'An error occurred' in html:
            logging.info('系统在更新')
            driver.quit()
            sys.exit()
        else:
            n = n-1
            time.sleep(1)

    while retrynum>0:
        try:
            # num = 3
            # while num>0:
            #     try:
            #         WebDriverWait(driver, 0.5).until(
            #             EC.visibility_of_element_located((By.XPATH, '//div[text()="我知道了"]')))
            #         driver.find_element_by_xpath('//div[text()="我知道了"]').click()
            #         break
            #     except:
            #         num = num -1
            #         continue
            WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="mis-login-user-name"]')))
            logging.info('找到元素%s' % '//input[@id="mis-login-user-name"]')
            driver.find_element_by_xpath('//input[@id="mis-login-user-name"]').clear()
            driver.find_element_by_xpath('//input[@id="mis-login-user-name"]').send_keys(info)
            xpath_click(driver, '//div[text()="登录"]&//div[@data-bind="click:login"]&//span[text()="登录"]')
            # isExitsInfo = isExistEle(driver, '//div[text()="用户名或密码错误!"]', retry_num=1)
            # if isExitsInfo:
            #     driver.quit()
            # else:
            #     if info != 'lk':
            #         intoSubSys(driver, '协同平台')
            #     else:
            #         intoSubSys(driver, '受理平台')
            break
        except:
            errorType = sys.exc_info()[0]
            print('没有找到元素%s' % '//input[@id="mis-login-user-name"]', ', 错误类型：', errorType, end='\n')
            retrynum -= 1
            continue

    # openflag = input("请确认是否关闭浏览器（y/n）:\n")
    openflag = 'n'
    try:
        if openflag == 'y':driver.quit()
        else:pass
    except: pass

def xpath_click(driver,loc):
    loc_list = loc.split('&')
    for i in range(len(loc_list)):
        try:
            WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.XPATH, loc_list[i])))
            logging.info('找到元素%s' % loc_list[i])
            driver.find_element_by_xpath(loc_list[i]).click()
            break
        except:
            errorType = sys.exc_info()[0]
            inst = sys.exc_info()[1]
            print('没有找到元素%s' % loc_list[i], ', 错误类型：', errorType, end = '\n')
            continue

def intoSubSys(driver,name,retry_num = 10):
    loc = '//div[@title="'+name+'"]'
    while retry_num>0:
        try:
            num = 3
            while num>0:
                try:
                    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="desktop-tool-nav-btn"]')))
                    driver.find_element_by_xpath('//div[@id="desktop-tool-nav-btn"]').click()
                    break
                except:
                    num = num - 1
                    continue
            WebDriverWait(driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, loc)))
            driver.find_element_by_xpath(loc).click()
            break
        except:
            errorType = sys.exc_info()[0]
            print('没有找到元素%s' % loc, ', 错误类型：', errorType, end='\n')
            retry_num -= 1
            continue

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


if __name__ == '__main__':
    url = "http://123.56.170.103:8080/eUrbanMIS0101/main.htm"
    # url = 'http://27.17.34.18:8082/eUrbanMIS1001hotfix/main.htm'
    # url = r'http://192.168.101.10:8095/eUrbanMISzjb/view/mohurd/index.html#/app/navHome' # 住建部
    # url = r'http://192.168.101.96:8095/eUrbanMISzjb' # 住建部达梦
    # url = 'http://192.168.101.96:8088/eUrbanMIS0901DM/main.htm'

    while True:
        info = input("请输入登录账号或退出标识'q':\n")
        # info= '综合执法管理办公室'
        if info == 'q':
            sys.exit()
        else:
            login_mis(url, info)


