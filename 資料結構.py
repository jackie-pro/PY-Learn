# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:23:00 2020

@author: Jackie
"""
#20200521
"""
資料結構
=>串列:list (等同資料容器，放資料用的)
  .一連串資料組成 (等同於陣列)
  .可存放不同型態的資料
  .以中括號前後括住資料,資料間以逗號隔開 => []
  .可以建構為多維串列(一維,二維.....)
    串列名稱[起始直 : 終止值]
              ^起始到中止-1的元素     
  .一維串列:
      .list:
"""
#列如:
list1 = []
list2 = [1,2,3,4,5]
list3 = ['apple','banana','orange']
list4 = [1,35,16.78,'pineapple']
print (list3[0]) 
             #^[]索引直]
print (list2[1:3])
print (list2[0:5])

"""
  .串列資料取得:
      串列名稱[索引直]
               ^重0起算      
"""
"""
  .len函式:求串列長度(元素個數)
  
"""
#列如:
print(len(list2))

"""
  .append()函式:加入元素(直接加在串列尾端)

     append(value)  將value加入到串列尾端

"""
#列如:
list1.append(10)
print(list1)
list1.append(20)
print(list1)

"""
  .insert()函式:加入元素(可指定加入串列的位置)
     insert(index,value) 加入元素在指定索引處
            ^索引處  ^元素
"""
#列如:
list1.insert(1,30)
print(list1)    

"""
  .pop()函式:移除串列最後一個元素
   pop(索引值):移除串列指定索引之元素    
   
"""
#列如:
print(list2)
list2.pop()
print(list2)
list2.pop(1)
print(list2)

"""
  .remove()函式:移除指定值
    remove(value)  串列中如有多個相同值,只移除整個串列中第一個value值
    
"""
#列如:
print(list2)
list2.remove(3) 
print(list2)

"""
  .count()函式:求串列值出現的次數 (value)
    count(value)

"""
#列如:
list3.append('apple')
print(list3)
print(list3.count('apple'))

"""
  .index():求串列值所在的索引
    index(value)

"""
#列如:
print(list3)
print(list3.index('apple')) #相同串列值,只顯示整個串列中第一個value值的索引
print(list3.index('banana'))
print(list3.index('orange'))

print(list1)
list1.append(30)
print(list1)
list1.append(40)
print(list1)
list1.append(10)
print(list1)
list1.pop(2)

"""
  .sort()函式:串列排序  #依UNICON碼由小到大
  
"""
#列如:
print(list1)
list1.sort()
print(list1)

"""
  .reverse()函式:串列元素反轉

"""
#列如:
print(list1)
list1.reverse()
print(list1)

"""
  .in / not in:傳回布林值 (判斷元素是否 在/不在 串列中)

"""
#列如:
print(list1)
print(30 in list1)
print(80 not in list1)
  
"""
  .sum()函式:求串列元素總和
  .max()函式:求串列元素最大值
  .min()函式:求串列元素最小值

"""
#列如:
print(list2)
print(sum(list1))
print(max(list1))
print(min(list1))

"""
  .+:連結串列
  .*:複製串列
  
"""
#列如:
print(list1)
print(list2)
print(list1+list2)
print(2 * list2)
print(list1[-1]) #從後面算第一個
print(list1[-3:-1]) #從後面算第三個往回算 到-1 -1 個(=-2個)
print(list1[-4:4]) #從後面算第四個往回算 到4 -1 個(=3個)
#列如:用迴圈取值
list3 = ['apple','banana','orange','kiwi']
print(list3)

for i in range(len(list3)):   #索引是從0開始,因為終使值也是0開始,所以不用填
    print('list3[%d] = %s' % (i, list3[i]))
  

#列如: 數值重複
import random
lotto = []
for i in range(1, 7):
    randNum = random.randint(1 ,49)
    lotto.append(randNum)
print("樂透號碼是 :")
for i in lotto:
    print("%4d" % i , end = '')
 
#列如: 數值不重複 輔助串列 checkNum []
import random
lotto = []
checkNum = []
          #^ checkNum[0,0,0,0,0,.....0,0]  
for i in range(0,50):   #迴圈 0-49 個數
    checkNum.append(0)  # checkNum = []元素全都以 0 帶入

count = 1 
while count <=6:  #while迴圈重複執行6次
    randNum = random.randint(1 ,49) #取亂數 1~49
    if checkNum[randNum] == 0:   #以取得的亂數為索引值帶入到
                                 #checkNum = []串列,判斷該元素是否為0
                                 #0:加入該索引值到lotto[]並設定該索引值checkNum元素為1
                                 #1:該亂數(索引)以加入 lotto[] count不計數(加1)          
        lotto.append(randNum)    #若為0 則將該所引值帶入到lotto[]串列
        count += 1
    checkNum[randNum] = 1     #將checkNum[]串列中該索引值位置支元素設定為1
    
print("樂透號碼是 : \n" , end = '')
for i in lotto:  #不帶range,用lotto表示用串列帶入
    print(i , end = ' ')   
print()
    
#列如:數值不重複 not in
import random
lotto = []
n = 1
while n <= 6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1
print("樂透號碼是 : \n" , end = '')
for i in lotto:
    print("%4d" % i , end = ' ') 
print()  

#列如:數值不重複 not in 並用 sort 排序
import random
lotto = []
n = 1
while n <=6:
    randNum = random.randint(1, 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1
print("樂透號碼是 : \n" , end = '')
for i in lotto: #不帶range,用lotto表示用串列帶入
    print("%4d" % i , end = ' ') 
print()  

lotto.sort()
print("號碼排序後 : ")
for i in lotto:
    print("%4d" % i , end = ' ') 
print()

#(TQC+)二維串列 (考題)
lst = [[1,2,3],[4,5,6]]
print(lst)
print(lst[0])
print(len(lst))  # len函式:求串列長度(元素個數)
print(len(lst[0]))      

"""
  .二維串列
    視為多個一維串列組成
    如5位學生,每位學生3科成績

st = [[85,68,73],[96,81,60],[87,77,58],[80,60,60],[75,81,55]]
        #^st[0]    ^st[1]     ^st[2]     ^st[3]     ^st[4]
        # ^----------^----------^----------^----------^ 5位學生
                           # ^--^--^ 3科成績 st[2][0]=87
                           #                st[2][1]=77
                           #                st[2][2]=58 => (二維串列)
[[1,2,3],[4,5,6]] 二維串列 = 2 x 3串列

"""
#列如:
list5 = [[1,2,3],[4,5,6]]
print(list5)
print(list5[0])
print(len(list5))
print(len(list5[1]))
print(sum(list5[1]))
print(sum(list5[1] + list5[0]))

#列如:
#輸入二維元素數量後,隨機產生該數量的1~50數值
import random
print('請在下面輸入二維串列的欄 與 列,將隨機產生二維串列:')
rows = eval(input('請輸入二維串列的 欄 數:'))
colums = eval(input('請輸入二維串列的 列 數:'))
lst = []
for i in range(rows):
    lst.append([])  #將lst 建為二維串列
    for j in range(colums):
        lst[i].append(random.randint(1, 50))
print(lst)


#列如:
#輸入二維元素數量後,隨機產生該數量的1~50數值,並列出完整二維串列
import random
print('請在下面輸入二維串列的欄 與 列,將隨機產生二維串列:')
rows = eval(input('請輸入二維串列的 欄 數:'))
colums = eval(input('請輸入二維串列的 列 數:'))
lst = []
for i in range(rows):
    lst.append([])  #將lst 建為二維串列
    for j in range(colums):
        lst[i].append(random.randint(1, 50))
print(lst)
print()
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print('lst[%d][%d] = %5d' % (i, j, lst[i][j]))
print()

#列如:
#輸入二維元素數量後,隨機產生該數量的1~50數值,並列出完整二維串列,並計算總合
import random
print('請在下面輸入二維串列的欄 與 列,將隨機產生二維串列:')
rows = eval(input('請輸入二維串列的 欄 數:'))
colums = eval(input('請輸入二維串列的 列 數:'))
lst = []
for i in range(rows):
    lst.append([])  #將lst 建為二維串列
    for j in range(colums):
        lst[i].append(random.randint(1, 50))
print(lst)
print()

for i in range(len(lst)):
    for j in range(len(lst[0])):
        print('lst[%d][%d] = %5d' % (i, j, lst[i][j]))
print()

for colum in range(len(lst[0])):
    total = 0
    for row in range(len(lst)):
        total += lst[row][colum]
    print('第 %d 行的總和 = %d' % (colum ,total))

for row in range(len(lst)):
    total = 0
    for colum in range(len(lst[0])):
        total += lst[row][colum]
    print('第 %d 欄的總和 = %d' % (colum ,total))

#=====================================================  
"""
=>元組(數組):tuple
  .與串列(list)類似
   不同如下:
    1.tuple內元素值不可改變
    2.無法刪除個別元素
    3.無法取代個別元素
    4.可刪除整個數組 #使用del刪除整個tuple
    5.以小括號建立tuple
    
"""
#列如:
tu1 = (1,2,3,4,5)
print(tu1)
tu2 = ()
tu3 = tuple([x for x in range(1,6)])
print(tu3)
tu4 = tuple('Python')
print(tu4)
tu1 += (6,7)
print(tu1)
tu1[2]
print(tu1[2])
tu1[3:6]
print(tu1[3:6])
tu3 = 2 * tu3
print(tu3)

for i in tu1:
    print(i, end=' ')

del tu1
print(tu1)

#=====================================================  
"""
=>集合:set  => 採自動排序 print 會看 hash map 的 bucket值
  .以大括號{} 建立
    s1 = {1,2,3}
    s2 = set()
    s3 = set([x for x in range(1,6)])
    print(s3)
    s4 = set((1,2,3))
    print(s4)
    
  .集合不包含重複資料
    s5 = set ((1,1,2,2,3))
    print(s5)
    
  .add(x):將X加入集合 (跟append一樣加到最後面)
    s10 = {1,3,6}
    s10.add(20)
    print(s10)
    
  .remove(x):將x從集合移除
    s10.remove(20)
    print(s10)
    del s10
    
  .聯集:union(集合) => | (符號)
    set20 = {1,6,8,10,20}
    set25 = {1,3,8,10}
    set20.union(set25)
    print(set20.union(set25))
    print(set20|set25)
    
  .交集:intersection(集合) => & (符號)
    print(set20&set25)
    
  .差集:difference(集合) => - (符號)
    print(set20-set25)
    
  .== :比較兩集合是否相等 (傳回布林值 True or False)
    print(set20==set25)
    
  .!= :比較兩集合是否不相等(傳回布林值 True or False)
    print(set20!=set25)
    
"""    
"""
=>詞典:dict
  .以大括號{}建立
  .資料已鍵值(key)及值(value)組成
  .格式: {key:value}
    dict1 = {'Taipei':'101','Paris':'Tour Eiffel','London':'Big Ben'}
    print(dict1)
    dict1['Berlin']='Wall'
    print(dict1['Taipei'])
    
    for key in dict1:
        print('%s %s' % (key, dict1[key]))
    
    del dict1['Taipei']
    
  .keys() : 列出key值
    dict1.keys()
    print(dict1.keys())
    
  .values() : 列出值
    dict1.values()
    print(dict1.values())
    
  .items() : 列出項目值
    dict1.items()
    print(dict1.items())
    
  tuple(dict1.items())
  print(tuple(dict1.items()))
  
"""
#列如:
dict1 = {'Taipei':'101','Paris':'Tour Eiffel','London':'Big Ben'}
dict2 = {1:'red',2:'yellow',3:'green'}
dict3 = {4:'blue',1:'red'}
dict4 = dict2.copy()
              #^ copy 是複製詞典
print(dict4)
dict4.update(dict3)
       #^ update 是合併詞典 ,相同key值,只取一個，取最後合併進來的值
print(dict4)

#===================================================== 
#實作作業:
宣告一個整數串列(大小為5)
傳遞給output(aList)函式
函式由輸入初始化(輸入資料)後，
回傳給主程式後並輸出該串列
再由主程式將該串列傳給
max(aList)及 min(aList)函式
輸出aList之最大值及最小值
(不可以使用系統函數)

#第一種
a,b,c,d,e = eval(input('請輸入5個串列數:'))
aList = [a,b,c,d,e]
print('aList串列:', aList)
aList.sort()
print('aList串列最大值為: %d ,最小值為 %d' % (aList[4],aList[0]))

#第二種
print('請輸入一個大小為5的串列 :')
aList = []
for i in range(5):
    j = eval(input('請輸入第 %d 個數值:' % (i+1)))
    aList.append(j)
print('aList串列:', aList)
aList.sort()   
print('aList串列最大值為: %d ,最小值為 %d' % (aList[4],aList[0]))

#第三種
print('請輸入一個大小為5的串列 :')
aList = []
def output(aList):
    for i in range(5):
        j = eval(input('請輸入第 %d 個數值:' % (i+1)))
        aList.append(j)
output(aList)
print('aList串列:',aList) 
aList.sort()
print('aList串列最大值為: %d ,最小值為 %d' % (aList[4],aList[0]))






#===================================================== 
#20200522
"""
資料結構整理:
=>串列:list
  .建立 -> 串列名稱 = [元素1,元素2,.....]
  .元素建立後即有索引值
  .索引值從0開始起算
    append:加入元素(元素可為資料,串列)
    extend:加入元素(元素為串列)

=>數組(元祖):Tuple
  .建立 -> 數組名稱 = (元素1,元素2,.....)
  .元數個數,元數值皆不可改變
    (其餘皆同串列)
    (不可使用append,insert)
  .串列功能比數組大
    優點:
        1.安全性
        2.執行數度比串列快 (因資料結構比較簡單(無法更改),所以執行速度比較快)

  .應用:串列與數組互相轉換
    轉換方式:
        數組轉換為串列 -> tuple1 = (1,2,3)
                        list1 = list(tuple1)
        串列轉換為數組 -> list2 = [4,5,6]
                        tuple2 = tuple(list2)
                        
=>字典(詞典):dict
  .建立:
      字典名稱 = {元素1,元素2,.....}
                 ^建值1:值1
                  key1:value
      字典名稱 = dict ([[key1,value1],[key2,value2],......])    
      
      字典名稱 = dict (key1=value1,key2=value2,......)
                      ^有限制: key值不可為數值
  .字典元素無一定的順序排列 
    (串列元素則為依序排列) --- 在記憶體中...
  .字典取值的方式: 字典名稱[key] 
    以key作為索引取得 value
      ^必須唯一       ^可重複
      ^若重複,則將key覆蓋,只有最後的key會存在
  .當key不存在,會產生錯誤
  .使用 get() 取得值 => 就算key不在也不會產生錯誤(若無key值,則得到None)
    格式: 字典名稱.get(key)
    列如:
        fruit = {'蘋果':15,'香蕉':10,'番茄':12}
        print(fruit.get('蘋果'))
        print(fruit.get('鳳梨'))
  .字典修改:
      字典名稱[key] = value
  .字典刪除:
      刪除特定元素: del 字典名稱[key]
      刪除所有元素: 字典名稱.clear()
      刪除字典: del 字典名稱
"""
#列如:
dict1 = {'A':'內向穩重','B':'外向樂觀','O':'堅強自信','AB':'聰明自然'}
name = input('輸入要查詢的血型:')
blood = dict1.get(name.upper())
if blood == None:
    print('沒有' + name.upper() + '血型!')
else:
    print(name.upper() + '血型個性為 :' + str(dict1[name.upper()]))



#自我練習:
bloe = {'A':'A型血液','B':'B型血液','AB':'AB型血液','O':'O型血液'}
bl = input('請輸入你的血型:')
if bl.upper() == 'A' :
    print('你的血型 %s' % bloe.get('A'))
elif bl.upper() == 'B' :
    print('你的血型 %s' % bloe.get('B'))
elif bl.upper() == 'AB' :
    print('你的血型 %s' % bloe.get('AB'))
elif bl.upper() == 'O' :
    print('你的血型 %s' % bloe.get('O'))
else:
    print('無此血型')
    
#列如:
    請輸入學生姓名:
    李大年的成績為:
    (學生已存在於字典中)    
    請輸入學生成績:
    輸入學生分數:
    印出字典內容...
    (如學生不在字典中,則輸入分數後加入字典)

dict1 = {'林美麗':85,'王大同':93,'李大年':67,}
name = input('請輸入學生姓名:')
if name in dict1:
    print(name + '的成績為' + str(dict1[name]))
else:
    score = input("輸入學生分數: ")
    dict1[name] = score
    print("字典內容: " + str(dict1))
    
#===================================================== 
"""
字串(srt)
=>Python 並無特別區分字元及字串,均以單,雙引號前後括住

=>建立空字串:
    s1 = str()
    s2 = ''
    
=>建立字串:
    s3 = str('這是Python程式設計')
    s4 = 'Today is rainy day'
    
=>len(字串名):字串長度(字元數)

=>max(字串名):字串最大值

=>min(字串名):字串最小值
    len(s4)
    max(s4)
    min(s4)
    
=>[位置數值] 可以取得字串的特定字元
  格式: 字串名[位置數值]  -> 位置數值從0開始算
    s4[3]
    s4[-5]  ->若為負值,則加上字串長度 # -5+18 =13 從0開始算
    
=>[起始值:終止值]
  取得從起始值~終止值-1的子字串
  格式: 字串名[起始值:終止值]
  s4[3:8]
  
=> + :串接
=> * :複製
  s5 = 'Simon'
  s6 = 'Lee'
  s5 + s6
  s5 * 2

=>字串測試: 字串名.函式()
  函式():傳回值為布林值 (True , False)
    .isalnum():字串是否為字元及數值
        s5.isalnum()
    
    .isalpha():字串是否為字元
        s5.isalpha()
    
    .isdigit():字串是否為數值
        s5.isdigit()
    
    .islower():字串是否皆為英文小寫
        s5.islower()
    
    .isupper():字串是否皆為英文大寫
        s5.isupper()
    
    .isspace():字串是否皆為空白字元
        s5.isspace()
        
=>子字串: 字串名.函式('子字串')
    .endswith('子字串'):字串尾端是否為子字串 -> 傳回值為布林值 (True , False)
   
    .startswith('子字串'):字串開頭是否為子字串 -> 傳回值為布林值 (True , False)
        s5.endswith('on')
        s5.startswith('Si')
   
    .find('子字串'): 字串中子字串的最小位置數值
        s5.find('o')    

    .rfind('子字串'): 字串中子字串的最大位置數值 (相同值取最後位置)
        s7='abcdeabcde'
        s7.rfind('e')
    
    .count('子字串'): 字串中子字串的個數
        s7.count('e')
  
=>字串轉換:
  .capitalize():將字串中第一個字元轉換為大寫,其餘為小寫
    字串名.capiyalize()

  .lower():將字串中所有字元轉換為小寫
    字串名.lower()
    
  .upper():將字串中所有字元轉換為大寫
    字串名.upper()
  
  .swapcase():將字串中的字元,大寫轉小寫,小寫轉大寫
    字串名.swapcase()
    
  .replace(str1,str2):將 str1 以 str2 取代  -> 常用會考
    字串名.replace(str1,str2) 

  .title():將字串中每一個單字第一個字元,轉為大寫,其餘為小寫
    字串名.title()
      s8 = 'welcome to taipei'
      s8.capitalize()
      s8.lower()
      s8.upper()
      s8.swapcase()
      s8.replace('taipei','taina')
      s8.title()
      s8

=>空白處理:字串名.函式()
  .lstrip():刪除字串左側空白
  .rstrip():刪除字串右側空白
  .strip():刪除字串左,右側空白
    s9 = '    welcome to taipei    '
    s9.lstrip()
    s9.rstrip()
    s9.strip()
    
=>對齊:
  .center(寬度值):
    將字串以寬度值置中對齊
    
  .ljust(寬度值):
    將字串以寬度值靠左對齊
    
  .rjust(寬度值):
    將字串以寬度值靠右對齊
      
    s10 = 'Taipei City'
    s10.center(20)
    s10.ljust(20)
    s10.rjust(20)
      
=>split():字串分割
  s11 = 'apple banana kiwi orange'   
  lst = s11.split() -> 預設以空白字元做分割字元
  lst
  s12 = '05-22-2020'
  lst1 = s12.split('-') -> 指定 - (減號)為分割字元
  lst1
  
  s12.replace('-','*')
"""
#===================================================== 
#練習題
"""
讓使用者輸入10個數字(不重複)至串列,並將該串列
傳遞給名為compute()的函式,此函式接收一個串列
lst和一個數字a(預設3),並回傳lst中a個最大的
數字。最後再將回傳結果輸出
"""
#練習一
print('請輸入一個大小為10的串列 :')
lst = []
def compute(lst):
    for i in range(10):
        j = eval(input('請輸入第 %d 個數值:' % (i+1)))
        lst.append(j)傳回值 到 main() 呼叫的 compute(lst)
compute(lst)
print('lst串列:',lst) 
lst.sort()
print('lst串列前三大的值為: %d , %d , %d ' % (lst[9],lst[8],lst[7]))

#解答
def compute(lst,a = 3):
    lst.sort()
    ans = []
    for i in range(-1, -1*a-1, -1):  #
        ans.append(lst[i])
    return ans  # -> 回傳至main()函數 呼叫 computer(lst)的位置

def main():
    lst = []
    for i in range(10):
        num = eval(input('請輸入數值:'))
        lst.append(num)
    print(lst)
    print(compute(lst))

main()




#===================
#研究中----未完成
print('請輸入一個大小為10的串列 :')
lst = []
a = 3
def compute(lst):
    for z in range(3):
        lst.append([])
        for i in range(10):
            j = eval(input('請輸入第 %d 個串列的第 %d 個數值:' % ((z+1),(i+1)))
            z.append(j)
compute(lst)
print('lst串列:',lst) 
lst.sort()
print('aList串列最大值為: %d ,最小值為 %d' % (aList[4],aList[0])) 
    
    

rows = eval(input('請輸入二維串列的 欄 數:'))
colums = eval(input('請輸入二維串列的 列 數:'))
lst = []
for i in range(rows):
    lst.append([])  #將lst 建為二維串列
    for j in range(colums):
        lst[i].append(random.randint(1, 50))
print(lst)
print()
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print('lst[%d][%d] = %5d' % (i, j, lst[i][j]))
print()   
 
#===================
#練習二  
"""
撰寫一程式,以lotto()函式產生大樂透號碼,並以
main()函式呼叫5次lotto()函式,及產生五組大樂透
號碼。請將大樂透號碼由小至大排序。
""" 
#研究中----未完成
import random
lotto = []
n = 0

def locof():
    while n <=6:
        randNum = random.randint(1, 49)
        if randNum not in lotto: 
            lotto.append(randNum)
            n += 1
        print("樂透號碼是 : \n" , end = '')
        for i in lotto:
            print("%4d" % i , end = ' ')
            lotto.sort()
        
locof()

for i in locof():
    i += 1

print("號碼排序後 : ")
for i in lotto:
    print("%4d" % i , end = ' ') 


#解答
import random
def lotto():
    lottoLst = []
    count = 0
    while count < 6:
        lottoNum = random.randint(1, 49) 
        if lottoNum not in lottoLst: #不在lottoLst裡的話往下,有了就不往下走count就不+1,重來(避免重複)
            lottoLst.append(lottoNum)
            count += 1 
    lottoLst.sort()
    print(lottoLst)
    
def main():
    for i in range(1, 6): # 呼叫 lotto() 跑5次
        lotto()

main()

#===================     
#練習三
"""
撰寫一個程式,以隨機亂數的方式產生100個介於
1~1000的亂數,將他置放於 randLst串列中,然後印
出第二小的數和第二大的數。(可重複)
"""  
import random
def stcof():
    randLst = []
    for i in range(100):
        num = random.randint(1, 1000) 
        randLst.append(num)
        randLst.sort()
        
    print('randLst串列(排序過) = %s' % randLst)
    print('第二小的數為 : %d ,第二大的數為 : %d' % (randLst[1],randLst[98]))

stcof()  


#解答
import random
randLst = []
for i in range(100):
    randNum = random.randint(1,1000)
    randLst.append(randNum)

randLst.sort()
for j in range(1,101): #輸出成矩陣
    if j % 10 == 0: # 除以10取於數 等於0 表示 10 個 一行
        print('%4d ' % (randLst[j-1]))
    else:
        print('4%d ' % (randLst[j-1]), end = '')

print()
print(randLst[1])
print(randLst[len(randLst)-2])
#===================
"""
輸入方式研究
要一次性輸入多筆資料 用空格來分隔
"""
a,b=map(int,input('請輸入數值:').split())
#===================
#練習四
"""
撰寫一個程式,以隨機亂數的方式產生100個介於
1~1000的亂數,將他置放於 randLst串列中,然後印
出第二小的數和第二大的數。(不可重複)
"""  
import random
def stcof():
    randLst = []
    count = 0
    while count < 100:
        num = random.randint(1, 1000) 
        if num not in randLst:
            randLst.append(num)
            count += 1
    randLst.sort()
    print('randLst串列(排序過) = %s' % randLst)
    print('第二小的數為 : %d ,第二大的數為 : %d' % (randLst[1],randLst[98]))
    print(len(randLst))
stcof()  

#解答
import random
randLst = []
count = 1
while count <= 100:
    randNum = random.randint(1, 1000) 
    if randNum not in randLst:
        randLst.append(randNum)
        count += 1
        
randLst.sort()
for j in range(1,101):
    if j % 10 == 0:
        print('%4d' % (randLst[j-1]))
    else:
        print('%4d' % (randLst[j-1]), end = '')
        
print()
print(randLst[1])
print(randLst[len(randLst) - 2])

#===============================================
#20200525
"""
檔案存取及例外處理
=>檔案運作的流程
  .使用open函式開啟檔案及設定模式
  .使用寫入函式寫入檔案或讀取函式讀取檔案
  .使用close函式關閉檔案

=>開啟檔案
  .open函式
  .格式:
      open(開啟的檔案,開啟模式)
  .開啟的檔案:檔案的"路徑"及檔案"全名"
  .開啟模式: w -> 寫入
            r -> 讀取
            a -> 附加
   例如:
    w(寫入) -> 檔案指標 指向檔案開頭,並清除掉原檔案的內容, 
              若檔案不存在,則建立新檔案
    a(附加) -> 檔案指標 指向檔案結尾,寫入資料附加在原檔案後方,
              若檔案不存在,則建立新檔案
    r(讀取) -> 檔案指標 指向檔案開頭,若檔案不存在,則發生錯誤
    
    #若檔案存取的是二進位檔案,則將開啟模式參數後加 小寫 b,
     (rb, wb , ab)

=>讀取及寫入:
  .寫入 -> write (寫入的資料)
  .讀取 -> read() -> 讀取所有內容
        -> readlines() -> 讀取所有內容
        -> readline() -> 讀取一行內容
        -> read(n) -> 讀取n個字元(指定要讀幾個字)

=>讀寫及開啟檔案的路徑:
  .檔案路徑若未指定,則以當時執行的系統預設路徑作為存取依據
    (未給路徑,只給檔名)
  .自訂路徑,程式碼撰寫時路徑分隔符號以 \\ 為主     

"""
#列如:
def main():
    outfile = open('C:\\GitHub\\python\\PY-Learn\\fruits.txt', 'w')
    #開啟檔案fruit.txt 不存在,則建立新檔
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange\n')
    outfile.write('蘋果\n')
    outfile.write('芒果\n')
    outfile.close()

main()


#例如
infile = open('C:\\GitHub\\python\\PY-Learn\\fruits.txt', 'r')
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()

print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))

print()
print(line1)
print(line2)
print(line3)
print(line4)
infile.close()

"""
=>repr函式:印出轉義(逸脫)字元
  .即字串資料若包含轉義字元(如\n)則不執行轉義字元的功能,
   直接將其印出
  .w, r, a參數後可加入 " + " 符號,即 w+, r+, a+ -> 以讀寫模式開啟檔案
  .seek函式:移動指標
    格式: seek(offset,where)
      offset -> 移動byte數
      where -> 從哪裡開始移位
               0:檔頭
               1:目前位置
               2:檔尾
     #Python 結束執行 write 後 檔案指標式指定在 檔尾 !
               
"""

infile = open('C:\\GitHub\\python\\PY-Learn\\fruits.txt', 'r')
line1 = infile.read()
print('使用read() 方法:')
print(repr(line1))
infile.close()

#例如
infile = open('C:\\GitHub\\python\\PY-Learn\\fruits.txt', 'r')
print('\n使用 readlines() 方法:')
line1 = infile.readlines()
print(line1)
infile.close()

#例如
def main():
    infile = open('c:\\GitHub\\python\\PY-Learn\\fruits.txt','r')
    print('使用read(3) 方法:') #只讀3個字元
    line1 = infile.read(3)
    print(repr(line1))
    
    print('使用 read(8) 方法:')
    line2 = infile.read(8) #只讀8個字元
    print(repr(line2))
    infile.close()
    
main()

#以迴圈讀取所有內容
def main():
    infile = open('c:\\GitHub\\python\\PY-Learn\\fruits.txt','r')
    line = infile.readline()
    while line != '':  #代表有讀到資料, '' 等於空字串!
        print(line)
        line = infile.readline()
    infile.close()

main()

#練習讀寫複製內容到另一新檔
def main():
    infile = open('c:\\GitHub\\python\\PY-Learn\\fruits.txt','r')
    line = infile.readline()
    outfile = open('c:\\GitHub\\python\\PY-Learn\\taaat.txt','w')
    while line != '':  #代表有獨到資料, '' 等於空字串!
        outfile.write(line)
        line = infile.readline()
    infile.close()
    outfile.close()

main()

#例如
def main():
    outfile = open('c:\\GitHub\\python\\PY-Learn\\cities.txt', 'w')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.close()
    
    infile = open('c:\\GitHub\\python\\PY-Learn\\cities.txt', 'r')
    data = infile.read()
    print(data)
    infile.close()

main()

#例如
def main():
    outfile = open('c:\\GitHub\\python\\PY-Learn\\cities.txt', 'w+')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.seek(0, 0)
    data = outfile.read()
    print(data)
    outfile.close()

main()
    
"""
=>二進位檔案存取
  .載入 pickle模組: import pickle
  .使用dump函式寫入二進位資料
  .使用load函式讀取資料
    #數值以二進位模式操作可加快其效率
  格式: pickle.dump (寫入的資料,寫入的檔案)
       pickle.load (讀取的檔案)
"""
#例如
import pickle
def main():
    outbinfile = open('c:\\GitHub\\python\\PY-Learn\\binaryFile.dat','wb')
    pickle.dump(123, outbinfile)
    pickle.dump(77.7, outbinfile)
    pickle.dump('Python is good programming', outbinfile)
    pickle.dump([11, 22, 33], outbinfile)
    pickle.dump('蘋果', outbinfile)
    outbinfile.close()
    
    inbinfile = open('c:\\GitHub\\python\\PY-Learn\\binaryFile.dat','rb')
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    inbinfile.close()
main()

#例如
import pickle
def main():
    outfile = open('c:\\GitHub\\python\\PY-Learn\\score.txt', 'wb')
    data = eval(input('請輸入整數,輸入 0 結束輸入:'))
    while data != 0:
        pickle.dump(data, outfile)
        data = eval(input('請輸入整數,輸入 0 結束輸入:'))
    outfile.close()
    
    infile = open('c:\\GitHub\\python\\PY-Learn\\score.txt', 'rb')
    end_of_file = False # -> 下方變 True 就結束迴圈
    while not end_of_file:
        try:  #異常處理機制
            print(pickle.load(infile), end = ' ')
        except EOFError: # EOFError : End of File Error
            end_of_file = True # -> 檔案結尾後 結束迴圈
    infile.close()
    print('\n所有資料已讀取')
main()

#=================================================
"""
for: 定數迴圈(執行次數固定)
while:不定數迴圈(執行次數不固定)
"""

"""
=>例外(異常)處理
當程式出現異常運作時的處理機制
  try:
      程式執行主體
  except 異常型態(錯誤類型):  #當執行有錯時,執行下面處理方式
      處理方式

=>多例外(多異常)處理

  try:
      程式執行主體
  except 異常型態 1:
      處理方式 1
  except 異常型態 2:
      處理方式 2
      ...
      ...
      ...
  except 異常型態 n:
      處理方式 n
  except:                #當以上異常都未發生時執行
      處理方式 n+1
  else:                  #當沒有異常發生時執行
      處理方式 n+2
      
  finally:               #最後一定會執行
      處理方式 n+3    
      

"""
#例如
def main():
    try:
        n1, n2 = eval(input('請輸入兩個數值,已逗號分隔:'))
        ans = n1 / n2
        print('%d / %d = %d' % (n1, n2, ans))
    except ZeroDivisionError: 
        print('除法分母不可以為 0 !')
    except SyntaxError:  #符號錯誤
        print('輸入資料必須以逗號分隔 !')
    except :
        print('輸入時發生錯誤 !')
    else:
        print('沒有異常錯誤 !')
    finally:
        print('finally 子句被執行')

main()

#=====================
#練習1
試撰寫一程式,以不定數迴圈輸入學生姓名,
微積分與會計成績。當輸入學生姓名為none時,
則結束輸入動作,並將上述的輸入資料
寫入名為students.dat的檔案中

outfile = open('c:\\GitHub\\python\\PY-Learn\\student.dat', 'w')
while True: # True 永遠成立
    name = input('請輸入學生姓名 : ')
    n1 = input('請輸入微積分成績 : ')
    n2 = input('請輸入會計成績 : ')
    if name == 'none': #配合 name == 'none' 來離開迴圈
        break   #離開迴圈,不往下走
    else:
        outfile.write(name)
        outfile.write(' ')
        outfile.write(n1)
        outfile.write(' ')
        outfile.write(n2)
        outfile.write(' ')
        outfile.write('\n')
       
outfile.close()

#=====================
#練習2
承上提,將 students.dat 讀取出來

infile = open('c:\\GitHub\\python\\PY-Learn\\students.dat', 'r')
line = infile.readline()
while line != '':  #代表有讀到資料, '' 等於空字串!
    print(line)
    line = infile.readline()
infile.close()

#=====================
#練習3
承上提,將 students.dat 讀取出來,並計算每位學生的平均成績,
微積分的比重是60%,會計的比重是40%

infile = open('c:\\GitHub\\python\\PY-Learn\\students.dat', 'r')
line = infile.readline()
while line != '':  #代表有讀到資料, '' 等於空字串!
    srt = line.split(' ')
    n1 = eval(srt[1])
    n2 = eval(srt[2])
    avg = n1 * 0.6 + n2 * 0.4
    print ('|%10s: %.2f|' % (srt[0], avg,))
    line = infile.readline()
infile.close()

#解析
1.讀取檔案
2.只要有讀到資料,將微積分即會計成績取出 -> 串列
3.將取出的資料計算
4.輸出格式

#=====================
#練習4
承上提,將 students.dat 讀取出來,並顯示哪位學生為積分分數最高

infile = open('c:\\GitHub\\python\\PY-Learn\\students.dat', 'r')
max = -1
line = infile.readline()
while line != '':  #代表有讀到資料, '' 等於空字串!
    srt = line.split(' ')
    n1 = eval(srt[1])
    if n1 > max:
        max = n1
        name = srt[0]
    line = infile.readline()
print ('微積分成績最高者是 \n %10s: %3d' % (name, max))
infile.close()

#解析
max 變數,設定一初始值 (參考) max =-1
讀入微積分成績 <-> max
              ^比大小
若微積分成績 > max 則將 微積分成績得值設定給max

讀入下一個微積分成績 比較

#=====================
#練習5
承上提,將 students.dat 讀取出來,並顯示哪位學生會計分數最低

infile = open('c:\\GitHub\\python\\PY-Learn\\students.dat', 'r')
min = 101
line = infile.readline()
while line != '':  #代表有讀到資料, '' 等於空字串!
    srt = line.split(' ')
    n2 = eval(srt[2])
    if n2 < min:
        min = n2
        name = srt[0]
    line = infile.readline()
print ('會計成績最高者是 \n %10s: %3d' % (name, min))
infile.close()

#解析
max 變數,設定一初始值 (參考) min = 101
讀入微積分成績 <-> min
              ^比大小
若微積分成績 < min 則將 微積分成績得值設定給max

讀入下一個微積分成績 比較

#=====================
#練習6 -- X
試撰寫一程式,以不定數迴圈要求,使用者輸入字串,
檢視若字串是以B(大寫)字元開頭,則將此字串加入到lst串列中
最後將其印出,當使用者輸入end時將結束輸入的動作,

lst = []
srt = input('請輸入一個字串,輸入 end 時,結束輸入:')
while srt != 'end':
    while srt.startswith('B'):
        i = lst.append(srt)
        srt = input('請輸入一個字串,輸入 end 時,結束輸入:')
    else:
        srt = input('請輸入一個字串,輸入 end 時,結束輸入:')
print(lst)
    
#解答
lst = []
while True:
    str = input('請輸入字串:')
    if str != 'end':
        if str.startswith('B'):
            lst.append(str)
    else:
        break
print(lst)
        
 
#=====================
#練習7 -- X
試撰寫一程式,輸入一個名為str的字串與欲尋找的字串,
將找到的字串以[Bright]字串取代之,若沒有找到欲尋找的字串,
則印出 [is not found]訊息.
如:
請輸入字串 I have an appointment with Amy
請輸入欲找尋的字串: Amy

輸出 : I have an appointment with Bright


srt = input('請輸入字串 :')
f = input('請輸入欲找尋的字串 :')
if srt.find(f) != -1:
    i = srt.replace(f,'Bright')
    print('輸出 : %s' % srt)
else:
    print(f + 'is not found')

#解答
str = input('請輸入字串 :')
fstr = input('請輸入欲找尋的字串 :')
if srt.find(fstr) != -1:
    endStr = str.replace(fstr, 'Bright')
    print(endStr)
else:
    Print(fstr + 'is not found')

#=======================================================    
#作業  
#01
以 while 迴圈撰寫九九乘法表。


#02
請撰寫一程式，
讓使用者輸入一個正整數(<100)，
然後以三角形的方式依序輸出此數的階乘結果。
提示：輸出欄寬為 4，且須靠左對齊。

輸入與輸出範例：
輸入：
    5
輸出：
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5


#03
請撰寫一程式，
讓使用者輸入兩個正整數 a、b (a<b)，
利用迴圈計算從 a 開始的偶數連加到 b 的總和。
例如：輸入 a = 1、b = 100，則輸出結果為 2550。

輸入與輸出範例：
輸入：
    1 
    100
輸出：
    total = 2550


#04
請撰寫一程式，
讓使用者輸入一個正整數(<100)，
印出以下的左上三角形。
提示：輸出欄寬為 4，且須靠左對齊。

輸入與輸出範例：
輸入：
    請輸入數值：6
輸出：
    1 2 3 4 5 6
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1


#05
請撰寫一程式，
由使用者輸入一數字，
然後印出 1 到此數字的階乘。

輸入與輸出範例：
輸入：
    10
輸出：
    # 1! = 1
    # 2! = 2
    # 3! = 6
    # 4! = 24
    # 5! = 120
    # 6! = 720
    # 7! = 5040
    # 8! = 40320
    # 9! = 362880
    # 10! = 3628800

#=======================================================   
"""
=>彙總

print:
輸出單一項目,如變數,字串(元)...等
多個項目以逗點隔開 (不須設定格式)
輸出資料如需設定格式,則以 ('格式字串1 格式字串2.....' % (資料1,資料2...))
設定之。                   ^對齊,位數(總位數,小數),以%符號開頭
資料採對應方式,即資料對應到格式字串1,格式字串個數 = 資料個數

如: print('%d / %d = %d' % (6, 2, 3))

"""