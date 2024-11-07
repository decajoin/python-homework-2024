from math import sqrt

# 初始变量设置
pi = 2.0         # 初始 pi 值
p = sqrt(2)      # 初始分母
temp_pi = 0.0    # 存储上一次的 pi 值，用于判断收敛
m = int(input("请输入 pi 的计算精度，有效位数为："))

# 迭代计算 pi 值，直到两次计算的差值小于指定精度
while abs(pi - temp_pi) > 10**(-m):
    temp_pi = pi                   # 更新 temp_pi 为当前 pi 值
    pi *= 2 / p                    # 更新 pi 值
    p = sqrt(2 + p)                # 递推更新分母

# 输出最终计算结果
print(f"精确到小数点后 {m} 位的 π 值为：{pi:.{m}f}")
