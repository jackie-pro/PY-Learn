# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:13:49 2020

@author: jackie-PC
"""
"""
#第一步 將原始檔 轉換成 所需格式 並存成csv檔 
  

"""
#處理自我加油紀錄=======
def main():
  infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
  line = infile.readline()
  outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new.txt','w', encoding = 'utf8')
  title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價']
  outfile.write('%s,%s,%s,%s,%s \n' % (title[0],title[1],title[2],title[3],title[4]))
  while line != '':  
      print(line)
      data = line.split('-')
      print('data = ',data)
      day = data[0] #取出日期
      print('加油日期 = ',day)
      sumkm = eval(data[1])  #取出累積公里數
      print('累積公里數 = ',sumkm)
      a = data[2]   # 取出加油油價與公升數資料
      print('a = ',a)
      q = len(a)
      print('q = ',q)
      if q > 10:
          b = a.split('/') #分割 加油油價與公升數
          print('b = ',b)
          op = eval(b[0]) #加油費用 (oil price) 轉成整數
          print('加油費用 = ',op)
          lit = eval(b[1]) #加油公升數 (liter) 轉成整數
          print('加油公升數 = ',lit)
          plop = eval(b[2])      #每公升油價 (per liter of oil price)
          print('每公升油價 = %.1f' % plop)
      else:
          b = a.split('/') #分割 加油油價與公升數
          print('b = ',b)
          op = eval(b[0]) #加油費用 (oil price) 轉成整數
          print('加油費用 = ',op)
          lit = eval(b[1]) #加油公升數 (liter) 轉成整數
          print('加油公升數 = ',lit)
          plop = op / lit      #每公升油價 (per liter of oil price)
          print('每公升油價 = %.1f' % plop)
      print('%s,%s,%s,%s,%.1f \n' % (day,sumkm,op,lit,plop))
      outfile.write('%s,%s,%s,%s,%.1f \n' % (day,sumkm,op,lit,plop))
      line = infile.readline()
  infile.close()
  outfile.close()

main() 


#處理公告歷史油價紀錄=======
def main():
  infile1 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score.txt','r', encoding = 'utf8')
  line1 = infile1.readline()
  outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-new.csv','w', encoding = 'utf8')
  while line1 != '':  
      print(line1)
      data1 = line1.split('	')
      print('data1 = ',data1)
      day1 = data1[0] #取出調價日期
      print('調價日期 = ',day1)
      oil95 = (data1[2])  #取出公告95無鉛汽油價格
      print('公告95無鉛汽油價格 = ',oil95)
      print('%s,%s \n' % (day1,oil95))
      if oil95 != '':
          outfile.write('%s,%s \n' % (day1,oil95))
      line1 = infile1.readline()
  infile1.close()
  outfile.close()

main() 


#==============================
def main():
  infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-1.txt','r',encoding = 'utf8')
  line = infile.readline()
  outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2.txt','w', encoding = 'utf8')
  title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','行駛公里數','油耗']
  outfile.write('%s,%s,%s,%s,%s,%s,%s \n' % (title[0],title[1],title[2],title[3],title[4],title[5],title[6]))
  print(line)
  while line != '':  
      print(line)
      data = line.split(',')
      print('data = ',data)
      day = data[0] #取出日期
      print('加油日期 = ',day)
      #print('上一次的公里數 = ',oldkm)
      sumkm = eval(data[1])  #取出累積公里數
      print('累積公里數 = ',sumkm)
      #nowkm = sumkm - oldkm  #計算出此次行使公里數
      #print('此次行使公里數 = ',nowkm) #此次行使公里數
      #oldkm = sumkm      # 將累積公里數設為上一次的公里數
      #print('將此次公里數設為上一次公里數 = ',oldkm)
      a = data[2]   # 取出油價公升資料
      print('a = ',a)
      q = len(a)
      print('q = ',q)
      if q > 10:
          b = a.split('/') #分割 加油油價與公升數
          print('b = ',b)
          op = eval(b[0]) #加油費用 (oil price) 轉成整數
          print('加油費用 = ',op)
          lit = eval(b[1]) #加油公升數 (liter) 轉成整數
          print('加油公升數 = ',lit)
          plop = eval(b[2])      #每公升油價 (per liter of oil price)
          print('每公升油價 = %.1f' % plop)
      else:
          b = a.split('/') #分割 加油油價與公升數
          print('b = ',b)
          op = eval(b[0]) #加油費用 (oil price) 轉成整數
          print('加油費用 = ',op)
          lit = eval(b[1]) #加油公升數 (liter) 轉成整數
          print('加油公升數 = ',lit)
          plop = op / lit      #每公升油價 (per liter of oil price)
          print('每公升油價 = %.1f' % plop)
      print('%s,%s,%s,%s,%.1f \n' % (day,sumkm,op,lit,plop))
      outfile.write('%s,%s,%s,%s,%.1f \n' % (day,sumkm,op,lit,plop))
      line = infile.readline()
  infile.close()
  outfile.close()

main() 
#==============


.sort()函式:串列排序  #依UNICON碼由小到大

#處理公告歷史油價紀錄=======
def main():
  import csv
  from datetime import datetime 
  
  infile2 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-new.csv','r', encoding = 'utf8')
  #line2 = infile2.readline()
  line3 = infile2.readlines()
  #print(line2)
  #print(line3)
  #data = line2.split(',')
  #takeOne = data[0]
  #print(takeOne) #lambda
  def parse(date_string,date_format='%Y/%m/%d'):
   return datetime.strptime(date_string,date_format)
  sorted(line3, key=parse, reverse=False)
  #line3.sort(key=lambda date: datetime.strptime(date,'%Y/%m/%d')) 
  print(line3)
  #line2 = infile2.readline()
  line3 = infile2.readlines()
  infile2.close()

main() 

import csv
with open(r'C:\GitHub\python\PY-Learn\oil-project\score-new.csv','r',encoding = 'utf8') as csvfile:
    with open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-1.csv', 'w',encoding = 'utf8') as csvnew:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(csvnew)
        header = next(csvreader) #取得讀取資料的表頭設定給變數header
        print(header) #印出表頭
        csvwriter.writerow(header) #將表頭寫入檔案
        for row in csvreader: #以迴圈逐行讀取資料
            print(row[1]) #使用join()方法將字串合併並印出
            csvwriter.writerow(row) 	#以寫入物件利用writerow()方法將每列資料寫入
import csv   
with open(r'C:\GitHub\python\PY-Learn\oil-project\score-new.csv','r',encoding = 'utf8') as csvfile: 
    data = csv.reader(csvfile, delimiter = ',')
    for row in data:
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4])
