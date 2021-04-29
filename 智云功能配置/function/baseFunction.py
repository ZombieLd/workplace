from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import sys, time

class initPage():
    def __init__(self):
        self.logger = logging.basicConfig(level=logging.INFO)
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    # 登录指定子系统
    def login(self, url, info, retrynum=10):
        self.driver.get(url)
        n = 3
        while n > 0:
            html = self.driver.page_source
            if '登录' in html: break
            elif 'An error occurred' in html:
                logging.info('系统在更新')
                self.driver.quit()
                sys.exit()
            else:
                n = n - 1
                time.sleep(1)

        while retrynum > 0:
            try:
                WebDriverWait(self.driver, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, '//input[@id="mis-login-user-name"]')))
                logging.info('找到元素%s' % '//input[@id="mis-login-user-name"]')
                self.driver.find_element_by_xpath('//input[@id="mis-login-user-name"]').clear()
                self.driver.find_element_by_xpath('//input[@id="mis-login-user-name"]').send_keys(info)
                self.xpath_click(self.driver, '//div[text()="登录"]&//div[@data-bind="click:login"]&//span[text()="登录"]')

                isExitsInfo = self.isExistEle('//div[text()="用户名或密码错误!"]', retry_num=1)
                if isExitsInfo:
                    self.driver.quit()
                else:
                    if info != 'lk':
                        self.intoSubSys( '协同平台')
                break
            except:
                errorType = sys.exc_info()[0]
                logging.info('没有找到元素%s' % '//input[@id="mis-login-user-name"]', ', 错误类型：', errorType, end='\n')
                retrynum -= 1
                continue

    # 点击元素
    def xpath_click(self, driver, loc):
        loc_list = loc.split('&')
        for i in range(len(loc_list)):
            try:
                WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.XPATH, loc_list[i])))
                logging.info('找到元素%s' % loc_list[i])
                driver.find_element_by_xpath(loc_list[i]).click()
                break
            except:
                errorType = sys.exc_info()[0]
                print('没有找到元素%s' % loc_list[i], ', 错误类型：', errorType, end='\n')
                continue

    # 元素是否存在
    def isExistEle(self, loc, retry_num=3):
        isExist = False
        while retry_num > 0:
            try:
                WebDriverWait(self.driver, 0.5).until(
                    EC.visibility_of_element_located((By.XPATH, loc)))
                logging.info('找到元素%s' % loc)
                isExist = True
                break
            except:
                errorType = sys.exc_info()[0]
                logging.info('没有找到元素%s' % loc, ', 错误类型：', errorType, end='\n')
                retry_num -= 1
                continue
        return isExist

    # 进入子系统平台
    def intoSubSys(self,name, retry_num=10):
        loc = '//div[@title="' + name + '"]'
        while retry_num > 0:
            try:
                num = 3
                while num > 0:
                    try:
                        WebDriverWait(self.driver, 1).until(
                            EC.visibility_of_element_located((By.XPATH, '//div[@id="desktop-tool-nav-btn"]')))
                        self.driver.find_element_by_xpath('//div[@id="desktop-tool-nav-btn"]').click()
                        break
                    except:
                        num = num - 1
                        continue
                WebDriverWait(self.driver, 1).until(
                    EC.visibility_of_element_located((By.XPATH, loc)))
                self.driver.find_element_by_xpath(loc).click()
                break
            except:
                errorType = sys.exc_info()[0]
                print('没有找到元素%s' % loc, ', 错误类型：', errorType, end='\n')
                retry_num -= 1
                continue


