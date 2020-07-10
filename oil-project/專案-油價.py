# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:24:21 2020
程式設計工程師專班 洪孝承 17號
@author: jackie Hung
"""
#==導入所需函式庫===
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt
#==處理中文字型問題===
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
plt.rc('axes',unicode_minus=False) #解決坐標軸負數的-號顯示問題

#==自我紀錄機車加油資料 處理======================================================
#計算出當次加油後到下次加油後行駛多少公里數
#===製作下次加油累積公里數-暫存檔 
# (score.txt -> temp-score.csv) 
in_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line1 = in_score_file1.readline()
out_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score.csv','w', encoding = 'utf8')
out_temp_file1_title = ['下次加油累積公里數']
out_temp_file1.write('%s \n' % out_temp_file1_title[0])
while line1 != '': #製作 下次加油累積公里數 暫存檔
    data1 = line1.split('-')
    sumkm1 = eval(data1[1])  #取出下次加油累積公里數
    out_temp_file1.write('%s \n' % sumkm1)
    line1 = in_score_file1.readline()
in_score_file1.close()
out_temp_file1.close()
#========================= 
#移除第一行標頭 
# (temp-score.csv -> temp-score-1.csv)
in_temp_csvfile1 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score.csv',encoding = 'utf8')
out_tmp_csvfile1 = in_temp_csvfile1.drop(in_temp_csvfile1.index[0]) #去掉第一個
out_tmp_csvfile1.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-1.csv',encoding='utf8',)
#=======
#===製作下次加油累積公里數 
# (temp-score-1.csv -> temp-score-2.csv)
#因為要把下一次加油的公里數取出來 這一次公里數相減 得出 這次加油後 跑了多少公里
in_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-1.csv','r',encoding='utf8',)
line2 = in_temp_file1.readline()
out_temp_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-2.csv','w', encoding = 'utf8')
while line2 != '': #製作 下次加油累積公里數 暫存檔-乾淨狀態
    data2 = line2.split(',')
    sumkm2 = data2[1]  #取出下次加油累積公里數
    out_temp_file2.write('%s' % sumkm2)
    line2 = in_temp_file1.readline()
in_temp_file1.close()
out_temp_file2.close()    
#========================= 
#===製作完整整理過後new score檔 
# (score.txt 
#  temp-score-2.csv -> temp-score-3.csv
#                      temp-score-4.csv
#                      temp-score-5.csv)
in_score_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line3 = in_score_file2.readline()
in_temp_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-2.csv','r', encoding = 'utf8')
line4 = in_temp_file2.readline() #把 下次加油累積公里數 暫存檔 的標頭 先讀取掉 不用
out_temp_file3 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-3.csv','w', encoding = 'utf8')
out_temp_file3_title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
out_temp_file3.write('%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % (out_temp_file3_title[0],out_temp_file3_title[1],out_temp_file3_title[2],out_temp_file3_title[3],out_temp_file3_title[4],out_temp_file3_title[5],out_temp_file3_title[6],out_temp_file3_title[7],out_temp_file3_title[8]))
out_temp_file4 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-4.csv','w', encoding = 'utf8')
out_temp_file4_title = ['year','nowkm','lit','op']
out_temp_file4.write('%s,%s,%s,%s \n' % (out_temp_file4_title[0],out_temp_file4_title[1],out_temp_file4_title[2],out_temp_file4_title[3]))
out_temp_file5 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-5.csv','w', encoding = 'utf8')
while line3 != '':
    data3 = line3.split('-')
    day = data3[0] #取出日期
    day1 = day.split('/')
    year1 = day1[0]
    a = data3[2]   # 取出加油油價與公升數資料
    q = len(a)
    if q > 10:
        b = a.split('/') #分割 加油油價與公升數
        op1 = eval(b[0]) #加油費用 (oil price) 轉成整數
        lit1 = eval(b[1]) #加油公升數 (liter) 轉成整數
        plop1 = eval(b[2])      #每公升油價 (per liter of oil price)
    else:
        b = a.split('/') #分割 加油油價與公升數
        op1 = eval(b[0]) #加油費用 (oil price) 轉成整數
        lit1 = eval(b[1]) #加油公升數 (liter) 轉成整數
        plop1 = op1 / lit1      #每公升油價 (per liter of oil price)        
    line4 = in_temp_file2.readline()    
    if line4 != '':
        nextkm1 = eval(line4) #轉成整數
        sumkm3 = eval(data3[1])  #取出累積公里數
        nowkm1 = nextkm1 - sumkm3 #計算出行駛公里數
        cpk1 = op1 / nowkm1 #算出每公里費用
        oilavg1 = nowkm1 / lit1 #算出油耗
        out_temp_file3.write('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm3,op1,lit1,plop1,nextkm1,nowkm1,oilavg1,cpk1))
        out_temp_file4.write('%s,%s,%s,%s \n' % (year1,nowkm1,lit1,op1))
        out_temp_file5.write('%s,%.2f \n' % (year1,plop1))
    else:
        print()            
    line3 = in_score_file2.readline()
in_score_file2.close()
in_temp_file2.close()
out_temp_file3.close()
out_temp_file4.close()
out_temp_file5.close()
#========================= 
#===製作所需資料合併數字new score檔 
# (temp-score-4.csv -> temp-score-6.csv)
in_temp_csvfile2 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-4.csv', encoding = 'utf8')
out_temp_csvfile2 = in_temp_csvfile2.groupby(['year']).sum() #合併種類的名稱，並且顯示該名稱欄位的所有數量總合
out_temp_csvfile2.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-6.csv',encoding='utf8')
#========================= 
#移除第一行標頭 
# (temp-score-6.csv -> temp-score-7.csv)
csvRows1 = []
in_temp_csvfile3 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-6.csv', 'r' ,encoding='utf8')
csv_reader1 = csv.reader(in_temp_csvfile3)
for row in csv_reader1:
	if csv_reader1.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows1.append(row)
in_temp_csvfile3.close() 
out_tmp_csvfile3  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-7.csv','w', encoding='utf8',newline='')
csv_Writer1 = csv.writer(out_tmp_csvfile3)
for row in csvRows1:
    if any(field.strip() for field in row):
        csv_Writer1.writerow(row)
out_tmp_csvfile3.close()
#=============================================================================
#==算出6年以來所有相關機車維修保養險費用============================================= 
#移除第一行標頭 
# (score-cost.txt -> temp-score-cost.csv)
csvRows1 = []
in_temp_csvfile3 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-cost.txt', 'r' ,encoding='utf8')
csv_reader1 = csv.reader(in_temp_csvfile3)
for row in csv_reader1:
	if csv_reader1.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows1.append(row)
in_temp_csvfile3.close() 
out_tmp_csvfile3  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-cost.csv','w', encoding='utf8',newline='')
csv_Writer1 = csv.writer(out_tmp_csvfile3)
for row in csvRows1:
    if any(field.strip() for field in row):
        csv_Writer1.writerow(row)
out_tmp_csvfile3.close()
#==處理所需資料
# (temp-score-cost.csv -> sumcost)
in_score_file3 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-cost.csv','r', encoding = 'utf8')
line5 = in_score_file3.readline()
sumcost = 0
while line5 != '':
    data4 = line5.split('\n')
    data41 = data4[0]
    data42 = data41.split(',')
    cost = eval(data42[1])
    sumcost += cost
    line5 = in_score_file3.readline()
in_score_file3.close()
print('六年維修保養險費用總計 =',sumcost)
print()
#=============================================================================
#==從政府開放資料-政府行政機關辦公日曆表 取出 每年放假日並算出工作日天數===================
#移除第一行標頭 
# (open-score-day.csv -> temp-open-score-day.csv)
csvRows2 = []
in_temp_csvfile4 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score-day.csv', 'r' ,encoding='utf8')
csv_reader2 = csv.reader(in_temp_csvfile4)
for row in csv_reader2:
	if csv_reader2.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows2.append(row)
in_temp_csvfile4.close()

out_tmp_csvfile4  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day.csv','w', encoding='utf8',newline='')
csv_Writer2 = csv.writer(out_tmp_csvfile4)
for row in csvRows2:
    if any(field.strip() for field in row):
        csv_Writer2.writerow(row)
out_tmp_csvfile4.close()
#========================= 
# 轉換資料格式
# (temp-open-score-day.csv ->temp-open-score-day-1.csv)
in_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day.csv','r',encoding = 'utf8')
line6 = in_score_file1.readline()
out_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day-1.csv','w', encoding = 'utf8')
while line6 != '': 
    data1 = line6.split(',')
    date = data1[0]  
    date = date.split('/')
    year = date[0]
    mon = eval(date[1])
    day = eval(date[2])
    isnot = data1[2] 
    out_temp_file1.write('%s,%s,%s,%s\n' % (year,mon,day,isnot))
    line6 = in_score_file1.readline()
in_score_file1.close()
out_temp_file1.close()

#==將政府資料開放資料 csv to json=========
# (temp-open-score-day-1.csv -> temp-open-score-day-1.json )
csvfile = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day-1.csv','r', encoding = 'utf8')
jsonfile = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day-1.json','w', encoding = 'utf8')
fieldnames = ("year","mon","day","isHoliday")
reader = csv.DictReader(csvfile,fieldnames)
jsonfile.write('[')
for row in reader:
    json.dump(row,jsonfile ,ensure_ascii=False,indent=4) #unicode碼問題
    jsonfile.write(',\n')
jsonfile.seek(jsonfile.tell()-3) #指定位置到最後一行的倒數第3個字元
jsonfile.write("]") #用]取代掉','
csvfile.close()
jsonfile.close()

#============
#計算出每年工作天數
# ( temp-open-score-day-1.json -> 所需資料)
with open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-day-1.json', encoding = 'utf8') as jsonfile:
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
#算出2014與2020佔每年天數
#2014/11/26 ~ 2014/12/31
days2014 = (30-25) + 31 #從11/26開始算 
days2015 = 365
days2016 = 366  #閏年2月有29天
days2017 = 365
days2018 = 365
days2019 = 365
#2020/01/01 ~ 2020/12/31
days2020 = 31+29+31+30+31+30  #閏年2月有29天       
workd1 = days2014 - count1 
workd2 = days2015 - count2
workd3 = days2016 - count3 
workd4 = days2017 - count4
workd5 = days2018 - count5
workd6 = days2019 - count6
workd7 = days2020 - count7 
alldays = days2014 + days2015 + days2016 + days2017 + days2018 + days2019 + days2020
print('2014/11/26 ~ 2014/12/31')
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year1,count1,workd1))
print('2015-01-01 ~ 2015-12-31')
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year2,count2,workd2))
print('2016-01-01 ~ 2016-12-31')
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year3,count3,workd3))
print('2017-01-01 ~ 2017-12-31')
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year4,count4,workd4))  
print('2018-01-01 ~ 2018-12-31')             
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year5,count5,workd5))
print('2019-01-01 ~ 2019-12-31')
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year6,count6,workd6))
print('2020/01/01 ~ 2014/06/30') 
print('%s年,休假日(國定假日+特休) %s 天, 上班日 %s 天' % (year7,count7,workd7))
print()
out_temp_file2.close()
#============================================================================== 
#==取出搭捷運所需要的費用==========================================================
#移除第一行標頭 
# (score-mrtcost.txt -> temp-score-mrtcost.csv)
csvRows2 = []
in_temp_csvfile4 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-mrtcost.txt', 'r' ,encoding='utf8')
csv_reader2 = csv.reader(in_temp_csvfile4)
for row in csv_reader2:
	if csv_reader2.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows2.append(row)
in_temp_csvfile4.close()

out_tmp_csvfile4  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-mrtcost.csv','w', encoding='utf8',newline='')
csv_Writer2 = csv.writer(out_tmp_csvfile4)
for row in csvRows2:
    if any(field.strip() for field in row):
        csv_Writer2.writerow(row)
out_tmp_csvfile4.close()
#==============
#取出並計算數值
# (temp-score-mrtcost.csv -> 所需數值)
in_score_file4 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-mrtcost.csv','r',encoding='utf8')
line7 = in_score_file4.readline()
while line7 != '':
    data5 = line7.split(',')
    mrtyear = eval(data5[0]) #取出日期
    mrtmcost = eval(data5[2]) #取出捷運月票費用
    if mrtyear == 2014:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2014 = mrtmcost * 2 / workd1
    elif mrtyear == 2015:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2015 = mrtmcost * 12 / workd2
    elif mrtyear == 2016:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2016 = mrtmcost * 12 / workd3
    elif mrtyear == 2017:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2017 = mrtmcost * 12 / workd4
    elif mrtyear == 2018:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2018 = mrtmcost * 12 / workd5
    elif mrtyear == 2019:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2019 = mrtmcost * 12 / workd6
    elif mrtyear == 2020:
        mrtdcost = eval(data5[1]) #取出日期
        mrtmdcost2020 = mrtmcost * 6 / workd7
    line7 = in_score_file4.readline()   
print('2014年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2014)
print('2015年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2015)
print('2016年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2016)
print('2017年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2017)
print('2018年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2018)
print('2019年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2019)
print('2020年,捷運月票平均每日費用 %.1f 元' % mrtmdcost2020)
print()
in_score_file4.close()
#==============================================================================
#==算出各項數據分析===================== 
# (temp-score-7.csv -> temp-score-8.csv
#                   -> temp-score-9.csv)
in_score_file5 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-7.csv','r',encoding='utf8')
line8 = in_score_file5.readline()
out_temp_file6 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-8.csv','w', encoding = 'utf8')
out_temp_file7 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-9.csv','w', encoding = 'utf8')
while line8 != '':
    data5 = line8.split(',')
    year2 = eval(data5[0]) #取出日期
    print('年份= %s 年' % year2)
    nowkm2 = eval(data5[1])
    print('年總行駛公里數 = %s 公里' % nowkm2)
    lit2 = eval(data5[2])   # 取出加油油價與公升數資料
    print('年總加油公升數 = %.1f 公升' % lit2)
    op2 = eval(data5[3])
    print('年總加油費用 = %s NTD' % op2)
    oilavg2 = nowkm2 / lit2
    print('平均油耗 = 每公升跑 %.1f 公里' % oilavg2)
    cpk2 = op2 / nowkm2
    print('每公里費用 = %.1f NTD' % cpk2)
    def p(a,b,c,d,e,f,g,h,i,j): 
        ywork = a        #一年上班日
        print('%s年上班天數 = 以 %d 天計算' % (h,ywork))
        motfixcotavg = (sumcost / alldays) * b #36 # 2014/11/26~2020/6/30
        print('%s年平均機車維修保養稅險費用 = %.1f 元' % (h,motfixcotavg))
        km = c #32 #到內湖公司公里數
        print('每天 騎機車 至 %s 上下班公里數 = %d 公里' % (j,km))
        dcost = km * cpk2 #一天油費
        print('每天 騎機車 至 %s 上下班費用 = %.1f 元' % (j,dcost))
        mrt = d * e * 2 #d=40 e=0.8#捷運三民高中站到 捷運西湖站
        print('每天 搭捷運 至 %s 上下班費用 = %d 元' % (j,mrt))
        mrtmdcost = i
        print('每天 搭捷運(月票) 至 %s 上下班省費 = %.1f 元' % (j,mrtmdcost))
        cot = mrt - dcost   #騎機車比搭捷運日省費用
        cot1 = mrtmdcost - dcost #騎機車比搭捷運(月票)日省費用
        print('每天 騎機車 比 搭捷運 至 %s 上下班省費 = %.1f 元' % (j,cot))
        ycot = (cot * ywork - motfixcotavg) #一年省錢
        print('%s年 騎機車 比 搭捷運 至 %s 上下班省費 = %.1f 元' % (h,j,ycot))
        ycot1 = (cot1 * ywork - motfixcotavg) #一年省錢
        print('%s年 騎機車 比 搭捷運(月票) 至 %s 上下班省費 = %.1f 元' % (h,j,ycot1))                
        time = f * 2    #騎車花費時間 #f =50
        print('每天 騎機車 至 %s 上下班花費時間 = %d 分鐘' % (j,time))            
        mtime = g * 2      #走路捷運全程花費時間 #g=80
        print('每天 搭捷運 至 %s 上下班花費時間 = %d 分鐘' % (j,mtime))
        cti = mtime - time  #騎機車比搭捷運日省時
        print('每天 騎機車 比 搭捷運 至 %s 上下班省時 = %d 分鐘' % (j,cti))
        ytime = cti * ywork / 60 #一年省時
        print('%s年 騎機車 比 搭捷運 至 %s 上下班省時 = %.1f 小時' % (h,j,ytime))         
        out_temp_file6.write('%s年,%.1f,%s,%.1f,%.1f,%.1f \n' % (year2,dcost,mrt,mrtmdcost,ycot,ycot1))
        out_temp_file7.write('%s年,%s,%s,%.1f \n' % (year2,time,mtime,ytime))
        print()
    if year2 == 2014:
        print('2014-11-26 ~ 2014-12-31')
        p(workd1,36,32,40,0.8,55,80,2014,mrtmdcost2014,'內湖區') #(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2015:
        print('2015-01-01 ~ 2015-12-31')
        p(workd2,365,32,40,0.8,55,80,2015,mrtmdcost2015,'內湖區')
    elif year2 == 2016:
        print('2016-01-01 ~ 2016-12-31')
        p(workd3,365,32,40,0.8,55,80,2016,mrtmdcost2016,'內湖區')
    elif year2 == 2017:
        print('2017-01-01 ~ 2017-12-31')
        p(workd4,365,26,35,0.8,50,70,2017,mrtmdcost2017,'信義區')
    elif year2 == 2018:
        print('2018-01-01 ~ 2018-12-31')
        p(workd5,365,26,35,0.8,50,70,2018,mrtmdcost2018,'信義區')
    elif year2 == 2019:
        print('2019-01-01 ~ 2019-12-31')
        p(workd6,365,26,35,0.8,50,70,2019,mrtmdcost2019,'信義區')
    elif year2 == 2020:
        print('2020-01-01 ~ 2020-06-30')
        p(workd7,182,30,30,1,40,60,2020,mrtmdcost2020,'忠孝敦化')
    line8 = in_score_file5.readline()   
in_score_file5.close()
out_temp_file6.close()
out_temp_file7.close()
#=============================================================================
#==中國石油open score 公告歷史油價，取出95無鉛汽油 並比對 自我紀錄機車加油資料============
# (open-score.csv -> temp-open-score.csv)
in_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score.csv','r', encoding = 'utf8')
line9 = in_open_score_file1.readline()
out_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score.csv','w', encoding = 'utf8')
while line9 != '':
    data6 = line9.split(',')
    day2 = data6[0] #取出調價日期
    oil95 = (data6[2])  #取出公告95無鉛汽油價格
    if oil95 != '':
        out_open_score_file1.write('%s,%s \n' % (day2,oil95))
    line9 = in_open_score_file1.readline()
out_open_score_file1.close()
out_open_score_file1.close()
#=======
#移除第一行標頭 csv -> csv
# (temp-open-score.csv -> temp-open-score-1.csv)
csvRows3 = []
in_temp_csvfile5 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score.csv', 'r' ,encoding='utf8')
csv_reader3 = csv.reader(in_temp_csvfile5)
for row in csv_reader3:
	if csv_reader3.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows3.append(row)
in_temp_csvfile5.close()

out_tmp_csvfile5  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-1.csv','w', encoding='utf8',newline='')
csv_Writer3 = csv.writer(out_tmp_csvfile5)
for row in csvRows3:
    if any(field.strip() for field in row):
        csv_Writer3.writerow(row)
out_tmp_csvfile5.close()
#========================= 
#依年份取出
#(temp-open-score-1.csv -> temp-open-score-2.csv )
in_open_score_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-1.csv', 'r' ,encoding='utf8')
line10 = in_open_score_file2.readline()
out_temp_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-2.csv', 'w' ,encoding='utf8')
while line10 != '':
    data7 = line10.split(',')
    data8 = data7[0].split('/')
    data9 = data7[1]
    year3 = eval(data8[0])  #取出調價日期的日
    out_temp_open_score_file1.write('%s,%s' % (year3,data9))
    line10 = in_open_score_file2.readline()
in_open_score_file2.close()
out_temp_open_score_file1.close()
#=============================================================================
#==繪製分析圖表==================================================================
#95無鉛汽油歷史公告油價(綠) 與 自我加油油價(紅) 比較表-散佈圖
colName3 = ['年度', '95無鉛汽油油價']
oil = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-5.csv', names = colName3)
colName4 = ['年度', '95無鉛汽油油價']
oil1 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-2.csv', names = colName4)
plt.plot(oil['年度'], oil['95無鉛汽油油價'], '^', color = 'r')
plt.plot(oil1['年度'], oil1['95無鉛汽油油價'], '*', color = 'g',alpha = 0.3)
plt.xlabel('年度')
plt.ylabel('95無鉛汽油油價')
plt.title('95無鉛汽油歷史公告油價(綠) 與 自我加油油價(紅) 比較表')
plt.show()

#=======================
#騎機車與坐捷運上下班費用比較表-費用圖
colName1 = ['年度','騎機車每日費用','坐捷運每日費用','坐捷運(月票)每日費用','每年節省費用','每年節省費用(月票)']
cost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-8.csv', names = colName1)
cost.set_index("年度" , inplace=True)
fig, ax = plt.subplots()
fig.suptitle('騎機車與坐捷運上下班費用比較表')
ax.set_ylabel('每年節省費用')
ax.set_xlabel('年度')
ax2 = ax.twinx()
ax2.set_ylabel('每日費用')
cost['每年節省費用(月票)'].plot(ax = ax, rot = 0,kind = 'bar',color = 'y',stacked = True)
cost['每年節省費用'].plot(ax = ax, rot = 0,kind = 'bar',stacked = True)
cost['騎機車每日費用'].plot(ax = ax2, style = 'r-*')
cost['坐捷運每日費用'].plot(ax = ax2, style = 'g-*')
cost['坐捷運(月票)每日費用'].plot(ax = ax2, style = 'b-*')
ax.legend(loc=2,facecolor='none')
ax2.legend(loc=1,facecolor='none')
plt.show()

#=======================
#騎機車與坐捷運上下班費時比較表-時間圖
colName2 = ['年度','騎機車每日費時(分)','坐捷運每日費時(分)','每年節省時間(時)']
time = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-9.csv', names = colName2)
time.set_index("年度" , inplace=True)
fig, ax = plt.subplots()
fig.suptitle('騎機車與坐捷運上下班費時比較表')
ax.set_ylabel('每年節省時間(時)')
ax.set_xlabel('年度')
ax2 = ax.twinx()
ax2.set_ylabel('每日費時')
time['每年節省時間(時)'].plot(ax = ax, rot = 0,kind = 'bar')
time['騎機車每日費時(分)'].plot(ax = ax2, style = 'r-*')
time['坐捷運每日費時(分)'].plot(ax = ax2, style = 'g-*')
ax.legend(loc = 1)
ax2.legend(loc = 6)
plt.show()

#=============================================================================

































