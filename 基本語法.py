# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:57:21 2020

@author: Jackie
"""
#===========================================================

#20200506 - 第一個測試

a=1
b=100
print("sum=",a+b)
print("Hello World")


#===========================================================

#輸入2個數字,求最大公因數
num1 = int(input('請輸入第一個數值:')) #num1=變數 int=資料型態(整數) input=
num2 = int(input('請輸入第二個數值:'))
if num1 < num2: #if=條件式 
    tmp_num = num1
    num1 = num2
    num2 = tmp_num
while num2 != 0 : #while=迴圈 (如果上面條件成立才執行)  != (不等於)
    tmp_num = num1 % num2
    num1 = num2
    num2 = tmp_num
print('最大公因數',num1) #print=輸出 (格式字串 % 資料)


#===========================================================
"""
Python程式檔格式: *.py
jupyter程式檔格式: *.ipynb
Jupyter檔案放置於本機端 使用者下 (C:\Users\Jackie\.ipynb_checkpoints)
"""
#===========================================================
"""
=>程式需區分英文大小寫
=>程式分行:  
 \ 
 +
"""
#列如：用　\ 分行
a = b = c = 12
y = a + \
    b + \
    c + \
    20
print("Total =", \
      y)
    
#列如：用　+ 分行
a = b = c = 12
y =(a + 
    b + 
    c + 
    20)
print("Total =", +
      y)    
    
y = a + b + c + 20
print("Total =",y)

"""
=>程式敘述以單行為主(一個完整的敘述語法)
  若要在單行撰寫2個以上的完整語法，
  其間以 ; 隔開每一個完整的敘述。
"""
#列如：多行多完整語法
a = 10
b = 20
print(a+b)

#列如：單行多完整語法
a = 10; b = 20 
print(a+b)

#===========================================================
"""
=>變數
  .在程式當中儲存資料供程式使用
  .隨程式執行而變動其值
  .命名規則:
      1.第一個字元可以是英文大小寫,底線符號(_),中文(不建議)
      2.其他字元可以是英文大小寫,底線符號(_),數字,中文(不建議)
      3.英文大小寫視為不同的變數名稱
      4.不可以使用Python內建的關鍵字,內建函式,內建類別名稱
      5.建議:儘量以該變數在程式中代表的功能,意義來命名，如 age 代表年齡
      例如: Class (錯誤，此為內建類別名稱)
            num@123 (錯誤，@是符號)
            7elevn (錯誤，第一個字不可以是數字)
            !name (錯誤，第一個字不可以是符號，_ 可以)
            my name (錯誤，中間不可以空格，空格是符號)
  .直接寫出使用，不須特別宣告
  .不須宣告其資料型態，系統會根據變數值自行設定
"""
#列如：
a,b,c = 10,6.8,"python"
print(a,b,c)
#===========================================================
"""
=>資料型別:
  .Python採動態型別(無需事先宣告)
  .另有強制型別宣告
  .型別:
      int (整數)
      float (浮點數)
      bool (布林值) -> true , false
      str (字串) -> 以單雙引號前後接住 列如: 'x' , "abc"
  .相同型別的資料方可運算
  .Python具備自動轉換型別的功能，若無法自動轉換，則採強制行別宣告:(使用下列函數)
      int(資料)
      float(資料)
      str(資料)
  .type(資料):查詢資料型態
"""
#列如：
  x = 10
  y = x /3
  print(x)
  print(type(x))
  print(y)
  print(type(y))

#列如：
  x = x + 5.5
  print(x)
  print(type(x))
  
"""  
  .int:
      預設為10進位
      另有:
          二進位:數值前加上 0b (數字0+英文b)
             轉換函數 bin(資料)
          八進位:數值前加上 0o (數字0+英文o)
            轉換函數 oct(資料)
          十六進位:數值前加上 0x (數字0+英文x)
            轉換函數 hex(資料)
"""
#列如：二進位轉換
x = 0b01000001
print(x) #65
y = 65
print(bin(y)) #01000001

#列如：八進位轉換
x = 0o101
print(x) #65
y = 65
print(oct(y)) #101

#列如：十六進位轉換
x = 0x41
print(x) #65
y = 65
print(hex(y)) #41

#列如：十六進位轉換
print(hex(255)) #ff
print(oct(255)) #377
print(bin(255)) #11111111

#建議背起來 2-15次方=32,768  2-16次方=65,536  2-24次方=16,777,216
#===========================================================

#20200508
"""
運算式
=>由運算元(進行運算的資料)及運算子(執行運算的動作)組成 
 
   a+B  a,b(運算元)  +(運算子)
  
=>運算子:
  .單一運算子 (運算元只有一個)
    -100 not a  a(運算元)
  .二元運算子
    運算元有兩個 (運算子放在二運算元之間)
    a+b  , 100+50 
  
函式:function
=>內建函式
  將特定功能予以包裝並以參數(若有的話)帶入資料運算,執行
  Python已定義完成，直接依功能使用
 
  函式格式:函式名稱(參數.....) 
                  ^帶入函式執行的資料
                  
  .input():供使用者輸入資料之用
    格式: 變數 = input([提示字串])
                         ^顯示訊息告知如何輸入
         輸入時按下Enter即表示輸入完畢，並將輸入資料存到變數中
"""
#列如：
score = input("請輸入國文成績:")
print(score)

#===========================================================
"""       
  .eval():將字串(數值型字串)轉換成數值
    格式: eval(資料)           
"""
#列如：
score = eval(input("請輸入國文成績:"))
sum = score + 20
print(sum)  

#===========================================================
"""       
  .print():輸出(格式化)
    格式: print(資料1,y資料2,...,sep=分隔字元,end=結束字元) 
                                ^預設為空白  ^輸出最後需要加入的字元，預設為換行(\n)         
                                
    換行符號: \n
    已字串型式寫出 = "\n"
    
         print(格式參數1 格式參數2 .... % 資料1 資料2 ....)
                                         ^可用()前後括住
                                       ->(資料1 資料2 ....)
                ^格式參數 -> %s (字串) 
                            %d (整數)
                            %f (浮點數)      
     
        PS: 格式參數1 會帶 資料1 , 格式參數2 會帶 資料2 , .......
  
   格式參數:
   %5s : 輸出5個字元 
        (小於5個字元,於左方填入空白)        
        (大於5個字元,則全數輸出)  
   %5d : 輸出5位整數 
        (小於5位整數,於左方填入空白)        
        (大於5位整數,則全數輸出)  
   %8.2f : 輸出8位數字(含小數點)
           小數2位
           若整數位小於5位(8-3),則在數字左方填入空白
           若小數小於2位,則在右方填入0
   + : 於格式數值前方加入
       若數值為正,則在資料左方加上 "+"
   - : 輸出格式資料空間有多餘時,則資料靠左對齊
"""
#列如：
score = eval(input("請輸入國文成績:"))
sum = score + 20
print(score,sum)  

#列如：
print("\n")  # = print()
print("多學程式設計,活絡思考")
print(100,"Python",200)
print(100,"Python",200,sep="&")

#列如：
a=100
print("x=/%-6d/" % a)
b=12.3
print("b=/%-7.2f/" % b)
c="deep"
print("c=/%-6s/" % c)
d=50
print("d=/%+6d/" % d)
e=13.3
print("e=/%+6.2f/" % e)

#練習：
請輸入國文成績：80
請輸入英文成績：70
請輸入數學成績：60
總成績：210 ，平均成績：70.00

num1 = int(input("請輸入國文成績:")) 
num2 = int(input("請輸入英文成績:"))
num3 = int(input("請輸入數學成績:"))
sum = num1 + num2 + num3
avg = (sum/3)               
print("總成績:%d" % sum,",","平均成績:%3.2f" % avg)

#老師解答：
chi = input("請輸入國文成績:")
math = input("請輸入英文成績:")
eng = input("請輸入數學成績:")
sum = int(chi) + int(math) + int(eng)
avg = sum / 3              
print("總成績:%d,平均成績:%5.2f" % (sum,avg))

#===========================================================
"""
流程控制
=>以特定結構控制的執行方式
=>條件式:
    .必須以縮排進行程式結構化
      條件式下的敘述式一定要往右縮排
                          ^會自動,可以按tab鍵(沒必要不要按)
      Python利用程式的縮排來認識程式的結構
      1.if:
        =>if 條件式: #條件式的結果為 布林值(true,false)
             敘述式
             ...
             ...
             ...
             
         (若條件成立,則執行敘述式)
    
    abs(X):計算x之絕對值
    abs = 求絕對值之函數
"""
#列如：
print()
num = eval(input("請輸入整數值:"))
if (int(num) < 0):
    num = abs(num)
print("絕對值是 %d" % num)

#===========================================================
"""
      2.if~else:
        =>if 條件式: #條件式的結果為 布林值(true,false)
             敘述式1
         else:
             敘述式2
             
         (若條件成立,則執行敘述式1,否則執行敘述式2)
"""
#列如：
print()
num = eval(input("請輸入任意整數值: ")) #eval = 轉成數值
rem = num % 2  # % => 除後得餘數
if (rem == 0): # == => 等於
    print("%d 是偶數" % num)
else:
    print("%d 是奇數" % num)

#練習：
    輸入圓半徑,計算圓面積
    輸出如下:
    圓半徑=    ,圓面積=
    若輸出的半徑值為負數,
    則輸出:圓半徑不能為負數

print()
num = eval(input("輸入圓半徑,計算圓面積: ")) 
a = (num * num * 3.14) 
if (num > 0): 
    print("圓半徑=", num ,",圓面積=",a)
else:
    print("圓半徑不能為負數")
    
#老師解答：  
PI = 3.14159
radius = eval(input("輸入圓半徑:"))
area = PI * radius * radius
if radius < 0:
    print("圓半徑不能是負數")
else:
    print("圓半徑=",radius, "圓面積=",area)
    
#===========================================================
"""
      3.if~elif:
        =>if 條件式1: #條件式的結果為 布林值(true,false)
             敘述式1
         elif 條件式2:
             敘述式2
             ...
             ...
             ...
         elif 條件式n:
             敘述式n
         else:
             敘述式n+1
             
        (逐一判斷條件,若成立,則執行該敘述試後離開if,
         當所有條件都不成立,則執行敘述n+1)
"""
#列如：
a , b , c = eval(input("請輸入 a,b,c 的值"))
d = b*b -4*a*c
if d > 0:
    print("一元二次方程式有兩個不同的解")
elif d == 0:
    print("一元二次方程式只有一個解")
else:
    print("一元二次方程式無解")
print("結束")

#列如：
    90分以上->優等
    80分以上->甲等
    70分以上->乙等
    60分以上->丙等
    其餘 ---->不及格
    
score = eval(input("請輸入考試成績 (0~100):"))
if score >= 90:
    print("分數評等為:優等")
elif score >= 80:
    print("分數評等為:甲等")
elif score >= 70:
    print("分數評等為:乙等")
elif score >= 60:
    print("分數評等為:丙等")
else:
    print("不及格!")

#列如：
    輸入      輸出
     1        one
     2        two
     3        three
     4        four
     5        five
     ~        輸入超出範圍
   
num = eval(input("請輸入 1~5 的整數:"))
if num == 1:
    print("ONE")
elif num == 2:
    print("TWO")
elif num == 3:
    print("THREE")
elif num == 4:
    print("FOUR")
elif num == 5:
    print("FIVE")
else:
    print("您輸入的資料超出範圍!")
    
#===========================================================
"""
      4.巢狀if:  #可套用到任何if條件式
        =>if 條件式1: #條件式的結果為 布林值(true,false)
             ...
             if 條件式2:  # if本身為條件式，同時也為上層if的敘述式
                ...
                if 條件式3:  # if本身為條件式，同時也為上層if的敘述式           
                    
"""  
#列如：
score = eval(input("請輸入考試成績 (0~100):"))
if score >= 90:
    print("分數評等為:優等")
else:
    if score >= 80:
       print("分數評等為:甲等")
    else:
        if score >= 70:
           print("分數評等為:乙等")
        else:
            if score >= 60:
               print("分數評等為:丙等")
            else:
                print("不及格!")      
                
#列如：                
num = eval(input("請輸入 1~5 的整數:"))
if num == 1:
    print("ONE")
else:
    if num == 2:
       print("TWO")
    else:
        if num == 3:
           print("THREE")
        else:
            if num == 4:
               print("FOUR")
            else:
                if num == 5:
                   print("FIVE")
                else:
                   print("您輸入的資料超出範圍!")                
#===========================================================
"""
=>迴圈:重複執行的敘述
  1.for:
      => for 變數 in iterator : 
         敘述式        ^使用range()函式
         ...             range(起始值,終止值,間隔值)
         ...                    起始值,間隔值->可以不指定
         ..               預設值  ^0     ^1
                                     終止值->迴圈執行時,不包含終止值
                                      (例如 終止值=11 , range 只跑到 10)



"""
#例如：
印出0~10的整數
for i in range(11):
    print(i)
   
#例如：
sum = 0
for i in range(1,101):
   sum = sum + i  # sum+= i
print("sum=",sum)

#例如：
印出1+到100的合
sum = 0
for i in range(1,101):
   sum+= i
else:
    print("sum=",sum)

#例如：
印出1+到輸入的整數的合
n = eval(input("請輸入你要1+到多少的整數:"))
sum = 0
for i in range(1,n+1):
   sum = sum + i  
print("sum=",sum)

#例如：
4+9+13+18+22+....+85+90+94+99

sum = 0
for i in range(4,95,9):
   sum = sum + i  
for i in range(9,100,9):
   sum = sum + i 
print("sum=",sum)

#例如：
4+9+13+18+22+....+85+90+94+99

sum = 0
for i in range(4,95,9):
   sum = sum + i + (i+5)  # (i+5) 是重點 要多想想
print("sum=",sum)

#練習：
請輸入正整數:6
6!=720
階乘: 6!=6x5x4x3x2x1

n = eval(input("請輸入正整數:"))
sum = 1
for i in range(1,n+1):
   sum = sum * i   
print("sum=",sum)

#===========================================================
"""
  2.while:
      => while 條件式:
          敘述式
          ...
          ...
          ...
          (當條件成立,則執行敘述式,然後再回圈)
"""
#例如：
印出0~10的整數
i = 0
while i < 11:
    print(i)
    i = i + 1

印出1+到100的合
sum = 0
i = 1
while i < 101:
    sum = sum + i
    i = i + 1
print (sum)

#例如：
請輸入第0位學生成績(輸入-1結束):
    ...
    ...
    ...
本班總成績:00分,平均00.00分(小數2位)

total = person = score = 0
while (score != -1): # != => 不等於
    person += 1    #第幾位學生 
    total += score 
    score = int(input("請輸入第 %d 位學生的成績(輸入 -1 結束):" % person))
average = total / (person - 1)
print("本班總成績: %d 分，平均成績: %5.2f 分" % (total, average))


#例如：
ans = input("請輸入[電腦]的英文:")
while ans.upper() != "COMPUTER":  # 字串物件.upper() -> 將字串轉換為全部大寫
      ans = input("答錯了，請重新輸入[電腦]英文:")
else:
    print("恭喜!您答對了。")
    
#作業
輸入年齡計算票價。
票價100元:
若<=6歲或>=70歲則打2折。
若7~12歲或是60~69歲則打5折。    


age = int(input("請輸入年齡，計算您的票價:"))
cost = 100
if age <= 6 or age >=70:
     cost = cost * 0.2
     print ("您的票價:%d" % cost)
elif (age >= 7 and age <= 12) or (age >= 60 and age <= 69):
     cost = cost * 0.5
     print ("您的票價:%d" % cost)
else:
    print ("您的票價:%d" % cost)
    
#===========================================================
#20200511
"""  
=>巢狀迴圈:
  .迴圈中的敘述式為另一迴圈結構
  .巢狀層數不限
  .for,while皆可構成巢狀結構
  
""" 
#練習：
九九乘法表

#第一種寫法 
i=1
j=1
for i in range(1,10):
   for j in range(1,10):
       print('%d*%d=%2d' % (i,j,i*j) , '\t' , sep='' , end='') #\t => 4個空白,等於按一個tab鍵
print()

    
#第二種寫法   
for i in range(1,10):
   for j in range(1,10):
       print(i,'*',j,"=",i*j,'\t',sep='',end='')

#拆解迴圈
# 外  條件   內  條件    結果
  i   i<=9  j   j<=9     
  1    V->  1    v->   1*1= 1 tab #tab => 空白4格
            2    v->   1*1= 1    1*2= 2 tab
            3    V->   1*1= 1  1*2= 2  1*3= 3 tab 

#第三種寫法 
for i in range(1,10):
   for j in range(1,10):
       s=i*j
       if s<10:
           s="0"+str(s)
       print(i, '*', j, '=', s, '\t',sep='', end='')
   print()
   
#===========================================================            
 """  
=>中斷迴圈:
  .break : 中斷後直接離開迴圈
  .continue : 中斷後,回到迴圈開頭繼續執行
  
"""            
#例如：
ans = input("請輸入[電腦]的英文:")
while ans.upper() != "COMPUTER":  # 字串物件.upper() -> 將字串轉換為全部大寫
    if ans.upper()== "QUIT":
        print("不玩了!")
        break
    ans = input("答錯了，請重新輸入[電腦]英文:")
else:
    print("恭喜!您答對了。")



#例如：
輸入大樓的樓層數
並列印出樓層數
請排除四樓

n= int(input("請輸入大樓的樓層數:"))
print("本大樓具有的樓層為:")
if(n > 3):
    n += 1
for i in range(1, n+1):
    if(i==4):
        continue
    print(i, end="")
print()

#例如：
輸入層數
以*列印出該層數的直角三角形

n=eval(input("請輸入直角三角形層數:"))
for a in range(1,n+1):
    for b in range(0,a):
        print('*',end='')
    print()

#拆解迴圈
# 外  條件   內  條件       結果
  a   a<=n  b   b<=a-1     
  1    V->  0   0<=1-1     * 
            1   1<=1-1 X 
  2         0   0<=2-1     *  
            1   1<=2-1      *
            2   1<=2-1 X
  3         0   1<=3-1     *
            1   1<=3-1      *
            2   1<=3-1       *
            3   1<=3-1 X      
            
#例如：
輸入層數
以*列印出該層數的倒直角三角形
n=eval(input("請輸入倒直角三角形層數:"))
for a in range(n,-1,-1):
    for b in range(1,a+1):
        print('*',end='')
    print()
    
#拆解迴圈
# 外  條件   內  條件       結果
  a   a<=n  b   b<=a     
  7    V->  1   1<=7+1     * 
            2   2<=7+1      *
            3   3<=7+1       *  
 
    
    
#例如：
輸入三位整數
判斷此三位整數是否為迴文數
PS:迴文數:又稱對稱數 
   將數值正,反向排列 如: 121

n=eval(input('請輸入三位整數:'))
r = (n % 10) * 100 + (n // 10 % 10) * 10 +(n // 100)
if n == r:
    print(n , '為迴文數')
else:
    print(n , '不是迴文數')

#迴圈拆解
n=121 代入    
(121 % 10) * 100 -> 1 * 100 = 100 # % =>除後取餘數
(121 // 10 % 10) * 10 -> 2 * 10 = 20 # // =>除後取整數
(121 // 100) -> 1 * 100 = 1 

#自我練習
輸入五位整數
判斷此五位整數是否為迴文數
PS:迴文數:又稱對稱數 
   將數值正,反向排列 如: 16861

n=eval(input('請輸入五位整數:'))
r = (n % 10) * 10000 + (n // 10 % 10) * 1000 + (n // 100 % 10) * 100 + (n // 1000 % 10) * 10 +(n // 10000)
if n == r:
    print(n , '為迴文數')
else:
    print(n , '不是迴文數')

#迴圈拆解   
a = (16861 % 10) * 10000
b = (16861 // 10 % 10) * 1000
c = (16861 // 100 % 10) * 100
d = (16861 // 1000 % 10) * 10
e = (16861 // 10000) 
print(a,b,c,d,e)


#例如：
輸入三個整數，比較大小

num1, num2, num3 = eval(input("輸入三個整數比較大小:"))
if num1 > num2:
    num1, num2 = num2, num1
    
if num2 > num3:
    num2, num3 = num3 ,num2
    
if num1 > num2:
    num1, num2 = num2, num1
    
print("三個整數大小分別為:", num1, num2, num3)

#===========================================================            
"""  
=>亂數產生器:
    
"""
#例如：
要產生10個,1~100的亂數

import random

for i in range(1,11):
    ramdum = random.randint(1,100)
    print('%4d' % ramdum, end='')

#例如：
要產生10個,1~100的亂數,並分辨幾個奇數幾個偶數

import random
x=0
y=0
for i in range(1,11):
    ramdum = random.randint(1,100)
    print('%4d' % ramdum, end='')
    rem = ramdum % 2 # % => 除後得餘數
    if (rem == 0):   # == => 等於
        x += 1       # 偶數+1
    else:
        y += 1       # 奇數+1
print()
print('偶數有:', x, '奇數有:', y, end='')   
    
#===========================================================            
"""  
函式:
=>定義:
  將一組具有特定程式功能的程式碼,
  以獨立的程式結構,建立為一個單元,並賦予一個名稱
  供後續程式呼叫使用   

=>優點:
  1.重複性:使用時以呼叫名稱方式執行,不需重複撰寫程式碼
  2.精簡:無須重複相同的程式碼
  3.可讀性:程式不複雜,可讀性提高

=>宣告函式:
  def 函式名稱(參數....):  #函式名稱 命名方式與變數一樣! #參數 帶入函數中運算執行的資料
      敘述式    ^多個參數以逗號隔開,若無參數,需保留小括號()
      ...
      ...
      ...
      return 傳回值  # 傳回值 傳回呼叫函式處
        ^無傳回值可省略  #省略 指整行省略   

=>呼叫:
    函式必須呼叫方可被執行
    .呼叫格式:
        無傳回值 -> 函式名稱(參數.....)
        有傳回值 -> 變數 = 函式名稱(參數.....)
"""
#例如：
要印出 20,30,50 個星號

for i in range(1,21):
    print('*', end='')
print()

for i in range(1,31):
    print('*', end='')
print()
    
for i in range(1,51):
    print('*', end='')
print()    
    
==========================
#第一種寫法
def printstart (n):
    for i in range(1,n+1):
        print('*', end='')
    print()
    
printstart(20)
printstart(30)
printstart(50)
   

#第二種寫法 =>考試會考
def printstart (n):
    for i in range(1,n+1):
        print('*', end='')
    print()

def main():
    printstart(20)
    printstart(30)
    printstart(50)
main()


#例如：
建立函式,求出1~100總和,(無參數,無傳回值)

def total():
    x = 0
    for i in range(1,101):
        x += i
    print('1+到100總和=',x)
total()

#例如：
建立函式,求出1~100總和,(無參數,有傳回值)
def total():
    sum = 0
    for i in range(1,101):
        sum += i
    return sum     #傳回值為 X
def main():
    t = total()  #呼叫 #傳回值X 傳回這
    print('1+到100總和=',t)
main() #呼叫

#例如：
建立函式,求1+到n的總和,(有參數,有傳回值)

def total(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum     #傳回值為 X
def main():
    t = total(100)  #呼叫 #傳回值X 傳回這
    print('1+到100總和=',t)
main() #呼叫

#例如：
建立函式,求輸入2整數的和,(無參數,無傳回值)

def total():
    x, y = eval(input("請輸入2個數，求總和:"))
    t = x + y
    print('總和為:',t)
total() #呼叫

#例如：
建立函式,求輸入2整數之間的總和,(有參數,有傳回值)
def total(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum
def main():
    x = eval(input('請輸入起始數值:'))
    y = eval(input('請輸入終止數值:'))
    t = total(x,y)
    print('%d 到 %d 的總和為:%d' % (x, y, t))

main()

#例如：
建立函式,求出1~100總和,和平均值(有參數,有傳回值)
def sumandaverage(n1 ,n2):
    total = 0
    average = 0.0
    for i in range(n1,n2+1):
        total += i
    average = total / (n2-n1+1)
    return total , average
def main():
    s, a = sumandaverage(1, 100)
    print('sum = %d , average = %.2f' % (s, a))
main()

#例如： 練習
建立函式,求輸入2整數之間的總和,和平均值(有參數,有傳回值)
def total(a,b):
    sum = 0
    ave = 0.0
    for i in range(a,b+1):
        sum += i
    ave = sum / (b-a+1)
    return sum , ave
def main():
    x = eval(input('請輸入起始數值:'))
    y = eval(input('請輸入終止數值:'))
    s, a = total(x,y)
    print('%d 到 %d 的總和為:%d , 平均值為: %.2f' % (x, y, s ,a))

main()

#===========================================================  
"""  
=>函式預設參數值:
  .函數宣告時,可只掉參數的預設值
  .當呼叫函式時,若無指定參數值,則會採用預設參數值
  .呼叫函式時,全不指定參數,則全部以預設值代入
  .預設參數值有設定,不可寫再無預設參數值的前面  # def total (a=1, b)  
                                                         ^錯誤
"""
#例如：
建立函式,求出1~100總和,和平均值(有參數,有傳回值)
def sumandaverage(n1 ,n2=100):
    total = 0
    average = 0.0
    for i in range(n1,n2+1):
        total += i
    average = total / (n2-n1+1)
    return total , average
def main():
    s, a = sumandaverage(1)
    print('sum = %d , average = %.2f' % (s, a))
main()

#例如：
建立函式,求出1~100總和,和平均值(有參數,有傳回值)
def sumandaverage(n1=1 ,n2=100):
    total = 0
    average = 0.0
    for i in range(n1,n2+1):
        total += i
    average = total / (n2-n1+1)
    return total , average
def main():
    s, a = sumandaverage()
    print('sum = %d , average = %.2f' % (s, a))
    s, a = sumandaverage(2)
    print('sum = %d , average = %.2f' % (s, a))
    s, a = sumandaverage(1,10)
    print('sum = %d , average = %.2f' % (s, a))
main()

#練習
請輸入攝氏溫度:36
攝氏36度 = 華氏 96.8度
公式:華氏 = (9/5)*攝氏+32
1.請以無傳回值方式撰寫
2.請以有傳回值方式撰寫

def ctof(c):
    f = (9/5)*c+32
    print('攝氏', c, '度=華氏', f,'度')
c = eval(input('請輸入攝氏溫度:'))
ctof(c)


def ctof(c):
    f= (9/5)*c+32
    return f
    print('攝氏', c, '度=華氏', f,'度')
c = eval(input('請輸入攝氏溫度:'))   
f = ctof(c)
print('攝氏', c, '度 = 華氏', f, '度')

#解答
def ctof(degc):
    degf=degc*1.8+32
    print('攝氏', degc, '度 = 華氏', degf, '度')
tempc = eval(input('請輸入攝氏溫度:'))
ctof(tempc)

print()
def ctof(degc):
    degf=degc*1.8+32
    return degf
tempc = eval(input('請輸入攝氏溫度:'))
tempf=ctof(tempc)
print('攝氏', tempc, '度 = 華氏', tempf, '度')

#===========================================================  
#作業一
#01
'''
請撰寫一程式，請使用者輸入華氏溫度，然後輸出其對應的攝氏溫度。
提示：攝氏溫度 = (華氏溫度-32)*5/9

輸入與輸出範例：
    輸入：212
    輸出：
        Fahrenheit 212.00 ---> Celsius 100.0
'''
#不回傳值
print()
def ctof(f):
    c = (f - 32) * 5/9 
    print('華氏', f, '度=攝氏', c,'度')
tempf = eval(input('請輸入華氏溫度:'))   
ctof(tempf)


#回傳值
print()
def ctof(f):
    c = (f - 32) * 5/9 
    return c   
tempf = eval(input('請輸入華氏溫度:'))   
tempc = ctof(tempf)
print('華氏', tempf, '度=攝氏', tempc,'度')


#02
'''
請撰寫一程式，以下一公式計算五邊形的面積：
 area = 5s^2/(4tan⁡(𝜋/5))，其中 s =2rsin(𝜋/5)，
 r 為五邊形的中心點到頂點的距離。
請使用者輸入 r，然後計算五邊形的面積(輸出到小數點後 2 位)。

輸入與輸出範例：
    輸入：5.5
    輸出：
        Area is 71.92
'''
#不回傳值
print()
import math
def rcof(n):
    s = 2*n*math.sin(math.pi/5)
    area = 5 * s**2 /(4*math.tan(math.pi/5))
    print('五邊形面積 = %.2f' % area, '平方')
n = eval(input('請輸入五邊形的中心點到頂點的距離 r : '))
rcof(n)


#回傳值
print()
import math
def rcof(n):
    s = 2*n*math.sin(math.pi/5)
    area = 5 * s**2 /(4*math.tan(math.pi/5))
    return area
n = eval(input('請輸入五邊形的中心點到頂點的距離 r : '))
area = rcof(n)
print('五邊形面積 = %.2f' % area, '平方')


#03
'''
給定飛機的加速度 a，
以及起飛的速度 v，
在不考慮外力耗損下(如輪胎磨擦力、空氣阻力等)，
則要讓飛機起飛的最短跑道長度為 length = v^2 / 2a 。
試寫一程式，提示使用者輸入以公尺 / 秒為單位的速度 v，
以及以公尺 / 秒平方為單位的加速度 a，
然後輸出最短的跑道長度(輸出到小數點後 2 位)。

輸入與輸出範例：
    輸入：70  , 4.3
    輸出：
        Minimum runway length is 569.77 meters
'''

#不回傳值
print()
def lcof(v, a):
    lenght = v ** 2 / (2 * a)
    print('最短的跑道長度 = %.2f' % lenght, '公尺')
v, a = eval(input('請輸入飛機的起飛速度(m/s) v 和 飛機的加速度(m/s^2) a : '))
lcof(v, a)


#回傳值
print()
def lcof(v, a):
    lenght = v ** 2 / (2 * a)
    return lenght
v, a = eval(input('請輸入飛機的起飛速度(m/s) v 和 飛機的加速度(m/s^2) a : '))
lenght = lcof(v, a)
print('飛機起飛所需的最短跑道長度 = %.2f' % lenght, '公尺')


#04
'''
請撰寫一程式，計算從起始溫度到最後溫度時熱水所需要的能量。
在程式中提示使用者輸入熱水量(公斤)、起始溫度與最後溫度。
計算能量的公式如下：
Q = M * (finalT – initial) * 4184
其中 M 式熱水的公斤數，
finalT 是最後溫度，
initial 是起始溫度，
Q 是以焦耳(joules)來衡量的能量(輸出到小數點後 2 位)

輸入與輸出範例：
    輸入：10  , 12 , 100
    輸出：
        Q = 3681920.00
        
    (表示輸入 10 公斤的熱水，
    溫度從 12 度 到 100 度，
    所需的能量是 3681920.00 焦耳)
'''
#不回傳值
print()
def qcof(m, l, t):
    q = m * (t-l) * 4184
    print('所需的能量是 Q = %.2f' % q, '焦耳')
m, l, t = eval(input('請輸入熱水量(公斤),起始溫度與最後溫度 : '))
qcof(m, l, t)


#回傳值
print()
def qcof(m, l, t):
    q = m * (t-l) * 4184
    return q
m, l, t = eval(input('請輸入熱水量(公斤),起始溫度與最後溫度 : '))
q = qcof(m, l, t)
print('所需的能量是 Q = %.2f' % q, '焦耳')

#05
'''
請撰寫一程式，計算圓柱體的底面積與體積(輸出到小數點後 2 位)。
在程式中提示使用者輸入圓柱的半徑和高。
 area = 𝜋r^2
 volume = area * height
其中 area 是底面積，
volume 是體積，
r 是圓柱體半徑，height 是圓柱體的高度。

輸入與輸出範例：
    輸入：6.5 , 10
    輸出：
        area : 132.73 , volume : 1327.32

'''
#不回傳值
print()
import math
def acof(r, h):
    area = math.pi * r **2
    volume = area * h
    print('圓柱體的底面積 = %.2f 平方,圓柱體的體積 = %.2f 立方' % (area, volume))
r, h = eval(input('請輸入圓柱的半徑和高 : '))
acof(r, h)


#回傳值
print()
import math
def acof(r, h):
    area = math.pi * r **2
    volume = area * h
    return volume
r, h = eval(input('請輸入圓柱的半徑和高 : '))
volume = acof(r, h)
print('圓柱體的底面積 = %.2f 平方,圓柱體的體積 = %.2f 立方' % (area, volume))



#===========================================================  
#作業二
#01
'''
一元二次方程式 ax^2+bx +c 的解為 (-b+(b^2+4ac)^1/2/2a 與 (-b-(b^2-4ac)^1/2/2a，
試輸入 a , b , c，求出此方程式的解。

輸入與輸出範例：
    輸入：
      a , b , c：2 , -8 , 6
    輸出：
      方程式解為：3.000000 與 1.000000
 
輸入與輸出範例：
    輸入：
      a , b , c：1 , -4 , 4
    輸出：
      方程式解為：2.000000
 
輸入與輸出範例：
    輸入：
      a , b , c：2 , 1 , 1
    輸出：
      方程式為無解
'''
#import math   
#math.sqrt(x) #sqrt=>開根號

#直出
import math 
a, b, c = eval(input('請輸入 a, b, c 求一元二次方程式解:'))
k = b ** 2 - (4 * a * c)
if k > 0:
    x1 = (-b + math.sqrt(k)) / (2 * a)
    x2 = (-b - math.sqrt(k)) / (2 * a)
    print('方程式解為： %.6f 與 %.6f' % (x1, x2))
if k == 0:
    x1 = -b / (2*a)
    x2 = x1
    print('方程式解為： %.6f ' % x1)
if k < 0:
   print('方程式為無解') 
   

#函數傳回值
import math   

def xcof(a, b, c):
    k = b ** 2 - (4 * a * c)
    if k > 0:
        x1 = (-b + math.sqrt(k)) / (2 * a)
        x2 = (-b - math.sqrt(k)) / (2 * a)
        print('方程式解為： %.6f 與 %.6f' % (x1, x2))
    if k == 0:
        x1 = -b / (2*a)
        x2 = x1
        print('方程式解為： %.6f ' % x1)
    if k < 0:
        print('方程式為無解')
a, b, c = eval(input('請輸入 a, b, c 求一元二次方程式解:'))
xcof(a, b, c)


#02
'''
試撰寫一程式，
由使用者的點座標 ( x , y)，
其中 x , y 皆為整數，
然後檢視該點是否位於中心點為 (0 , 0)，
半徑為 8 的圓內或圓外。

提示：
若點座標與圓心 (0 , 0) 的距離小於或等於 8，
則表示該點位於圓內，否則位於圓外。

輸入與輸出範例：
    輸入：
      3 , 6
    輸出：
      (3 , 6) 是位於圓內
      
輸入與輸出範例：
    輸入：
      8 , 9
    輸出：
      (8 , 9) 是位於圓外
'''

#import math   
#math.sqrt(x) # sqrt=>開庚號
# a**2 + b**2 = C**2

#直出
import math 
x, y = eval(input('請輸入(x,y)2點座標,以分辨是否在圓內:'))
z = x ** 2 + y ** 2
k = math.sqrt(z)
if k <= 8:
    print('(%d , %d)是位於圓內' % (x, y))
else:
    print('(%d , %d)是位於圓外' % (x, y))
    
#傳函數回值
import math 
def kcof(x, y):
    z = x ** 2 + y ** 2
    k = math.sqrt(z)
    if k <= 8:
        print('(%d , %d)是位於圓內' % (x, y))
    else:
        print('(%d , %d)是位於圓外' % (x, y))
x, y = eval(input('請輸入(x,y)2點座標,以分辨是否在圓內:'))
kcof(x, y)


#03
'''
試撰寫一程式，
利用亂數產生器產生介於 1~100 之間的亂數，
然後檢視這個亂數是 3 的倍數或是 5 的倍數或皆是或皆不是。

提示：此亂數若除以 3，餘數為 0 時，則為 3 的倍數；
若除以 5，餘數為 0 時，則為 5 的倍數。

輸入與輸出範例：
    輸入：
      68
    輸出：
      68 不是 3 或 5 的倍數
  
輸入與輸出範例：
    輸入：
      66
    輸出：
      66 是 3 的倍數
  
輸入與輸出範例：
    輸入：
      45
    輸出：
      45 是 3  與 5 的倍數
'''

#and 

#直接亂數產生

import random
x = random.randint(1,100)
a = x % 3 
b = x % 5
if (a == 0 and b == 0):
    print('%d 是 3 和 5 的倍數' % x)
elif (a != 0 and b != 0):
    print('%d 不是 3 或 5 的倍數' % x)
elif (b == 0):
    print('%d 是 5 的倍數' % x)
elif (a == 0):
    print('%d 是 3 的倍數' % x)
        

#輸入數值判斷
    
x = eval(input('請輸入一數值,來判斷是否為3或5的倍數 : '))
a = x % 3 
b = x % 5
if (a == 0 and b == 0):
    print('%d 是 3 和 5 的倍數' % x)
elif (a != 0 and b != 0):
    print('%d 不是 3 或 5 的倍數' % x)
elif (b == 0):
    print('%d 是 5 的倍數' % x)
elif (a == 0):
    print('%d 是 3 的倍數' % x)


#04研究中----未完成
'''
試撰寫一程式，
將使用者輸入的十六進位的字元轉換為其十進位所對應的數值。

輸入與輸出範例：
    輸入：
      請輸入 16 進位數值：9
    輸出：
      對應的十進位數值為 9
  
輸入與輸出範例：
    輸入：
      請輸入 16 進位數值：A
    輸出：
      對應的十進位數值為 10
  
輸入與輸出範例：
    輸入：
      請輸入 16 進位數值：G
    輸出：
      無效的數值
'''
#研究中----未完成
x = eval(input('請輸入一個十六進位的值 : ')
a = int(str(x), base=16)
print(a)

x = f 
y = int(str(x), 16)
print(y)

x = d
y = int(str(x),16)
print(y)


#05
'''
試撰寫一程式，
從使用者輸入一個整數，
檢視它是否被 5 或 8 整除，
或被 5 與 8 整除，
或無法被 5 或 8 整除。

輸入與輸出範例：
    輸入：
      請輸入數值：40
    輸出：
      40 可以被 5 或 8 整除
      40 可以被 5 與 8 整除
  
輸入與輸出範例：
    輸入：
      請輸入數值：15
    輸出：
      15 可以被 5 或 8 整除

輸入與輸出範例：
    輸入：
      請輸入數值：19
    輸出：
      19 不可以被 5 或 8 整除
'''
#and

x = eval(input('請輸入一數值,來判斷是否為3或5的倍數 : '))
a = x % 5 
b = x % 8
if (a == 0 and b == 0):
    print('%d 可以被 5 或 8 整除' % x)
    print('%d 可以被 5 與 8 整除' % x)
elif (a != 0 and b != 0):
    print('%d 不可以被 5 或 8 整除' % x)
elif (a == 0 or b == 0):
    print('%d 可以被 5 或 8 整除' % x)

#===========================================================  

  
