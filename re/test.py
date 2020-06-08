
import re
t = """首部台灣國語古裝劇《才子佳人乾隆皇》，即擔綱飾演一個女主角沈雨棠。之後，又到民視挑戰台語古裝劇《飛龍在天》，飾演金蘭花一角而受到關注。
2003年與岳翎、黃維德、宋逸民參演馮凱執導的古裝電視劇《青龍好漢》。2004年與王識賢﹑張鳳書﹑劉至翰參演台灣民視製作超長篇電視劇《意難忘》。2006年3月因酬勞與周遊鬧合約糾紛，後來由民視出面協調解決，2人在2007年解約。2008年4月經由朋友劉至翰介紹，加盟新東家天合演藝經紀有限公司。
2009年出演三立電視劇《天下父母心》。2010年9月與孫協志相識相戀，於2011年11月21日正式登記結婚，2012年補請宴客。2011年與天合演藝經紀有限公司因合約到期而不再續約，韓瑜出書「幸福花嫁的決定」。2012年1月加入由孫協志經營的不動心娛樂事業有限公司[2]並開始運作。2013年年底參演三立電視劇《世間情》
。2013年參演三立自製台灣好戲《孤戀花》女主角，一人飾演兩角葉秋憐﹑白玉蘭。2014年3月參演中國電視公司《月亮上的幸福》
。2015年4月，離開不動心娛樂事業有限公司改簽約至亞樂演藝經紀並參演三立電視劇《甘味人生》。同年10月已與孫協志辦妥了離婚手續。結束4年婚姻，膝下無子。他在個人網站表示：「分開，是因為彼此對未來的生活目標，有了不同的計劃與想法[3]」。
2016年4月與前男友李政穎一起合演大愛劇場竹南往事。2017年3月22日在三立台灣臺定裝，準備接演八點檔大戲《一家人》。同年12月21日在三立台灣臺定裝，接演八點檔大戲《金家好媳婦》。"""

# ste = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", t)
# print(ste)
# results = re.findall(r'《.+?》',ste)  #匹配
# print(results)

results_d = re.findall(r'\d',t)  #匹配
results_d_plus = re.findall(r'\d+',t)  #匹配
print("\d: ",results_d)
print("\d+: ",results_d_plus)
print('|:',re.findall('com|cn',"www.baidu.com/www.tmooc.cn"))
print('[^0-9]:',re.findall('[^0-9]',"Use 007 port"))

print('^Jame:',re.findall('^Jame',"Jame,hello"))
print('^Jame:',re.findall('^Jame',"Hi,Jame"))
print('Jame$:',re.findall('Jame$',"Hi,Jame"))
print('^Jame$:',re.findall('^Jame$',"Hi,Jame"))
print('^Jame|Jame$:',re.findall('^Jame|Jame$',"Jame,hello"))


print('wo*:',re.findall('wo*',"wooooo~~w!"))
print(':*:',re.findall('[0-9]+年', t))

en_text = """
In cell phone footage taken Monday by a bystander, 
Chauvin can be seen kneeling on Floyd’s neck for nearly eight minutes while arresting him over allegedly paying with a counterfeit $20 bill. 
Floyd, a 46-year-old black man, was handcuffed and can be heard saying that he cannot breathe. Floyd was pronounced dead later that night while in police custody.
"""
print('大寫字母開頭:',re.findall('[A-Z][a-z]+',en_text))

# print('正數:',re.findall('[^-][0-9]+?',"18, -26 12 13 -19"))
print('所有數:',re.findall('-?[0-9]+',"18, -26 12 13 -19"))
print('負數:',re.findall('-[0-9]+',"18, -26 12 13 -19"))

print('手機號:',re.findall('09[0-9]{8}',"A:0958888888,B:095888877788"))
print('IP地址:',re.findall('[a-z0-9]{4}::[a-z0-9]{4}:[a-z0-9]{4}:[a-z0-9]{4}:[a-z0-9]{4}',"A_IP:fe80::46d3:1722:bbf7:35ac,A:095888877788"))

print('PORT:',re.findall('\d{1,5}',"Mysql: 3306, http:80"))
print('other:',re.findall('\D+',"Mysql: 3306, http:80"))

print('日薪:',re.findall('\$\d+',"日薪:$1500"))