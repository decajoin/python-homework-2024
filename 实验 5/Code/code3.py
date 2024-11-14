# 获取用户输入的字符串
input_string = input("请输入字符串：")

# 初始化各类字符计数器
letters = 0  # 字母计数
spaces = 0   # 空格计数
digits = 0   # 数字计数
others = 0   # 其他字符计数

# 遍历字符串中的每个字符并分类
for char in input_string:
    if char.isalpha():  # 判断是否是字母（中英文都包括）
        letters += 1
    elif char.isspace():  # 判断是否是空格
        spaces += 1
    elif char.isdigit():  # 判断是否是数字
        digits += 1
    else:  # 其他字符
        others += 1

# 输出结果
print(f"字母个数: {letters}")
print(f"空格个数: {spaces}")
print(f"数字个数: {digits}")
print(f"其他字符个数: {others}")
