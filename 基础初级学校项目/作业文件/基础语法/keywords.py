import keyword

print("Python 关键字：")
print(", ".join(keyword.kwlist))
print(f"'if' 是关键字吗？{keyword.iskeyword('if')}")
