class Number:
    def __init__(self, n1=8, n2=4):
        self.__n1 = n1
        self.__n2 = n2

    def addition(self):
        return self.__n1 + self.__n2

    def subtraction(self):
        return self.__n1 - self.__n2

    def multiplication(self):
        return self.__n1 * self.__n2

    def division(self):
        return self.__n1 / self.__n2 if self.__n2 != 0 else "除数不能为0"

# 测试
calculator = Number(8, 19)
print("加法:", calculator.addition())
print("减法:", calculator.subtraction())
print("乘法:", calculator.multiplication())
print("除法:", calculator.division())
