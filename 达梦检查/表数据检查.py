import  pymysql
import jaydebeapi

def tempList(m):
    temp = []
    for i in m :
        temp.append(i[0].upper())

    return temp

def compare(dmConnectInfo,mysqlConnectInfo,resultPath):
    dm_conn = jaydebeapi.connect(dmConnectInfo['driver'], dmConnectInfo['url'],
                              dmConnectInfo['userinfo'], dmConnectInfo['jarpath'])
    dm_curs = dm_conn.cursor()

    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'],port=mysqlConnectInfo['port'], user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'],database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()

    mysql_curs.execute('select table_name from information_schema.TABLES where TABLE_SCHEMA="%s"' % mysqlConnectInfo['database'])
    tableLists = tempList(mysql_curs.fetchall())

    dmOwner=dmConnectInfo['userinfo'][0]
    dm_curs.execute("select TABLE_NAME from dba_tables where owner='%s'" % dmOwner)
    dmTableLists = tempList(dm_curs.fetchall())
    # print(dmTableLists)

    # 检查表数据量情况
    result = []
    for i in tableLists:
        if i.upper() in dmTableLists:
            sql = 'select count(*) from %s;' % i
            dm_curs.execute(sql)
            dm_num = dm_curs.fetchall()[0][0]
            mysql_curs.execute(sql)
            mysql_num = mysql_curs.fetchall()[0][0]
            if dm_num != mysql_num:
                result.append(i)

    import datetime
    now_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    file = resultPath+'\\'+'表数据量不一致的表%s.sql'%now_time
    with open(file,'w') as f:
        for i in result:
            temp = 'select * from %s;\n'%i
            f.write(temp)

    print('表数据量检查完毕！请查看文件：%s'% file)

    mysql_curs.close()
    mysql_conn.close()
    dm_curs.close()
    dm_conn.close()

if __name__ == '__main__':
    dmConnectInfo = {'driver':'dm.jdbc.driver.DmDriver',
                     'url':'jdbc:dm://192.168.101.96:5242?clobAsString=true',
                    "userinfo":['SYSDBA', "SYSDBA"],
                     'jarpath':r'DmJdbcDriver18.jar'}

    mysqlConnectInfo={'host':'localhost',"port":3306,'user':'root','password':'egova','database':'cgdb_xj'}

    resultPath = r'C:\Users\asd\Desktop\达梦迁移'

    compare(dmConnectInfo,mysqlConnectInfo,resultPath)


