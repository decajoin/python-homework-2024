# 获取用户输入的数字
num = int(input("请输入一个数字: "))

# 将数字转换为字符串
num_str = str(num)

# 判断回文数的方法
if num_str == num_str[::-1]:
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")
