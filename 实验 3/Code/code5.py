# 从键盘输入字符串
input_str = input("请输入一个字符串: ")

# 初始化计数字典
char_count = {'字母': 0, '数字': 0, '其他': 0}

# 遍历字符串，统计字母、数字和其他字符的数量
for char in input_str:
    if char.isalpha():  # 检查是否为字母
        char_count['字母'] += 1
    elif char.isdigit():  # 检查是否为数字
        char_count['数字'] += 1
    else:  # 其他字符
        char_count['其他'] += 1

# 输出统计结果
print(char_count)
