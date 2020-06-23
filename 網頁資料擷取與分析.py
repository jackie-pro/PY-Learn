# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:22:08 2020

@author: Jackie
"""
#20200601
"""

網頁資料擷取與分析
主題:
1.資料處理
2.網頁資料擷取與轉換  
  .必須會網頁結構 -> 要會網頁設計 -> (1.HTML3, 2.CSS3) 
3.資料分析
4.資料視覺化
5.產出報告(綜合以上資料給出結論心得)
 #^業界需要
"""
#=====================================
"""
1.資料處理

=> Python第三方函式庫:
   .Python函式庫: (版本區分)
     .Python官方
     .協力廠商開發#非常多


=>jieba(結巴):中文分詞函式庫
  .使用於中文自然語言處理(NLP - Nature Language Processing)
  .屬於一種人工智慧的應用,功用為:
    .分析文章主題
    .分析文章內容
    .文章分數關聯
    .作者撰寫習慣
  
  .步驟:
    .取得文章(注意版權)
    .將內容切割為一個個的字詞,並記錄字詞出現的次數
    .用方法來衡量每個字詞的重要性,以 tf-idf 分析每個字詞的重要性
      tf:term frequency 字詞頻率
       某字詞出現次數 / 所有字詞總和出現次數
       導出:字詞在文章中的重要性 => 次數高代表重要性高
      idf:inverse document frequency 逆向檔案頻率
       總文章數 / 某詞出現的文章數
       導出:出現在越多的文章代表越不重要 (大家都有的字詞越不重要)
            (越稀有的越重要)
            
@安裝Python的函式庫@
以命令列:Anaconda Prompt輸入 
      => 輸入指令: pip install 函式名稱
                  pip install jieba
         
"""

ex:
    
import jieba
import jieba.analyse
f = open(r'C:\GitHub\python\PY-Learn\test-jieba.txt' , 'r' , encoding = 'utf-8')
article = f.read()                                         #^為避免檔案讀取錯誤      
tags = jieba.analyse.extract_tags(article , 10)
print('最重要的字詞:', tags)

"""
=>jieba.analyse.extract_tags (文章, 提取字詞分析 之 權重最大值)
                                    ^依據為tf-idf  ^預設20

  結果:分析出文章最重要的10個字詞


=>open data:開放資料
  .建議格式:
    JSON
    XML
    試算表(MS Excel)=>新版.xlsx (xls多一個x ,代表加了XML的資料)
    CSV (以逗號分隔)
    文書 (PDF,word,ODF...)
    純文字(*.txt)

=>HTML轉PDF:
  1.pdfkit:安裝函式庫  => 輸入指令: pip install pdfkit

"""
ex:

import pdfkit
config = pdfkit.configuration(wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

pdfkit.from_url('https://www.csf.org.tw/main/index.asp', r'C:\GitHub\python\PY-Learn\out1.pdf', configuration=config)

pdfkit.from_string('Hello World', r'C:\GitHub\python\PY-Learn\out2.pdf', configuration=config)

pdfkit.from_file(r'C:\GitHub\python\PY-Learn\CSF.html', r'C:\GitHub\python\PY-Learn\out3.pdf', configuration=config)

pdfkit.from_file(r'C:\GitHub\python\PY-Learn\test.html', r'C:\GitHub\python\PY-Learn\out4.pdf', configuration=config)

#PDF檔
"""
pdfkit.from_url (網址,轉存的PDF檔,組態)
 #將網頁轉成PDF檔
pdfkit.from_string (字串,轉存的PDF檔,組態)
 #將字串轉存為PDF檔
pdfkit.from_file (檔案,轉存的PDF檔,組態)
 #將檔案轉存為PDF檔

##^ 組態 => 執行的wkhtmltopdf程式
"""
"""
HTML:
<table> 建立表格
<th> :欄 ->  #裡面的字是粗體
<td> :欄 -> 必須放在<table>之內
<tr> :列 ->
<tr>
  <td>123</td>
  <td>456</td>
</tr>

"""
"""
=>HTML轉PDF:
  2.pypdf2:安裝函式庫  => 輸入指令: pip install pypdf2
   執行PDF讀取,寫入,合併,分割......
   
  =>pdfFileReader(PDF檔案):讀取PDF檔案 ->建立一個PDF物件
  =>PDF物件.getDocumentInfo():取得頁面資訊  
  =>PDF物件.getPageLayout():取得頁面配置  
  =>PDF物件.getPageMode():取得頁面模式 
  =>PDF物件.getXmpMetadata():取得檢索資料  
  =>PDF物件.getNumPages():取得頁數  
       以上為PDF讀取
  ex2:
  =>PdfFileWriter物件.addPage(寫入的頁面)
                      ^增加一寫入頁  ^通常由pdfFileReader讀取而取得
  =>PdfFileRader物件.getPage(頁面索引)#取得頁面索引頁
  =>PdfFileWrite物件.write(寫入的檔案)#寫入資料到檔案中
  =>PdfFileWrite物件.addBlankPage() #寫入空白頁

"""
ex:

from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = r'C:\GitHub\python\PY-Learn\water.pdf'
pdfFileReader = PdfFileReader(readFile)

documentInfo = pdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)

pageLayout = pdfFileReader.getPageLayout()
print('pageLayout = %s ' % pageLayout)

pageMode = pdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)

xmpMetadata = pdfFileReader.getXmpMetadata()
print('xmpMetadata = %s ' % xmpMetadata)

pageCount = pdfFileReader.getNumPages()
print('pageCount = %s' % pageCount)



ex2:

from PyPDF2 import PdfFileReader, PdfFileWriter
readFile = r'C:\GitHub\python\PY-Learn\health.pdf'
pdfFileReader = PdfFileReader(readFile,strict=False)
                                         #^錯誤警告關閉,預設為True
#^藉由PdfFileRead讀入readFile設定到 pdfFileReader (即為health.pdf)
documentInfo = pdfFileReader.getDocumentInfo()
outFile = r'C:\GitHub\python\PY-Learn\health_out.pdf'
#outFile即為輸出檔 health_out.pdf
pdfFileWriter = PdfFileWriter()
#設定寫入檔案PdfFileWriter為pdfFileWriter

numPages = pdfFileReader.getNumPages()
#numPages:總頁數
for index in range(0, numPages):
    pageobj = pdfFileReader.getPage(index)
    #取得頁面(每一頁)pageobj  
    pdfFileWriter.addPage(pageobj)
    #加入每一頁
    pdfFileWriter.write(open(outFile, 'wb'))
    #將加入的每一頁寫入到檔案
    
pdfFileWriter.addBlankPage()
    #加入空白頁
pdfFileWriter.write(open(outFile, 'wb'))
    #將空白頁寫入 health_out.pdf
#================================================
#20200603
"""
切割PDF頁
"""
ex:
from PyPDF2 import PdfFileReader, PdfFileWriter
readFile  = r'C:\GitHub\python\PY-Learn\health.pdf'
#設定檔案來源為 readFile 變數
pdfFileReader = PdfFileReader(readFile,strict=False)
#讀取檔案並設定給 pdfFileReader 變數
documentInfo = pdfFileReader.getDocumentInfo()
#取得檔案資訊並設定給 documentInfo 變數
outFile = r'C:\GitHub\python\PY-Learn\health_cut.pdf'
#設定輸出檔案名稱為 outFile 變數
pdfFileWriter = PdfFileWriter()
#將檔案寫入方法設定給 pdfFileWriter 變數
numPages = pdfFileReader.getNumPages()
#讀取檔案頁數並設定給 numPages 變數
if numPages > 3:
    #若是頁數大於 3   
    
    for index in range(3, numPages):
        #則將頁數帶入迴圈，從3開始到最後的頁數
        pageObj = pdfFileReader.getPage(index)
        #以迴圈每一圈的index值取得該頁並設定給pageObj變數
        pdfFileWriter.addPage(pageObj)
        #將取得的頁面加入
    pdfFileWriter.write(open(outFile, 'wb'))
    #將所有加入的頁面寫入輸出檔案
    
ex2:合併
import PyPDF2
pdfFiles = [r'C:\GitHub\python\PY-Learn\out1.pdf',
            r'C:\GitHub\python\PY-Learn\out2.pdf',
            r'C:\GitHub\python\PY-Learn\out3.pdf']
#設定要讀取的檔案
pdfWriter = PyPDF2.PdfFileWriter()
#將檔案寫入方法設定給 pdfWriter 變數
pdfOutput = open(r'C:\GitHub\python\PY-Learn\comb.pdf', 'wb')
#以寫入模式開啟檔案comb.pdf，若不存在則建立，並設定給 pdfOutput 變數(輸出檔案)
for fileName in pdfFiles:
    #以檔案名稱做為迴圈的執行參數fileName
    pdfReader = PyPDF2.PdfFileReader(open(fileName, 'rb'))
    #以讀取模式開啟檔案並設定給 pdfReader  變數
    for pageNum in range(pdfReader.numPages):
        #以開啟的檔案頁數作為迴圈執行的次數
        print(pdfReader.getPage(pageNum))
        #將讀取的頁面印出
        pdfWriter.addPage(pdfReader.getPage(pageNum))
        #將讀取的頁面加入
pdfWriter.write(pdfOutput)
#將所有加入的頁面寫入輸出檔案
pdfOutput.close()
#關閉寫入後的檔案

#====================
#讀取txt檔案
f = open(r'C:\GitHub\python\PY-Learn\score.txt')
#開啟檔案(唯讀) ,open不加參數 預設唯讀
a = f.read()
#以 read()方法讀取 f 並設定給變數a
L = a.split()
#以 split() 方法分割資料成為一個串列 L，串列中的資料為整數字串
for i in range(0, len(L)): #以串列資料做為迴圈執行的次數
    L[i] = int(L[i]) #以索引帶入串列L中取得每一個元素並轉成整數後設定回給元素自己

    #分類統計各級別人數到列表 c
c = [0,0,0,0,0,0]
for x in L: #以串列L中的元素作為迴圈執行依據
    if x >= 90: #若串列L元素>=90，則將串列c的第一個元素值加1
        c[0] += 1
    elif x >= 80: #若串列L元素>=80，則將串列c的第二個元素值加1
        c[1] += 1
    elif x >= 70: #若串列L元素>=70，則將串列c的第三個元素值加1
        c[2] += 1
    elif x >= 60: #若串列L元素>=60，則將串列c的第四個元素值加1
        c[3] += 1
    elif x >= 40: #若串列L元素>=40，則將串列c的第五個元素值加1
        c[4] += 1
    else:         #其餘則將串列c的第六個元素值加1
        c[5] += 1
#輸出各級別統計結果
print('90分以上 %d 人' % c[0], end = '\n')
print('89-80分以上 %d 人' % c[1], end = '\n')
print('79-70分以上 %d 人' % c[2], end = '\n')
print('69-60分以上 %d 人' % c[3], end = '\n')
print('59-40分以上 %d 人' % c[4], end = '\n')
print('39分以下 %d 人' % c[5], end = '\n')

#====================
#寫入txt檔案
import math
#載入數學模組
with open(r'C:\GitHub\python\PY-Learn\data5.txt', 'r') as fin:
    #以讀取模式開啟data5.txt設定給變數fin
    with open(r'C:\GitHub\python\PY-Learn\data5_w.txt', 'w') as fout:
        #以寫入模式開啟data5.txt設定給變數fout
        for line in fin: #以讀取的檔案作為迴圈執行依據，逐一讀取data5.txt的資料
            data = math.ceil(20 / (float(line) * 0.001425))
            #執行數學模組的ceil()方法：取得大於或等於該數值得最小整數，運算後設定給data變數
            #math.floor -> 小於或等於取得該數值的最大整數
            print('每股價格: %5.2f, 每日需購股數: %5.0f' % (float(line), data))
            fout.write(str(data)+ '\n')
            #將data寫入fout

#====================            
"""
開放資料(Open Data)
=>政府資料開放平台:data.gov.tw
=>各部會資料平台:中央氣象局、環保署、健保屬、文化部

"""       
#CSV檔     
ex:
import csv
#載入csv套件
with open(r'C:\GitHub\python\PY-Learn\ubike_1.csv', 'r', encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    #delimiter指定分隔字元
    plots = csv.reader(csvfile, delimiter = ',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in plots:  #以讀取的plots資料做為迴圈依據
        print(row[0]+" "+row[1]+" "+row[3]+" "+row[5]+" "+row[12])
        #每一個欄位(row)以索引取出該欄位資料      
        
ex:
import csv
#載入csv套件
with open(r'C:\GitHub\python\PY-Learn\air.csv', 'r', encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    #delimiter指定分隔字元
    air = csv.reader(csvfile, delimiter = ',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in air:  #以讀取的plots資料做為迴圈依據
        print(row[0]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5])
        #每一個欄位(row)以索引取出該欄位資料      

ex:
import csv
#載入csv套件
with open(r'C:\GitHub\python\PY-Learn\stock.csv', 'r') as fin:
#以讀取模式開啟檔案stock.csv並設定為變數fin    
    with open(r'C:\GitHub\python\PY-Learn\stock_out.csv', 'w') as fout:
        #以寫入模式開啟檔案stock_out.csv，若檔案不存在則建立，並設定為變數out
        csvreader = csv.reader(fin, delimiter = ',')
        #以csv套件的reader方法將檔案fin讀入並設定給變數csvreader(為一個讀取物件)
        csvwriter = csv.writer(fout, delimiter = ',')
        #以csv套件的writer方法將寫入檔案fout並設定給變數csvwriter(為一個寫入物件)
        header = next(csvreader) #取得讀取資料的表頭設定給變數header
        print(header) #印出表頭
        csvwriter.writerow(header) #將表頭寫入檔案
        for row in csvreader: #以迴圈逐行讀取資料
            row[6] = row[6].replace('/', '-') #將每一行日期字串中的 / 改為 -
            print(','.join(row)) #使用join()方法將字串合併並印出
            csvwriter.writerow(row) 	#以寫入物件利用writerow()方法將每列資料寫入
            
#====================
#Json檔
import json
#載入JSON套件
print(json.dumps(['two', {'bar': ('jaz', None, 2.0, 1)}]))
print(json.dumps('\'two\bar'))
print(json.dumps('\u4321'))
print(json.dumps('\\'))
print(json.dumps({'c': 0, 'b': 0, 'd': 0}, sort_keys = True))
                                           #^ sort_keys = True ->遞增排序
print(json.dumps([0,1, 2, 3, {'4': 5, '6': 7}], separators = (',', ':')))
                                                #^分隔符號 -> 型態是數組
                                                # separators(item符號, dict符號)
                                                #             ^項目     ^字典 
print(json.dumps({'4': 5, '6': 7}, sort_keys = True, indent = 3))
#json.dumps()：將Python中的文件序列化為json格式字串       ^位置
#json.loads()：為json.dumps()的反向，將已編碼的json字串解碼為Python物件
d1 = { 'b' : 789 , 'c' : 456 , 'a' : 123}
d2 = json.dumps(d1, sort_keys = True, indent = 4)
print(d2)

#====================
"""
#JSON：JavaScritp Object Notation
=>JavaScript 開放資料交換格式
=>JSON 為JavaScript程式的一個子集合

#JSON型態轉換到Python型態的對照：

Json         => Python
=========================
object       => dict
array        => list
string       => unicode
number(int)  => int,long
number(real) => float
true         => True
false        => False
null         => None


資料格式如下：
menu = \
  {
  "breakfast" : {
      "hours": "7-10",
      "items": {
    "breakfast burritos": "$60",
    "pancakes": "$35"
  }
      },
  "lunch" : {
   .....
  }
      },
  "dinner" : {
    .....
  }
      }
}
"""
#====================
#Json轉Python
ex:
import json
#載入JSON套件
with open(r'C:\GitHub\python\PY-Learn\ubike_1.json', encoding = 'utf8') as file:
#開啟JSON檔並設定給變數file
    data = json.load(file)
    #執行loads()方法將JSON檔案解碼為Python物件，並設定給data變數
    for item in data:
        #以data作為迴圈執行的依據，即解碼後的資料設為item
        print([item['sno'], item['sna'], item['tot']])
        #以索引列印item各欄位資料
        
#==================== 
"""
#XML：eXtensible Markup Language；可延伸標記語言
=>是一種電腦標記語言
=>規則特性：
    => 是一種標籤語法
    => 以<名稱>開頭，後面接一段內容，再以</名稱>結尾。
    => 忽略空格
    => <名稱>下可能有<子名稱>，層層結構。
    => <名稱>可稱為一個節點
    => <名稱 屬性=屬性值>：代表該名稱的設定功能
    => 通常用於資料傳遞與消息發佈，如RSS....，一般業界會自訂客製化的XML格式。
"""    
"""
#每個 Element (元素；標籤)有以下的特性：
	#tag(標籤)
	#attributes(屬性)
	#text(文字)
"""   
#====================
#Xml轉Python
ex:
import xml.etree.ElementTree as et
#載入xml.etree.ElementTree套件
tree = et.ElementTree(file = r'C:\GitHub\python\PY-Learn\menu.xml' )
#讀取XML檔，儲存到 tree 變數

root = tree.getroot()
#取得根節點(即XML標籤)

print(root.tag)
#輸出根節點(menu標籤名)
for child in root:
#(menu標籤下的子標籤)
    print('tag:', child.tag, 'attributes:', child.attrib)
    #tag：取得標籤、attrib：取得標籤屬性
    for grandchild in child:  #子標籤下的子標籤
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
        #\t => tab鍵(空4格)
print(len(root))    # 菜單選項的數目
print(len(root[0])) # 早餐選項的數目


ex: #xml檔讀取
import xml.etree.ElementTree as ET
#載入 xml.etree.ElementTree 套件

tree = ET.ElementTree(file = r'C:\GitHub\python\PY-Learn\country_data.xml' )
#以parse讀取解析XML檔案
root = tree.getroot()  
#取得根節點<data>     #^ .getroot -> 取得根結點標籤 
print('Coutry_data.xml的根結點:'+root.tag) 
#輸出根節點(標籤名)
print('根節點標籤裡的屬性和屬性值:'+str(root.attrib)) #Data標籤 -> 根結點
#輸出根節點的屬性與屬性值

for child in root: #子結點 country
#以迴圈取得子節點標籤、屬性、屬性值
    print(child.tag, child.attrib)

print('排名:'+root[0][0].text, '國內生產總值:'+root[0][2].text,)
#以 text 輸出 country 標籤下的子標籤內容 
                        #^.text -> <>標簽前後括的值 如: <> XXXX <>                        

for neighbor in root.iter('neighbor'): 
    #以迴圈取得 neighbor 標籤屬性與屬性值
    #Element.iter (目標) => 1.尋找所有元素內 符合目標值的項目
    #2.尋找所有目標的 tag
        print(neighbor.attrib)

for country in root.findall('country'):
#以 findall() 方法取得根節點下的子節點標籤中符合的標籤取出顯示
    rank = country.find('rank').text 
    #利用 .find的方法搜尋country下的子結點,並取出其文字
    name = country.get('name')
    #利用 .get的方法取出country中的屬性
    print(name,rank)
 
#20200604    
ex: #xml檔修改/寫入
import xml.etree.ElementTree as ET
#載入 xml.etree.ElementTree 套件
tree = ET.parse(r'C:\GitHub\python\PY-Learn\country_data.xml' )
#以parse讀取解析XML檔案
root = tree.getroot()
#取得根節點<data>

for rank in root.iter('rank'):
#以迴圈取得<root>節點下符合rank的節點，執行修改 rank 標籤
    new_rank = int(rank.text) + 1
    #設定 rank 標籤顯示的文字轉換為整數後 + 1，並設定給變數new_rank
    rank.text = str(new_rank)
    #將加 1 後的顯示文字轉換為字串，並設定給變數rank.text
    rank.set('updated','yes')
    #以set()方法設定 rank 標籤的屬性、屬性值
    #Element.set(屬性 , 屬性值)：設定元素的屬性、屬性值
    
tree.write(r'C:\GitHub\python\PY-Learn\country_data_optput.xml', encoding = 'utf-8' )
#利用write()方法寫入 XML 資料


ex: #xml檔刪除
import xml.etree.ElementTree as ET
#載入 xml.etree.ElementTree 套件
tree = ET.ElementTree(file = r'C:\GitHub\python\PY-Learn\country_data.xml' )
#以parse讀取解析XML檔案
root = tree.getroot()  
#取得根節點<data>    #^ .getroot -> 取得根結點標籤
for country in root.findall('country'):
    #以 findall() 方法取得根節點下的子節點標籤中符合country的標籤取出
#再以迴圈執行根節點下所有 country 標籤
    rank = int(country.find('rank').text)
    #以find()方法尋找 country 標籤下的子節點 rank 標籤的文字並轉換為整數
    
    if rank > 50: 
        #若 rank 標籤顯示文字大於 50
        root.remove(country)
        #則使用 remove() 方法移除根節點下的 country 標籤

tree.write(r'C:\GitHub\python\PY-Learn\country_data_optput01.xml', encoding = 'utf-8')
#利用write()方法寫入 XML 資料

#====================
"""
#SQLite：
=>是包含在一個相對小的C程式庫中的關聯式資料庫管理系統。
=>不是一個用戶端/伺服器端結構的資料庫引擎。
=>被整合在用戶程式中，使用動態的SQL語法操作。
=>特性：
    .支援交易ACID(單一性、一致性、孤立性、耐久性)
    .無需設定與管理，因此若要管理，需要搭配第三方套件所提供的工具。
    .支援ANSI-SQL92語法(資料庫查詢語言標準)
    .資料庫系統是一個檔案。
    .檔案大小最大支援到2TB。
    .記憶體需求小：原始程式採用不到30000行的C語言撰寫，僅需要小於250KB的程式空間。
    .免費使用。
    .使用 unicode。

#Python使用sqlite3模組(2.5版以上已內建)
=>使用方法：
    .sqlite3.connect：開啟資料庫的連結，成功開啟則傳回一個連線物件。
    .sqlite3.cursor：建立cursor(資料指標)
    .sqlite3.execute：執行SQL語法
    .sqlite3.commit：提交目前的交易(執行資料庫的操作)
    .sqlite3.rollback：回復上一次呼叫commit()對資料庫的更改。
    .sqlite3.close：關閉資料庫連結。
"""
#連結資料庫
ex:
import sqlite3
#載入 sqlite3 模組

conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
print('Opend database successfully')

c = conn.cursor()
#建立 cursor(游標物件) 供資料庫後續操作

c.execute('''CREATE TABLE COMPANY1
          (ID INT PRIMARY KEY NOT NULL, NAME TEXT   NOT NULL,
          AGE  INT NOT NULL, ADDRESS   CHAR(50), SALARY   REAL);''')
#執行 SQL 指令
#建立資料表(create table)
          
print('Table created successfully')

conn.commit()
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令

obj = c.execute('''SELECT * FROM COMPANY1''')
for row in obj:
    print(row[0],row[1],row[2],row[3],row[4])

conn.close()
#關閉資料庫(不會自動呼叫 commit())

ex:
import sqlite3
#載入 sqlite3 模組

conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案

c=conn.cursor()
#建立 cursor(游標物件) 供資料庫後續操作

print('Opend database successfully')

c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00)");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00)");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00)");
c.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00)");
#執行 SQL 指令
#新增記錄(insert into)
          
conn.commit()
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print('Record created successfully')
conn.close()
#關閉資料庫(不會自動呼叫 commit())

#==========================
import sqlite3
conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
print('Opend database successfully')
c=conn.cursor()
obj = c.execute('SELECT * FROM COMPANY')
for row in obj:
    print(row[0],row[1],row[2],row[3],row[4])
conn.close()
print('Closed database successfully')
#==========================
ex:  #取得資料
import sqlite3
#載入 sqlite3 模組
conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor()
#建立 cursor(游標物件) 供資料庫後續操作

print('Opend database successfully')
cursor = c.execute("SELECT id, name, address, salary  from COMPANY1")
#執行 SQL 指令
#查詢記錄(select)
for row in cursor:
    print('ID = ', row[0])
    print('NAME =', row[1])
    print('ADDRESS = ', row[2])
    print('SALARY = ', row[3], '\n')
#以 cursor 物件c 執行 SQL 查詢指令後，得到查詢結果，取得後顯示
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後設定給對應的變數。

print('Operation dobe successfully')
conn.close()
#關閉資料庫(不會自動呼叫 commit())



ex:  #取得後修改資料
import sqlite3
conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor()
#建立 cursor(游標物件) 供資料庫後續操作
print("Opened database successfully")

c.execute('UPDATE COMPANY set SALARY = 25000.00 where ID = 1')
#執行 SQL 指令
#更新記錄(update set)
conn.commit()
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print("Toal number of rows updated :", conn.total_changes)
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。 
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
#執行 SQL 指令
#更新記錄(select)
#以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後顯示。
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()
#關閉資料庫(不會自動呼叫 commit())

ex:  #取得後刪除資料
import sqlite3
conn = sqlite3.connect(r'C:\GitHub\python\PY-Learn\test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor()
#建立 cursor(游標物件) 供資料庫後續操作
print("Opened database successfully")

c.execute('DELETE from COMPANY1 where ID = 2;')
#執行 SQL 指令
#刪除記錄(DELETE)
conn.commit()
#執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print("Toal number of rows updated :", conn.total_changes)
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。 
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
#執行 SQL 指令
#更新記錄(select)
#以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
#以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
#再以索引將記錄的欄位資料取得後顯示。
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()
#關閉資料庫(不會自動呼叫 commit())

#==============================================================
"""
資料處理總結:
    資料檔案以 *.csv , *.xml , *.json 為主
    讀取,寫入為基本操作   
    
"""
#==============================================================


"""
2.網頁資料擷取與轉換 
=> Python擷取網頁的流程:
    .存取網站取得內容
    .解析取得的內容
    .處理資料(分析,視覺化)

=> Python取得網頁資料
    .靜態網頁資料
      .網站中不含.js檔
      .伺服器回傳的是一整個網頁
      .靜態網頁處理方式:解析HTML檔案
      .HTML網頁架構:
          1.標籤(tag)     --->
          2.屬性(attribute)--> 元素 -> 以樹狀結構構成
          3.內容(content) --->
      .HTML標籤結構:
          <標籤名 屬性...>內容</標籤>
      .常用HTML標籤:(網頁擷取用)
          .<header>  表頭
          .<title>   標題
          .<body>    網頁主體
          .<div>     區塊
          .<h1>      標題文字第一級
          .<a href>  超連結
          .<form>    表單
          .<tr>,<td> 表格列 / 表格欄
      .常用HTML屬性:
          .id        網頁識別
          .class     元素分類(類別)
          .href      超連結


"""
"""
安裝套件: 
    1.pip install requests
    2.pip install bs4
"""
ex:
import csv  #載入 csv 模組，處理csv檔案格式
import requests #載入 requests 模組，存取網站取得內容
from bs4 import BeautifulSoup
#載入 BeautifulSoup 模組，解析網頁
#BeautifulSoup讀取 HTML 原始碼，自動進行解析並產生一個 BeautifulSoup 物件，
#此物件中包含了整個 HTML 文件的結構
from time import localtime, strftime, strptime, mktime
#處理時間系列
from datetime import datetime
#處理日期時間
from os.path import exists
#處理檔案儲存路徑、查看特定的路徑是否存在，不分檔案或目錄

html = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-tw')
#html = requests.get('https://www.armedbase.com.tw')
#取得網站內容 -> requests.get(網址)

bsobj = BeautifulSoup(html.content, 'lxml') # html.content->把整個網站取出來
#^bsobj ->經分析後的網站樹狀結構
#print(bsobj)#將取得的網站內容分析並建立物件bsObj

for single_tr in bsobj.find('table', {'title':'牌告匯率'}).find('tbody').findAll('tr'):
#靜態網頁中的資訊結構為table→tbody→tr，很多tr，故使用findall找出所有tr    
    cell = single_tr.findAll('td')
    #findall找出所有的td儲存到cell->儲存格
    currency_name = cell[0].find('div', {'class':'visible-phone'}).contents[0]
    #在cell[0]下找到class屬性是visible-phone的欄位
    #以contents回傳欄位內容給currency_name(匯率名稱)
    currency_name = currency_name.replace('\r','')
    currency_name = currency_name.replace('\n','')
    currency_name = currency_name.replace(' ','')
    #刪除表格中不必要的資料如\r , \n , 空白鍵
    currency_rate = cell[2].contents[0] #contents -> 內容
    #以contents回傳欄位內容給currency_rate(匯率)
    print(currency_name, currency_rate)
    file_name = r'C:\GitHub\python\PY-Learn\bkt_rate' + currency_name + '.csv'
    #建立csv檔案
    now_time = strftime('%Y-%m-%d %H:%M:%S', localtime())
    #取得目前時間   ^設定時間格式:大Y->西元年
    if not exists(file_name):
        data = [['時間', '匯率'],[now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    #寫入csv檔，如果檔案不存在，則抓取網頁上的時間及匯率寫入，若檔案存在，即使用原資料
    #如果檔案不存在，加入一行資料，以串列中的串列處理每天的匯率資料。
    #每一個串列代表擷取得每一筆匯率資料。
    f = open(file_name, 'a') #開啟csv檔
    w = csv.writer(f)        #寫入csv檔
    w.writerows(data)        #寫入data物件
    f.close()                #關閉csv檔案

#==============================================================
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
#20200605
"""
=>urllib
  .使用urllib.reguest的urlopen方法,取得遠端網頁,
   再利用read()方法讀取內容
  .BeautifulSoup的網頁解析器 
  => html.parser(官方的) ,lxml, xml, html5lib

=>print的 format格式:
    print(輸出字串參數.format(輸出資料1,輸出資料2,......)
            ^以{}格式執行
    prit('{}{}{}'.format('A','B','C'))

=> enumerate : 列舉資料中的每一個項目(包含索引)
   ex:
      a1 = [1,2,3,4,5,6]
      for index,value in enumerate(a1):
          print('%d,%d' % (index,value))
          
=> 讀取網站檔案: requests
    .發送get請求
      .Browser輸入網址,再由伺服器回應到使用著端
              ^輸入網址這個動作就是請求get
      .requests 可以不經過Browser發送get直接存取網頁
      語法格式:
          import requests
          變數 = request.get(網址,請求時的附帶參數)
           ^回應物件

=> httpbin.org:
    .測試網站requests(請求)及response(回應)的服務
    請求網址: http://httpbin.org/get
             http://httpbin.org/post
      若帶參數請求,則以 ?,& 合併於網址後
           
      使用者 --------> 網站
             ^requests      
     使用者 <-------- 網站
             ^response
     (clint)         (server)
     (客戶端)         (伺服器端)
   
=> session / cookie
    .建立session: requests.session
        身分認證通常是搭配session使用
    .網頁擷取(在身分認證頁面):
        建立session以post方式帶入參數登入
        再使用cookies帶入參數進入頁面

            拜訪
    client --------> server
      ^ 發               | 
      | 給               |
      ------產生憑證------
    
    憑證儲存在server端 => 叫做 session --- 未過期,server即可辨識
    憑證儲存在client端的Browser => 叫做 cookie ---- 未過期,server即可辨識
    
    
    
"""


ex: 統一發票網路擷取最近2次開獎號碼

from __future__ import unicode_literals, print_function
#設定Python程式中新舊版本對unicode字串與輸出入的相容性 
import urllib  #存取網頁
from bs4 import BeautifulSoup  #解析網頁
import urllib.request   #存取網頁

request_url = 'http://invoice.etax.nat.gov.tw/'
# 財政部官網

htmlContent = urllib.request.urlopen(request_url).read()
# 以urllib.request.urlopen開啟網頁物件並以read()讀取網頁內容
soup = BeautifulSoup(htmlContent,'html.parser')
#將取得的網站內容分析並建立物件soup，以html.parser方法解析(解析HTML、XHTML)
results = soup.find_all('span', class_ = 't18Red') #span ->通常指一行  div -> 指一個區塊
#搜尋所有網頁中標籤為span，且class屬性為t18Red者設定給results
subTitle = ['特別獎', '特獎', '頭獎', '增開六獎']
# 設定獎項串列
months = soup.find_all('h2', {'id': 'tabTitle'})
#搜尋所有網頁中標籤為h2，且id屬性為tabTitle者設定給months

month_newest = months[0].find_next_sibling('h2').text
# 最新一期，使用months物件的find_next_sibling方法找尋標籤為'h2'下的內容
month_previous = months[1].find_next_sibling('h2').text
# 上一期
print('最新一期統一發票開獎號碼 ({0}):'.format(month_newest))
for index, item in enumerate(results[:4]): #(results[:4]) -> index 0-3 共4組 
#enumerate：列舉資料中的每一個項目(包含索引)
    print('>> {0} : {1}'.format(subTitle[index], item.text))
print('上一期統一發票開獎號碼 ({0}):'.format(month_previous))
for index2, item2 in enumerate(results[4:8]): #(results[4:8]) -> index 4-7 共4組 
    print('>> {0} : {1}'.format(subTitle[index2], item2.text))


ex: 擷取yahoo首頁原始碼
import requests
url = 'https://tw.yahoo.com/'
html = requests.get(url) #html取得的回應就是網站伺服器的回應
html.encoding = 'utf-8'
    #^ .encoding 設定用UFT-8編碼去讀取
print(html.status_code) # => 200
print(requests.codes.ok) # => 200
if html.status_code == requests.codes.ok: # requests.codes.ok => 回應代碼OK = 200
        #^ .status_code 取得回應狀態碼
    print(html.text)
               #^ .text => 全部內容

ex: #requests.get
import requests
payload = {'ID': 'admin', 'psw': '12345678'}
#^字典
html = requests.get('https://httpbin.org/get', params = payload)
                                               #^請求時的附帶參數
print(html.url)
          #^ .url => 取得網址          

ex: #requests.post
import requests
payload = {'account': 'admin', 'passwd': '12345678'}
#^字典
html = requests.post('https://httpbin.org/post', data = payload)
                                                 #^請求時的附帶參數
print(html.text)
          #^ .text => 取得網站內容  
print(html.url)
          #^ .url => 取得網址   

"""
擷取PPT熱門問題排行躲過 滿18歲 頁面 程式流程:
    1.查詢網頁表單傳送方式為post
    2.按鈕value值為yes
    以1.2. -> 以Python程式寫出進入網址,按下按鈕值
"""
ex: #擷取PPT熱門問題排行躲過 滿18歲 頁面
import requests
from bs4 import BeautifulSoup
payload = {
    'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
    'yes': 'yes'
}
#1.查詢網頁表單傳送方式為post
#2.按鈕value值為yes
#以1.2. -> 以Python程式寫出進入網址,按下按鈕值 => payload
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)' \
        'AppleWebKit/537.36 (KHTML, like Gecko) chrome/56.0.2924.87 safari/537.36'
}
#讓程式去模擬瀏覽器的操作(運作),以騙過網站伺服器的防護

rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data = payload, headers = headers)
#經過這一行,伺服器端就會產生所屬的cookies ,參數帶headers
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers = headers)
#擷取網頁資料, 參數帶headers
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, \
          item.select('.title')[0].text)  

"""
網頁資料分析與擷取: BeautifulSoup (網頁解析)
=> 格式:
    BeautifulSoup 物件 = BeautifulSoup(網頁原始碼, 'html.parser')

=>常用方法:
    .find() : 傳回一個符合的標籤內容,傳回值是一個字串
    .findall() : 傳回所有符合的標籤內容,傳回值為串列
      .格式: find
            find_all (標籤名稱, {屬性名稱:屬性值})
                                 ^字典型別 => 過濾條件 
    .select() : 以css選擇器的方式讀取指定的資料,傳回值為串列  
      1.讀取css id :必須於id前加上 #,這樣才會知道是css id
        如: <div id='first'>內容</div>
           py: data = BeautifulSoup物件.select('#first') 
      2.讀取css類別 : 必須於類別錢加上 .
        如: <p class='second'>內容</p>
           py: data = BeautifulSoup物件.select('.second')
      3.多層標籤 : 逐層依序寫出
        如: <html><head><title>內容</title></head></html>
           py: data = BeautifulSoup物件.select('html head title')
           
"""
ex:
html = '''
<html><head><title>網頁標籤</title></head>
<p class="header"><h2>文件標題</h2></p>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
'''

from bs4 import BeautifulSoup
sp = BeautifulSoup(html, 'html.parser')
#sp 就是 BeautifulSoup取得的網頁程式碼內容
print(sp.title)
#sp.title 可以取得網頁的標題內容
print(sp.find('h2'))
#找出h2標籤的內容
print(sp.find_all('a'))
#讀取所有a標籤的內容
print(sp.find_all("a", {"class":"red"}))
#讀取所有a標籤中,屬性class等於red的內容
data1 = sp.find("a", {"href": "http://example.com/one"})
#找出a標籤當中屬性href是相同網址的內容
print(data1.text)
data2 = sp.select("#link1")
#找出 標籤是 link1 的內容 => 傳回的是串列 =>id是唯一值
print(data2[0].text)
#印出 data2串列的[0]的內容
print(data2[0].get("href"))
#用get讀取 data2串列的[0]得網址
print(data2[0]["href"])
#印出data2串列的[0]的網址
print(sp.find_all(['title','h2']))
#標籤是title跟h2的 內容
print(sp.select('div img')[0]['src'])
#透過select讀取div標籤中的img標籤中的src屬性
    
    
"""
瀏覽器自動化操作: selenium
=> 藉由程式指令,自動操作網頁
=> 使用: 1.安裝 selenium模組 => pip install selenium
        2.下載並解壓縮 chrome webdriver 
=>取得網業元素:
    .find_element_by_id (元素id)
    .find_element_by_name (元素名稱)
    .find_element_by_tag_name (元素標籤名)
    .find_element_by_css_selector (元素css選擇器)
    .find_element_by_link_text (元素連結文字)
"""    
ex: #自動登入FB
from selenium import webdriver
driver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe'
url = 'https://www.facebook.com/'
email = '帳號'
password = '密碼'
driver = webdriver.Chrome(driver_path)

driver.maximize_window()
#視窗最大化
driver.get(url)
#取得網址
driver.find_element_by_id('email').send_keys(email)
dirver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()  
                                          #^ .click 點滑鼠一下
ex: #自動開氣象局網站人後關閉
from selenium import webdriver
import time

deiver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe'
web = webdriver.Chrome(driver_path)
web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0)
#設定瀏覽器位置(原點在左上角)
web.set_window_size(700,700)
#設定視窗大小
time.sleep(5)
web.find_element_by_link_text('衛星').click()
#找到網頁文字'衛星'的連結,然後點一下
time.sleep(5)
web.close()

ex: #自動開yahoo搜尋
from selenium import webdriver
url = 'https://tw.yahoo.com/'
driver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe' 
browser = webdriver.Chrome(driver_path)
browser.get(url)

element = browser.find_element_by_id('UHSearchBox')
element.send_keys('Hello World')
sumbit = browser.find_element_by_id('UHSearchWeb').click()

ex: #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe' 
driver = webdriver.Chrome(driver_path)
driver.get('http://www.python.org')
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "NO results found." not in driver.page_source
print(driver.page_source)
#driver.close()
    
    
# assert 條件 -> 成立 則進去 做
#               不成立 呼叫例外  

ex: #IMDB  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("http://www.imdb.com/")
search_elem = driver.find_element_by_css_selector('#navbar-query')
dearch_elem.send_keys('The Shape of water')
time.sleep(3)
search_button_elem = driver.find_element_by_css_selector("#navbar-submit-button .navbarSprite")
search_button_elem.click()
time.sleep(3)
first_result_elem = driver.find_element_by_css_selector("#findSubHeader+ .findSection .odd:nth-child(1) .result_text a")
first_result_elem.click()
time.sleep(3)
rating_elem = driver.find_element_by_css_selector("strong span")
rating = float(rating_elem.text)
cast_elem =driver.find_element_by_css_selector(".itemprop .itemprop")
cast_list = [cast.text for cast in cast_elem]
driver.close()
print(rating, cast_list)

ex:
from selenium import webdriver
driver_path = r'C:\GitHub\python\PY-Learn\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("https://tw.finance.yahoo.com/")
more_rank_elem = driver.find_elem_by_css_selector('.yui-text-left .yui-text-left table tr:nth-child(1) .stext div a')
more_rank_elem.click()
price_rank_elem = driver.find_element_by_css_selector('.yui-text-left+ .yui-text-left tr:nth-child(5) a')
price_rank_elem.click()
top_100_elem = driver.find_element_by_css_selector('p a+ a')
top_100_elem.click()
ticker_name_elem = driver.find_element_by_selector('.name')
ticker_name = [tn.text for tn in ticker_name_elem]
#driver.clock()
print(ticker_name)
    
    
#========================================== 
#測試 是否跳過登入防護 回傳200表示過了!
import requests
from bs4 import BeautifulSoup

#url = 'https://www.armedbase.com.tw/shop/index.php?action=product_sort&prod_sort_uid=257'
url = 'https://www.armedbase.com.tw/member/index.php?action=trial_member_5885_login&b_action=product_sort&prod_sort_uid=257&r_byeurl=shop'
r = requests.get(url)
print(r.status_code)
print(r.text)
#========================================== 
#20200608
"""
3.資料分析
=>Pandas模組(資料存取)
  .功能:
      自動讀取網頁表格資料
      匯入外部資料
      資料修改
      資料排序
      繪製圖表
   .DataFrame:
      Pandas 資料儲存型態
      為一個二維資料結構
      格式: pandas.DataFrame(資料)
                             ^
                   (data, columns, index)
                   ^存放的二維資料     ^欄標題
                             ^列標題
   .DataFrame的資料儲存方法:
      .to_csv        儲存為CSV格式
      .to_excel      儲存為Excel格式
      .to_sql        儲存為SQLite格式
      .to_json       儲存為JSon格式
      .to_html       儲存為HTML格式 
   
    .資料讀取csv: read_csv方法
      pandas.DataFrame(data, columns, index_col =0)
                                        ^設定第一欄為index值
=>numpy模組:建立資料矩陣
    numpy.array(串列,串列,....)
    numpy.random.random((4,2)) -> 隨機0~1的4*2矩陣
    
=>Mayplotlib模組:
    .大多繪圖功能放在 matplotlib.pyplot中
    .主要功能:繪圖 x,y 座標圖
        通常將x,y放在串列中,傳給matplotlib繪圖
    .繪圖方法:
        模組名稱.plot(x座標串列,y座標串列)
                      ^color參數 ->彩色英文 預設值藍色
                                 ->16進位值(色彩) -> #00ff00(綠色)
                      ^linewidth = lw -> 線寬預設值 1
                      ^linestyle = ls -> 線的樣式: 預設實線
                                                  -  :實線
                                                  -- :虛線
                                                  -. :點虛線
                                                  :  :點線
        模組名稱.show()->顯示繪圖
        模組名稱.figure():繪圖畫面中可再容納多個小圖形
        模組名稱.subplot(列數,欄數,位置):將figure區域以欄列劃分並將子圖繪製在位置處
            1 2
            3 4
    .柱狀圖:(直條圖、直方圖)
        格式: 模組名稱.bar(x座標串列, y座標串列,其他參數)
        參數: align -> center 直條中央對齊座標刻度
                       edge   直條邊緣對齊座標刻度
             width -> 直條的寬度->正直的寬度往右,負值的寬度往左
    .numpy.linspace : 產生間隔數列
       格式: numpy.linspace(起始,終止,數量,其他參數)
      
    .圓餅圖: =>一組數據,適合表示數據百分佔比
       格式: 模組名稱.pie(資料串列,其他參數) 
                     ^預設為橢圓形  
      資料串列:
             size:資料串列
      參數:
          labels:資料標籤
          autopct:數值比分比格式 =>
                 格式: %格式%%
       
          labeldistance:資料標籤與圓心的距離是半徑的幾倍
          shadow:設定陰影
          startange:繪圖的起始角度       
          pctdistance:百分比文字與圓心的距離是半徑的幾倍
          explode:設定圓形分離區塊的距離,以串列設定對應至資料項目           

    .散布圖: Scatter(x, y, s, c, alpha, maker)
                    ^  ^  ^  ^色彩 ^    ^圖示
                    數據 數量   不透明度
                        格式
        因np.random.rand(整數int)=>需要整數
         x=產生的值若為浮點數(非整數)
        所以 x則以 *x.shape轉為int

"""
ex: #資料儲存方法
import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
#存放的二維資料
indexs = ['李大年','王大同','黃美娟','陳美玲']
#列標題
columns = ['國文','數學','英文','自然','社會']
#欄標題
df = pd.DataFrame(datas, columns = columns, index = indexs)
#帶入datas資料,建立成為DataFrame格式的資料
print(df)

df.to_csv(r'C:\GitHub\python\PY-Learn\pdout.csv', encoding = 'utf-8-sig')
# .to_csv 存成CSV檔 ->一般來說轉CSV機會非常多,一定要注意編碼


ex: #資料讀取csv: read_csv方法
import pandas as pd
rd = pd.read_csv(r'C:\GitHub\python\PY-Learn\pdout.csv', encoding = 'utf-8-sig', index_col =0)
print(rd)    

ex:
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
           #^建立numpy陣列(矩陣)2*3矩陣
print(arr)

ex:
ran_arr = np.random.random((4,2))
                #^建立隨機分布於0~1的4*2
print(ran_arr)                                                                     #^設定第一欄為index值

ex:
import matplotlib.pyplot as plt
listx = [1,5,7,9,13,16] #=>串列格式
listy = [15,50,80,40,70,50]  #=>串列格式
plt.plot(listx, listy)
plt.show()
    #^ .show->顯示繪圖

ex:
import matplotlib.pyplot as plt
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, label = 'Male')
                          #^圖例
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, color = 'red', linewidth = 5, linestyle = '--', label = 'Female')
                         #^預設為藍色      ^線寬預設值1    ^線的樣式           ^圖例      
plt.legend() #顯示圖例->搭配 label 用,不下lefend不會顯示 label
plt.xlim(0, 20)
    #^x軸範圍
plt.ylim(0, 100)
    #^y軸範圍
plt.title('Pocket Money')
    #^圖表標題
plt.xlabel('Age')
    #^x座標標題
plt.ylabel('Money')
    #^y座標標題
plt.show()

ex: #正弦波圖
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
        #^迴圈的range
y = np.sin(x)
        #^正弦
plt.title('sine wave form')
plt.plot(x, y)
plt.show()

ex: #四合一圖
import matplotlib.pyplot as plt
plt.figure()
#^劃分區域
plt.subplot(2, 2, 1)
plt.plot([0, 1],[0, 1])
plt.subplot(2, 2, 2)
plt.plot([0, 1],[0, 2])
plt.subplot(2, 2, 3)
plt.plot([0, 1],[0, 3])
plt.subplot(2, 2, 4)
plt.plot([0, 1],[0, 5])
plt.show()


ex: #直條圖(柱狀圖)
from matplotlib import pyplot as plt
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x, y, align = 'center')
plt.bar(x2, y2, color = 'g', align = 'center')
                              #^對齊   #^中央對齊座標刻度
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

ex:
import matplotlib.pyplot as plt
x = ['bk','sw','ph','rd','gu']
a = [8, 7, 1, 6, 5]
b = [12, 2, 9, 5, 3]
plt.bar(x, a, label = 'a', align = 'edge', width = 0.3)
plt.bar(x, b, label = 'b', align = 'edge', width = -0.3)
plt.show()


ex:
import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
y = 2 * x + 5
plt.title('Matplotlib demo')
plt.xlabel('X axis caption')
plt.ylabel('Y axis caption ')
plt.plot(x, y, 'hm') #o -> 圓標記 , b ->藍色
plt.show()           #s -> 實心方塊 r ->紅色
                     #p -> 五邊形   g ->綠色
                     #v -> 倒三角   y ->黃色
                     #^ -> 正三角   w ->白色 
                     #* -> 星型     k ->黑色
                     #H,h ->六邊型  m ->洋紅色
                     #             c ->青色

ex:
import numpy
x = numpy.linspace(1, 10, 20)
print(x)

ex:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 50)
print(x)
y1 = 2 * x + 1
y2 = x ** 2
plt.plot(x, y1)
plt.show()
plt.plot(x, y2)
plt.show()

ex:
import matplotlib.pyplot as plt
labels = 'A','B','C','D','E','F'
size = [35, 52, 12, 17,62,48]
plt.pie(size, labels = labels, autopct = '%1.1f%%')
       #^資料串列 ^資料標籤      ^數值百分比格式=>格式: %格式%%
plt.axis('equal')
plt.show()

ex:
import matplotlib.pyplot as plt

#===設定python系統的字形樣式(對中文顯示問題)
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '12'}
plt.rc('font', **font) 
plt.rc('axes',unicode_minus=False) #解決坐標軸負數的-號顯示問題
#===設定python系統的字形樣式
labels = ["東部", "南部", "北部", "中部"]
sizes = [5, 10, 20, 15]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.05, 0) 
plt.pie(sizes, explode = explode, labels = labels, colors = colors,\
               #^設定圓形分離區塊的距離,以串列設定對應至資料項目 
    labeldistance = 1.1, autopct = "%3.1f%%", shadow = True,\
    #^資料標籤與圓心的距離是半徑的幾倍             ^設定陰影
    startangle = 90, pctdistance = 0.6)
    #^繪圖的起始角度    ^百分比文字與圓心的距離是半徑的幾倍
plt.axis("equal")
plt.legend(loc = 'lower right', fontsize = 12)
           #^位置  ^左下角
plt.show()

ex: #散布圖 :Scatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#Fixing random state for reproducibility
np.random.seed(20180731)
                #^設定亂數種子,讓亂數更亂,讓亂數更加不可被預測

x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
#x=產生的值若為浮點數(非整數)
#因np.random.rand(整數int)=>需要整數
#所以 x則以 *x.shape轉為int
s = np.random.rand(*x.shape) * 800 + 500

plt.scatter(x, y, s, c = 'g', alpha = 0.5, marker = r'$\clubsuit$', label = 'Luck')
plt.xlabel('Leprechauns')     #^透明度=>0.5->半透明        ^python內建圖示
                                             #^maker=>圖標
plt.ylabel("Gold")
plt.legend()
plt.show()

ex:
import matplotlib.pyplot as plt
x = [1, 2, 4, 6, 8, 1, 2, 9, 3]
y = [5, 7, 2, 3, 1, 4, 6, 5, 8]
plt.scatter(x, y)
plt.show()

ex:
import matplotlib.pyplot as plt
x = [1, 2, 4, 6, 8, 1, 2, 9, 3]
y = [5, 7, 2, 3, 1, 4, 6, 5, 8]
plt.scatter(x, y, s = [150 for i in range(len(x))], c = 'r', alpha = 0.5)
plt.title('Scatter Simple')
plt.xlabel('X axes')
plt.ylabel('Y axes')
plt.show()

ex:
import csv
from datetime import datetime  #處理日期時間
from matplotlib import pyplot as plt

filename = r'C:\GitHub\python\PY-Learn\death_valley_2014.csv' #資料皆為處理過的整齊乾淨的資料
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            #將CSV裡的日期時間轉成字串格式
            high = (int(row[1])-32) * 5 / 9
            #華氏轉攝氏
            low = (int(row[3])-32) * 5 / 9
            #華氏轉攝氏
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
fig = plt.figure(dpi = 128, figsize = (5, 3))
                           #^設定繪圖區域的大小 5行3列
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
    #^兩個繪圖圖形之間的區域填塞
title = 'Dauly high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

#=========================================
#20200610
ex:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x, y1, label = "$ y = sin(x) $")
plt.plot(x, y2, label = "$ y = sin(2 * x) $")
plt.legend(loc = 3)
#plt.fill_between(x, y1, y2, facecolor = 'blue', alpha = 0.1)

plt.show()


ex:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.fill(x, y1, color = "g", alpha = 0.3)
plt.fill(x, y2, color = "b", alpha = 0.3)
   #^.fill 填充會圖區域的顏色 
#plt.legend(loc = 3)
#plt.fill_between(x, y1, y2, facecolor = 'blue', alpha = 0.1)

plt.show()


ex:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x, y1, c = "g")
plt.plot(x, y2, c = "r")
#plt.legend(loc = 3)
plt.fill_between(x, y1, y2, facecolor = 'yellow')
    #^兩個繪圖圖形之間的區域填塞
plt.show()


ex:
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 4.0 * np.pi, 0.01)
#產生模擬資料
y = np.sin(x)

plt.plot(x, y)
plt.plot((x.min(), x.max()), (0,0))
#繪製水平基準線
plt.xlabel('x')
plt.xlabel('y')

plt.fill_between(x, y, where = (2.3 < x) & (x < 4.3) | (x > 10), facecolor = 'purple')
#兩繪圖之間的部分填塞    #^繪圖的條件式      ^and        ^ or
plt.fill_between(x, y, where = (7 < x) & (x < 8), facecolor = 'green')
#兩繪圖之間的部分填塞
plt.show()

#=====================================
"""
影像辨識
=>openCV
  安裝: pip install opencv-python
=>讀取影像:imread()
  格式: cv2.imread(檔案名稱,flag)
                          ^檔案類型->彩色:IMREAD_COLOR(1)-3頻道
                                    灰階:IMREAD_GRAYSCALE(0)-2頻道
                                    所有的影像頻道(包含透明度):IMREAD_UNCHANGED(-1)
  imread讀取:
      讀取的資料會儲存成一個numpy的陣列(串列)=>[[0],[1],[2]]
      陣列的前2個維度維圖片的高度,寬度=>[0],[1]
      img.shapes[0] =>圖片垂直高度 =>行
      img.shapes[1] =>圖片的水平寬度 =>列
      img.shapes[2] =>channel數
      第三個維度試圖片色彩 channel -> [2]
                   RGB圖片:channel = 3
                  灰階圖片:channel = 2
                                 
=>視窗命名: cv2.namedWindow(視窗名稱, 參數)
    參數: cv.WINDOW_NORMAL =>視窗可調整大小
=>顯示影像: cv2.imshow(視窗名稱, 顯示的影像)   
=>關閉視窗: cv2.destoryWindow(視窗名稱)
  關閉所有視窗: cv2.destoryAllWindow()
=>按鍵等待: cv2.waitKey(delay) =>視窗等待按鍵關閉

=>讀取影像: imwrite      
  格式: cv2.imwrite(寫入的檔案名稱,要寫入的檔案)   

=>繪圖:
    .共同參數:
        img -> 要繪製圖形的影像
        color ->色彩 (使用BGR模型)不同一般RGB,剛好相反 要注意!
                以數組型態儲存,如(255,0,0) = Blue
        thickness -> 線條粗細,預設1
        linetype -> 線條類型
    .畫線:
        格式: cv2.line(img,  起點座標, 終點座標, color, thickness, linetype)


=>資料擷取:<--->目的網站->防護、網頁改版     

 -> np.zeros(): 建立一個所有數值都是0的數組
       numpy.zeros((512, 512, 3), np.uint8)
       建立512 x 512大小的影像圖片,每一格中有3個元素都是0(BRG)->黑色,由imshow讀入
       參數: np.uint8 -> 無號的8為元整數
    .畫矩形:
        格式: cv2.rectangle(img, 頂點1, 頂點2, color, thickness, linetype)
 -> np.ones(): 建立一個所有數值都是1的數組
       numpy.zeros((512, 512, 3), np.uint8)
       建立512 x 512大小的影像圖片,每一格中有3個元素都是1(BRG)->白色,由imshow讀入
       參數: np.uint8 -> 無號的8位元整數     
       
       np.zeros(a,b,3)->黑色
       np.ones(a,b,3)*255 ->白色
       
     .畫圓:
         格式: cv2.circle(img, 圓心, 半徑, color, thickness, linetype)
                     ^參數必為整數              ^-1 => 填滿
     
     .畫橢圓:
         格式: cv2.ellipse(img, 圓心, (軸1, 軸2), 旋轉角度, 圓弧起始角度, 圓弧結束角度, color, thickness, linetype)
                                                            S = 0,    e=360 => 完整橢圓
                                                            s = 0,    e=180 => 半橢圓         
        
 -> round函數: => 將數值取小數位的四捨五入值
     格式: round(數值,小數位數)
                      ^預設為整數位
                      
      .畫多邊形:
          格式: cv2.polylines(img, 頂點座標, isClosed, color, thickness, linetype)
                                            ^布林值    
            頂點座標必須是一個陣列(串列)
            其資料型態必須為 numpy.int32
            繪圖前必須以reshape重新計算調整
                               ^頂點
        步驟:
        建立頂點座標:
        1. x = numpy.array([[a,b],[c,d],...], numpy.int32)
        2. y = x.reshape(頂點數量,1,2)
                          ^頂點數量通常設為-1 -> 由其他參數機算得出
        3. cv2.polylines(img, [y], isClosed, color, thickness, linetype)


     .寫文字:
         格式: cv2.putText(img, 文字, 座標, 字型, 大小, color, thickness, linetype, bottomLeftOrigin)
                                                                                  ^文字映射(True/False)
         使用自訂字型:
             載入 PIL 模組下的:
              1. ImageFont -> ImageFont.truetype
                                   ^載入字體
              2. Image -> Image.fromarray
                           ^將numpy陣列轉為PIL影像
              3. ImageDraw -> ImageDraw.Draw
                               ^在PIL影像上寫文字
              4.使用text方法以設定的字型及大小寫入文字

"""

ex: #用python方法讀檔

import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena_01.jpg')
#opencv不支援中文路徑
cv.namedWindow('image')
cv.imshow('image', img)
#img1 = cv.imread(r'C:\GitHub\python\PY-Learn\lena.jpg')
#cv.namedWindow('image1')
#cv.imshow('image1', img1)

cv.waitKey()

ex: #用python方法寫入

import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\tpe101.jpg', 0)
                                                        #以灰階模式開啟(轉灰階)       
cv.namedWindow('image')
#cv.namedWindow('image', cv.WINDOW_NORMAL)
                         #^視窗可調整大小
cv.imshow('image', img)
x = cv.waitKey()
if x == 27: # 27-> ASCII碼 = Esc鍵
    cv.destroyAllWindows()
elif x == ord('s'): #按 s 鍵
    cv.imwrite(r'C:\GitHub\python\PY-Learn\tpe101gray.jpg',img)
               
    cv.destroyAllWindows()  


ex: #用numpy方法畫圖框和線

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
       #^建立512 x 512大小的影像圖片,每一格中有3個元素都是0(BRG)->黑色,由imshow讀入
                             #^無號的8位元整數
cv.line(img, (0, 0),(511, 511),(255, 0, 0), 5)
cv.imshow('img', img)
cv.waitKey()


ex: #用numpy方法畫圖框和線

import cv2 as cv
import numpy as np 
n = 300
img = np.zeros((n + 1, n + 1, 3), np.uint8)
img = cv.line(img, (0, 0), (n, n), (255, 0, 0), 3)
img = cv.line(img, (0, 100), (n, 100), (0, 255, 0), 1)
img = cv.line(img, (100, 0), (100, n),(0, 0, 255), 6)
cv.imshow("image", img)
cv.waitKey()



ex: #畫矩形

import cv2 as cv
img = np.zeros((512, 512, 3), np.uint8)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)
cv.imshow('image', img)
cv.waitKey()


ex: #畫矩形

import cv2 as cv
import numpy as np 
n = 300
img = np.ones((n, n, 3), np.uint8) * 255 # np.ones = 1 * 255 (經運算) -> 白色
       #^建立512 x 512大小的影像圖片,每一格中有3個元素都是1(BRG)->白色,由imshow讀入
                             #^無號的8位元整數
cv.rectangle(img, (50, 0), (n-100, n-50), (0, 0, 255), -1) # -1 -> 填滿
cv.imshow('image', img)
cv.waitKey()


ex: #畫圓

import cv2 as cv
import numpy as np 
img = np.zeros((512, 512, 3), np.uint8)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1) # -1 -> 填滿
cv.imshow('image', img)
cv.waitKey()



ex: #畫同心圓1

import cv2 as cv
import numpy as np 
img = np.zeros((512, 512, 3), dtype ='uint8')
                         #^channel = 3 =>彩色
for r in range(0, 175, 25):
    cv.circle(img, (img.shape[1] // 2, img.shape[0] // 2), r, (255, 255, 255))
    #取得中心點,(img.shape[1] // 2, img.shape[0] // 2)
cv.imshow('image', img)
cv.waitKey()


ex: #畫同心圓2

import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d, d, 3), dtype ='uint8') * 255

(centerX, centerY) = (round(img.shape[1] / 2), round(img.shape[0] / 2))                       
red = (0, 0, 255)      #^用round取整數
for r in range(5, round(d / 2), 12):
    cv.circle(img, (centerX, centerY), r, red, 3)

cv.imshow('image', img)
cv.waitKey()


ex: #畫橢圓1

import cv2 as cv
import numpy as np 

img = np.zeros((512, 512, 3), np.uint8)
img.fill(200)

cv.ellipse(img, (180, 200), (100, 60), 45, 0, 360, (128, 0, 255), 2)
cv.ellipse(img, (180, 200), (50, 100), 45, 0, 180, (255, 0, 128), -1)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()


ex: #畫橢圓2

import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d, d, 3), np.uint8) * 255

center = (round(d / 2), round(d / 2))
size = (100, 200)
for i in range(0, 10):
    angle =np.random.randint(0, 361)
    
    color = np.random.randint(0, high = 256, size = (3, )).tolist()
    thickness = np.random.randint(1, 9)
    cv.ellipse(img, center, size, angle, 0, 360, color, thickness)

cv.imshow('image', img)
cv.waitKey()


ex: #畫多邊形

import cv2 as cv
import numpy as np 

img = np.zeros((512, 512, 3), np.uint8)
pts = np.array([[10, 5], [60, 90], [130, 80], [110, 70]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

cv.imshow('image', img)
cv.waitKey()

ex: #寫文字1
    
import cv2 as cv
import numpy as np 
img = np.zeros((512, 512, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)
                                                                   #^反鋸齒處理
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()


ex: #寫文字2
    
import cv2 as cv
import numpy as np 
img = np.zeros((512, 512, 3), np.uint8)
img.fill(64) #把每一個向點填滿 64的顏色
text = 'OpenCV for Python' #寫入文字

cv.putText(img, text, (10, 40), cv.FONT_HERSHEY_SIMPLEX,
           1, (0, 255, 255), 1, cv.LINE_AA)
cv.putText(img, text, (10, 80), cv.FONT_HERSHEY_PLAIN,
           1, (0, 255, 255), 2, cv.LINE_AA)
cv.putText(img, text, (10, 120), cv.FONT_HERSHEY_DUPLEX,
           1, (0, 255, 255), 1, cv.LINE_AA)
cv.putText(img, text, (10, 160), cv.FONT_HERSHEY_COMPLEX,
           1, (0, 255, 255), 2, cv.LINE_AA)
cv.putText(img, text, (10, 200), cv.FONT_HERSHEY_TRIPLEX,
           1, (0, 255, 255), 1, cv.LINE_AA)
cv.putText(img, text, (10, 240), cv.FONT_HERSHEY_COMPLEX_SMALL,
           1, (0, 255, 255), 2, cv.LINE_AA)
cv.putText(img, text, (10, 280), cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
           1, (0, 255, 255), 1, cv.LINE_AA)
cv.putText(img, text, (10, 320), cv.FONT_HERSHEY_SCRIPT_COMPLEX,
           1, (0, 255, 255), 2, cv.LINE_AA)
#所有字型
                                                                  
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()

ex: #寫文字3-描邊
    
import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d, d, 3), np.uint8) * 255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (0, 200), font, 3, (0, 255, 0), 15)
cv.putText(img, 'OpenCV', (0, 200), font, 3, (0, 0, 255), 5)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()


ex: #寫文字4-描邊
    
import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d, d, 3), np.uint8) * 255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (20, 150), font, 3, (0, 255, 0), 15, cv.LINE_AA)
cv.putText(img, 'OpenCV', (20, 220), font, 3, (0, 0, 255), 15, cv.FONT_HERSHEY_SCRIPT_SIMPLEX, True)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()


ex: #寫文字5-自訂字型
 
from PIL import ImageFont, ImageDraw, Image
import cv2 as cv
import numpy as np 
img = np.zeros((512, 512, 3), np.uint8)
img.fill(64)

img[:] = (0, 0, 192) #背景顏色
text = '恭賀\n新囍'

fontPath = r'C:\GitHub\python\PY-Learn\TaipeiSansTCBeta-Bold.ttf'

font = ImageFont.truetype(fontPath, 224)

imgPil = Image.fromarray(img) #將numpy陣列轉PIL影像

draw = ImageDraw.Draw(imgPil) #在PIL影像上寫文字

draw.text((30, 30), text, font = font, fill = (0, 0, 0, 0))
                                                #^填滿黑色,第4個0為透明度

img = np.array(imgPil) #將PIL影像轉回numpy陣列
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()

#cv.waitKey(1000)
#cv.destroyAllWindows()

#x = cv.waitKey()
#if x == 27:
#    cv.destroyAllWindows()

#=====================================
#20200615
"""
Pandas:

=>專為Python編寫的外部模組，執行數據處理及分析

=>主要資料結構: panel, dataframe, series
               ^---Pandas名稱由來---^

=>Series:
    .一維資料結構(類似二維)
    .可存放整數、浮點、字串、Python物件
    .類似Python list、具有索引結構

  格式: pandas.Series(data, index, dtype, name....)
              .concat(): 資料合併
                 .concat 參數 axis(預設為0)=>直向排列
                 .concat 參數 axis(設為1)=>類似二維排列
    .資料結構方法: columns
       格式:資料.columns = columns名稱   
    .以 name 參數指定 columns
       格式: series資料.name = 名稱
           資料在concat時以名稱作為columns名

=>Dataframe:
    .為二維資料結構.
    .可存放整數、浮點數、字串、Python物件...
    .格式:
        pandas.DataFrame(data, index, dtype, name....)
    
    .DataFrame資料建立:
       .字典的串列 [{...}{...},{...},....]
          字典key若無對應,則對應出將填入 NaN (無資料,空白之意)
       .字典 {key:values}
         .以index屬性設定為row
         .將字典內的元素設為index
       .以Numpy建立DataFrame

=>寫入CSV檔案:  資料構成->以列row為主,每一列即一筆資料!
    csv: Comma Separated Values
    .以 to_csv() 將 DataFrame物件寫入csv檔案
    .格式: 
        to_csv(path, spe, header, index, encoding,....)

         .path     : 檔案路徑
         .spe      : 分隔符號,預設為逗號
         .header   : 是否保留 header,預設為True (欄)
         .index    : 是否保留 index, 預設為True (列)
         .encoding : 檔案編碼
         
=>讀取CSV檔案:  
    .以 read_csv() 將csv檔案讀入(也可以讀取txt檔)
    .格式: 
        read_csv(path, spe, header, encoding, index_col, usecols, nrows)

         .path     : 檔案路徑
         .spe      : 分隔符號,預設為逗號
         .header   : 設定哪一個row為欄位座標
         .encoding : 檔案編碼         
         .index_col: 欄位column索引
         .usecols  : 讀取欄位
         .nrows    : 讀取列

=>繪圖:
    .將數據建立為Series 以 Pandas繪圖
    .Pandas繪圖使用plot()方法
    .將數據建立為DataFrame以Pandas繪圖
    .繪圖->plot() + plt() => matplotlib.pyplot
    .kind : 繪圖模式 => kind = 'bar' => 直條圖 ,預設值 = 'line' =>直條圖
    
    .左邊、下面=主座標軸  右邊、上面=副座標軸 => 多軸座標 
    
    .fig:整體圖表物件
    .ax :第一個軸
    .subplots :在同一個圖表中繪製不同軸的數據
    .fig.suptitle:標題
    .ax.set_ylabel:設定Y軸標題文字
    .ax.set_xlabel:設定X軸標題文字
    .ax.twinx:產生一個新軸
    .rot : 旋轉座標刻度(文字方向)

  =>圓形(餅)圖: autopct %格式%%
      .只能一組數據
      .數值格式化為百分比
      .切開圓形圖 explode

=>時間序列:
    .數據由時間順序列出
    .時間為一個系列的時間戳記
    .匯入時間模式: from datetime import datetime
       .now() => 取得目前日期、時間
    .設定特定時間:
        格式: 時間 = datetime.datetime(年,月,日,時,分,秒)
    .時間區間: (一段時間)
        格式: 時間 = datetime.timedelta(weeks,days,hours,minutes,seconds)
  
  =>日期範圍 : date_range(起始日期,終止日期)
     
      
"""
ex: #各城市三年的三月份平均溫度
import pandas as pd
years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index = years)
hongkong = pd.Series([25, 26, 27], index = years)
singapore = pd.Series([30, 29, 31], index = years)
             #^建立Series格式資料      ^years當索引
#^透過index = 2020、2021、2022 自動對應前面的data 
citydf = pd.concat([beijing, hongkong, singapore])
#^資料合併 => 現在為預設 =>預設合併為直向合併 
print(type(citydf))
print(citydf)
print(hongkong)

ex: #各城市三年的三月份平均溫度
import pandas as pd
years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index = years)
hongkong = pd.Series([25, 26, 27], index = years)
singapore = pd.Series([30, 29, 31], index = years)

citydf = pd.concat([beijing, hongkong, singapore], axis = 1)
#將以上三個Series資料合併,非直向排列                   ^axis(設為1)=>類似二維排列
print(type(citydf))
print(citydf)

    
ex: #各城市三年的三月份平均溫度
import pandas as pd
years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index = years)
hongkong = pd.Series([25, 26, 27], index = years)
singapore = pd.Series([30, 29, 31], index = years)
citydf = pd.concat([beijing, hongkong, singapore], axis = 1)
#將以上三個Series資料合併,非直向排列 
cities = ['北京(Beijing)', '香港(Hongkong)', '新加坡(Singapore)']
#建立一串列列資料
citydf.columns = cities
#將一個串列資料以columns設定為 cities                                        
print(citydf)   
    

ex: #各城市三年的三月份平均溫度
import pandas as pd
years = range(2020, 2023)
beijing = pd.Series([20, 21, 19], index = years)
hongkong = pd.Series([25, 26, 27], index = years)
singapore = pd.Series([30, 29, 31], index = years)
beijing.name = 'Beijing'
hongkong.name = 'Hongkong'
singapore.name = 'Singapore'
#用.name方式來,在concat時不需要設定columns,就會自動帶入name
citydf = pd.concat([beijing, hongkong, singapore], axis = 1)
#將以上三個Series資料合併,非直向排列                                     
print(citydf)  

ex:
import pandas as pd
data = [{'apple' : 50, 'Orange' : 30, 'Grape' : 80}, {'apple' : 50, 'Grape' : 80}]
fruits = pd.DataFrame(data)
print(fruits)

ex:
import pandas as pd
cities = {'country' : ['China', 'Japan', 'Singapore'],
          'town' : ['Beijing', 'Tokyo', 'Singapore'],
          'population' : [2000, 1600, 600]}
citydf = pd.DataFrame(cities)
print(citydf)

ex: #以index屬性設定為row
import pandas as pd
cities = {'country' : ['China', 'Japan', 'Singapore'],
          'town' : ['Beijing', 'Tokyo', 'Singapore'],
          'population' : [2000, 1600, 600]}
rowindex = ['first', 'second', 'tird']
citydf = pd.DataFrame(cities, index = rowindex)
print(citydf)

ex: #將字典內的元素設為index
import pandas as pd
cities = {'country' : ['China', 'Japan', 'Singapore'],
          'town' : ['Beijing', 'Tokyo', 'Singapore'],
          'population' : [2000, 1600, 600]}
citydf = pd.DataFrame(cities, columns = ['town','population'],
                      index = cities['country'])
print(citydf)


ex:
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns = ['x', 'y', 'z', 's'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns = ['x', 'y', 'z', 's'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns = ['x', 'y', 'z', 's'])

print(df1)
print(df2)
print(df3)


ex:
import pandas as pd
import numpy as np
name = ['Frank', 'Peter', 'John']
score = ['first', 'second', 'final']
df = pd.DataFrame(np.random.randint(60, 100, size = (3, 3)), columns = name, index = score)
#建立3*3陣列，每一格的數據在60~99之間
print(df)


ex:
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame([chinese, eng, math, nature, social], columns = course,
                  index = range(1,6))
df.to_csv(r'C:\GitHub\python\PY-Learn\out_a.csv')
df.to_csv(r'C:\GitHub\python\PY-Learn\out_b.csv', header = False, index = False) 
                                                  #^ header和index都設False,表示不要欄列標題          

ex:
import pandas as pd   
course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
x = pd.read_csv(r'C:\GitHub\python\PY-Learn\out_a.csv', index_col = 0)
y = pd.read_csv(r'C:\GitHub\python\PY-Learn\out_b.csv', names = course)
print(x)
print(y)


ex: #1950~2010 台灣人口統計數字,單位 萬人
#建立 Series方法
import pandas as pd  
import matplotlib.pyplot as plt

population = [800, 1100, 1450, 1800, 2020, 2200, 2260]
tw = pd.Series(population, index = range(1950, 2011, 10))
#建立 Series物件
tw.plot(title = 'Population in Taiwan')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()                                      


ex: #世界人口統計圖
#以建立DataFrame方法
import pandas as pd  
import matplotlib.pyplot as plt

cities = {'population' : [1000, 850, 800, 1500, 600, 800],
         'town' : ['New York', 'Chicago', 'Bangkok', 'Tokyo',
                   'Singapore', 'Hongkong']}
#字典格式{[]:[]}
tw = pd.DataFrame(cities, columns = ['population'], index = cities['town'])
#建立 DataFarme物件
tw.plot(title = 'Population in the World')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()


ex: #世界人口統計圖 => 直條圖
import pandas as pd  
import matplotlib.pyplot as plt

cities = {'population' : [1000, 850, 800, 1500, 600, 800],
         'town' : ['New York', 'Chicago', 'Bangkok', 'Tokyo',
                   'Singapore', 'Hongkong']}
tw = pd.DataFrame(cities, columns = ['population'], index = cities['town'])

tw.plot(title = 'Population in the World', kind = 'bar')
                                           #^直條圖呈現
plt.xlabel('City')
plt.ylabel('Population')
plt.show()


ex: #世界人口統計圖->兩筆資料
import pandas as pd  
import matplotlib.pyplot as plt

cities = {'population' : [1000, 850, 800, 1500, 600, 800],
          'area' : [400, 500, 850, 300, 200, 320],
         'town' : ['New York', 'Chicago', 'Bangkok', 'Tokyo',
                   'Singapore', 'Hongkong']}
tw = pd.DataFrame(cities, columns = ['population', 'area'], index = cities['town'])

tw.plot(title = 'Population in the World')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()


ex: #世界人口統計圖->兩筆資料 單位 1人 =>錯誤示範
import pandas as pd  
import matplotlib.pyplot as plt

cities = {'population' : [10000000, 8500000, 8000000, 15000000, 6000000, 8000000],
          'area' : [400, 500, 850, 300, 200, 320],
         'town' : ['New York', 'Chicago', 'Bangkok', 'Tokyo',
                   'Singapore', 'Hongkong']}
tw = pd.DataFrame(cities, columns = ['population', 'area'], index = cities['town'])

tw.plot(title = 'Population in the World')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()

ex: #世界人口統計圖->兩筆資料 單位 1人=>多座標軸示範
import pandas as pd  
import matplotlib.pyplot as plt

cities = {'population' : [10000000, 8500000, 8000000, 15000000, 6000000, 8000000],
          'area' : [400, 500, 850, 300, 200, 320],
         'town' : ['New York', 'Chicago', 'Bangkok', 'Tokyo',
                   'Singapore', 'Hongkong']}
tw = pd.DataFrame(cities, columns = ['population', 'area'], index = cities['town'])

fig, ax = plt.subplots()
#^整體圖表物件   ^在同一個圖表中繪製不同軸的數據
    #^第一個軸
fig.suptitle('City Statistics')
#^圖表標題
ax.set_ylabel('Popylation')
#第一個軸的 y座標,標題文字
ax.set_xlabel('City')
#第一個軸的 X座標,標題文字

ax2 = ax.twinx()
       #^產生一個新軸
ax2.set_ylabel('Area')
#新軸的 y座標,標題文字
tw['population'].plot(ax = ax, rot = 90)
                               #^旋轉座標刻度(文字方向) = 90度
tw['area'].plot(ax = ax2, style = 'r-')
                             #^樣式=>顏色
ax.legend(loc = 1)
#^圖例     ^位置=> 1=右上  
ax2.legend(loc = 2)
#^圖例     ^位置=> 2=左上  
plt.show()


ex: #圓形圖
import pandas as pd
import matplotlib.pyplot as plt

fruits = ['Apple', 'Bananas', 'Grapes', 'Pears', 'Qranges']
s = pd.Series([2300, 5000, 1200, 2500, 2900], index = fruits, name = 'Fruits Shop')

explode = [0.4, 0, 0, 0.2, 0]
s.plot.pie(explode = explode, autopct = '%1.2f%%')
plt.show()


ex:
from datetime import datetime
tn = datetime.now()
print(type(tn))
print('現在時間:', tn)


ex:
from datetime import datetime
timeNow = datetime.now()
print(type(timeNow))
print('現在時間:', timeNow)
print('年     :', timeNow.year)
print('月     :', timeNow.month)
print('日     :', timeNow.day)
print('時     :', timeNow.hour)
print('分     :', timeNow.minute)
print('秒     :', timeNow.second)


ex:
import pandas as pd
from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)
dates = [start + timedelta(days = x) for x in range(0, ndays)]
#日期時間是可以做數學運算的 ^ start + 1~4 day
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index = dates)
print(type(ts))
print(ts)



ex:
import pandas as pd
from datetime import datetime, timedelta

ndays = 5
start = datetime(2019, 3, 11)
dates = [start + timedelta(days = x) for x in range(0, ndays)]
#日期時間是可以做數學運算的 ^ start + 1~4 day
data1 = [34, 44, 65, 53, 39]
ts1 = pd.Series(data1, index = dates)

data2 = [34, 44, 65, 53, 39]
ts2 = pd.Series(data2, index = dates)

addts = ts1 + ts2
print('ts1+ts2')
print(addts)

meants = (ts1 + ts2) / 2
print("(ts1+ts2)/2")
print(meants)


ex:
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('3/11/2019', '3/15/2019')
           #^日期範圍 date_range(起始日期,終止日期)
data = [34, 44, 65, 53, 39]
ts = pd.Series(data, index = dates)
ts.plot(title = 'Data in Time Series')
plt.xlabel('Date')
plt.ylabel('Data')
plt.show()


#====================================
"""
專案分析

鳶尾花資料集分析 (Iris)

=>數據分析中有名的資料集
=>為加州大學爾灣分校作為機器學習(machine learning)之常用資料集
=>數據資料150筆,包含以下:
    資料:
        花萼長度(sepal length)
        花萼寬度(sepal width)
        花瓣長度(petal length)
        花瓣寬度(petal width)
        類別(species, setosa, versicolor, virginica)

"""
=> step1:
    下載資料集並儲存為CSV檔
      原始檔 iris.data
#===       
import requests

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

try:
    htmlfile = requests.get(url)
    print('下載成功!')
except Exception as error:
    print('下載失敗 >< !')

fn = 'iris.csv'
with open(fn, 'wb') as fileobj:
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage)
    
#=== 
        
=> step2:
    讀取csv檔並轉換為DataFrame
    
   describe() => 可以顯示數據的數量(count 數量
                                  mean 平均值
                                  std 標準差
                                  min 最小值
                                  max 最大值
                                  25% 1/4分位數
                                  50% 1/2分位數
                                  75% 3/4分位數)

#=== 
import pandas as pd

colName = ['sepal_len', 'speal_wd', 'petal_len', 'petal_wd', 'species']
iris = pd.read_csv(r'C:\GitHub\python\PY-Learn\iris.csv', names = colName)
print('資料集長度 :', len(iris)) 
print(iris)
s = iris.describe()
         #^ 可以顯示數據的數量

print(s)    
    
#===   

=> step3:
    資料視覺化
    .直方圖

#===
#直方圖
import pandas

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal_length', 'speal_width', 'petal_length', 'petal_width', 'class']
dataset = pandas.read_csv(url, names = names)
print(dataset.describe())
dataset.hist()

#===   