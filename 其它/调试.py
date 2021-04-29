import jpype

with open(r'C:\Users\asd\Desktop\新建文本文档.txt' ) as f:
    jars  = []
    for i in f.readlines():
        if '详细' in i:
            name = (i.split('].')[0]).split('/')[-1]
            # print(name)
            if name not in jars:
                jars.append(name)

    str = ''
    for j in jars:
        str = str+j+','

    print(str)