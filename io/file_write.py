file_name = "./Data/io_demo.txt"
# f = open(file_name, mode='w', encoding='utf8')
# # mode='w' 如需要換行，需加 \n
# f.write("hello, 死鬼~\n")
# f.write("誰給你叫死鬼~\n")
# f.close()

# # # mode='a' 追加，如需要換行，需加 \n
# f = open(file_name, mode='a', encoding='utf8')
# f.write("誰叫我是你老婆~\n")
# f.close()
f = open(file_name, mode='w', encoding='utf8')
# 寫入列表內容，一口氣寫入全部
l = ["hi hi","ha ha"]
f.writelines(l)