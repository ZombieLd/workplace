import requests

# 直接采用接口登记案件
def recSave():
    s = requests.session()
    s.__module__.encode(encoding='utf-8')
    url = 'http://123.56.170.103:8080/eUrbanMIS0901/login/validpassword'
    data = {'userName':'lk','password':'', 'browserVersion':'chrome/74.0.3729.157','osVersion':'Win10/32','content-type': 'charset=utf-8'}
    headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
               'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
               'Accept-Encoding':'gzip, deflate'
    }
    res = s.post(url, data=data ,headers =headers)
    print(res.content.decode('utf-8'))
    cookies = res.cookies
    # print(res.apparent_encoding)

    recSaveUrl = 'http://123.56.170.103:8080/eUrbanMIS0901/home/mis/rec/saverec'
    data3 = {"eventSrcID":"11","eventGradeID":"1","recTypeID":"1","eventTypeID":"1","mainTypeID":"348","subTypeID":"374",
             "eventDesc":"挂账案件测试","newInstCondID":"1","timeAreaID":"2",
             "address":"世界城加州阳光快递服务站(湖北省武汉市洪山区加州阳光3栋2单元002)(东南44.04米)",
             "districtID":"1","streetID":"102","communityID":"10005","cellID":"1000010","patrolID":"100508",
             "partCode":"","customDeadline":"","patrolDealFlag":"0","shopName":"","otherTaskNum":"",
             "returnVisitFlag":"0","telReply":"","callTypeID":"1","telCall":"",
             "caseEmotion":"70","eventDate":"","isTransit":"1","isOntimeAnswer":"1",
             "reporterName":"匿名","genderID":"1","homeAddress":"","birthday":"",
             "idCardType":"10","ageRangeID":"70","recPushFlag":"0","roadDirection":"",
             "isLawFlag":"0","litigantName":"","propertyCompanyInfo":"","houseCode":"",
             "unitContactHuman":"","dispatchedStreetFlag":"0","coordinateX":"12736381.6407065",
             "coordinateY":"3547519.047862","eventSrcName":"社会公众举报","eventGradeName":"日常",
             "recTypeName":"城市管理类","eventTypeName":"事件","mainTypeName":"市容环境",
             "subTypeName":"病虫害","newInstCondName":"绿植（园林树木）病虫害","timeAreaName":"核心区",
             "districtName":"洪山区","streetName":"洪山街道1","communityName":"洪山社区2",
             "cellName":"420111001002001","patrolName":"wq","noDealContent":"","cmDataTableID":"-1",
             "maxEventTypeID":"374","maxEventTypeName":"病虫害","funcForbidReporterInfoFlag":"1",
             "contact":"","accepterID":"100500","accepterName":"lk","squadronID":"","squadronName":"","isTransitFlag":"false"}

    info = s.post(recSaveUrl, data=data3, cookies = cookies, headers = headers)
    print(info.content.decode('utf-8'))

    s.close()

def recTransit(s, url,cookies,headers):
    # 参数意思？
    data = {"actID":"4836","taskListID":"2","transInfo":"290,887,0,0","opinion":"请及时处理！","addNum":"0"}
    res = s.post(url, data = data, headers = headers,cookies = cookies)



if __name__ == '__main__':
    recSave()