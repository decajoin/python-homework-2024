# 模拟用户登录
def user_login():
    # 用户及对应的密码
    users = ["张三", "李四", "王五", "赵六"]
    passwords = ["123", "456", "abcd", "5try"]

    # 定义尝试次数
    attempts = 3

    while attempts > 0:
        # 输入用户名和密码
        username = input("Enter username: ")
        password = input("Enter password: ")

        # 判断用户是否存在
        if username in users:
            index = users.index(username)  # 获取用户名对应的索引
            if passwords[index] == password:
                print("Login successful!")
                return
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

        attempts -= 1
        print(f"Remaining attempts: {attempts}")

    print("Login failed. No attempts left.")

# 运行登录函数
user_login()
