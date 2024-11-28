# 找出1000以内的完全数
def is_perfect_number(n):
    # 找到所有除本身外的因子
    factors = [i for i in range(1, n) if n % i == 0]
    return sum(factors) == n  # 判断因子之和是否等于自身

# 遍历1000以内的数，找出完全数
perfect_numbers = [n for n in range(1, 1001) if is_perfect_number(n)]

# 输出结果
print("Perfect numbers within 1000:", perfect_numbers)
