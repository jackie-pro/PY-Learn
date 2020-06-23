# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:29:24 2020

@author: Jackie
"""


#Python Exercise
#20200612
"""
1.輸入國文、英文、數學三科成績後，計算總分以及平均成績。
"""
#ans:

x = eval(input('請輸入國文成績:'))
y = eval(input('請輸入英文成績:'))
z = eval(input('請輸入數學成績:'))

su = x + y + z
avg = su / 3

print('總分為: %d 平均成績為: %.2f' % (su, avg))

"""
2.輸入上底、下底與高的數值後，計算梯形的面積。
  (梯形面積公式:(上底+下底)*高/2)
"""
#ans:

x = eval(input('請輸入梯形的上底:'))
y = eval(input('請輸入梯形的下底:'))
z = eval(input('請輸入梯形的高:'))

s = (x + y) * z / 2
print('梯形面積為: %.2f' % s)

"""
3.百貨公司周年慶，公司決定消費超過2000元的顧客就打75折
  增加買氣。請幫公司寫出一成是，輸入顧客購買總金額後，
  計算顧客實際需付的金額。
"""
#ans:

x = eval(input('請輸入顧客總金額:'))

if x >= 2000:
    s = x * 0.75
    print('顧客消費已達折扣金額，所以應付金額打75折: %.2f' % s)
else:
    print('顧客消費未達則扣金額，所以應付: %d' % x)

"""
4.請輸入月份，判斷是甚麼季節?
  (春天: 3~5月,夏天:6~8月,秋天:9-11月,冬天:12~2月)
"""
#ans:

m = eval(input('請輸入月份:'))

if m >= 3 and m <= 5:
    print('%d 月份是 春天 !' % m)
elif m >=6 and m <= 8:
    print('%d 月份是 夏天 !' % m)
elif m >=9 and m <= 11:
    print('%d 月份是 秋天 !' % m)
elif m >=1 and m <= 2 or m == 12:
    print('%d 月份是 冬天 !' % m)
else:
    print('無此月份 !')

"""
5.請設計一程式，計算級數1+2+4+7+11...+106的過程和結果。
"""
#ans:
x = 1
y = 0
for i in range(0,15):
    x = x + i
    print(x)
    y += x 
print('總和:',y)

#=========
x=1
y=1
s=0
print(x)
while x < 106:
    s += x
    x += y
    y += 1
    print(x)
z = s + 106
print(z)
#=========
Sum = 0
i = 1
j = 1
while (i <= 106):
    Sum += i
    print('i = {:d} Sum = {:d}'.format(i,Sum))
    i = i + j
    j = j + 1
    print('Sum = {:d}'.format(Sum))
    
#=========

"""
6.請設計一程式，讓使用者輸入英文句子，程式會以空格來切割句子，
  切成多個單字並輸出。
"""
#ans:
w = str(input('請輸入英文句子:'))
lst = w.split()
for i in lst:
    print(i)
     
"""
7.請設計一程式，讓使用者輸入姓名與電話,當期要結束輸入通訊資料
  時，可以輸入[finish] 結束。接著可以查詢通訊錄姓名，程式會
  回應其通訊電話，若沒偶會回覆[不在通訊錄中]。
"""
#ans:
def conf():
    dic = {}
    while True:
        key = input('請輸入姓名:')
        if key == 'finish':
            break
        
        value = input('請輸入電話:')
        dic[key] = value
        print(dic)
        
    search = input('請輸入要查尋的姓名:')
    print('%s 的電話是 : %s' % (search,(dic.get(search,'不在通訊錄中!'))))
    
dict1 = conf()



"""
8.請設計一程式，呼叫一個自訂函式f(),計算某一整數的n次方。
  例如[請輸入要計算的整數: x]，[請輸入要計算的次方數: y]
  ，輸出[x的y次方 結果是:]。
"""
#ans:

def f():
    x = int(input('請輸入要計算的整數 : '))
    y = int(input('請輸入要計算的次方數 : '))
    z = (x ** y)
    print('%d 的 %d 次方 結果是: %d' % (x, y, z))
    return
f()

    