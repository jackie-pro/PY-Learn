# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:25:20 2020

@author: Jackie
"""
#===============================
#1.處理原始資料
def main():
    #import csv
    import pandas as pd
    
    infile1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
    line1 = infile1.readline()
    tempfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp.txt','w', encoding = 'utf8')
    title1 = ['下次加油累積公里數']
    tempfile.write('%s \n' % title1[0])
    while line1 != '': #製作 下次加油累積公里數 暫存檔
        print(line1)
        data1 = line1.split('-')
        print('data1 = ',data1)
        sumkm1 = eval(data1[1])  #取出下次加油累積公里數
        print('下次加油累積公里數 = ',sumkm1)
        tempfile.write('%s \n' % sumkm1)
        line1 = infile1.readline()
    infile1.close()
    tempfile.close()  
    df = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp.txt',encoding = 'utf8')
    print(df)
    df1 = df.drop(df.index[0]) #去掉第一個
    print(df1)
    df1.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp1.txt',encoding='utf8',)
    df2 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp1.txt','r',encoding='utf8',)
    line2 = df2.readline()
    temp2file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp2.txt','w', encoding = 'utf8')
    while line2 != '': #製作 下次加油累積公里數 暫存檔-乾淨狀態
        print(line2)
        data2 = line2.split(',')
        print('data2 = ',data2)
        sumkm2 = data2[1]  #取出下次加油累積公里數
        print('下次加油累積公里數 = ',sumkm2)
        temp2file.write('%s' % sumkm2)
        line2 = df2.readline()
    df2.close()
    temp2file.close()    
    infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score.txt','r',encoding = 'utf8')
    line = infile.readline()
    outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-1.txt','w', encoding = 'utf8')
    out1file = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2.csv','w', encoding = 'utf8')
    df3 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-temp2.txt','r', encoding = 'utf8')
    line3 = df3.readline() #把 下次加油累積公里數 暫存檔 的標頭 先讀取掉 不用
    title = ['加油日期','累積公里數','加油費用','加油公升數','95無鉛汽油油價','下次加油累積公里數','行駛公里數','油耗','每公里費用']
    outfile.write('%s,%s,%s,%s,%s,%s,%s,%s,%s \n' % (title[0],title[1],title[2],title[3],title[4],title[5],title[6],title[7],title[8]))
    title2 = ['year','nowkm','lit','op']
    out1file.write('%s,%s,%s,%s \n' % (title2[0],title2[1],title2[2],title2[3]))
    while line != '':
        print(line)
        data = line.split('-')
        print('data = ',data)
        day = data[0] #取出日期
        print('加油日期 = ',day)
        day1 = day.split('/')
        year = day1[0]
        print('年分 = ',year)
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
        line3 = df3.readline()
        if line3 != '':
            nextkm = eval(line3) #轉成整數
            print('下次加油累積公里數 = ', nextkm)
            sumkm = eval(data[1])  #取出累積公里數
            print('累積公里數 = ',sumkm)
            nowkm = nextkm - sumkm #計算出行駛公里數
            print('行駛公里數 = ', nowkm)
            cpk = op / nowkm #算出每公里費用
            print('每公里費用 = %.2f' % cpk)
            oilavg = nowkm / lit #算出油耗
            print('油耗 = %.2f' % oilavg)
            print('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm,op,lit,plop,nextkm,nowkm,oilavg,cpk))
            outfile.write('%s,%s,%s,%s,%.2f,%s,%s,%.2f,%.2f \n' % (day,sumkm,op,lit,plop,nextkm,nowkm,oilavg,cpk))
            print('%s,%s,%s,%s \n' % (year,nowkm,lit,op))
            out1file.write('%s,%s,%s,%s \n' % (year,nowkm,lit,op))
        else:
            print()
            
        line = infile.readline()
    infile.close()
    outfile.close()
    out1file.close()
    df3.close()
    
main()

#=======================
#2.合併數字
import csv
import pandas as pd
csvfile = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2.csv', encoding = 'utf8')
csvsum = csvfile.groupby(['year']).sum() #合併種類的名稱，並且顯示該名稱欄位的所有數量總合
csvsum.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2-temp.csv',encoding='utf8',)
print(csvsum)

csvRows = []
csvFileObj = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2-temp.csv', 'r' ,encoding='utf8')
readerObj = csv.reader(csvFileObj)
for row in readerObj:
	if readerObj.line_num == 1:
		continue	# skip first row
	csvRows.append(row)
csvFileObj.close()
 
csvFileObj1  = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.csv','w', encoding='utf8',newline='')
csvWriter = csv.writer(csvFileObj1)
for row in csvRows:
    if any(field.strip() for field in row):
        csvWriter.writerow(row)
csvFileObj.close()
csvFileObj1.close()
#=======================
#3.處理所需資料
#====================
infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.csv',encoding='utf8')
line = infile.readline()
outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt','w', encoding = 'utf8')
outfile1 = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-4.txt','w', encoding = 'utf8')
#==算出6年以來所有相關機車維修保養險費用
sumfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-cost.txt','r', encoding = 'utf8')
linea = sumfile.readline()
sumcost = 0
while linea != '':
    print(linea)
    data = linea.split('/n')
    print('data = ',data)
    cost = eval(data[0])
    sumcost += cost
    linea = sumfile.readline()
sumfile.close()
print('六年維修保養險費用總計 =',sumcost)
#====================
while line != '':
    data1 = line.split(',')
    year = eval(data1[0]) #取出日期
    print('年份= %s 年' % year)
    nowkm = eval(data1[1])
    print('年總行駛公里數 = %s 公里' % nowkm)
    lit = eval(data1[2])   # 取出加油油價與公升數資料
    print('年總加油公升數 = %.1f 公升' % lit)
    op = eval(data1[3])
    print('年總加油費用 = %s NTD' % op)
    oilavg = nowkm / lit
    print('平均油耗 = 每公升跑 %.1f 公里' % oilavg)
    cpk = op / nowkm
    print('每公里費用 = %.1f NTD' % cpk)
    def p(a,b,c,d,e,f,g,h): 
        ywork = a #20       #一年預計上班日20天
        print('%s年上班天數 = 以 %d 天計算' % (h,ywork))
        motfixcotavg = (sumcost / 2043) * b #36 
        print('%s年平均機車維修保養稅險費用 = %.1f 元' % (h,motfixcotavg))
        km = c #32 #到內湖公司公里數
        print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
        dcost = km * cpk #一天油費
        print('每天 騎機車 至 內湖區 上下班費用 = %.1f 元' % dcost)
        mrt = d * e * 2 #d=40 e=0.8#捷運三民高中站到 捷運西湖站
        print('每天 搭捷運 至 內湖區 上下班費用 = %d 元' % mrt)
        cot = mrt - dcost   #騎機車比搭捷運日省費用
        print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f 元' % cot)
        ycot = (cot * ywork - motfixcotavg) #一年省錢(單位百)
        print('%s年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f 元' % (h,ycot))            
        time = f * 2    #騎車花費時間 #f =50
        print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)            
        mtime = g * 2      #走路捷運全程花費時間 #g=80
        print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
        cti = mtime - time  #騎機車比搭捷運日省時
        print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
        ytime = cti * ywork / 60 #一年省時
        print('%s年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % (h,ytime))         
        outfile.write('%s年,%.1f,%s,%.1f \n' % (year,dcost,mrt,ycot))
        print('%s年,%.1f,%s,%.1f \n' % (year,dcost,mrt,ycot))
        outfile1.write('%s年,%s,%s,%.1f \n' % (year,time,mtime,ytime))
        print('%s年,%s,%s,%.1f \n' % (year,time,mtime,ytime))
    if year == 2014:
        print('2014-11-26 ~ 2014-12-31')
        p(20,36,32,40,0.8,55,80,2014) 
    elif year == 2015:
        print('2015-01-01 ~ 2015-12-31')
        p(200,365,32,40,0.8,55,80,2015) 
    elif year == 2016:
        print('2016-01-01 ~ 2016-12-31')
        p(200,365,32,40,0.8,55,80,2016)
    elif year == 2017:
        print('2017-01-01 ~ 2017-12-31')
        p(200,365,26,35,0.8,50,70,2017)
    elif year == 2018:
        print('2018-01-01 ~ 2018-12-31')
        p(200,365,26,35,0.8,50,70,2018)
    elif year == 2019:
        print('2019-01-01 ~ 2019-12-31')
        p(200,365,26,35,0.8,50,70,2019)
    elif year == 2020:
        print('2020-01-01 ~ 2020-06-30')
        p(100,182,30,30,1,40,60,2020)
    line = infile.readline()   
infile.close()
outfile.close()
outfile1.close()
#=======================

#=======================

#=======================

#=======================
#費用圖
import pandas as pd  
import matplotlib.pyplot as plt

font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
plt.rc('axes',unicode_minus=False) #解決坐標軸負數的-號顯示問題

colName = ['年度','騎機車每日費用','坐捷運每日費用','每年節省費用']
cost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt', names = colName)
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
#時間圖
import pandas as pd  
import matplotlib.pyplot as plt

font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
plt.rc('axes',unicode_minus=False) #解決坐標軸負數的-號顯示問題

colName = ['年度','騎機車每日費時(分)','坐捷運每日費時(分)','每年節省時間(時)']
cost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-4.txt', names = colName)
cost.set_index("年度" , inplace=True)
fig, ax = plt.subplots()
fig.suptitle('騎機車與坐捷運上下班費時比較表')
ax.set_ylabel('每年節省時間(時)')
ax.set_xlabel('年度')
ax2 = ax.twinx()
ax2.set_ylabel('每日費時')
cost['每年節省時間(時)'].plot(ax = ax, rot = 0,kind = 'bar')
cost['騎機車每日費時(分)'].plot(ax = ax2, style = 'r-')
cost['坐捷運每日費時(分)'].plot(ax = ax2, style = 'g-')
ax.legend(loc = 1)
ax2.legend(loc = 6)

plt.show()


#======================
import csv
  

 