import os,shutil

def beforeProcess(path):
    # 删除eUrbanMIS下view/mobile文件夹
    if os.path.exists(path + '\\eUrbanMIS\\view\\mobile'):
        # shutil.rmtree(path + '\\eUrbanMIS\\view\\mobile')
        print('111111111')

    # 删除eUrbanMIS/WEB-INF/lib/下的egova-statis-ex.jar
    file_dir = path + '\\eUrbanMIS\\WEB-INF\\lib'
    if os.path.exists(file_dir + '\\egova-statis-ex-1.0.1-mysql.jar'):
        # os.remove(file_dir + '\\egova-statis-ex-1.0.1-mysql.jar')
        print(222222)


beforeProcess(r'D:\0501版本管理\3.2.6\test')