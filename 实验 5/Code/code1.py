total = 0
s = ['0', 'a', 'b', 'c', 'd']
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 排除重复的字母
            if i != j and j != k and i != k:
                print(s[i], s[j], s[k])
                total += 1
print(total)
