# 获取用户输入
a = input("请输入一个数字a: ")
n = int(input("请输入加数的个数n: "))

# 初始化总和为0
s = 0

# 循环累加重复数字构成的项
for i in range(1, n + 1):
    # 构造当前项，重复数字a i次，并转换为整数
    current_term = int(a * i)
    s += current_term

# 输出结果
print(f"结果是: {s}")
