def find_max_and_sum(*args):
    if not args:
        return None, 0
    max_val = max(args)
    total_sum = sum(args)
    return max_val, total_sum

# 输入并计算
numbers = list(map(int, input("请输入多个整数，以空格分隔：").split()))
max_val, total_sum = find_max_and_sum(*numbers)
print(f"最大值：{max_val}, 总和：{total_sum}")
