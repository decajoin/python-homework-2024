# 输入一个自然数，输出它的二进制、八进制、十六进制表示
num = int(input("请输入一个自然数："))

# 二进制表示
binary = bin(num)
print("二进制表示：", binary)

# 八进制表示
octal = oct(num)
print("八进制表示：", octal)

# 十六进制表示
hexadecimal = hex(num)
print("十六进制表示：", hexadecimal)