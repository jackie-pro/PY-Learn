# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:13:35 2020

@author: Jackie
"""
'''
#==================
#將unix時間戳記 timestamp 轉換為日期時間
import csv
unix_ts = 1527812465
time = datetime.datetime.fromtimestamp(unix_ts)
print(time)

import datetime
import time
ltime=time.localtime(1527812465)
print(ltime)
timeStr=time.strftime("%Y",ltime)
print(timeStr)
#==================
'''
#==導入所需函式庫====
import csv
import pandas as pd
import matplotlib.pyplot as plt
import time
#==處理中文字型問題===
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
#==去掉第一行title===========
csvRows = []
#讀取原始檔
in_score_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY_1594624781643.csv', 'r' ,encoding='utf8')
csv_reader = csv.reader(in_score_csvfile)
for row in csv_reader:
	if csv_reader.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows.append(row)
in_score_csvfile.close() 
#開啟暫存檔
out_tmp_csvfile  = open(r'C:\GitHub\python\PY-Learn\mi\BODY\temp_BODY.csv','w', encoding='utf8',newline='')
csv_Writer = csv.writer(out_tmp_csvfile)
for row in csvRows: #一行一行寫入暫存檔
    if any(field.strip() for field in row):
        csv_Writer.writerow(row)
out_tmp_csvfile.close()
#==清理所需資料格式================
#讀取暫存檔
in_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\temp_BODY.csv','r' , encoding = 'utf8')
line = in_csvfile.readline()
#開啟清理過後的資料檔
out_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY.csv','w', encoding = 'utf8')
out_csvfile_title = ['date','weight'] #只寫入日期與體重
out_csvfile.write('%s,%s \n' %(out_csvfile_title[0],out_csvfile_title[1]))
while line != '': #用迴圈取出紀錄做整理
    data = line.split(',') #先分割
    unix_ts = eval(data[0]) #將unix時間戳記取出
    ltime = time.localtime(unix_ts) #將unix時間戳記轉換成正常時間
    ldate = time.strftime("%Y/%m/%d",ltime) #只取出年月日
    lweight = eval(data[1]) #取出體重
    out_csvfile.write('%s,%.1f\n' % (ldate,lweight)) #將體重以小數點後一位寫入
    line = in_csvfile.readline()  
out_csvfile.close()
in_csvfile.close()
#==以同日期中取出最小值的體重，再寫入暫存檔==========
minw = pd.read_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY.csv')
date = minw.groupby('date').min() #取最小值
date.to_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY-new.csv',encoding='utf8')
#==分析圖======
weights = pd.read_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY-new.csv', index_col=0)
weights.plot(title = '體重紀錄分析表')
plt.xlabel('日期')
plt.ylabel('體重')
plt.show()



