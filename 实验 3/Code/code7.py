# （1）创建初始的通信录字典 dicTXL
dicTXL = {
    '小明': {'手机号': '13912345678', 'QQ号': '12345678'},
    '小华': {'手机号': '13987654321', 'QQ号': '87654321'},
    '小李': {'手机号': '13911223344', 'QQ号': '11223344'}
}

# 假设隔壁舍长的字典 dicOther
dicOther = {
    '小王': {'手机号': '13800000001', 'QQ号': '22233344'},
    '大王': {'手机号': '13800000002', 'QQ号': '33344455'}
}

# （2）合并 dicOther 到 dicTXL
dicTXL.update(dicOther)

# （3）添加微信号字典 dicWX
dicWX = {
    '小明': 'wx_xiaoming123',
    '小王': 'wx_xiaowang456'
}

# 为每个同学添加微信号，如果没有微信号则默认设置为手机号
for name in dicTXL:
    if name in dicWX:
        dicTXL[name]['微信号'] = dicWX[name]
    else:
        dicTXL[name]['微信号'] = dicTXL[name]['手机号']

# （1）更改“大王”的手机号
dicTXL['大王']['手机号'] = '13914000004'

# 定义查找功能
def find_contact(name):
    if name in dicTXL:
        contact = dicTXL[name]
        return f"姓名: {name}, 手机号: {contact['手机号']}, QQ号: {contact['QQ号']}, 微信号: {contact['微信号']}"
    else:
        return "没有该同学的联系方式"

# 测试查找功能
print(find_contact('小明'))  # 查找小明的联系方式
print(find_contact('大王'))  # 查找大王的联系方式
print(find_contact('未知'))  # 查找不存在的同学
