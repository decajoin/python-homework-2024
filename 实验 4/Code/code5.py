# 输入两个整数
a = int(input("请输入第一个整数 a: "))
b = int(input("请输入第二个整数 b: "))

# 确保 a >= b
if a < b:
    a, b = b, a

# 使用循环求最大公约数
while b != 0:
    r = a % b  # 求余数
    a = b      # 更新 a 为 b
    b = r      # 更新 b 为 r

# 当 b 为 0 时，a 即为最大公约数
print("两个数的最大公约数是:", a)
