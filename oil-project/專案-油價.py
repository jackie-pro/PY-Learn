# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:25:52 2020
程式設計工程師專班 洪孝承 17號
@author: jackie Hung
"""
#==導入所需函式庫===
import csv
import pandas as pd
import matplotlib.pyplot as plt
#==處理中文字型問題===
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
plt.rc('axes',unicode_minus=False) #解決坐標軸負數的-號顯示問題
#==自我紀錄機車加油資料======
#===製作下次加油累積公里數-暫存檔 txt -> txt
# (score.txt -> temp-score.txt) 
in_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line1 = in_score_file1.readline()
out_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score.txt','w', encoding = 'utf8')
out_temp_file1_title = ['下次加油累積公里數']
out_temp_file1.write('%s \n' % out_temp_file1_title[0])
while line1 != '': #製作 下次加油累積公里數 暫存檔
    print(line1)
    data1 = line1.split('-')
    print('data1 = ',data1)
    sumkm1 = eval(data1[1])  #取出下次加油累積公里數
    print('下次加油累積公里數 = ',sumkm1)
    out_temp_file1.write('%s \n' % sumkm1)
    line1 = in_score_file1.readline()
in_score_file1.close()
out_temp_file1.close()
#========================= 

#=======
#移除第一行標頭 txt -> txt
# (temp-score.txt -> temp-score-1.txt)
in_temp_csvfile1 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score.txt',encoding = 'utf8')
print(in_temp_csvfile1)
out_tmp_csvfile1 = in_temp_csvfile1.drop(in_temp_csvfile1.index[0]) #去掉第一個
print(out_tmp_csvfile1)
out_tmp_csvfile1.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-1.txt',encoding='utf8',)
#=======
#===製作下次加油累積公里數 txt -> txt
# (temp-score-1.txt -> temp-score-2.txt)
#因為要把下一次加油的公里數取出來 這一次公里數相減 得出 這次加油後 跑了多少公里
in_temp_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-1.txt','r',encoding='utf8',)
line2 = in_temp_file1.readline()
out_temp_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-2.txt','w', encoding = 'utf8')
while line2 != '': #製作 下次加油累積公里數 暫存檔-乾淨狀態
    print(line2)
    data2 = line2.split(',')
    print('data2 = ',data2)
    sumkm2 = data2[1]  #取出下次加油累積公里數
    print('下次加油累積公里數 = ',sumkm2)
    out_temp_file2.write('%s' % sumkm2)
    line2 = in_temp_file1.readline()
in_temp_file1.close()
out_temp_file2.close()    
#========================= 
#===製作完整整理過後new score檔 txt -> txt -> csv
# (score.txt -> temp-score-3.txt 
#            -> temp-score-4.csv)
in_score_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
line3 = in_score_file2.readline()
in_temp_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-2.txt','r', encoding = 'utf8')
line4 = in_temp_file2.readline() #把 下次加油累積公里數 暫存檔 的標頭 先讀取掉 不用
out_temp_file3 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-3.txt','w', encoding = 'utf8')
out_temp_file3_title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
out_temp_file3.write('%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % (out_temp_file3_title[0],out_temp_file3_title[1],out_temp_file3_title[2],out_temp_file3_title[3],out_temp_file3_title[4],out_temp_file3_title[5],out_temp_file3_title[6],out_temp_file3_title[7],out_temp_file3_title[8]))
out_temp_file4 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-4.csv','w', encoding = 'utf8')
out_temp_file4_title = ['year','nowkm','lit','op']
out_temp_file4.write('%s,%s,%s,%s \n' % (out_temp_file4_title[0],out_temp_file4_title[1],out_temp_file4_title[2],out_temp_file4_title[3]))
out_temp_file5 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-5.csv','w', encoding = 'utf8')
while line3 != '':
    print(line3)
    data3 = line3.split('-')
    print('data3 = ',data3)
    day = data3[0] #取出日期
    print('加油日期 = ',day)
    day1 = day.split('/')
    year1 = day1[0]
    print('年分 = ',year1)
    a = data3[2]   # 取出加油油價與公升數資料
    print('a = ',a)
    q = len(a)
    print('q = ',q)
    if q > 10:
        b = a.split('/') #分割 加油油價與公升數
        print('b = ',b)
        op1 = eval(b[0]) #加油費用 (oil price) 轉成整數
        print('加油費用 = ',op1)
        lit1 = eval(b[1]) #加油公升數 (liter) 轉成整數
        print('加油公升數 = ',lit1)
        plop1 = eval(b[2])      #每公升油價 (per liter of oil price)
        print('每公升油價 = %.2f' % plop1)
    else:
        b = a.split('/') #分割 加油油價與公升數
        print('b = ',b)
        op1 = eval(b[0]) #加油費用 (oil price) 轉成整數
        print('加油費用 = ',op1)
        lit1 = eval(b[1]) #加油公升數 (liter) 轉成整數
        print('加油公升數 = ',lit1)
        plop1 = op1 / lit1      #每公升油價 (per liter of oil price)
        print('每公升油價 = %.2f' % plop1)
        
    line4 = in_temp_file2.readline()
    
    if line4 != '':
        nextkm1 = eval(line4) #轉成整數
        print('下次加油累積公里數 = ', nextkm1)
        sumkm3 = eval(data3[1])  #取出累積公里數
        print('累積公里數 = ',sumkm3)
        nowkm1 = nextkm1 - sumkm3 #計算出行駛公里數
        print('行駛公里數 = ', nowkm1)
        cpk1 = op1 / nowkm1 #算出每公里費用
        print('每公里費用 = %.2f' % cpk1)
        oilavg1 = nowkm1 / lit1 #算出油耗
        print('油耗 = %.2f' % oilavg1)
        out_temp_file3.write('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm3,op1,lit1,plop1,nextkm1,nowkm1,oilavg1,cpk1))
        print('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm3,op1,lit1,plop1,nextkm1,nowkm1,oilavg1,cpk1))
        out_temp_file4.write('%s,%s,%s,%s \n' % (year1,nowkm1,lit1,op1))
        print('%s,%s,%s,%s \n' % (year1,nowkm1,lit1,op1))
        out_temp_file5.write('%s,%.2f \n' % (year1,plop1))
        print('%s,%.2f \n' % (year1,plop1))
    else:
        print()
            
    line3 = in_score_file2.readline()
in_score_file2.close()
in_temp_file2.close()
out_temp_file3.close()
out_temp_file4.close()
out_temp_file5.close()
#========================= 
#===製作所需資料合併數字new score檔 csv -> csv
# (temp-score-4.csv -> temp-score-6.csv)
in_temp_csvfile2 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-4.csv', encoding = 'utf8')
out_temp_csvfile2 = in_temp_csvfile2.groupby(['year']).sum() #合併種類的名稱，並且顯示該名稱欄位的所有數量總合
out_temp_csvfile2.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-6.csv',encoding='utf8',)
print(out_temp_csvfile2)
#=======
#移除第一行標頭 txt -> txt
# (score-cost.txt -> temp-score-cost.txt)
csvRows1 = []
in_temp_csvfile3 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-cost.txt', 'r' ,encoding='utf8')
csv_reader1 = csv.reader(in_temp_csvfile3)
for row in csv_reader1:
	if csv_reader1.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows1.append(row)
in_temp_csvfile3.close()
 
out_tmp_csvfile3  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-cost.txt','w', encoding='utf8',newline='')
csv_Writer1 = csv.writer(out_tmp_csvfile3)
for row in csvRows1:
    if any(field.strip() for field in row):
        csv_Writer1.writerow(row)
out_tmp_csvfile3.close()
#========================= 
#==處理所需資料 txt -> txt
#算出6年以來所有相關機車維修保養險費用
# (temp-score-cost.txt -> sumcost)
in_score_file3 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-cost.txt','r', encoding = 'utf8')
line5 = in_score_file3.readline()
sumcost = 0
while line5 != '':
    print(line5)
    data4 = line5.split('/n')
    print('data4 = ',data4)
    cost = eval(data4[0])
    sumcost += cost
    line5 = in_score_file3.readline()
in_score_file3.close()
print('六年維修保養險費用總計 =',sumcost)
#====================
#=======
#移除第一行標頭 csv -> csv
# (temp-score-6.csv -> temp-score-7.csv)
csvRows2 = []
in_temp_csvfile4 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-6.csv', 'r' ,encoding='utf8')
csv_reader2 = csv.reader(in_temp_csvfile4)
for row in csv_reader2:
	if csv_reader2.line_num == 1:
		continue	# 停止第一行的讀取
	csvRows2.append(row)
in_temp_csvfile4.close()

out_tmp_csvfile4  = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-7.csv','w', encoding='utf8',newline='')
csv_Writer2 = csv.writer(out_tmp_csvfile4)
for row in csvRows2:
    if any(field.strip() for field in row):
        csv_Writer2.writerow(row)
out_tmp_csvfile4.close()
#========================= 
# (temp-score-7.csv -> temp-score-8.txt
#                 -> temp-score-9.txt)
in_score_file4 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-7.csv','r',encoding='utf8')
line6 = in_score_file4.readline()
out_temp_file6 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-8.txt','w', encoding = 'utf8')
out_temp_file7 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-9.txt','w', encoding = 'utf8')
while line6 != '':
    data5 = line6.split(',')
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
    def p(a,b,c,d,e,f,g,h): 
        ywork = a #20       #一年預計上班日20天
        print('%s年上班天數 = 以 %d 天計算' % (h,ywork))
        motfixcotavg = (sumcost / 2043) * b #36 
        print('%s年平均機車維修保養稅險費用 = %.1f 元' % (h,motfixcotavg))
        km = c #32 #到內湖公司公里數
        print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
        dcost = km * cpk2 #一天油費
        print('每天 騎機車 至 內湖區 上下班費用 = %.1f 元' % dcost)
        mrt = d * e * 2 #d=40 e=0.8#捷運三民高中站到 捷運西湖站
        print('每天 搭捷運 至 內湖區 上下班費用 = %d 元' % mrt)
        cot = mrt - dcost   #騎機車比搭捷運日省費用
        print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f 元' % cot)
        ycot = (cot * ywork - motfixcotavg) #一年省錢
        print('%s年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f 元' % (h,ycot))            
        time = f * 2    #騎車花費時間 #f =50
        print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)            
        mtime = g * 2      #走路捷運全程花費時間 #g=80
        print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
        cti = mtime - time  #騎機車比搭捷運日省時
        print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
        ytime = cti * ywork / 60 #一年省時
        print('%s年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % (h,ytime))         
        out_temp_file6.write('%s年,%.1f,%s,%.1f \n' % (year2,dcost,mrt,ycot))
        print('%s年,%.1f,%s,%.1f \n' % (year2,dcost,mrt,ycot))
        out_temp_file7.write('%s年,%s,%s,%.1f \n' % (year2,time,mtime,ytime))
        print('%s年,%s,%s,%.1f \n' % (year2,time,mtime,ytime))
    if year2 == 2014:
        print('2014-11-26 ~ 2014-12-31')
        p(20,36,32,40,0.8,55,80,2014) #(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2015:
        print('2015-01-01 ~ 2015-12-31')
        p(200,365,32,40,0.8,55,80,2015) #(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2016:
        print('2016-01-01 ~ 2016-12-31')
        p(200,365,32,40,0.8,55,80,2016)#(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2017:
        print('2017-01-01 ~ 2017-12-31')
        p(200,365,26,35,0.8,50,70,2017)#(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2018:
        print('2018-01-01 ~ 2018-12-31')
        p(200,365,26,35,0.8,50,70,2018)#(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2019:
        print('2019-01-01 ~ 2019-12-31')
        p(200,365,26,35,0.8,50,70,2019)#(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    elif year2 == 2020:
        print('2020-01-01 ~ 2020-06-30')
        p(100,182,30,30,1,40,60,2020)#(工作日數,年佔日數,騎車距離,捷運費用,遊遊卡打折,騎車費時,坐捷運費時,年度)
    line6 = in_score_file4.readline()   
in_score_file4.close()
out_temp_file6.close()
out_temp_file7.close()
#==中國石油open score 公告歷史油價，取出95無鉛汽油 並比對 自我紀錄機車加油資料======================
in_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\open-score.csv','r', encoding = 'utf8')
line7 = in_open_score_file1.readline()
out_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score.csv','w', encoding = 'utf8')
while line7 != '':
    data6 = line7.split(',')
    day2 = data6[0] #取出調價日期
    oil95 = (data6[2])  #取出公告95無鉛汽油價格
    if oil95 != '':
        print('data6 = ',data6)
        print('調價日期 = ',day2)
        print('公告95無鉛汽油價格 = ',oil95)
        out_open_score_file1.write('%s,%s \n' % (day2,oil95))
        print('%s,%s \n' % (day2,oil95))
    line7 = in_open_score_file1.readline()
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
in_open_score_file2 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score-1.csv', 'r' ,encoding='utf8')
line8 = in_open_score_file2.readline()
out_temp_open_score_file1 = open(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score.csv', 'w' ,encoding='utf8')
while line8 != '':
    print(line8)
    data7 = line8.split(',')
    print(data7)
    data8 = data7[0].split('/')
    print(data8)
    data9 = data7[1]
    print(data9)
    year3 = eval(data8[0])  #取出調價日期的日
    print(year3)
    out_temp_open_score_file1.write('%s,%s' % (year3,data9))
    print('%s,%s' % (year3,data9))
    line8 = in_open_score_file2.readline()
in_open_score_file2.close()
out_temp_open_score_file1.close()
#========================= 

#==繪製圖表==================
#95無鉛汽油歷史公告油價(綠) 與 自我加油油價(紅) 比較表-散點圖

colName3 = ['年度', '95無鉛汽油油價']
oil = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-5.csv', names = colName3)
colName4 = ['年度', '95無鉛汽油油價']
oil1 = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-open-score.csv', names = colName4)


plt.plot(oil['年度'], oil['95無鉛汽油油價'], '^', color = 'r')
plt.plot(oil1['年度'], oil1['95無鉛汽油油價'], '*', color = 'g',alpha = 0.3)
plt.xlabel('年度')
plt.ylabel('95無鉛汽油油價')
plt.title('95無鉛汽油歷史公告油價(綠) 與 自我加油油價(紅) 比較表')

plt.show()

#=======================
#騎機車與坐捷運上下班費用比較表-費用圖

colName1 = ['年度','騎機車每日費用','坐捷運每日費用','每年節省費用']
cost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-8.txt', names = colName1)
cost.set_index("年度" , inplace=True)
fig, ax = plt.subplots()
fig.suptitle('騎機車與坐捷運上下班費用比較表')
ax.set_ylabel('每年節省費用')
ax.set_xlabel('年度')
ax2 = ax.twinx()
ax2.set_ylabel('每日費用')
cost['每年節省費用'].plot(ax = ax, rot = 0,kind = 'bar')
cost['騎機車每日費用'].plot(ax = ax2, style = 'r-')
cost['坐捷運每日費用'].plot(ax = ax2, style = 'g-')
ax.legend(loc = 1)
ax2.legend(loc = 6)

plt.show()

#=======================
#騎機車與坐捷運上下班費時比較表-時間圖

colName2 = ['年度','騎機車每日費時(分)','坐捷運每日費時(分)','每年節省時間(時)']
time = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\temp-score-9.txt', names = colName2)
time.set_index("年度" , inplace=True)
fig, ax = plt.subplots()
fig.suptitle('騎機車與坐捷運上下班費時比較表')
ax.set_ylabel('每年節省時間(時)')
ax.set_xlabel('年度')
ax2 = ax.twinx()
ax2.set_ylabel('每日費時')
time['每年節省時間(時)'].plot(ax = ax, rot = 0,kind = 'bar')
time['騎機車每日費時(分)'].plot(ax = ax2, style = 'r-')
time['坐捷運每日費時(分)'].plot(ax = ax2, style = 'g-')
ax.legend(loc = 1)
ax2.legend(loc = 6)

plt.show()

#=======================

































