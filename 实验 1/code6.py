# 输入一个包含若干整数的列表，输出列表中所有整数连乘的结果
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# 测试
numbers = input("请输入一个列表：")
numbers = list(map(int, numbers.split()))
print(multiply_list(numbers))