# 用户名和密码列表
Users = ["张三", "李四", "王五", "赵六"]
Passwords = ["123", "456", "abcd", "5try"]

# 获取用户输入的用户名和密码
input_username = input("请输入用户名: ")
input_password = input("请输入密码: ")

# 判断用户名是否在Users列表中
if input_username in Users:
    # 获取用户名对应的索引
    index = Users.index(input_username)

    # 比较输入的密码与该用户名对应的密码
    if input_password == Passwords[index]:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名不存在")
