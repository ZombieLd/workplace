from selenium import webdriver
from browsermobproxy import Server

from selenium.webdriver.chrome.options import Options

server = Server(r'C:\Users\asd\AppData\Local\Google\Chrome\Application\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

options = Options()
options.add_argument('--proxy-server={0}'.format(proxy.proxy))
options.add_argument("-headless")

driver = webdriver.Chrome(chrome_options=options)

base_url = r"http://123.56.170.103:8080/eUrbanMIS1101/main.htm"
proxy.new_har("MIS", options={'captureHeaders': True, 'captureContent': True})
driver.get(base_url)

result = proxy.har

for entry in result['log']['entries']:
    _url = entry['request']['url']
    # 根据URL找到数据接口
    if _url:
        _response = entry['response']
        _content = _response['content']
        # 获取接口返回内容
        print(_content)

server.stop()
driver.quit()
