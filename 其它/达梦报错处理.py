import jaydebeapi

def excuteSql(sql):
    conn = jaydebeapi.connect('dm.jdbc.driver.DmDriver', 'jdbc:dm://192.168.101.96:5233?clobAsString=true',['SYSDBA',"SYSDBA"],'D:\Program Files\dmdbms\drivers\jdbc\DmJdbcDriver18.jar')
    curs = conn.cursor()
    try:
        curs.execute(sql)
        result = curs.fetchall()
        info = result
        flag = 1
        return flag, info
    except:
        import sys
        t = sql.split('\n')[0]+'\n'+str(sys.exc_info()[1])
        if 'dm.jdbc.driver.DMException: SQL语句为NULL或空值' in t:
            return None, 0
        else:
            info=t
            flag = 0
            return flag, info
    curs.close()
    conn.close()



def helpSql(sqlList):
    successSqlList = []
    defaultSqlList = []
    for i in sqlList:
        # print(i)

        flag,info = excuteSql(i)
        tempDic = {flag:info}
        if flag == 1:
            successSqlList.append(tempDic)
        else:
            defaultSqlList.append(tempDic)

    return successSqlList, defaultSqlList

def fileProcess(file):
    f = open(file, 'r')
    list = f.read().split('\n\n')
    print(list)
    tableList = []
    errorInfoList = []
    for i in list:
        str = ''
        error = ''
        for j in i.split('\n'):
            if '/*' not in j:
                str = str + j + '\n'
            else:
                error = error +j + '\n'
        tableList.append(str)
        errorInfoList.append(error)
    print(tableList)
    print(errorInfoList)

    successSqlList, defaultSqlList = helpSql(tableList)
    print(len(successSqlList))
    from pprint import pprint
    pprint(defaultSqlList)

    f.close()



if __name__ == '__main__':
    file = r'C:\Users\asd\Desktop\1\业务库错误记录.txt'
    fileProcess(file)
#     sql = '''CREATE TABLE "SYSDBA"."TR_STAT_ELAPSED"
# (
#  "LOG_ID" INT NOT NULL,
#  "QUERY_ID" INT NULL,
#  "QUERY_TYPE" INT NULL,
#  "HUMAN_ID" INT NULL,
#  "START_TIME" TIMESTAMP(0) NULL,
#  "END_TIME" TIMESTAMP(0) NULL,
#  "ELAPSED_SECONDS" INT IDENTITY(1,1) NULL,
#  "STAT_COND_STR" VARCHAR(4000) NULL,
#  "ANTI_PARAM" VARCHAR(4000) NULL,
#  "SORT_FIELD" VARCHAR(100) NULL,
#  "SORT_TYPE" VARCHAR(100) NULL,
#  "PAGE_SIZE" INT NULL,
#  "PAGE_NUM" INT NULL,
#  "HUMAN_FILTER" VARCHAR(100) NULL,
#  "IS_ANTIQUERY" INT NULL,
#  "QUERY_NAME" VARCHAR(4000) NULL
# );'''
#     excuteSql(sql)