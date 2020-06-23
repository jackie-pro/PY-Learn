# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:19:57 2020

@author: Jackie
"""


"""
資料結構
=>串列:list (等同資料容器，放資料用的)
  .一連串資料組成 (等同於陣列)
  .可存放不同型態的資料
  .以中括號前後括住資料,資料間以逗號隔開 => []
  .可以建構為多維串列(一維,二維.....)
    串列名稱[起始直 : 終止值]
              ^起始到中止-1的元素     
  .一維串列:
      .list:
"""
"""
  .串列資料取得:
      串列名稱[索引直]
               ^重0起算      
"""
"""
  .len函式:求串列長度(元素個數)
  
"""
"""
  .append()函式:加入元素(直接加在串列尾端)

     append(value)  將value加入到串列尾端

"""
"""
  .insert()函式:加入元素(可指定加入串列的位置)
     insert(index,value) 加入元素在指定索引處
            ^索引處  ^元素
"""
"""
  .remove()函式:移除指定值
    remove(value)  串列中如有多個相同值,只移除整個串列中第一個value值
    
"""
"""
  .count()函式:求串列值出現的次數 (value)
    count(value)

"""
"""
  .index():求串列值所在的索引
    index(value)
    

"""

"""
  .sort()函式:串列排序  #依UNICON碼由小到大
  
"""
"""
  .reverse()函式:串列元素反轉

"""
"""
  .in / not in:傳回布林值 (判斷元素是否 在/不在 串列中)

"""
"""
  .sum()函式:求串列元素總和
  .max()函式:求串列元素最大值
  .min()函式:求串列元素最小值

"""
"""
  .+:連結串列
  .*:複製串列
  
"""
"""
  .二維串列
    視為多個一維串列組成
    如5位學生,每位學生3科成績

st = [[85,68,73],[96,81,60],[87,77,58],[80,60,60],[75,81,55]]
        #^st[0]    ^st[1]     ^st[2]     ^st[3]     ^st[4]
        # ^----------^----------^----------^----------^ 5位學生
                           # ^--^--^ 3科成績 st[2][0]=87
                           #                st[2][1]=77
                           #                st[2][2]=58 => (二維串列)
[[1,2,3],[4,5,6]] 二維串列 = 2 x 3串列

"""
"""
=>元組(數組):tuple
  .與串列(list)類似
   不同如下:
    1.tuple內元素值不可改變
    2.無法刪除個別元素
    3.無法取代個別元素
    4.可刪除整個數組 #使用del刪除整個tuple
    5.以小括號建立tuple
    
"""
"""
=>集合:set  => 採自動排序 print 會看 hash map 的 bucket值
  .以大括號{} 建立
    s1 = {1,2,3}
    s2 = set()
    s3 = set([x for x in range(1,6)])
    print(s3)
    s4 = set((1,2,3))
    print(s4)
    
  .集合不包含重複資料
    s5 = set ((1,1,2,2,3))
    print(s5)
    
  .add(x):將X加入集合 (跟append一樣加到最後面)
    s10 = {1,3,6}
    s10.add(20)
    print(s10)
    
  .remove(x):將x從集合移除
    s10.remove(20)
    print(s10)
    del s10
    
  .聯集:union(集合) => | (符號)
    set20 = {1,6,8,10,20}
    set25 = {1,3,8,10}
    set20.union(set25)
    print(set20.union(set25))
    print(set20|set25)
    
  .交集:intersection(集合) => & (符號)
    print(set20&set25)
    
  .差集:difference(集合) => - (符號)
    print(set20-set25)
    
  .== :比較兩集合是否相等 (傳回布林值 True or False)
    print(set20==set25)
    
  .!= :比較兩集合是否不相等(傳回布林值 True or False)
    print(set20!=set25)
    
"""    
"""
=>詞典:dict
  .以大括號{}建立
  .資料已鍵值(key)及值(value)組成
  .格式: {key:value}
    dict1 = {'Taipei':'101','Paris':'Tour Eiffel','London':'Big Ben'}
    print(dict1)
    dict1['Berlin']='Wall'
    print(dict1['Taipei'])
    
    for key in dict1:
        print('%s %s' % (key, dict1[key]))
    
    del dict1['Taipei']
    
  .keys() : 列出key值
    dict1.keys()
    print(dict1.keys())
    
  .values() : 列出值
    dict1.values()
    print(dict1.values())
    
  .items() : 列出項目值
    dict1.items()
    print(dict1.items())
    
  tuple(dict1.items())
  print(tuple(dict1.items()))
  
"""
"""
資料結構整理:
=>串列:list
  .建立 -> 串列名稱 = [元素1,元素2,.....]
  .元素建立後即有索引值
  .索引值從0開始起算
    append:加入元素(元素可為資料,串列)
    extend:加入元素(元素為串列)

=>數組(元祖):Tuple
  .建立 -> 數組名稱 = (元素1,元素2,.....)
  .元數個數,元數值皆不可改變
    (其餘皆同串列)
    (不可使用append,insert)
  .串列功能比數組大
    優點:
        1.安全性
        2.執行數度比串列快 (因資料結構比較簡單(無法更改),所以執行速度比較快)

  .應用:串列與數組互相轉換
    轉換方式:
        數組轉換為串列 -> tuple1 = (1,2,3)
                        list1 = list(tuple1)
        串列轉換為數組 -> list2 = [4,5,6]
                        tuple2 = tuple(list2)
                        
=>字典(詞典):dict
  .建立:
      字典名稱 = {元素1,元素2,.....}
                 ^建值1:值1
                  key1:value
      字典名稱 = dict ([[key1,value1],[key2,value2],......])    
      
      字典名稱 = dict (key1=value1,key2=value2,......)
                      ^有限制: key值不可為數值
  .字典元素無一定的順序排列 
    (串列元素則為依序排列) --- 在記憶體中...
  .字典取值的方式: 字典名稱[key] 
    以key作為索引取得 value
      ^必須唯一       ^可重複
      ^若重複,則將key覆蓋,只有最後的key會存在
  .當key不存在,會產生錯誤
  .使用 get() 取得值 => 就算key不在也不會產生錯誤(若無key值,則得到None)
    格式: 字典名稱.get(key)
    列如:
        fruit = {'蘋果':15,'香蕉':10,'番茄':12}
        print(fruit.get('蘋果'))
        print(fruit.get('鳳梨'))
  .字典修改:
      字典名稱[key] = value
  .字典刪除:
      刪除特定元素: del 字典名稱[key]
      刪除所有元素: 字典名稱.clear()
      刪除字典: del 字典名稱
"""
"""
字串(srt)
=>Python 並無特別區分字元及字串,均以單,雙引號前後括住

=>建立空字串:
    s1 = str()
    s2 = ''
    
=>建立字串:
    s3 = str('這是Python程式設計')
    s4 = 'Today is rainy day'
    
=>len(字串名):字串長度(字元數)

=>max(字串名):字串最大值

=>min(字串名):字串最小值
    len(s4)
    max(s4)
    min(s4)
    
=>[位置數值] 可以取得字串的特定字元
  格式: 字串名[位置數值]  -> 位置數值從0開始算
    s4[3]
    s4[-5]  ->若為負值,則加上字串長度 # -5+18 =13 從0開始算
    
=>[起始值:終止值]
  取得從起始值~終止值-1的子字串
  格式: 字串名[起始值:終止值]
  s4[3:8]
  
=> + :串接
=> * :複製
  s5 = 'Simon'
  s6 = 'Lee'
  s5 + s6
  s5 * 2

=>字串測試: 字串名.函式()
  函式():傳回值為布林值 (True , False)
    .isalnum():字串是否為字元及數值
        s5.isalnum()
    
    .isalpha():字串是否為字元
        s5.isalpha()
    
    .isdigit():字串是否為數值
        s5.isdigit()
    
    .islower():字串是否皆為英文小寫
        s5.islower()
    
    .isupper():字串是否皆為英文大寫
        s5.isupper()
    
    .isspace():字串是否皆為空白字元
        s5.isspace()
        
=>子字串: 字串名.函式('子字串')
    .endswith('子字串'):字串尾端是否為子字串 -> 傳回值為布林值 (True , False)
   
    .startswith('子字串'):字串開頭是否為子字串 -> 傳回值為布林值 (True , False)
        s5.endswith('on')
        s5.startswith('Si')
   
    .find('子字串'): 字串中子字串的最小位置數值
        s5.find('o')    

    .rfind('子字串'): 字串中子字串的最大位置數值 (相同值取最後位置)
        s7='abcdeabcde'
        s7.rfind('e')
    
    .count('子字串'): 字串中子字串的個數
        s7.count('e')
  
=>字串轉換:
  .capitalize():將字串中第一個字元轉換為大寫,其餘為小寫
    字串名.capiyalize()

  .lower():將字串中所有字元轉換為小寫
    字串名.lower()
    
  .upper():將字串中所有字元轉換為大寫
    字串名.upper()
  
  .swapcase():將字串中的字元,大寫轉小寫,小寫轉大寫
    字串名.swapcase()
    
  .replace(str1,str2):將 str1 以 str2 取代  -> 常用會考
    字串名.replace(str1,str2) 

  .title():將字串中每一個單字第一個字元,轉為大寫,其餘為小寫
    字串名.title()
      s8 = 'welcome to taipei'
      s8.capitalize()
      s8.lower()
      s8.upper()
      s8.swapcase()
      s8.replace('taipei','taina')
      s8.title()
      s8

=>空白處理:字串名.函式()
  .lstrip():刪除字串左側空白
  .rstrip():刪除字串右側空白
  .strip():刪除字串左,右側空白
    s9 = '    welcome to taipei    '
    s9.lstrip()
    s9.rstrip()
    s9.strip()
    
=>對齊:
  .center(寬度值):
    將字串以寬度值置中對齊
    
  .ljust(寬度值):
    將字串以寬度值靠左對齊
    
  .rjust(寬度值):
    將字串以寬度值靠右對齊
      
    s10 = 'Taipei City'
    s10.center(20)
    s10.ljust(20)
    s10.rjust(20)
      
=>split():字串分割
  s11 = 'apple banana kiwi orange'   
  lst = s11.split() -> 預設以空白字元做分割字元
  lst
  s12 = '05-22-2020'
  lst1 = s12.split('-') -> 指定 - (減號)為分割字元
  lst1
  
  s12.replace('-','*')
"""
"""
檔案存取及例外處理
=>檔案運作的流程
  .使用open函式開啟檔案及設定模式
  .使用寫入函式寫入檔案或讀取函式讀取檔案
  .使用close函式關閉檔案

=>開啟檔案
  .open函式
  .格式:
      open(開啟的檔案,開啟模式)
  .開啟的檔案:檔案的"路徑"及檔案"全名"
  .開啟模式: w -> 寫入
            r -> 讀取
            a -> 附加
   例如:
    w(寫入) -> 檔案指標 指向檔案開頭,並清除掉原檔案的內容, 
              若檔案不存在,則建立新檔案
    a(附加) -> 檔案指標 指向檔案結尾,寫入資料附加在原檔案後方,
              若檔案不存在,則建立新檔案
    r(讀取) -> 檔案指標 指向檔案開頭,若檔案不存在,則發生錯誤
    
    #若檔案存取的是二進位檔案,則將開啟模式參數後加 小寫 b,
     (rb, wb , ab)

=>讀取及寫入:
  .寫入 -> write (寫入的資料)
  .讀取 -> read() -> 讀取所有內容
        -> readlines() -> 讀取所有內容
        -> readline() -> 讀取一行內容
        -> read(n) -> 讀取n個字元(指定要讀幾個字)

=>讀寫及開啟檔案的路徑:
  .檔案路徑若未指定,則以當時執行的系統預設路徑作為存取依據
    (未給路徑,只給檔名)
  .自訂路徑,程式碼撰寫時路徑分隔符號以 \\ 為主     

"""
"""
=>repr函式:印出轉義(逸脫)字元
  .即字串資料若包含轉義字元(如\n)則不執行轉義字元的功能,
   直接將其印出
  .w, r, a參數後可加入 " + " 符號,即 w+, r+, a+ -> 以讀寫模式開啟檔案
  .seek函式:移動指標
    格式: seek(offset,where)
      offset -> 移動byte數
      where -> 從哪裡開始移位
               0:檔頭
               1:目前位置
               2:檔尾
     #Python 結束執行 write 後 檔案指標式指定在 檔尾 !
               
"""
"""
=>二進位檔案存取
  .載入 pickle模組: import pickle
  .使用dump函式寫入二進位資料
  .使用load函式讀取資料
    #數值以二進位模式操作可加快其效率
  格式: pickle.dump (寫入的資料,寫入的檔案)
       pickle.load (讀取的檔案)
"""
"""
for: 定數迴圈(執行次數固定)
while:不定數迴圈(執行次數不固定)
"""

"""
=>例外(異常)處理
當程式出現異常運作時的處理機制
  try:
      程式執行主體
  except 異常型態(錯誤類型):  #當執行有錯時,執行下面處理方式
      處理方式

=>多例外(多異常)處理

  try:
      程式執行主體
  except 異常型態 1:
      處理方式 1
  except 異常型態 2:
      處理方式 2
      ...
      ...
      ...
  except 異常型態 n:
      處理方式 n
  except:                #當以上異常都未發生時執行
      處理方式 n+1
  else:                  #當沒有異常發生時執行
      處理方式 n+2
      
  finally:               #最後一定會執行
      處理方式 n+3    
      

"""
"""
=>彙總

print:
輸出單一項目,如變數,字串(元)...等
多個項目以逗點隔開 (不須設定格式)
輸出資料如需設定格式,則以 ('格式字串1 格式字串2.....' % (資料1,資料2...))
設定之。                   ^對齊,位數(總位數,小數),以%符號開頭
資料採對應方式,即資料對應到格式字串1,格式字串個數 = 資料個數

如: print('%d / %d = %d' % (6, 2, 3))

"""
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
"""
開放資料(Open Data)
=>政府資料開放平台:data.gov.tw
=>各部會資料平台:中央氣象局、環保署、健保屬、文化部

"""   

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


"""
擷取PPT熱門問題排行躲過 滿18歲 頁面 程式流程:
    1.查詢網頁表單傳送方式為post
    2.按鈕value值為yes
    以1.2. -> 以Python程式寫出進入網址,按下按鈕值
"""

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


