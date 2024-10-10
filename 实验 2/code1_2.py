# 基于蒙特卡罗方法来计算圆周率 π
import random
import turtle
import time

# 设置屏幕大小和画布
window = turtle.Screen()
window.screensize(400, 400)
window.setworldcoordinates(-1, -1, 1, 1)

# 设置画笔
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# 画正方形和圆
pen.penup()
pen.goto(-1, 1)
pen.pendown()
for _ in range(4):
    pen.forward(2)
    pen.right(90)

pen.penup()
pen.goto(0, -1)
pen.pendown()
pen.circle(1, steps=100)

# 计算 π 的函数
def estimate_pi(num_points):
    inside_circle = 0
    pen.penup()
    for _ in range(num_points):
        # 随机生成点的坐标
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # 计算该点是否在圆内
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
            pen.goto(x, y)
            pen.dot(3, "blue")  # 圆内点为蓝色
        else:
            pen.goto(x, y)
            pen.dot(3, "red")  # 圆外点为红色

        time.sleep(0.0001)  # 延时效果，可视化过程

    # 计算 π 的值
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate

# 运行 π 估算函数
num_points = 1000  # 你可以增加这个数值来获得更精确的结果
estimated_pi = estimate_pi(num_points)
print("估算出的 π 值：", estimated_pi)

# 关闭窗口
window.mainloop()
