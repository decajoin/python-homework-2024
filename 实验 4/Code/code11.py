import math

def cos_taylor(x, precision=10):
    # 迭代计算直到最后一项的绝对值小于10^(-precision)
    epsilon = 10 ** (-precision)

    cos_x = 1.0  # 初始化cos(x)的值为1
    term = 1.0   # 当前项的初始值
    n = 0        # 当前项的幂指数

    while abs(term) >= epsilon:
        term *= -x ** 2 / ((2 * n + 1) * (2 * n + 2))
        cos_x += term
        n += 1

    return round(cos_x, precision)

if __name__ == "__main__":
    degree = float(input("输入角度(度数): "))
    radian = degree / 360 * 2 * math.pi  # 将度数转换为弧度

    result = cos_taylor(radian)
    print(f"cos({degree:.2f}°) = {result:.6f}")