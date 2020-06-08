list01 = ['A', 'B', 'C']
list02 = [101, 102, 103]
print("=============練習zip================")
for item in zip(list01, list02):
     print(item)

print("=============練習自建造zip================")
def my_zip1(obj1, obj2):
    star_num = -1
    while star_num < len(obj1) or star_num < len(obj2):
        if star_num > len(obj1)-1 or star_num >len(obj2)-1:
            raise StopIteration
        star_num += 1
        yield obj1[star_num],obj2[star_num]

def my_zip2(obj1, obj2):
    for i in range(len(obj1)):
        yield obj1[i],obj2[i]


# for item in my_zip1(list01, list02):
#     print(item)
for item in my_zip2(list01, list02):
    print(item)
# ctrl+p
# for item in zip():
#      print(item)