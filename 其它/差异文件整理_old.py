import os
import shutil


def create_dir_structure(path):
    all = ['eGovaMobile（标准智信apk需改打包地址不包含市政环保环卫多网）',
           'eUrbanMIS',
           '其他',
           '更新说明（必读）.txt']
    all_other = ['多网', '环保', '市政园林采集员环卫排水']
    for i in range(len(all)):
        if i == len(all) - 1:
            f = open(path + '\\' + all[i], 'w')
            f.close()
        elif i == len(all) - 2:
            os.mkdir(path + '\\' + all[i])
            for j in all_other:
                os.mkdir(path + '\\' + all[i] + '\\' + j)
        else:
            os.mkdir(path + '\\' + all[i])

def get_files(path,files_list=[],dir_list=[]):
    all = os.listdir(path)
    items = path.split('\\')

    for i in range(len(path.split('\\'))):
        num = len(items)-i-1
        if items[num] != '':
            for i in all:
                str = path + '\\' + i
                if os.path.isdir(str):
                    dir_list.append(path)
                else:
                    file_dict=str
                    files_list.append(file_dict)
            break
        else:
            continue

    for i in all:
        str = path+'\\'+i
        if os.path.isdir(str):
            get_files(str, files_list, dir_list)

    return files_list

def get_package(difFile_flag,path,path_old):
    '''
    先按照上个小版本的hotfix先整理现有文件；
    然后整理增加或减少的文件。
    只针对lib文件下的包，其他文件不管
    '''
    # 获取新包内lib的所有jar包
    path_lib = path + '\\eUrbanMIS\\WEB-INF\\lib'
    path_old_others = path_old + '\\其他'
    new_packages = os.listdir(path_lib)

    if difFile_flag == 'y':
        # 获取上个小版本升级包的路径下所有文件
        package_paths = get_files(path_old_others)
        for package_path in package_paths:
            package_name = package_path.split('\\')[-1]
            if package_name in new_packages:
                pass
            else:
                print('本次更新'+package_path+' 没变化')
                package_paths.remove(package_path)

        # 按照path_old_others移动包
        for item in package_paths:
            package_name = item.split('\\')[-1]
            temp_path = path_lib+'\\'+package_name

            path_new = path + r'\其他'+item.split('其他')[-1].replace('\\'+package_name,'')
            shutil.copy(temp_path, path_new)
            os.remove(temp_path)
        print('完成移动包！')

def get_compare(path_release, path_hotfix,path):
    '''
    :param path_release: 版本lib路径
    :param path_hotfix: hotfix的lib路径
    :param path:新升级文件的根目录
    :return:
    '''
    hotfix_package = os.listdir(path_hotfix)
    release_package = os.listdir(path_release)
    path_package = os.listdir(path+'\\eUrbanMIS\\WEB-INF\\lib')
    for i in hotfix_package:
        if (i not in release_package) and i in path_package and i.startswith('egova'):

            with open(path+'新增包.txt', 'w') as f:
                str = '新增包'+i+'\n'
                f.write(str)

            shutil.copy(path_hotfix+'\\'+i, path+'\\其他')
            os.remove(path+'\\eUrbanMIS\\WEB-INF\\lib'+'\\'+i)

def get_addOrDel(path):
    # 删除eUrbanMIS下view/mobile文件夹
    if os.path.exists(path + '\\eUrbanMIS\\view\\mobile'):
        shutil.rmtree(path + '\\eUrbanMIS\\view\\mobile')

    # 删除eUrbanMIS/WEB-INF/lib/下的egova-statis-ex.jar
    file_dir = path + '\\eUrbanMIS\\WEB-INF\\lib'
    if os.path.exists(file_dir + '\\egova-statis-ex-1.0.1-mysql.jar'):
        os.remove(file_dir + '\\egova-statis-ex-1.0.1-mysql.jar')

    path_release = input('请输入版本的lib路径：\n')
    path_hotfix = input('请输入hotfix的lib路径：\n')

    # 保存并移动新增的包
    get_compare(path_release, path_hotfix, path)

     # 配置文件暂时手动进行

    print('完成！')

def get_jsinfo(path):
    '''
    :param path: 根路径
    :return:
    '''
    file_list = get_files(path)
    with open(path+'\\修改的JS文件记录.txt','w') as i:
        for f in file_list:
            if f.endswith('.js'):
                i.write(f+'\n')
        i.write('\n'+'重点JS文件：'+'\n')
        for f in file_list:
            if f.endswith('i18n.js'):
                i.write(f + '\n')

def get_DifConf():
    path_release = input('请输入版本的conf路径：\n')
    path_hotfix = input('请输入hotfix的conf路径：\n')

    confFiles_release = get_files(path_release)
    confFiles_hotfix = get_files(path_hotfix)

def work_main():
    '''
    处理差异文件主流程：
    1、创建文件结构，需手动输入root_path，创建文件基本结果，拷贝bc差异文件至eUrbanMIS文件下；
    2、提取本版本相比release新增的文件夹或文件；
    3、按照上个版本的文件结构处理当前版本内的文件，然后处理新增的文件；
    4、文件内容对比，获取修改的内容；自动完成txt内容的编写。
    '''

    # 创建文件结构，提示拷贝bc差异文件至eUrbanMIS文件下
    path = input('请输入根目录：\n')
    if os.listdir(path):
        print('根目录不为空。\n清理根目录。')
        for i in os.listdir(path):
            item_path = path + '\\' + i
            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)
        print('根目录清理完成。')

        create_dir_structure(path)
        print('文件结构完成。')
    else:
        create_dir_structure(path)
        print('文件结构完成。')

    # 以上次整理的其他文件夹为基准进行整理本次包
    difFile_flag = input('是否已放入差异文件至eUrbanMIS下(y/n);\n')
    path_old = input('请输入之前hotfix版本升级文件根路径来作为包的基准：\n')
    get_package(difFile_flag,path,path_old)

    # 增加或减少的包整理、各种文件的删除。增加的包以及文件写进txt文件
    get_addOrDel(path)

    # i18l.js如果有更新，找到更新的内容，并把相关内容写进在txt并保存下来
    get_jsinfo(path)


if __name__ == '__main__':
    work_main()

