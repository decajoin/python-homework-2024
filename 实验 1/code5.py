# 输入一个输入一个包含若干整数的列表，输出新列表，要求新列表中所有的元素来自输入的列表，并且降序排列
numbers = input("请输入列表：")
numbers = list(map(int, numbers.split()))
numbers.sort(reverse=True)
print(numbers)