import requests

s = requests.session()
data1 = {'u':'lk','p':'RANDOM_IVZNstnMmXQWvPGkKcDVzWADY07rps5JaqN0snjA==','ip':None,'browserVersion':'chrome/88.0.4324.104',
         'osVersion':'Win10/32','validCode':None,'validWay':0}

res1 = s.post("http://123.56.170.103:8080/eUrbanMIS0101/login/validpassword",data=data1)
print(res1.content)

srcFields = [{"displayOrder":"0","fieldCaption":"area","fieldID":301,"fieldName":"area","fieldTypeInfo":"string","phyLayerID":10029},{"displayOrder":"1","fieldCaption":"citycode","fieldID":302,"fieldName":"citycode","fieldTypeInfo":"string","phyLayerID":10029},{"displayOrder":"2","fieldCaption":"cityname","fieldID":303,"fieldName":"cityname","fieldTypeInfo":"string","phyLayerID":10029},{"displayOrder":"3","fieldCaption":"geom","fieldID":304,"fieldName":"geom","fieldTypeInfo":"MultiSurfacePropertyType","phyLayerID":10029}]

f = []

import json
a = json.dumps(srcFields)
b = json.dumps(f)
data2 = {'phyLayerID': 10029,
'phyLayerName': '武汉市',
'displayOrder': 10000,
'phyLayerTname': '武汉市',
'phyLayerTag': '武汉市',
'serviceLayerID': '武汉市',
'phyLayerType': 3,
'layerUsageType': '',
'phyLayerGroupID': 1,
'serviceID': 7,
'fields': b,
'srcFields':a }





import json
res2 = s.post('http://123.56.170.103:8080/eUrbanGIS0101/home/gisbuilder/phylayer/savephylayer?gisBuilderToken=MTYxMTg5NjY5NjA1NkdaS1FQRUtTUGpobjU3MzE4WE1KUVJY',headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'},data = data2)
print(res2.content.decode('utf-8'))

