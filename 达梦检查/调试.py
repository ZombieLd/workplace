import  pymysql

def excuteSql(mysqlConnectInfo):
    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()

    citySql = "SELECT * from tc_region where region_type = 5 and senior_id in (422995, 422996, 423172, 423298, 423446, 423576, 423735, 423854, 424175, 424348, 424419, 424837, 425285, 425994, 426669, 426670, 426709, 426754, 426798, 426814, 427299, 427741, 427742, 427824, 427941, 428310, 428618, 428886, 429268, 429594, 429887, 429888, 430000, 430067, 430126, 430156, 430375, 430500, 430605, 430812, 430989, 431106, 431273, 431457, 431686, 431687, 431871, 432095, 432590, 432913, 433215, 433491, 433765, 434354, 434604, 434605, 434699, 434818, 435014, 435015, 435236, 435366, 435676, 436280, 436733, 436734, 437120, 437592, 437984, 438295, 438734, 439147, 439809, 439810, 439936, 440121, 440461, 440895, 441043, 441109, 441329, 441651, 441947, 441948, 442104, 442417, 442857, 443329, 443663, 444352, 444956, 445487, 445558, 446056, 446413, 446414, 446626, 446741, 446947, 447165, 447386, 447592, 447593, 447812, 448226, 448649, 448875, 449478, 449899, 450234, 450528, 450815, 451020)"
    mysql_curs.execute(citySql)
    city = []
    for  i in mysql_curs.fetchall():
        city.append(i[0])
    print(city)

    mysql_curs.close()
    mysql_conn.close()


if __name__ == '__main__':
    mysqlConnectInfo = {'host': '192.168.101.94', "port": 3306, 'user': 'root', 'password': 'egova', 'database': 'cgdb20201001hotfix'}
    excuteSql(mysqlConnectInfo)
