class RiverChiefDataManage():
    '''河长制数据管理'''

    # 导航图标

    """基础信息管理-河流基本信息"""
    # 基本信息管理栏
    basicInfoManage = ('xpath', '//div[text()="基础信息管理"]')
    # 河流基本信息
    riverBasicInfo = ('xpath', '//div[text()="河流基本信息"]')
    # 河流列表
    riverList = ('xpath', '//ul[@id="riverTree"]/li/ul/li[%s]/div/span[@class="tree-title"]')
    # 河流 新增按钮
    riverAdd = ('xpath', '//div[@data-bind="click:add,text: textAddButton"]')
    # 河流 新增河流列表记录
    riverAddList = ('xpath', '//ul/li[%s]/div/span[contains(text(),"新增河流")]')
    # 河流编码
    riverCode = ('xpath', '//div[text()="河流编码"]//following-sibling::input')
    # 河流名称
    riverName = ('xpath', '//div[text()="河流名称"]//following-sibling::input')
    # 河流曾用名
    riverUsedname = ('xpath', '//div[text()="曾用名"]//following-sibling::input')
    # 河流简称
    riverShortName = ('xpath', '//div[text()="简称"]//following-sibling::input')
    # 河流所在水系名称
    riverSystem = ('xpath', '//div[text()="所在水系名称"]//following-sibling::input')
    # 河流上级河流
    riverSuper = ('xpath', '//div[text()="上级河流"]//following-sibling::input')
    # 河流长度
    riverLength = ('xpath', '//div[text()="河流长度(KM)"]//following-sibling::input')
    # 河流面积
    riverArea = ('xpath', '//div[text()="流域面积(KM2)"]//following-sibling::input')
    # 河流经度
    riverLongitude = ('xpath', '//div[text()="河源地理坐标X"]//following-sibling::input')
    # 河流纬度
    riverlatitude = ('xpath', '//div[text()="河源地理坐标Y"]//following-sibling::input')
    # 河流河源
    riverSource = ('xpath', '//div[text()="河源"]//following-sibling::input')
    # 河流河口
    riverEntry = ('xpath', '//div[text()="河口"]//following-sibling::input')
    # 河流河口经度
    riverEntryLongitude = ('xpath', '//div[text()="河口地理坐标X"]//following-sibling::input')
    # 河流河口纬度
    riverEntrylatitude = ('xpath', '//div[text()="河扣地理坐标Y"]//following-sibling::input')
    # 河流跨界类型
    riverOutAreaType = ('xpath', '//div[text()="跨界类型"]//following-sibling::input')
    # 河流行政区域名称
    riverAdministrativeRegion = ('xpath', '//div[text()="行政区域名称"]//following-sibling::input')
    # 河流 保存按钮
    riverSave = ('xpath', '//div[text()="保存"]')
    # 河流 保存确认
    riverSaveCommit = ('xpath', '//div[text()="确定"]')
    # 河流 删除
    riverDel = ('xpath', '//div[@data-bind="click:del,text: textDelButton" and text()="删除"]')
    # 河流 删除确认
    riverDelCommit = ('xpath', '//div[text()="是"]')

    """基础信息管理-河段基本信息"""
    # 河段基本信息菜单栏
    rSecTab = ('xpath', '//div[text()="河段基本信息"]')
    # 河段列表下的河流
    upRiverList = ('xpath', '//ul[@id="riverSegTree"]/li/div/span[text()="%s"]')
    # 新增按钮
    rSecAddBtn = ('xpath', '//div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[text()="新增"]')
    # 河段基本信息Tab
    rSecBasicInfo = ('xpath', '//*[@id="riverBuilder-riverSegInfo-container"]/div[2]/div[1]/div[3]/div[text()="基本信息"]')
    # 河段基本信息
    rSecCode = ('xpath', '//div[text()="河段编码"]//following-sibling::input')
    rSecName = ('xpath', '//div[text()="管理河段名称"]//following-sibling::input')
    rSecInRiver = ('xpath', '//div[text()="所属河流"]//following-sibling::input')
    rSecSuper = ('xpath', '//div[text()="上级河段"]//following-sibling::input')
    rSecLength = ('xpath', '//div[text()="河段长度"]//following-sibling::input')
    rSecArea = ('xpath', '//div[text()="所属区域名称"]//following-sibling::input')
    rSecCenX = ('xpath', '//div[text()="河段中间点X坐标"]//following-sibling::input')
    rSecCenY = ('xpath', '//div[text()="河段中间点Y坐标"]//following-sibling::input')
    rSecUX = ('xpath', '//div[text()="上河口X坐标"]//following-sibling::input')
    rSecUY = ('xpath', '//div[text()="上河口Y坐标"]//following-sibling::input')
    rSecULoc = ('xpath', '//div[text()="上河口位置描述"]//following-sibling::input')
    rSecDLoc = ('xpath', '//div[text()="下河口位置描述"]//following-sibling::input')
    rSecDX = ('xpath', '//div[text()="下河口X坐标"]//following-sibling::input')
    rSecDY = ('xpath', '//div[text()="下河口Y坐标"]//following-sibling::input')