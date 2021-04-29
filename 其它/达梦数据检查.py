import  pymysql
import jaydebeapi

def tempList(m):
    temp = []
    for i in m :
        temp.append(i[0])

    return temp

def compare():
    dm_conn = jaydebeapi.connect('dm.jdbc.driver.DmDriver', 'jdbc:dm://192.168.101.96:5235?clobAsString=true',
                              ['SYSDBA', "SYSDBA"], 'D:\Program Files\dmdbms\drivers\jdbc\DmJdbcDriver18.jar')
    dm_curs = dm_conn.cursor()

    mysql_conn = pymysql.connect(host='localhost', user='root',password='egova',database='cgdb0901')
    mysql_curs = mysql_conn.cursor()

    mysql_curs.execute('select table_name from information_schema.TABLES where TABLE_SCHEMA="cgdb0901"')
    tableLists = tempList(mysql_curs.fetchall())

    dm_curs.execute("select TABLE_NAME from dba_tables where owner='SYSDBA'")
    dmTableLists = tempList(dm_curs.fetchall())
    # print(dmTableLists)

    # 获取未迁移的数据库表或者视图
    for i in tableLists:
        if i.upper() not in dmTableLists:
            pass

    # 检查表数据量情况
    for i in tableLists:
        if i.upper() in dmTableLists:
            sql = 'select count(*) from %s;' % i
            dm_curs.execute(sql)
            dm_num = dm_curs.fetchall()[0][0]
            mysql_curs.execute(sql)
            mysql_num = mysql_curs.fetchall()[0][0]
            if dm_num != mysql_num:
                print(i)

    mysql_curs.close()
    mysql_conn.close()
    dm_curs.close()
    dm_conn.close()

if __name__ == '__main__':
    compare()
