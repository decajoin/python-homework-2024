# 使用map()对列表每个元素平方，并提取平方值大于10的元素
lst = [1, 2, 3, 4, 5]

# 使用map()对列表元素平方
squared = list(map(lambda x: x**2, lst))  # [1, 4, 9, 16, 25]

# 列表推导式提取大于10的平方值
result = [x for x in squared if x > 10]  # [16, 25]

# 打印结果
print(result)
