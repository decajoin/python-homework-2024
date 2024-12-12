import pickle

i = 13000000
a = 99.056
s = '中国人民123abc'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 10, 8)
coll = {4, 5, 6}
dic = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}
data = [i, a, s, lst, tu, coll, dic]

# 序列化
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# 反序列化并保存到txt文件
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(str(loaded_data))
