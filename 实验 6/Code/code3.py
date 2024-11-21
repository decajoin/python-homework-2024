def fun(s):
    digit_number = 0
    space_number = 0
    alpha_number = 0
    else_number = 0
    for i in s:
        if i.isdigit():
            digit_number += 1
        elif i.isspace():
            space_number += 1
        elif i.isalpha():
            alpha_number += 1
        else:
            else_number += 1

    return ("数字为:" + str(digit_number),
            "空格为：" + str(space_number),
            "字母为：" + str(alpha_number),
            "其他为：" + str(else_number))

ans = fun(input("请输入一串字符："))
print(ans)
