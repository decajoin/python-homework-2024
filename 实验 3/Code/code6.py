# 评分表
dic_score = {
    '012': [90, 94, 85, 54, 68, 75, 71, 21],
    '005': [8, 75, 21, 65, 89, 97, 25, 75],
    '108': [87, 54, 78, 25, 14, 98, 67, 57],
    '037': [45, 87, 54, 82, 95, 91, 57, 32],
    '066': [95, 67, 51, 48, 98, 92, 80, 39],
    '020': [85, 81, 65, 97, 35, 62, 71, 84]
}

# 计算每位选手的平均分
final_scores = {}
for contestant, scores in dic_score.items():
    sorted_scores = sorted(scores)  # 排序评分
    trimmed_scores = sorted_scores[1:-1]  # 去掉一个最高分和一个最低分
    average_score = sum(trimmed_scores) / len(trimmed_scores)  # 计算平均分
    final_scores[contestant] = average_score

# 按平均分由高到低排序
sorted_final_scores = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)

# 输出结果
for contestant, score in sorted_final_scores:
    print(f"选手编号: {contestant}, 平均分: {score:.2f}")
