class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def superficial(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

# 实例化对象
b1 = Box(1, 1, 1)
print("体积:", b1.volume())
print("表面积:", b1.superficial())
