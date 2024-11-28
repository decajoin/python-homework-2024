# 对字符串去重并按字母排序
s = "ajldjlajfdljfddd"

# 使用set去重并转为列表
unique_list = list(set(s))  # 去重

# 对列表排序
unique_list.sort()  # 按字母从小到大排序

# 将排序后的字符连接成字符串
result = "".join(unique_list)  # "adfjl"

# 输出结果
print(result)
