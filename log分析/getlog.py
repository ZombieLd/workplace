import paramiko

def getRealtimeLog(severInfo, path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(severInfo['ip'], severInfo['port'], severInfo['username'], severInfo['password'], timeout=5)

    import datetime
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    # print(nowTime)

    sentence = "cd %s;tail -n +1 catalina.%s.out" % (path,nowTime)
    info = client.exec_command(sentence)
    files = bytes.decode(info[1].read())
    s = files.split('\n')
    print(files)
    for i in range(len(s)):
        str = ''
        if "IllegalArgumentException" in s[i]:
            try:
                context = s[i-3:i+15]
                for j in context:
                    str = str+j+'\n'
                # print(str)
            except:
                continue



if __name__ == '__main__':
    # severInfo = {'ip':'47.93.224.52','port':22,'username':'root','password':'egovaCS@2020'}
    # path = r'/egova/apache-tomcat-7.0.105-20201001/logs/'
    # # path2 = r'/egova/apache-tomcat-7.0.105-20200901-2/logs/'
    # # getRealtimeLog(severInfo,path)
    #
    #
    # f1 = open(r'C:\Users\asd\Desktop\mysqldb\cgdb.sql','r',encoding='utf-8')
    # f2 = open(r'C:\Users\asd\Desktop\mysqldb\cgdb_01.sql','w',encoding='utf-8')
    # for i in f1.readlines():
    #     if i.startswith(r'/'):
    #         continue
    #     else:
    #         f2.write(i)
    # f2.close()
    # f1.close()

    f = open(r'C:\Users\asd\Desktop\1.txt')

    for i in f.readlines():
        m = i.strip()
        print("select * from %s;"%m)

    f.close()




