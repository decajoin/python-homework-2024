import random

def generate_passwords():
    random.seed(0x1010)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    passwords = []
    while len(passwords) < 10:
        password = ''.join(random.sample(chars, 10))
        if not any(p[0] == password[0] for p in passwords):
            passwords.append(password)
    with open("随机密码.txt", "w") as f:
        f.writelines(p + '\n' for p in passwords)

generate_passwords()
