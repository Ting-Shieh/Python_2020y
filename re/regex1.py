import re

s="同婚1周年囉，2019年05月24日通過法案~"

# 返回迭代對象
res_iter = re.finditer(r'\d+',s,flags = 0)
for item in res_iter:
    # 返回 re.Match object  = item
    print(item.group()) #獲取　Match　對象內容


# 完全匹配
obj = re.fullmatch(r'.+',s)
print(obj.group())


# 匹配start
obj2 = re.match(r'\w+',s)
print(obj2.group())