import random

# 计算 π 的函数
def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        # 随机生成点的坐标
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # 计算该点是否在圆内
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1

    # 计算 π 的值
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

# 运行 π 估算函数
num_points = 1000000  # 你可以根据需要调整这个数值
estimated_pi = estimate_pi(num_points)
print(f"使用 {num_points} 个点估算出的 π 值：", estimated_pi)
