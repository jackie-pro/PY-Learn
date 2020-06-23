# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:24:51 2020

@author: jackie-PC
"""


#102
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
print('|%7.2f %7.2f|' % (num1,num2))
print('|%7.2f %7.2f|' % (num3,num4))
print('|%-7.2f %-7.2f|' % (num1,num2))
print('|%-7.2f %-7.2f|' % (num3,num4))

#104
import math
r = eval(input())
p = 2 * r * math.pi
a= r * r * math.pi
print('Radius = %.2f' % r)
print('Perimeter = %.2f' % p)
print('Area = %.2f' % a)

#202
x = eval(input())
if x % 3 == 0 and x % 5 == 0:
    print('%d is a multiple of 3 and 5.' % x)
elif x % 3 == 0:
    print('%d is a multiple of 3.' % x)
elif x % 5 == 0:
    print('%d is a multiple of 5.' % x)
else:
    print('%d is not a multiple of 3 or 5.' % x)
    
#204    
a = eval(input())
b = eval(input())
x = input()
ans = 0
if x == '+': ans = a + b
elif x == '-': ans = a - b 
elif x == '*': ans = a * b
elif x == '/': ans = a / b
elif x == '//': ans = a // b
elif x == '%': ans = a % b
print(ans)
 

#302
a = eval(input())
b = eval(input())
ans = 0
for i in range(a, b+1):
    if i % 2 == 0:
       ans += i 
print(ans)

#304
a = int(input())
ans = 0
for i in range(1, a+1):
    if i % 5 == 0:
        ans += i
print(ans)


#402
a = eval(input())
min_a = a
while a != 9999:
    a = eval(input())
    if a < min_a:
        min_a = a
print(min_a)

#404
a = eval(input())

if a == 0:
    print(a)
else:
    while a !=0:
        print(a % 10, end ='')
        a //= 10


#502     
def compute(x,y):
    return x * y
x = eval(input())
y = eval(input())
       
print(compute(x,y))


#504
def compute():
    return a ** b
a = eval(input())
b = eval(input())

print(compute())

#602
a = []
b = 0

for i in range(5):
    a.append(input())
    
for i in range(5):
    if a[i] == 'A': b += 1
    elif a[i] == 'J': b += 11
    elif a[i] == 'Q': b += 12
    elif a[i] == 'K' : b += 13
    elif a[i] == '10' : b += 10
    else:
        b += eval(a[i])
print(b)


#604
size = 10
a = []
c = [0] * size

for i in range(size):
    num = int(input())
    
    a.append(num)
    c[a.index(num)] += 1

num_o = max(c)

print(a[c.index(num_o)])
print(num_o)

#702
tup1=()
tup2=()
print('Create tuple1:')
while True:
    num = eval(input())
    if num == -9999:
        break
    tup1 += (num,)
    
print('Create tuple2:')
while True:
    num = eval(input())
    if num == -9999:
        break
    tup2 += (num,)

tup_cob = tup1 +tup2
print('Combined tuple before sorting:',tup_cob)
lst_cob = list(tup_cob)
print('Combined list after sorting:', sorted(lst_cob))    


#704
num=set()

while True:
    inp = eval(input())
    if inp == -9999:
        break
    num.add(inp)
    
print('Length:', len(num))
print('Max:', max(num))
print('Min:', min(num))
print('Sum:', sum(num))

#802
total = 0
string = input()

for i in range(0, len(string)):
    num = ord(string[i])
    print("ASCII code for '%s' is %d" % (string[i], num))
    total += num
print(total)

#804
st = input()
str1 = st.upper()
print(str1)

str2 = st.title()
print(str2)

#902
f = open('read.txt', 'r')
data = f.read()
f.close

num = data.split(' ')
total = 0
for i in range(0, len(num)):
    total += eval(num[i])

print(total)

#904
with open('read.txt', 'r') as file:
    for line in file:
        print(line)
        tmp = line.strip('\n').split(' ')
        tmp = [tmp[0], eval(tmp[1]), eval(tmp[2])]
        data.append(tmp)
name = [data[x][0] for x in range(len(data))]
height = [data[x][1] for x in range(len(data))]
weight = [data[x][2] for x in range(len(data))]
print('Average height: %.2f' % (sum(height) / len(height)))
print('Average weight: %.2f' % (sum(weight) / len(weight)))

max_h = max(height)
max_w = max(weight)
print('The tallest is %s with %.2fcm' % (name[height.index(max_h)], max_h))
print('The heaviest is %s with %.2fkg' % (name[weight.index(max_w)], max_w))







