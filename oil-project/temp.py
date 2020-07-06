# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:39:36 2020

@author: Jackie
"""
import csv
import json

#==從政府開放資料-政府行政機關辦公日曆表 取出 每年放假日===========
#移除第一行標頭 csv -> csv
# (政府行政機關辦公日曆表.csv -> open-score-day.csv)
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
# 轉換資料格式
# (open-score-day.csv ->temp-open-score-day.csv)
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
    mon = eval(date[1])
    print('月 = ',mon)
    day = eval(date[2])
    print('日 = ',day)
    isnot = data1[2]
    print('isnot = ',isnot)
    '''
    if mon < 10:
        nmon = '%02d' % mon
        out_temp_file1.write('%s,%s,' % (year,nmon))
        print('%s,%s,' % (year,nmon))
    else:
        out_temp_file1.write('%s,%s,' % (year,mon))
        print('%s' % mon)        
    if day < 10:
        nday = '%02d' % day
        out_temp_file1.write('%s,' % (nday))
        print('%s,' % (nday))
    else:
        out_temp_file1.write('%s,' % (day))
        print('%s' % day)
'''        
    out_temp_file1.write('%s,%s,%s,%s\n' % (year,mon,day,isnot))
    print('%s,%s,%s,%s\n' % (year,mon,day,isnot))
    line1 = in_score_file1.readline()
in_score_file1.close()
out_temp_file1.close()

#將日期月分與日補0成雙數


#==將政府資料開放資料 csv to json=========
# (政府行政機關辦公日曆表.csv -> open-score-day.json )
csvfile = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day.csv','r', encoding = 'utf8')
jsonfile = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.json','w', encoding = 'utf8')
fieldnames = ("year","mon","day","isHoliday")
reader = csv.DictReader(csvfile,fieldnames)
jsonfile.write('[')
for row in reader:
    json.dump(row,jsonfile ,ensure_ascii=False,indent=4) #unicode碼問題
    jsonfile.write(',\n')
jsonfile.seek(jsonfile.tell()-3) #指定位置到最後一行的倒數第3個字元
print(jsonfile.tell())
jsonfile.write("]") #用]取代掉','
print(jsonfile.tell())
csvfile.close()
jsonfile.close()

#=======
out_temp_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day-1.csv','w', encoding = 'utf8')
with open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.json', encoding = 'utf8') as jsonfile:
    jsondata = json.load(jsonfile)
    #依比例 設定每年10天特休
    count1 = 1 
    count2 = 10
    count3 = 10
    count4 = 10
    count5 = 10
    count6 = 10
    count7 = 5
    for item in jsondata:
        if eval(item['year']) == 2014 and eval(item['mon']) == 11 and eval(item['day']) >= 26:
            year1 = 2014
            if item['isHoliday'] == '是':
                count1 += 1
        elif eval(item['year']) == 2014 and eval(item['mon']) == 12 and eval(item['day']) <= 31:
            year1 = 2014
            if item['isHoliday'] == '是':
                count1 += 1
        elif eval(item['year']) == 2015:
            year2 = 2015
            if item['isHoliday'] == '是':
                count2 += 1
        elif eval(item['year']) == 2016:
            year3 = 2016
            if item['isHoliday'] == '是':
                count3 += 1
        elif eval(item['year']) == 2017:
            year4 = 2017
            if item['isHoliday'] == '是':
                count4 += 1
        elif eval(item['year']) == 2018:
            year5 = 2018
            if item['isHoliday'] == '是':
                count5 += 1
        elif eval(item['year']) == 2019:
            year6 = 2019
            if item['isHoliday'] == '是':
                count6 += 1       
        elif eval(item['year']) == 2020 and eval(item['mon']) <= 6 and eval(item['day']) <= 30:
            year7 = 2020
            if item['isHoliday'] == '是':
                count7 += 1
workd1 = ((30-25) + 31) - count1 #從11/26開始算
workd2 = 365 - count2
workd3 = 365 - count3
workd4 = 365 - count4
workd5 = 365 - count5
workd6 = 365 - count6
workd7 = (365-(31+29+31+30+31+30)) - count7 #今年2月有29天
print('2014/11/26 ~ 2014/12/31')
print('%s年,休假日 %s 天, 上班日 %s 天' % (year1,count1,workd1))
print('%s年,休假日 %s 天, 上班日 %s 天' % (year2,count2,workd2))
print('%s年,休假日 %s 天, 上班日 %s 天' % (year3,count3,workd3))
print('%s年,休假日 %s 天, 上班日 %s 天' % (year4,count4,workd4))               
print('%s年,休假日 %s 天, 上班日 %s 天' % (year5,count5,workd5))
print('%s年,休假日 %s 天, 上班日 %s 天' % (year6,count6,workd6))
print('2020/01/01 ~ 2014/06/30') 
print('%s年,休假日 %s 天, 上班日 %s 天' % (year7,count7,workd7))

out_temp_file2.close()




     




















 