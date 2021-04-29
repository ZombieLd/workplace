import  pymysql
import jaydebeapi


def CLOBtoVarchar2(dmConnectInfo,tableName):
    dm_conn = jaydebeapi.connect(dmConnectInfo['driver'], dmConnectInfo['url'],
                              dmConnectInfo['userinfo'], dmConnectInfo['jarpath'])
    dm_curs = dm_conn.cursor()

    # dmOwner=dmConnectInfo['userinfo'][0]
    # dm_curs.execute("select TABLE_NAME from dba_tables where owner='%s'" % dmOwner)
    # # dm_curs.execute("select TABLE_NAME from dba_tables where owner='CGDB'")
    # dmTableLists = tempList(dm_curs.fetchall())
    # print(dmTableLists)

    tempsql = "select column_name,data_type from all_tab_columns where Table_Name = '%s';" % tableName
    dm_curs.execute(tempsql)
    dmFieldLists = dm_curs.fetchall()
    print(dmFieldLists)

    clobFields = []
    for i in dmFieldLists:
        if i[1].upper() == 'CLOB':
            clobFields.append(i[0])

    print("clob字段：%s"%clobFields)

    for i in clobFields:
        updatesql = f"alter table {tableName} add(c varchar(4000));" \
            f"update {tableName} set c={i};" \
            f"alter table {tableName} drop column {i};" \
            f"alter table {tableName} rename column c to {i};commit;"
        print(updatesql)
        #dm_curs.execute(updatesql)
        #print("字段%s已由clob修改为varchar（4000）" % i)
    #dm_conn.commit()
    dm_curs.close()
    dm_conn.close()
    #print("完成对表%s内所有字段clob的转换！！"%tableName)

if __name__ == '__main__':
    dmConnectInfo = {'driver':'dm.jdbc.driver.DmDriver',
                     'url':'jdbc:dm://172.25.27.11:5235?clobAsString=true',
                    "userinfo":['SYSDBA', "SYSDBA"],
                     'jarpath':'DmJdbcDriver18.jar'}

    tableName = input("请输入问题表名（注意别输入错误了）：\n")
    CLOBtoVarchar2(dmConnectInfo,tableName)

    # tc_stat_group_permission tc_query_permission tc_human_role tc_query