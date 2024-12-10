class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.scores)

# 测试
student1 = Student("zhangming", 20, [69, 88, 100])
print(student1.get_name())  # 输出姓名
print(student1.get_age())   # 输出年龄
print(student1.get_course())  # 输出最高成绩
