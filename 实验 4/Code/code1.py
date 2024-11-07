# 提示用户输入三个整数并转换为整型
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
num3 = int(input("请输入第三个整数: "))

# 使用 min 函数求出最小值
min_value = min(num1, num2, num3)

# 输出最小值
print("三个数中的最小值是:", min_value)
