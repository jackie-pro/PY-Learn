# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:16:32 2020

@author: Jackie
"""


"""    
#20200604 作業
前往環保署下載[細懸浮微粒資料(PM2.5)]
共三種格式 json,xml,csv
請分別寫3各Python程式
將[細懸浮微粒資料(PM2.5)]資料讀出
觀察各地測站的PM2.5偵測值


Site(測站名稱)、county(縣市名稱)、PM25(細懸浮微粒濃度)、
DataCreationDate(資料建置日期)、ItemUnit(測項單位)
"""
#ans: CSV

import csv

with open(r'C:\GitHub\python\PY-Learn\pm25.csv', 'r', encoding = 'utf8') as file:
    pm = csv.reader(file, delimiter = ',')

    for row in pm:  
        print('測站: %s 縣市: %s PM2.5 = %s' % (row[0],row[1],row[2]))

#老師解答:
import csv 
with open(r'C:\GitHub\python\PY-Learn\pm25.csv', 'r', encoding = 'utf8') as csvfile:        
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        print(row[0]+' '+row[1]+' '+row[2])

ans: json


import json

with open(r'C:\GitHub\python\PY-Learn\pm25.json', encoding = 'utf8') as file:
    pm = json.load(file)
    
    for row in pm:
        print('測站: %s 縣市: %s PM2.5 = %s' % (row['Site'], row['county'], row['PM25']))

#老師解答:
import json

with open(r'C:\GitHub\python\PY-Learn\pm25.json', encoding = 'utf8') as file:
    data = json.load(file)
    
    for item in data:
        print([item['Site'], item['county'], item['PM25']])    
      
ans: xml

import xml.etree.ElementTree as ET

tree = ET.ElementTree(file = r'C:\GitHub\python\PY-Learn\pm25.xml' )
root = tree.getroot()  

for row in root.findall('Data'):
    site = row.find('Site').text 
    county = row.find('county').text
    pm25 = row.find('PM25').text
    print('測站: %s --縣市: %s --PM2.5 = %s' % (site,county,pm25))
 
#老師解答:    
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file = r'C:\GitHub\python\PY-Learn\pm25.xml' )
#讀取解析XML檔案
root = tree.getroot()  
#取得跟節點
for s in root.findall('Data'):
    site = s.find('Site').text 
    county = s.find('county').text
    pm = s.find('PM25').text
    print('測站: ', site, '--縣市: ', county, '--PM2.5 = ', pm)
#以findall()方法取得跟結點下的子結點標籤中符合的標籤取出顯示
    
#==============================================
#同學較晚整範例(選單式,直接擷取網頁資料分析處理,不需要先下載!)
import xml.etree.ElementTree as et
import requests
from io import BytesIO
from datetime import datetime

def findPM25():
    url = "http://opendata.epa.gov.tw/webapi/Data/PM25/?$orderby=MonitorDate%20desc&$skip=0&$top=1000&format="
    datatype = ""
    while True:
        cmd = input("請選擇下載的檔案格式:\n1.JSON\n2.CSV\n3.XML\n4.離開程式\n")
        if not cmd.isnumeric():
            print("請輸入選項(1~4)")
            continue
        cmd = int(cmd)
        print("資料擷取中...")
        startsearch = datetime.now()

        if cmd == 1:
            datatype = "json"
            error_code = datafromjson(url+datatype)
            if error_code == 0:
                print("請重新操作一次")
                continue
            else:
                endsearch = datetime.now()
                print("操作成功(耗時:%d sec)" % (endsearch - startsearch).seconds)
                continue
        elif cmd == 2:
            datatype = "csv"
            error_code = datafromcsv(url+datatype)
            if error_code == 0:
                print("請重新操作一次")
                continue
            else:
                endsearch = datetime.now()
                print("操作成功(耗時:%d sec)" % (endsearch - startsearch).seconds)
                continue
        elif cmd == 3:
            datatype = "xml"
            error_code = datafromxml(url+datatype)
            if error_code == 0:
                print("請重新操作一次")
                continue
            else:
                endsearch = datetime.now()
                print("操作成功(耗時:%d sec)" % (endsearch - startsearch).seconds)
                continue
        elif cmd == 4:
            print("離開系統...")
            break
        else:
            continue




def datafromxml(url):
    with requests.Session() as request:
        download = request.get(url)
        if download.status_code != 200:
            print("status_code:%d" % download.status_code)
            return 0
        download = download.content
        file_byte = BytesIO(download)
        tree = et.parse(file_byte)
        root = tree.getroot()
        for data in root:
            sitename = "{:s}".format(data[0].text).ljust(4, " ")
            monitorDate = "{:s}".format(data[1].text)
            concentration = ""
            if data[2].text is None :
                concentration = "{:s}".format("").rjust(4, "-")
            else:
                concentration = "{:s}".format(data[2].text).rjust(4, "-")
            itemUnit = "{:s}".format(data[3].text)
            print("%s%s\t%s %s" % (sitename,monitorDate,concentration,itemUnit))
    return 1



def datafromcsv(url):
    with requests.Session() as request :
        download = request.get(url)
        if download.status_code != 200:
            print("status_code:%d" % download.status_code)
            return 0
        download = download.content.decode("utf-8")
        download = download.replace("SiteName,MonitorDate,Concentration,ItemUnit","")
        download = download.split("\r\n")
        download = [x.split(",") for x in download]
        download.pop(0)
        download.pop(len(download)-1)

        for site in download:
            sitename = "{:s}".format(site[0]).ljust(4," ")
            monitorDate = "{:s}".format(site[1])
            concentration = "{:s}".format(site[2]).rjust(4,"-")
            itemUnit = "{:s}".format(site[3])

            print("%s%s\t%s %s" % (sitename,monitorDate,concentration,itemUnit))
    return 1



def datafromjson(url):

    with requests.Session() as request:
        download = request.get(url)
        if download.status_code != 200:
            print("status_code:%d" % download.status_code)
            return 0
        json1 = download.json()
        for item in json1:
            sitename = "{:s}".format(item['SiteName']).ljust(4," ")
            monitorDate = "{:s}".format(item['MonitorDate'])
            concentration = "{:s}".format(item['Concentration']).rjust(4,"-")
            itemUnit = "{:s}".format(item['ItemUnit'])

            print("%s%s\t%s %s" % (sitename,monitorDate,concentration,itemUnit))

    return 1



if __name__ == '__main__':

    starttime = datetime.now()
    findPM25()
    endtime = datetime.now()
    print("%d sec" % (endtime-starttime).seconds)

#==============================================