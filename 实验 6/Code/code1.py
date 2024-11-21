import random

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    while True:
        passwords = []
        first_chars = set()

        # 生成10个符合要求的密码
        while len(passwords) < 10:
            password = ''.join(random.choice(chars) for _ in range(10))

            # 检查首字符是否已被使用
            if password[0] not in first_chars:
                passwords.append(password)
                first_chars.add(password[0])

        # 将密码写入文件
        with open("./实验 6/随机密码.txt", "w") as file:
            for pwd in passwords:
                file.write(pwd + "\n")

        return passwords

# 运行程序并生成密码
password_list = generate_password()
print("生成的密码：")
for pwd in password_list:
    print(pwd)
