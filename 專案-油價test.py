# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:13:49 2020

@author: jackie-PC
"""
"""
#第一步 將原始檔 轉換成 所需格式 並存成csv檔 
  

"""
#處理沒有每公升油價的部分=======
def main():
  infile = open(r'D:\aaa\GitHub\PY-Learn\oil-project\score.txt','r')
  line = infile.readline()
  outfile = open(r'D:\aaa\GitHub\PY-Learn\oil-project\score-new.csv','w')
  while line != '':  
      print(line)
      data = line.split('-')
      print('data = ',data)
      day = data[0] #取出日期
      print('day = ',day)
      km = eval(data[1])  #取出公里數
      print('km = ',km)
      a = data[2]   # 取出油價公升資料
      print('a = ',a)
      q = len(a)
      print('q = ',q)
      if q > 10:
          b = a.split('/') #分割 油價與公升
          print('b = ',b)
          op = eval(b[0]) #油價 (oil price) 轉成整數
          print('op = ',op)
          lit = eval(b[1]) #公升數 (liter) 轉成整數
          print('lit = ',lit)
          plop = eval(b[2])      #每公升油價 (per liter of oil price)
          print('plop = %.1f' % plop)
      else:
          b = a.split('/') #分割 油價與公升
          print('b = ',b)
          op = eval(b[0]) #油價 (oil price) 轉成整數
          print('op = ',op)
          lit = eval(b[1]) #公升數 (liter) 轉成整數
          print('lit = ',lit)
          plop = op / lit      #每公升油價 (per liter of oil price)
          print('plop = %.1f' % plop)
      print('%s,%s,%s,%s,%.1f \n' % (day,km,op,lit,plop))
      outfile.write('%s,%s,%s,%s,%.1f \n' % (day,km,op,lit,plop))
      line = infile.readline()
  infile.close()
  outfile.close()

main() 

import csv
#載入csv套件
with open(r'D:\aaa\GitHub\PY-Learn\oil-project\score-new.csv', 'r', encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    #delimiter指定分隔字元
    plots = csv.reader(csvfile, delimiter = ',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in plots:  #以讀取的plots資料做為迴圈依據
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4])
        #每一個欄位(row)以索引取出該欄位資料      

#==============
"""


"""



  
s =("2014/11/26-62615-105/3.39")  
data = s.split('-')
day = data[0]
days = day.split('/','-')
year = days[0]
mou = days[1]
a = data[2]
b = a.split('/')
c = eval(b[0])
d = eval(b[1])
e = c / d
print(data)
print(day)
print(days)
print(year)
print(mou)
print(a)
print(b)
print(c)
print(d)
print('每公升95無鉛汽油 = %.1f' % e)
  
 

def main():
  infile = open(r'D:\aaa\GitHub\PY-Learn\oil-project\oil-np1.txt','r')
  line = infile.readline()
  while line != '':
      print(line)
      data = line.split('-')
      day = data[0] #取出日期
      km = data[1]  #取出公里數
      a = data[2]   # 取出油價公升資料
      q = len(a) 
      b = a.split('/') #分割 油價與公升
      op = eval(b[0]) #油價 (oil price) 轉成整數
      lit = eval(b[1]) #公升數 (liter) 轉成整數
      plop = eval(b[2])     #每公升油價 (per liter of oil price)
      print('data = ',data)
      print('day = ',day)
      print('km = ',km)
      print('a = ',a)
      print('q = ',q)
      print('b = ',b)
      print('op = ',op)
      print('lit = ',lit)
      print('plop = %.1f' % plop)
      print('%s,%s,%s,%s,%.1f,\n' % (day,km,op,lit,plop))
      line = infile.readline()
  infile.close()


main()