def is_narcissistic(num):
    # 将数字转为字符串,方便获取各位数字
    num_str = str(num)

    # 计算各位数字的立方和
    cube_sum = sum(int(digit) ** len(num_str) for digit in num_str)

    # 如果立方和等于原数字,则为水仙花数
    return cube_sum == num

def print_narcissistic_numbers():
    """
    输出所有3位数的水仙花数
    """
    for num in range(100, 1000):
        if is_narcissistic(num):
            print(num)

if __name__ == "__main__":
    print("所有3位数的水仙花数为:")
    print_narcissistic_numbers()