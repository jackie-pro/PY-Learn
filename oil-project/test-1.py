# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:25:52 2020

@author: jackie-PC
"""
import csv
import pandas as pd
#===製作下次加油累積公里數-暫存檔 txt -> txt
# (score.txt -> score-temp.txt) 
in_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line1 = in_score_file1.readline()
out_temp_file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-temp.txt','w', encoding = 'utf8')
out_temp_file_title1 = ['下次加油累積公里數']
out_temp_file.write('%s \n' % out_temp_file_title1[0])
while line1 != '': #製作 下次加油累積公里數 暫存檔
    print(line1)
    data1 = line1.split('-')
    print('data1 = ',data1)
    sumkm1 = eval(data1[1])  #取出下次加油累積公里數
    print('下次加油累積公里數 = ',sumkm1)
    out_temp_file.write('%s \n' % sumkm1)
    line1 = in_score_file1.readline()
in_score_file1.close()
out_temp_file.close()
#=========================  
#===製作下次加油累積公里數-去掉第一行(ROW)-暫存檔 txt -> txt -> txt
# (score-temp.txt -> score-temp1.txt -> score-temp2.txt) 
in_temp_file = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-temp.txt',encoding = 'utf8')
print(in_temp_file)
tmp = in_temp_file.drop(in_temp_file.index[0]) #去掉第一個
print(tmp)
tmp.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-temp1.txt',encoding='utf8',)
out_temp1_file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-temp1.txt','r',encoding='utf8',)
line2 = out_temp1_file.readline()
out_temp2_file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-temp2.txt','w', encoding = 'utf8')
while line2 != '': #製作 下次加油累積公里數 暫存檔-乾淨狀態
    print(line2)
    data2 = line2.split(',')
    print('data2 = ',data2)
    sumkm2 = data2[1]  #取出下次加油累積公里數
    print('下次加油累積公里數 = ',sumkm2)
    out_temp2_file.write('%s' % sumkm2)
    line2 = out_temp1_file.readline()
out_temp1_file.close()
out_temp2_file.close()    
#========================= 
#===製作完整整理過後new score檔 txt -> txt -> csv
# (score.txt -> new-score.txt -> new-score.csv) 
in_score_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line3 = in_score_file2.readline()
out_temp2_file = open(r'C:\GitHub\python\PY-Learn\oil-project\new-score.txt','w', encoding = 'utf8')
out_temp3_file = open(r'C:\GitHub\python\PY-Learn\oil-project\new-score.csv','w', encoding = 'utf8')
out_temp4_file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-temp2.txt','r', encoding = 'utf8')
line4 = out_temp4_file.readline() #把 下次加油累積公里數 暫存檔 的標頭 先讀取掉 不用
out_temp2_file_title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
out_temp2_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % (out_temp2_file_title[0],out_temp2_file_title[1],out_temp2_file_title[2],out_temp2_file_title[3],out_temp2_file_title[4],out_temp2_file_title[5],out_temp2_file_title[6],out_temp2_file_title[7],out_temp2_file_title[8]))
out_temp3_file.title = ['year','nowkm','lit','op']
out_temp3_file.write('%s,%s,%s,%s \n' % (out_temp3_file.title[0],out_temp3_file.title[1],out_temp3_file.title[2],out_temp3_file.title[3]))
while line3 != '':
    print(line3)
    data3 = line3.split('-')
    print('data3 = ',data3)
    day = data3[0] #取出日期
    print('加油日期 = ',day)
    day1 = day.split('/')
    year = day1[0]
    print('年分 = ',year)
    a = data3[2]   # 取出加油油價與公升數資料
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
        print('每公升油價 = %.2f' % plop)
    else:
        b = a.split('/') #分割 加油油價與公升數
        print('b = ',b)
        op = eval(b[0]) #加油費用 (oil price) 轉成整數
        print('加油費用 = ',op)
        lit = eval(b[1]) #加油公升數 (liter) 轉成整數
        print('加油公升數 = ',lit)
        plop = op / lit      #每公升油價 (per liter of oil price)
        print('每公升油價 = %.2f' % plop)
        
    line4 = out_temp4_file.readline()
    if line4 != '':
        nextkm = eval(line4) #轉成整數
        print('下次加油累積公里數 = ', nextkm)
        sumkm = eval(data3[1])  #取出累積公里數
        print('累積公里數 = ',sumkm)
        nowkm = nextkm - sumkm #計算出行駛公里數
        print('行駛公里數 = ', nowkm)
        cpk = op / nowkm #算出每公里費用
        print('每公里費用 = %.2f' % cpk)
        oilavg = nowkm / lit #算出油耗
        print('油耗 = %.2f' % oilavg)
        print('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm,op,lit,plop,nextkm,nowkm,oilavg,cpk))
        out_temp2_file.write('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm,op,lit,plop,nextkm,nowkm,oilavg,cpk))
        print('%s,%s,%s,%s \n' % (year,nowkm,lit,op))
        out_temp3_file.write('%s,%s,%s,%s \n' % (year,nowkm,lit,op))
    else:
        print()
            
    line3 = in_score_file2.readline()
in_score_file2.close()
out_temp2_file.close()
out_temp3_file.close()
out_temp4_file.close()
