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




def main():
    #import csv
    import pandas as pd
    
    infile1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
    line3 = infile1.readline()
   
    tempfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp.txt','w', encoding = 'utf8')
    title1 = ['下次加油累積公里數']
    tempfile.write('%s \n' % title1[0])
    while line3 != '': #製作 下次加油累積公里數 暫存檔
        print(line3)
        data1 = line3.split('-')
        print('data1 = ',data1)
        sumkm1 = eval(data1[1])  #取出下次加油累積公里數
        print('下次加油累積公里數 = ',sumkm1)
        tempfile.write('%s \n' % sumkm1)
        line3 = infile1.readline()
    infile1.close()
    tempfile.close()
    df = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp.txt',encoding = 'utf8')
    print(df)
    df1 = df.drop(df.index[0]) #去掉第一個
    print(df1)
    df1.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp1.txt',encoding='utf8',)
    df2 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp1.txt','r',encoding='utf8',)
    line1 = df2.readline()
    temp2file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp2.txt','w', encoding = 'utf8')
    while line1 != '': #製作 下次加油累積公里數 暫存檔-乾淨狀態
        print(line1)
        data2 = line1.split(',')
        print('data2 = ',data2)
        sumkm2 = data2[1]  #取出下次加油累積公里數
        print('下次加油累積公里數 = ',sumkm2)
        temp2file.write('%s' % sumkm2)
        line1 = df2.readline()
    df2.close()
    temp2file.close()
    df3 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp2.txt','r', encoding = 'utf8')
    line2 = df3.readline() #把 下次加油累積公里數 暫存檔 的標頭 先讀取掉 不用
    print(line2)
    infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
    line = infile.readline()
    outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-1.txt','w', encoding = 'utf8')
    #title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
    #outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%ss \n' % (title[0],title[1],title[2],title[3],title[4],title[5],title[6],title[7],title[8]))
    while line != '':
        print(line)
        data = line.split('-')
        print('data = ',data)
        day = data[0] #取出日期
        print('加油日期 = ',day)
        day1 = day.split('/')
        year = day1[0]
        print('年分 = ',year)
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
            print('每公升油價 = %.2f' % plop)
        line2 = df3.readline() #取出下次加油累積公里數
        nextkm = eval(line2) #轉成整數
        print('下次加油累積公里數 = %s' % nextkm)
        nowkm = nextkm - sumkm #計算出行駛公里數
        print('行駛公里數 = %s' % nowkm)
        oilavg = nowkm / lit #算出油耗
        print('油耗 = %.2f' % oilavg)
        cpk = op / nowkm #算出每公里費用
        print('每公里費用 = %.2f' % cpk)
        print('%.2f,%.2f,%.2f,%s \n' % (plop,oilavg,cpk,year))
        outfile.write('%.2f,%.2f,%.2f,%s \n' % (plop,oilavg,cpk,year))
        line = infile.readline()
    df3.close()
    infile.close()
    outfile.close()
    
main() 

import pandas as pd
import matplotlib.pyplot as plt

colName = ['plop','oilavg','cpk']
oilcost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-1.txt', encoding = 'utf8', names = colName)

oilcost_mean = oilcost.groupby('cpk', as_index = False).mean()
oilcost_mean.plot(kind = 'bar')
plt.xticks(oilcost_mean.index, oilcost_mean['cpk'], rotation = 0)
plt.show()

#['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
#plt.plot(oilcost['油耗'], oilcost['每公里費用'], '*', color = 'g')
#要繪圖的參數
#plt.xlabel('油耗')
#plt.ylabel('每公里費用')
#plt.title('5HG-567 CUXI 100 油耗表')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

colName = ['sepal_len', 'sepal_wd', 'petal_len', 'petal_wd', 'species']
iris = pd.read_csv(r'D:\aaa\GitHub\PY-Learn\iris.csv', names = colName)

iris_mean = iris.groupby('species', as_index = False).mean()
iris_mean.plot(kind = 'bar')
plt.xticks(iris_mean.index, iris_mean['species'], rotation = 0)

plt.show()