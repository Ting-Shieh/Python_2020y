import re

s = "Alex:1197,Sunny:1996,Joy:2006"


pattern = r'(\w+):(\d+)'
l =re.findall(pattern,s)
print(l)

regex =re.compile(pattern)
l2 =regex.findall(s)
print(l2)


l3 =re.split(r",",s)
print(l3)

l4 =re.sub(r":", '--',s,count=2)
print(l4)