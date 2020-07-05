# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:39:36 2020

@author: Jackie
"""


import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
#=======
#移除第一行標頭 csv -> csv
# (temp-score-6.csv -> temp-score-7.csv)
csvRows2 = []
in_temp_csvfile4 = open(r'C:\GitHub\python\PY-Learn\oil-project\政府行政機關辦公日曆表.csv', 'r' ,encoding='utf8')
csv_reader2 = csv.reader(in_temp_csvfile4)
for row in csv_reader2:
	if csv_reader2.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows2.append(row)
in_temp_csvfile4.close()

out_tmp_csvfile4  = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.csv','w', encoding='utf8',newline='')
csv_Writer2 = csv.writer(out_tmp_csvfile4)
for row in csvRows2:
    if any(field.strip() for field in row):
        csv_Writer2.writerow(row)
out_tmp_csvfile4.close()
#========================= 
in_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.csv','r',encoding = 'utf8')
line1 = in_score_file1.readline()
out_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day.csv','w', encoding = 'utf8')
while line1 != '': 
    print(line1)
    data1 = line1.split(',')
    print('data1 = ',data1)
    date = data1[0]  
    print('date = ',date)
    date = date.split('/')
    year = date[0]
    print('年分 = ',year)
    isnot = data1[2]  
    print('isnot = ',isnot)
    out_temp_file1.write('%s,%s \n' % (year,isnot))
    print('%s,%s \n' % (year,isnot))
    line1 = in_score_file1.readline()
in_score_file1.close()
out_temp_file1.close()


#==將政府資料開放資料 csv to json=========
# (政府行政機關辦公日曆表.csv -> open-score-day.json )
csvfile = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day.csv','r', encoding = 'utf8')
jsonfile = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.json','w', encoding = 'utf8')

fieldnames = ("date","isHoliday")

reader = csv.DictReader(csvfile,fieldnames)
for row in reader:
    json.dump(row,jsonfile ,ensure_ascii=False) #unicode碼問題
    jsonfile.write('\n')
	
jsonfile.close()
csvfile.close()

#=======
import json
with open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.json', encoding = 'utf8') as jsonfile:

    jsondata = json.load(jsonfile)
    
    for item in jsondata:
        
        print([item['date'], item['isHoliday']])
      