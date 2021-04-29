# coding=utf-8
"""
2016-05-26
lib文件重复文件检查
liukai
"""

import os

def a(path):
    fileLists = os.listdir(path)
    # print(fileLists)

    depenFiles = fileLists
    # for i in fileLists:
    #     if not i.startswith('egova'):
    #         depenFiles.append(i)
    # print(depenFiles)

    from copy import deepcopy
    compareLists = []
    temp = deepcopy(depenFiles)
    for i in depenFiles:
        temp.remove(i)
        for j in temp:
            compareLists.append([i, j])
    # print(compareLists)

    # 处理：数字前得完全一样，作为一样得
    res=[]
    for i in compareLists:
        a = i[0].split('-')
        b = i[1].split('-')
        num_flag1 = 0
        num_flag2 = 0
        for m in range(len(a)):
            if a[m][0].isdigit():
                num_flag1 = m
                break
        for n in range(len(b)):
            if b[n][0].isdigit():
                num_flag2 = n
                break
        if num_flag1 == num_flag2:
            if a[:num_flag1]==b[:num_flag1] and a[:num_flag1] != []:#and ((len(i[0])==len(i[1])) or (len(i[0])+1==len(i[1])) or (len(i[0])==len(i[1])+1)):
                res.append(i)

    return res




if __name__ == '__main__':
    import sys
    path = r'D:\0501版本管理\egova-app\WEB-INF\lib'
    # path = sys.argv[1]
    res= a(path)
    from pprint import pprint
    pprint(res)
