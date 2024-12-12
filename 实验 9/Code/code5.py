import json

with open("天龙八部-网络版.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("天龙八部-序列化.json", "wb") as f:
    f.write(json.dumps(content).encode("utf-8"))
