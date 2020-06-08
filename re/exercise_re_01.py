import re


# TODO 匹配一個.com E-mail 的字符串格式
print("E-mail ANS: ",re.findall(r"\w+\@\w+.com","Email_1:zsting29@gmail.com,Email_2:ting0429@gmail.com,Email_3:ting0429@g163.com"))
# TODO 匹配一個密碼，包含數字字母下滑線 8-12位
print("密碼 ANS: ",re.findall(r"\w{8,12}","密碼1:qazxsw123,密碼2:wsx45_errfv5,密碼3:rty_1f_223_f"))
# TODO 匹配一個 數字  整數  小數  負數 百分位數  分數
print("3.ANS: ",re.findall(r"-?\d+\.?/?\d*\%?","100 12.3 -2.3 23.5% 2/3"))
# TODO 匹配一段文字中以大小字母開頭的單詞，若單詞為全大寫英文字母，也要匹配到
print("4.ANS: ",re.findall(r"\b[A-Z][a-zA-Z]*","This is my new NB and iPython"))


print('IP地址:',re.search('([a-z0-9]{4}\:){4}[a-z0-9]{4}',"A_IP:fe80:46d3:1722:bbf7:35ac,A:095888877788").group())

print('()Name:',re.search(r'(王|李)\w{1,3}',"王小名 王大明 謝吳祖 李明明 李白").group())

