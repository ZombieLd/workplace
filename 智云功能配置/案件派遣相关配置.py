from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import sys

logging.basicConfig(level=logging.INFO)

def xpath_sendkeys(driver,loc,value=None):
    try:
        WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, loc)))
        is_visible = True
    except:
        is_visible = False
    if is_visible:
        logging.info('找到元素%s'%loc)
        driver.find_element_by_xpath(loc).send_keys(value)
    else:
        logging.info('没有找到元素%s'%loc)

def xpath_click(driver,loc,value=None):
    loc_list = loc.split('&')
    for i in range(len(loc_list)):
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, loc_list[i])))
            is_visible = True
        except:
            is_visible = False
        if is_visible:
            logging.info('找到元素%s' % loc_list[i])
            driver.find_element_by_xpath(loc_list[i]).click()
            break
        else:
            if i == len(loc_list)-1:
                logging.info('没有找到最后的元素%s,自动结束程序' % loc_list[i])
                sys.exit()
            else:
                logging.info('没有找到元素%s' % loc_list[i])

class PQ:
    def __init__(self, driver):
        logging.info('启动浏览器')
        self.driver = driver
        self.driver.implicitly_wait(30)

        # 登录MIS
        logging.info('登录MIS')
        self.driver.get('http://123.57.5.118:8080/eUrbanMIS0901/main.htm')
        xpath_sendkeys(self.driver,'//input[@id="mis-login-user-name"]','egova')
        xpath_click(self.driver,'//div[@data-bind="click:login"]&//span[text()="登录"]')
        logging.info('MIS登录成功')

    def PQ_config(self,value='应用管理'):
        logging.info('开始进入')
        xpath_click(self.driver, '//*[@id="desktop-tool-nav-btn"]')
        if value =='应用管理':
            xpath_click(self.driver, '//div[text()="应用管理"]')
            logging.info('应用管理进入成功')
        elif value == '工作流构建':
            xpath_click(self.driver, '//div[text()="工作流构建"]')
            logging.info('工作流构建进入成功')
        else:
            logging.info('请输入正确想要进入的地方!!!')
            sys.exit()


    def PQ0601(self):
        logging.info('开始派遣排序配置')
        xpath_click(self.driver, '//span[text()="一级监督一级指挥 (草稿)"]')
        xpath_click(self.driver,'//div[text()="工作流阶段"]')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    a =PQ(driver)
    a.PQ_config(value='工作流构建')
