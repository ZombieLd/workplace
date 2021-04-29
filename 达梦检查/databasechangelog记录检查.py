import  pymysql
import jaydebeapi


def compare(dmConnectInfo,mysqlConnectInfo):
    dm_conn = jaydebeapi.connect(dmConnectInfo['driver'], dmConnectInfo['url'],
                              dmConnectInfo['userinfo'], dmConnectInfo['jarpath'])
    dm_curs = dm_conn.cursor()

    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'],port=mysqlConnectInfo['port'], user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'],database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()

    mysql_curs.execute('select * from databasechangelog' )
    tableLists = mysql_curs.fetchall()
    mysqlChangelogIds = {}
    for i in tableLists:
        mysqlChangelogIds[i[0]] = i

    dm_curs.execute("select * from databasechangelog")
    dmTableLists = dm_curs.fetchall()
    dmChangelogIds = {}

    for i in dmTableLists:
        dmChangelogIds[i[0]] = i

    res = {}
    num = 0
    for i in mysqlChangelogIds.keys():
        #if (i not in dmChangelogIds.keys()) and (not i.startswith('20') )and ('epidemiccontrol' not in i) and (not i.startswith('contract')) and (not i.startswith('epdemiccontrol')) and ('epidemiccontrol' not in mysqlChangelogIds[i][2]) and (not i.startswith('gis')):
        if (i not in dmChangelogIds.keys()) and (i.startswith('gis')):
            res[i] = mysqlChangelogIds[i]
            num = num + 1

    from pprint import pprint
    pprint(res)
    print(num)

    mysql_curs.close()
    mysql_conn.close()
    dm_curs.close()
    dm_conn.close()

if __name__ == '__main__':
    dmConnectInfo = {'driver':'dm.jdbc.driver.DmDriver',
                     'url':'jdbc:dm://192.168.101.94:5235?clobAsString=true',
                    "userinfo":['SYSDBA', "SYSDBA"],
                     'jarpath':r'DmJdbcDriver18.jar'}

    mysqlConnectInfo={'host':'47.93.224.52',"port":3306,'user':'root','password':'123456','database':'cgdb20210101'}


    compare(dmConnectInfo,mysqlConnectInfo)


