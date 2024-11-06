# 定义电话簿字典
phone_book = {
    'mayun': '13309283335',
    'zhaolong': '18989227822',
    'zhangmin': '13382398921',
    'Gorge': '19833824743',
    'Jordan': '18807317878',
    'Curry': '15093488129',
    'Wade': '19282937665'
}

# 提示用户输入联系人名字
name = input("请输入联系人名字: ")

# 查询并输出电话号码，如果联系人不存在，则提示用户
if name in phone_book:
    print(f"{name} 的电话号码是: {phone_book[name]}")
else:
    print(f"抱歉，电话簿中没有找到 {name}。")
