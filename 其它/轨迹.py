import pymysql,datetime
from pymysql.constants import CLIENT


mysqlConnectInfo = {'host': '47.93.224.52', "port": 3306, 'user': 'root', 'password': '123456',
                        'database': 'cgdb20210401'}

def getMaxPid(tableName):
    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'])
    mysql_curs = mysql_conn.cursor()
    mysql_curs.execute('select MAX(pos_id) from %s' % tableName)
    maxpid = mysql_curs.fetchone()[0]
    mysql_curs.close()
    mysql_conn.close()
    return maxpid

def work(startTime,num):

    max_pos_id = getMaxPid('to_vehicle_pos_history')
    time = startTime
    step = datetime.timedelta(milliseconds=60)

    sqls = ''

    for i in range(num):
        pos_id = max_pos_id + i +1
        #print(pos_id)

        timefmt = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
        temptime = timefmt + step
        time = temptime.strftime('%Y-%m-%d %H:%M:%S.%f')
        newtime = time.split('.')[0]

        #print(time)

        sql = "INSERT INTO to_vehicle_pos_history(`pos_id`, `address`, `altitude`, `angle`, `coordinate_x`, `coordinate_y`, `fuel`, `handle_flag`, `instant_fuel_consumption`, `latitude`, `longitude`, `oil`, `record_time`, `road_id`, `road_name`, `sim_card_num`, `speed`, `status`, `today_course`, `total_course`, `upload_time`, `today_mileage`, `total_mileage`, `sealed_state`, `lift_state`, `payload_state`, `payload_state_change`, `rmp`, `on_off_group`, `working`, `fuelad`, `current_water`, `payload`, `acc_status`) VALUES (%s, NULL, NULL, NULL, 12741376.000000, 3542661.750000, NULL, NULL, NULL, NULL, NULL, NULL, '%s', NULL, NULL, '202103240928', 18.42, NULL, NULL, NULL, '%s', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);commit;"%(pos_id,newtime,newtime)

        sqls = sqls+sql

    print(sqls)

    mysql_conn = pymysql.connect(host=mysqlConnectInfo['host'], port=mysqlConnectInfo['port'],
                                 user=mysqlConnectInfo['user'],
                                 password=mysqlConnectInfo['password'], database=mysqlConnectInfo['database'],client_flag=CLIENT.MULTI_STATEMENTS)
    mysql_curs = mysql_conn.cursor()
    mysql_curs.execute(sqls)
    mysql_conn.commit()
    mysql_curs.close()
    mysql_conn.close()

    print('插入%s条数据成功！'%num)







if __name__ == '__main__':

    work('2021-03-24 17:51:25.00',2)



