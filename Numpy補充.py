# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:08:34 2020

@author: Jackie
"""


#20200730
  



#------------------------------------------------------------------------------
'''Numpy
        多維陣列的高速運轉 
        應用於  機器學習,深度學習,影像處理,音訊處理
         (ex. 1000維像量 python迴圈運算 使用numpy速度約為不使用的50倍)
'''

import numpy as np

a =np.array([1,2,3])#.array 建立np陣列
type(a)#numpy.ndarray numpy的型別
print(a)#array([1, 2, 3])

a*3  #array([3, 6, 9])
a+2 #array([3, 4, 5])
#numpy 執行加減乘除的 會逐一地去對 每個元素進行運算
 
list_a=[1,2,3]
list_a*3
#python 不會逐一運算 只會複製

b =np.array([2,2,0])
a+b
a/b #會出錯 因為分母不可為0
a*b

np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#np.arange(起始,終止(終止前一個-1),間隔)

np.arange(0,10,2)

np.linspace(0,10,15) #.linspace 可以在一定範圍內來均勻地撒點 0~10 之間 產出15個點

c =np.array([[1,2,3],[4,5,6]])
# array([[1, 2, 3],
#        [4, 5, 6]])

c.shape #表示各維度大小的元組 
c.dtype #陣列資料類型的物件

# ----如要修改 任何修改都直接改了原陣列---------


#(2,4,3) ==   2組 4欄*3列 的陣列   (要要努力看到前面就會知道為這樣)

d=np.array([[ [1,2,3],[4,5,6],
              [7,8,9],[10,11,12] ],
            [ [13,14,15],[16,17,18],
              [19,20,21],[22,23,24] ]]) #(2,4,3)
d.shape

qd=np.array([[[ [1,2,3],[4,5,6],
              [7,8,9],[10,11,12]],
            [[13,14,15],[16,17,18],
              [19,20,21],[22,23,24] ]]]) #(1,2,4,3)
qd.shape

c.reshape(3,2) #進行矩陣形狀變化 3個為裡面的[]數量 2為裡面元素的數量
c  #方法不會改變原矩陣的資料、形狀等，而只是返回一個新的矩陣
#除非再指定回去給c  



#04 有沒有用numpy 處理速度差異  (結論 有差! 用了快)
import time
def c_time():
    a =np.random.randn(100000)
    b =list(a)
    start_t =time.time()
    for i in range(1000):
        sum1 =np.sum(a)
    print('使用numpy  %f 秒' %(time.time() - start_t))

    start_t =time.time()
    for i in range(1000):
        sum2 =np.sum(b)
    print('不不不使用numpy  %f 秒' %(time.time() - start_t))

c_time()#有(結論 有差! 用了快)
#------------------------------------------------------------------------------

#   ndarray : 以相同型別 相同大小構成的容器

b =np.array([[1,2,3],[4,5,6]])
b
b.T #.T陣列轉置 (長條的方式顯示)



#  軸axis /維度 dimension
#       [[x11,x12,x13],[x21,x22,x23]]

#   二維陣列(2,3)
#   二軸陣列:
#        第0軸(axis =0) ->第二個元素構成的陣列
#        第1軸(axis =1) ->二個子陣列內 各有三個元素

#   維度:　陣列每一軸所含的元素個數　稱為每一軸的維度

#   結論:
#       第0軸 ==2維         
#       第1軸 ==3維
#---------------------------------------------
#   axis =1 == ----->是水平往右 的方向
#   axis =0 ==  是垂直往下 的方向

a =np.array([[1,2,3],[4,5,6]])
a.shape #(2, 3) ==2*3維陣列
a.ndim #2軸  ndarray的shape有幾個数字 ndim就是多少


#"多個相同shape" 之二軸陣列組成 三軸陣列
a =np.array([[0,1],[2,3],[4,5]])
b =np.array([a,a])
b.shape #(2, 3, 2)  2軸 3欄 2列
b
b.sum(axis =0)
b.sum(axis =1)
b.sum(axis =2)


np.random.rand()#建立維度的亂數(浮點)
np.random.randint(10)
np.random.ramd(2,3)#建立 0~1(不含1)之間的浮點數
np.random.randint(10, size =(2,3))#與np.random.ramd相同 差別於 產生"整數"亂數


#np.zeros(n) 產生元素皆為 0 的陣列
#np.ones(n) 產生元素皆為 1 的陣列
np.zeros(10)#預設型態為浮點
np.zeros(10,dtype =int)#改為int

np.zeros((4,3))

#------------------------------------------------------------------------------
'''回歸分析(Regression Analysis)
    
    執行方式:
        1.假設求出結果的方程式 直線: f(x) =x w1+w0
          若所有資料點無法擬合到一條直線 則採用 多項式回歸
        2.多項式回歸:
            將次方中之 x 加上次方項(ex. 一次方,二次方, 三次方..) 
            則方程式為: (w0,w1,w2為係數)
            f(x) =w2x**2  + w1x +w0

'''
# ex 01
import numpy as np
x =np.random.rand(20)*8-4 #
x#純亂數
y =np.sin(x) +np.random.rand(20)*0.2 #np.six(x) 為了要產生關連性 或者說建立x ,y 之間的相依性
y#純亂數

#ex 02
# f(x) =w1x +w0
#使用np.polyfit(x,y,次方數) 回傳系數w1 w0(以一次方項 為例)
oma =np.polyfit(x,y,1)

#ex 03 
# 完成學習 測試結果
# poly1d(多項式係數)
# 傳回polyd 物件 代表係數組成的多項式

f =np.poly1d(oma)
import matplotlib.pyplot as plt 
plt.xlabel('x')
plt.ylabel('y')
plt.title('poltyfitfunction')
plt.grid()
plt.scatter(x,y,marker ='x',c ='red')

xx =np.linspace(-4,4,100)
#-4~4 之間產生100個值(x座標)
plt.plot(xx,f(xx),c ='green') #f(xx) 產生座標
plt.show()
#此直線無法 擬合所有20個資料點 
#一次方項方程式 無法完成回歸分析


#ex 04
#因為無法擬合 所以要修改次方 項
oma =np.polyfit(x,y,5)#從2 --> 一直試驗到5
#以一元五次多項式 可使20資料點擬合於曲線上 完成回歸分析

#------------------------------------------------------------------------------

'''資料模型
    回歸分析 ---> 回歸模型
    自變量 --->模型 --->因變量
    (多個)                (一個)

    資料分析::
        資料產生/取得
        工具(套路,程式<python>..)
        資料預處理(資料清洗 丟棄 補 丟棄 轉換)
        樣本分析(抽樣數 樣本權重 分析方法(回歸分析 聚類分析))
        
    分析模型
        依不同功能 產業別 有不同的建置
    會員類型模型:(以樹狀結構圖建立)
        會員類型模型
        會員活絡度模型
        會員價值模型
    商品模型:
        商品價格(敏感度)模型
        新商品市場定位模型
        銷售模型
        商品關聯性模型
        
'''
 
'''
    補充課外的連結可以學習:
        1. GitHub
        2.O'Reilly(歐茱禮)
        3.PyimageSearch
        4. Java Code Greeks
        5.DataCamp
        6. Stack overflow 
        
        機器學習 影像學習的
        1.Data Point
        2.Medium Daily Digest
        3.Towards Data Science

'''

