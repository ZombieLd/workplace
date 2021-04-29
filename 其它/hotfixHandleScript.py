# -*- coding: utf-8 -*-
import os
import shutil
import time

def handlePath(path):
    res = ''
    if path.endswith('\\') or path.endswith('/'):
        res = path[:-1]
    else:
        res = path
    return res


def processFiles_win(misPath, misPatchPath):
    '''
    :param patchPath: 补丁包根路径
    :param misPath: mis代码根路径
    :return:
    '''

    '''智信核心H5替换'''
    # 找到需要替换的H5包
    patchH5Path = misPatchPath + r'\view\mobile\vue\dist'
    patchH5Files = os.listdir(patchH5Path)
    print(patchH5Files)

    timetag_all = int(time.time())
    '''备份mis代码'''
    misBakPath = misPath+'_bak%s'%timetag_all
    print('正在备份mis代码至%s'%misBakPath)
    shutil.copytree(misPath, misBakPath)
    print("mis代码备份完成")

    misPatchPath = handlePath(misPatchPath)

    '''智信核心H5替换'''
    # 找到需要替换的H5包
    patchH5Path = misPatchPath + r'\view\mobile\vue\dist'
    patchH5Files = os.listdir(patchH5Path)
    print(patchH5Files)

    # 备份删除原来的包后复制新包到H5下

    misH5Path = misPath+r'\view\mobile\vue\dist'
    misH5Files = os.listdir(misH5Path)


    for i in patchH5Files:
        if i in misH5Files:
            shutil.rmtree(misH5Path+'\\'+i)
            shutil.copytree(patchH5Path+'\\'+i, misH5Path+'\\'+i)
            print('%s更新成功' % i)


    netFlag = input('请确认是否需要替换多网H5（y/n）:\n')
    netFlag = str(netFlag)

    # netFlag = 'y'
    '''多网H5替换'''
    # 找到需要替换的H5包

    if netFlag == 'y':
        netH5Path = input('请输入多网H5补丁包代码根目录：\n')
        netH5Path = str(netH5Path)
        netH5Path = handlePath(netH5Path)
        netH5Files = os.listdir(netH5Path)
        if netH5Files != []:
            for i in netH5Files:
                if i in misH5Files:
                    shutil.rmtree(misH5Path + '\\' + i)
                    shutil.copytree(netH5Path + '\\' + i, misH5Path+ '\\' + i)
                    print('%s更新成功' % i)

    '''市政前端替换'''
    # 补丁包市政
    patchFacPath = misPatchPath + '\\' + r'view\facilities-new'
    patchFacFiles = os.listdir(patchFacPath)

    # mis包市政
    misFacPath = misPath+'\\'+r'view\facilities-new'
    misFacFiles = os.listdir(misFacPath)

    if patchFacFiles != []:
        for i in patchFacFiles:
            if i in misFacFiles:
                shutil.rmtree(misFacPath + '\\' + i)
                shutil.copytree(patchFacPath + '\\' + i, misFacPath+ '\\' + i)
                print('%s更新成功' % i)


    '''删除jar'''
    jarDeleteFile = misPatchPath + '\\' + 'jarDelete.txt'
    import io
    with io.open(jarDeleteFile, encoding='utf-8') as f:
        jars = f.read().split('\n')
        print(jars)
        for i in jars:
            if i != '':
                jarpath = misPath + r'\WEB-INF\lib' + '\\' + i
                if os.path.exists(jarpath):
                    print(jarpath)
                    os.remove(jarpath)
        print('已删除旧版本jar')

    print("已完成处理！请阅读完更新必读后，确认没问题，便可直接覆盖更新！")

def processFiles_linux(misPath, misPatchPath):
    '''
    :param patchPath: 补丁包根路径
    :param misPath: mis代码根路径
    :return:
    '''
    '''智信核心H5替换'''
    # 找到需要替换的H5包
    patchH5Path = misPatchPath + r'/view/mobile/vue/dist'
    patchH5Files = os.listdir(patchH5Path)
    print(patchH5Files)

    timetag_all = int(time.time())
    '''备份mis代码'''
    misBakPath = misPath+'_bak%s'%timetag_all
    print('正在备份mis代码至%s'%misBakPath)
    shutil.copytree(misPath, misBakPath)
    print("mis代码备份完成")

    misPatchPath = handlePath(misPatchPath)



    # 备份删除原来的包后复制新包到H5下

    misH5Path = misPath+r'/view/mobile/vue/dist'
    misH5Files = os.listdir(misH5Path)


    for i in patchH5Files:
        if i in misH5Files:
            shutil.rmtree(misH5Path+'/'+i)
            shutil.copytree(patchH5Path+'/'+i, misH5Path+'/'+i)
            print('%s更新成功' % i)


    netFlag = input('请确认是否需要替换多网H5（y/n）:\n')
    netFlag = str(netFlag)
    # netFlag = 'y'
    '''多网H5替换'''
    # 找到需要替换的H5包

    if netFlag == 'y':
        netH5Path = input('请输入多网H5补丁包代码根目录：\n')
        netH5Path= str(netH5Path)
        netH5Path = handlePath(netH5Path)
        netH5Files = os.listdir(netH5Path)
        if netH5Files != []:
            for i in netH5Files:
                if i in misH5Files:
                    shutil.rmtree(misH5Path + '/' + i)
                    shutil.copytree(netH5Path + '/' + i, misH5Path+ '/' + i)
                    print('%s更新成功' % i)

    '''市政前端替换'''
    # 补丁包市政
    patchFacPath = misPatchPath + r'/view/facilities-new'
    patchFacFiles = os.listdir(patchFacPath)

    # mis包市政
    misFacPath = misPath+'/'+r'view/facilities-new'
    misFacFiles = os.listdir(misFacPath)

    if patchFacFiles != []:
        for i in patchFacFiles:
            if i in misFacFiles:
                shutil.rmtree(misFacPath + '/' + i)
                shutil.copytree(patchFacPath + '/' + i, misFacPath+ '/' + i)
                print('%s更新成功' % i)


    '''删除jar'''
    jarDeleteFile = misPatchPath + '/' + 'jarDelete.txt'
    import io
    with io.open(jarDeleteFile, encoding='utf-8') as f:
        jars = f.read().split('\n')
        print(jars)
        for i in jars:
            if i != '':
                jarpath = misPath + r'/WEB-INF/lib' + '/' + i
                if os.path.exists(jarpath):
                    print(jarpath)
                    os.remove(jarpath)
        print('已删除旧版本jar')

    print("已完成处理！请阅读完更新必读后，确认没问题，便可直接覆盖更新！")


if __name__ == '__main__':
    misPath = input('请输入mis代码根目录：\n')
    misPatchPath = input('请输入mis补丁包代码根目录：\n')
    misPath = str(misPath)
    misPatchPath = str(misPatchPath)
    misPath = handlePath(misPath)
    try:
        processFiles_win(misPath, misPatchPath)
    except:
        print('系统为linux服务器')
        processFiles_linux(misPath, misPatchPath)

