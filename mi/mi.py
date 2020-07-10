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
#import datetime
import time
#==處理中文字型問題===
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
#==去掉第一行title===========
csvRows = []
in_score_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY_1594344484383.csv', 'r' ,encoding='utf8')
csv_reader = csv.reader(in_score_csvfile)
for row in csv_reader:
	if csv_reader.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows.append(row)
in_score_csvfile.close() 
out_tmp_csvfile  = open(r'C:\GitHub\python\PY-Learn\mi\BODY\temp_BODY.csv','w', encoding='utf8',newline='')
csv_Writer = csv.writer(out_tmp_csvfile)
for row in csvRows:
    if any(field.strip() for field in row):
        csv_Writer.writerow(row)
out_tmp_csvfile.close()
#==================
in_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\temp_BODY.csv','r' , encoding = 'utf8')
line = in_csvfile.readline()
out_csvfile = open(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY.csv','w', encoding = 'utf8')
out_csvfile_title = ['date','weight']
out_csvfile.write('%s,%s \n' %(out_csvfile_title[0],out_csvfile_title[1]))
while line != '':
    data = line.split(',')
    unix_ts = eval(data[0])
    print(unix_ts)
    ltime = time.localtime(unix_ts)
    print(ltime)
    ldate = time.strftime("%Y-%m",ltime)
    print(ldate)
    lweight = data[1]
    print(lweight)
    out_csvfile.write('%s,%s\n' % (ldate,lweight))
    print('%s,%s\n' % (ldate,lweight))
    line = in_csvfile.readline()  
out_csvfile.close()
in_csvfile.close()


#============
fortune = pd.read_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY.csv')
#date = fortune.groupby('日期').mean()
date = fortune.groupby('date').min()
date.to_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY-new.csv',encoding='utf8')
print(date)

#==分析圖======
#colName = ['日期','體重']
weights = pd.read_csv(r'C:\GitHub\python\PY-Learn\mi\BODY\BODY-new.csv', index_col =0)
print(weights)
type(weights)
tw = pd.DataFrame(weights, columns = ['date'], index = weights['weight'])
plt.plot(tw['date'],tw['weight'])
plt.title('體重紀錄分析表')
plt.xlabel('日期')
plt.ylabel('體重')
plt.show()
    
