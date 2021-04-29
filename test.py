# -*- coding: UTF-8 -*-
import pymysql
import os
import json
# from flask_cors import *

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask, request

app = Flask(__name__)


@app.route('/index1', methods=['POST'])
def getcontent():
    mysql_conn = pymysql.connect(host='47.93.224.52', port=3306,
                                 user='root',
                                 password='123456', database='cgdb20201101')
    cur = mysql_conn.cursor()
    sql = "SELECT IDENTITYNO,NAME FROM tcCMresident"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    para = {"tableName": "tcCMresident",'data':[]}
    for i in data:
        text = {'IDENTITYNO': i[0], 'NAME': i[1]}
        # print(text)
        para['data'].append(text)
    return json.dumps(para, ensure_ascii=False)#, indent=2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5590)
    #
