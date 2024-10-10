# 输入一个包含若干整数的列表，输出一个新列表，要求新列表中只包含原列表中的偶数
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# 测试
numbers = input("请输入列表：")
numbers = list(map(int, numbers.split()))
even_numbers = filter_even_numbers(numbers)
print(even_numbers)
