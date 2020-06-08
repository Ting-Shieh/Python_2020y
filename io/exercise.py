
word = input("請輸入單字:")
file_name = "./Data/dict.txt"
f = open(file_name, mode='r', encoding='utf8')
# for line in f:
#     if word[0] == line[0]:
#         if word == line[0:len(word)] and line[len(word)] ==" ":
#             print(line)

for line in f:
    # print(line.split(".")[-1])
    target = line.split(" ")[0]
    # 遍歷的單字已經大於目標，表示找不到
    if  target > word:
        print("沒找到該單字")
        break
    elif word == target:
        print(line)
        break
# 考慮輸入的單字特別大的防呆
else:
    print("沒找到該單字")

f.close()