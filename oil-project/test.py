# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:25:20 2020

@author: Jackie
"""


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
import csv
import pandas as pd
csvfile = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-2.csv', encoding = 'utf8')

while line != '':
dfTotal=csvfile.groupby(['year']).sum() 
#合併種類的名稱，並且顯示該名稱欄位的所有數量總合
#dfTotal.sum() 
print(dfTotal)
dfTotal.to_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.csv',encoding='utf8',)
#=======================
#=======================
#import csv
#import pandas as pd
sumfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-cost.txt','r', encoding = 'utf8')
line = sumfile.readline()
sumcost = 0
while line != '':
    print(line)
    data = line.split('\n')
    print('data = ',data)
    cost = eval(data[0])
    sumcost += cost
    line = sumfile.readline()
sumfile.close()
yavgcost = sumcost / 6
print ('六年總計 =',sumcost)
print ('一年平均 = %d' % yavgcost)


#=======================


infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.csv',encoding='utf8',)
line = infile.readline()
outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt','w', encoding = 'utf8')
while line != '':
        #print(line)
        data = line.split(',')
        #print('data = ',data)
        year = eval(data[0]) #取出日期
        print('加油年份= %s 年' % year)
        nowkm = eval(data[1])
        print('年總行駛公里數 = %s 公里' % nowkm)
        lit = eval(data[2])   # 取出加油油價與公升數資料
        print('年總加油公升數 = %.1f 公升' % lit)
        op = eval(data[3])
        print('年總加油費用 = %s NTD' % op)
        oilavg = nowkm / lit
        print('平均油耗 = 每公升跑 %.1f 公里' % oilavg)
        cpk = op / nowkm
        print('每公里費用 = %.1f NTD' % cpk)
        motfixcotavg = 23,218 / 6#
        print('平均6年多來機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
        if year >= 2014 and year <= 2016:
            km = 32 #到內湖公司公里數
            print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 內湖區 上下班費用 = %.1f NTD' % dcost)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)
            mrt = 40 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 內湖區 上下班費用 = %d NTD' % mrt)
            mtime = 80 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
            cot = mrt - dcost   #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % cot)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
            ywork = 200       #一年預計上班日200天
            print('一年上班天數 = 以 %d 天計算' % ywork)
            ycot = cot * ywork #一年省錢
            print('每年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % ycot)
            ytime = cti * ywork / 60 #一年省時
            print('每年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % ytime)
        elif year >= 2017 and year <= 2019:
            km = 26 #到信義公司公里數
            print('每天 騎機車 至 信義區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 信義區 上下班費用 = %.1f NTD' % dcost)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 信義區 上下班花費時間 = %d 分鐘' % time)
            mrt = 35 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 信義區 上下班費用 = %d NTD' % mrt)
            mtime = 70 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 信義區 上下班花費時間 = %d 分鐘' % mtime)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % cot)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省時 = %d 分鐘' % cti)
            ywork = 200       #一年預計上班日200天
            print('一年上班天數 = 以 %d 天計算' % ywork)
            ycot = cot * ywork #一年省錢
            print('每年 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % ycot)
            ytime = cti * ywork /60 #一年省時
            print('每年 騎機車 比 搭捷運 至 信義區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2020:
            km = 30 #到忠孝上課公里數
            print('每天 騎機車 至 忠孝聯成 上下課公里數 = %d公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 忠孝聯成 上下課費用 = %.1f NTD' % dcost)
            time = 40 * 2    #騎車花費時間
            print('每天 騎機車 至 忠孝聯成 上下課花費時間 = %d 分鐘' % time)
            mrt = 30 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 忠孝聯成 上下課費用 = %d NTD' % mrt)
            mtime = 60 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 忠孝聯成 上下課花費時間 = %d 分鐘' % mtime)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 忠孝聯成 上下課省費 = %.1f NTD' % cot)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 忠孝聯成 上下課省時 = %d 分鐘' % cti)
            ywork = 200       #一年預計上班日200天
            print('一年上班天數 = 以 %d 天計算' % ywork)
            ycot = cot * ywork #一年省錢
            print('每年 騎機車 比 搭捷運 至 忠孝聯成 上下課省費 = %.1f NTD' % ycot)
            ytime = cti * ywork / 60 #一年省時
            print('每年 騎機車 比 搭捷運 至 忠孝聯成 上下課省時 = %.1f 小時' % ytime)
        line = infile.readline()
        #print('%s,%s,%.2f,%s,%.2f,%.2f,%.2f,%s,%s,%s,%.2f,%s,%.2f,%.2f \n' % (year,nowkm,lit,op,oilavg,cpk,dcost,time,mrt,mtime,cot,cti,ycot,ytime))
        #outfile.write('%s,%s,%.2f,%s,%.2f,%.2f,%.2f,%s,%s,%s,%.2f,%s,%.2f,%.2f \n' % (year,nowkm,lit,op,oilavg,cpk,dcost,time,mrt,mtime,cot,cti,ycot,ytime))
        #print('%.2f,%.2f,%s \n' % (ycot,ytime,year))
        print()
        outfile.write('%.1f,%.1f,%s \n' % (ycot,ytime,year))
infile.close()
outfile.close()
#=======================
infile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.csv',encoding='utf8',)
line = infile.readline()
outfile = open(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt','w', encoding = 'utf8')
while line != '':
        data = line.split(',')
        year = eval(data[0]) #取出日期
        print('年份= %s 年' % year)
        nowkm = eval(data[1])
        print('年總行駛公里數 = %s 公里' % nowkm)
        lit = eval(data[2])   # 取出加油油價與公升數資料
        print('年總加油公升數 = %.1f 公升' % lit)
        op = eval(data[3])
        print('年總加油費用 = %s NTD' % op)
        oilavg = nowkm / lit
        print('平均油耗 = 每公升跑 %.1f 公里' % oilavg)
        cpk = op / nowkm
        print('每公里費用 = %.1f NTD' % cpk)
        if year == 2014:
            print('2014-11-26 ~ 2014-12-31')
            ywork = 20       #一年預計上班日20天
            print('2014年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 36 
            print('2014年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 32 #到內湖公司公里數
            print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 內湖區 上下班費用 = %.1f NTD' % dcost)
            mrt = 40 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 內湖區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost   #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2014年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % ycot)            
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)            
            mtime = 80 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork / 60 #一年省時
            print('2014年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2015:
            print('2015-01-01 ~ 2015-12-31')
            ywork = 200       #一年預計上班日200天
            print('2015年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 365 
            print('2015年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 32 #到內湖公司公里數
            print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 內湖區 上下班費用 = %.1f NTD' % dcost)
            mrt = 40 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 內湖區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost   #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2015年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % ycot) 
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)
            mtime = 80 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork / 60 #一年省時
            print('2015年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2016:
            print('2016-01-01 ~ 2016-12-31')
            ywork = 200       #一年預計上班日200天
            print('2016年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 365 
            print('2016年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 32 #到內湖公司公里數
            print('每天 騎機車 至 內湖區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 內湖區 上下班費用 = %.1f NTD' % dcost)
            mrt = 40 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 內湖區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost   #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2016年 騎機車 比 搭捷運 至 內湖區 上下班省費 = %.1f NTD' % ycot)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 內湖區 上下班花費時間 = %d 分鐘' % time)
            mtime = 80 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 內湖區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 內湖區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork / 60 #一年省時
            print('2016年 騎機車 比 搭捷運 至 內湖區 上下班省時 = %.1f 小時' % ytime)        
        elif year == 2017:
            print('2017-01-01 ~ 2017-12-31')
            ywork = 200       #一年預計上班日200天
            print('2017年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 365 
            print('2017年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 26 #到信義公司公里數
            print('每天 騎機車 至 信義區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 信義區 上下班費用 = %.1f NTD' % dcost)
            mrt = 35 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 信義區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2017年 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % ycot)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 信義區 上下班花費時間 = %d 分鐘' % time)
            mtime = 70 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 信義區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork /60 #一年省時
            print('2017年 騎機車 比 搭捷運 至 信義區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2018:
            print('2018-01-01 ~ 2018-12-31')
            ywork = 200       #一年預計上班日200天
            print('2018年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 365 
            print('2018年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 26 #到信義公司公里數
            print('每天 騎機車 至 信義區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 信義區 上下班費用 = %.1f NTD' % dcost)
            mrt = 35 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 信義區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2018年 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % ycot)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 信義區 上下班花費時間 = %d 分鐘' % time)
            mtime = 70 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 信義區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork /60 #一年省時
            print('2018年 騎機車 比 搭捷運 至 信義區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2019:
            print('2019-01-01 ~ 2019-12-31')
            ywork = 200       #一年預計上班日200天
            print('2019年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 365 
            print('2019年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 26 #到信義公司公里數
            print('每天 騎機車 至 信義區 上下班公里數 = %d 公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 信義區 上下班費用 = %.1f NTD' % dcost)
            mrt = 35 * 0.8 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 信義區 上下班費用 = %d NTD' % mrt)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2019年 騎機車 比 搭捷運 至 信義區 上下班省費 = %.1f NTD' % ycot)
            time = 50 * 2    #騎車花費時間
            print('每天 騎機車 至 信義區 上下班花費時間 = %d 分鐘' % time)
            mtime = 70 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 信義區 上下班花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 信義區 上下班省時 = %d 分鐘' % cti)
            ytime = cti * ywork /60 #一年省時
            print('2019年 騎機車 比 搭捷運 至 信義區 上下班省時 = %.1f 小時' % ytime)
        elif year == 2020:
            print('2020-01-01 ~ 2020-06-30')
            ywork = 182       #一年預計上班日200天
            print('2020年上班天數 = 以 %d 天計算' % ywork)
            motfixcotavg = (23218 / 2043) * 182 
            print('2020年平均機車維修保養稅險費用 = %.1f NTD' % motfixcotavg)
            km = 30 #到忠孝上課公里數
            print('每天 騎機車 至 忠孝聯成 上下課公里數 = %d公里' % km)
            dcost = km * cpk #一天油費
            print('每天 騎機車 至 忠孝聯成 上下課費用 = %.1f NTD' % dcost)
            mrt = 30 * 2 #捷運三民高中站到 捷運西湖站
            print('每天 搭捷運 至 忠孝聯成 上下課費用 = %d NTD' % mrt)
            cot = mrt - dcost #騎機車比搭捷運日省費用
            print('每天 騎機車 比 搭捷運 至 忠孝聯成 上下課省費 = %.1f NTD' % cot)
            ycot = cot * ywork - motfixcotavg #一年省錢
            print('2020年 騎機車 比 搭捷運 至 忠孝聯成 上下課省費 = %.1f NTD' % ycot)
            time = 40 * 2    #騎車花費時間
            print('每天 騎機車 至 忠孝聯成 上下課花費時間 = %d 分鐘' % time)
            mtime = 60 * 2      #走路捷運全程花費時間
            print('每天 搭捷運 至 忠孝聯成 上下課花費時間 = %d 分鐘' % mtime)
            cti = mtime - time  #騎機車比搭捷運日省時
            print('每天 騎機車 比 搭捷運 至 忠孝聯成 上下課省時 = %d 分鐘' % cti)
            ytime = cti * ywork / 60 #一年省時
            print('2020年 騎機車 比 搭捷運 至 忠孝聯成 上下課省時 = %.1f 小時' % ytime)
        line = infile.readline()
        #print('%s,%s,%.2f,%s,%.2f,%.2f,%.2f,%s,%s,%s,%.2f,%s,%.2f,%.2f \n' % (year,nowkm,lit,op,oilavg,cpk,dcost,time,mrt,mtime,cot,cti,ycot,ytime))
        #outfile.write('%s,%s,%.2f,%s,%.2f,%.2f,%.2f,%s,%s,%s,%.2f,%s,%.2f,%.2f \n' % (year,nowkm,lit,op,oilavg,cpk,dcost,time,mrt,mtime,cot,cti,ycot,ytime))
        #print('%.2f,%.2f,%s \n' % (ycot,ytime,year))
        print()
        outfile.write('%.1f,%.1f,%s \n' % (ycot,ytime,year))
infile.close()
outfile.close()

#=======================
import pandas as pd
import matplotlib.pyplot as plt

colName = ['ycot','ytime','year']
oilcost = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt', encoding = 'utf8', names = colName)

oilcost_mean = oilcost.groupby('year', as_index = False).mean()
oilcost_mean.plot(kind = 'bar')
plt.xticks(oilcost_mean.index, oilcost_mean['year'], rotation = 0)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

colName = ['ycot','ytime','year']
iris = pd.read_csv(r'C:\GitHub\python\PY-Learn\oil-project\score-new-3.txt', names = colName)

iris['year'] = iris['year'].apply(lambda x: x.replace("Iris-",""))
                                                  #^把標題的不需要字串用空字號取代       
iris_mean = iris.groupby('year', as_index = False).mean()
iris_mean.plot(kind = 'bar')
plt.xticks(iris_mean.index, iris_mean['year'], rotation = 0)

plt.show()
