def calculate_average_score():
    scores = []
    while True:
        score = input("请输入分数: ")
        if not score:
            break
        try:
            scores.append(float(score))
        except ValueError:
            print("无效的分数格式,请重新输入")
            continue

        continue_input = input("是否继续输入下一个分数? (yes/no) ").lower()
        if continue_input == "no":
            break

    if not scores:
        return 0.0

    average_score = sum(scores) / len(scores)
    return average_score

if __name__ == "__main__":
    average_score = calculate_average_score()
    print(f"平均分为: {average_score:.2f}")