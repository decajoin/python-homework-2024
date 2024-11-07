# 提示用户输入20个评分
scores = []
for i in range(20):
    score = float(input(f"请输入第{i+1}位评委的评分（1-10之间）: "))
    # 确保评分在1到10之间
    while score < 1 or score > 10:
        print("评分无效，请输入1到10之间的数值。")
        score = float(input(f"请重新输入第{i+1}位评委的评分: "))
    scores.append(score)

# 去掉一个最高分和一个最低分
scores.sort()
trimmed_scores = scores[1:-1]  # 去掉第一个和最后一个

# 计算平均分
average_score = sum(trimmed_scores) / len(trimmed_scores)

# 输出选手的平均得分
print(f"选手的平均得分为: {average_score:.2f}")
