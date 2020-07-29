# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:20:12 2020

@author: USER
"""
#前面為0424的

#======================================================
#======================================================
#0717
'''影像加權和
        計算影像像素值和並加入加權值計算
使用函數: addWeighted
    addWeighted(src1,a,src2,b,c)
#src1 影像1  a 影像1加權   src2 影像2   b 影像2加權   c亮度調節
    
公式: src1*a + src2*b + c

'''
#01
import cv2 as cv
import numpy as np
img1=np.ones((3,4,3),dtype=np.uint8)*100
img2=np.ones((3,4,3),dtype=np.uint8)*10
a=3
img3=cv.addWeighted(img1,0.6,img2,5,a)
print(img3)

'''
兩影像的大小及類型 必須相同
'''
#02 大小不同不可讀取
import cv2 as cv
img1=cv.imread(r'C:\GitHub\python\PY-Learn\landscape512.jpg')
img2=cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
reslt=cv.addWeighted(img1,0.6,img2,0.4,0)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('img3',reslt)
cv.waitKey()

'''
ROI:Regin Of Interest
    感興趣的區域 於程中自行設定 所需要處理的  區域範圍
'''
#03 加權
import cv2 as cv
img=cv.imread(r'C:\GitHub\python\PY-Learn\lena_01.jpg',1)
us1=cv.imread(r'C:\GitHub\python\PY-Learn\US1_600.jpg',1)
cv.imshow('image',img)
cv.imshow('banknote',us1)
img_face=img[80:230,250:370]#影像的ROI
us1_face=us1[80:230,240:360]#鈔票的ROI
add=cv.addWeighted(img_face,0.6,us1_face,0.4,0)#影像的ROI執行加權運算 
us1[80:230,240:360]=add#加權後的影像蓋在鈔票上
cv.imshow('reselt',us1)
cv.waitKey()

'''逐位元邏輯運算
bitwise_and :且
bitwise_or :或
bitwise_xor :互斥
bitwise_not :反向

and運算:
    兩個運算元(邏輯值)都為真  其結果為真
    
函數:bitwise_and
    bitwise_and(src1,src2)
 
    
任何數值n 與 數值0 做and運算 結果為0

    11011011
and)00000000
---------------
    00000000

任何數值n 與數值255 做and運算 結果為數值n 本身

    11011011
and)11111111
---------------
    11011011

以上述定理 可建立 掩膜影像
                    只有兩個值 0,255 
                 

                    
or運算:
        兩個運算元(邏輯值)有一個為真 結果為真                    
函數:bitwise_or
    bitwise_or(src1,src2)                    


not運算:
        將運算元反向                    
函數:bitwise_not
    bitwise(src1,src2)    


xor運算:
        兩個運算元(邏輯值)都不相同   結果為真                    
函數:bitwise_xor
    bitwise_xor(src1,src2)    

    11000110  (198)
xor)11011011  (219)
--------------------
    00011101  (29)

'''
#04 掩膜影像
import cv2 as cv
import numpy as np
img1 =np.random.randint(0,255,(5,5),dtype =np.uint8)
img2 =np.zeros((5,5),dtype =np.uint8)
img2[0:3,0:3] =255
img2[4,4] =255
a =cv.bitwise_and(img1,img2)
print('img1=\n',img1)
print('img2=\n',img2)
print('a=\n',a)
#05
import cv2 as cv
import numpy as np
img1=cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)#設0為灰階
img2=np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400]=255
img2[100:500,100:200]=255#0 為黑 255 為白==白就是看得到的地方
a=cv.bitwise_and(img1,img2)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()
#06 跟5一樣
import cv2 as cv
import numpy as np
img1=cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',1)#設1為彩色
img2=np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400]=255
img2[100:500,100:200]=255
a=cv.bitwise_and(img1,img2)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()
#07
import cv2 as cv
import numpy as np
img1 =np.ones((4,4),dtype=np.uint8)*3
img2 =np.ones((4,4),dtype=np.uint8)*5
mask =np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4] =1
img3 =np.ones((4,4),dtype=np.uint8)*66
print('img1=\n',img1)
print('img2=\n',img2)
print('mask=\n',mask)
print('初值 img3=\n',img3)
img3 =cv.add(img1,img2,mask =mask)
print('求和後 img3=\n',img3)
#08
import cv2 as cv
import numpy as np
img =cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',1)
w,h,c =img.shape
mask =np.zeros((w,h),dtype =np.uint8)
mask[100:400,200:400] =255
mask[100:500,100:200] =255#0 為黑 255 為白==白就是看得到的地方
c =cv.bitwise_and(img,img,mask=mask)
print('img.shape =',img.shape)
print('mask.shape =',mask.shape)
cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('c',c)
cv.waitKey()

''' 
位元平面分解   (去掉雜訊)
    將灰階影像中同一個位元上的 二進位像素值 進行組合可得到到一個二進位影像
    該影像稱為"灰階影像的位元平面"
    其組合過程稱為為位元平面分解
    
    灰階影像中  每一項訴使用8位元 二進位值表示 值的範圍為0~255
    表示為:
        a^7 * 2^7 + a^6 * 2^6 + a^5 * 2^5 + a^4 * 2^4 + a^3 * 2^3
         ~ + a^2 * 2^2 + a^1 * 2^1 + a^0 * 2^0
    
        a^7 ~ a^0 的值為0或是1
        
        a^7值對影像影像最大
        a^0值對影像影像最小
        
        a^7 加權最高 某位元平面與原影像相關性最高 與原影像最相似
        a^0      低                          低 該為元平面最雜亂

執行步驟:
    1.影像前置處理
    2.建置分析矩陣
    3.分析位元平面
    4.設定值處理
    5.顯示影像

'''
#09
import cv2 as cv
import numpy as np 
img =cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
cv.imshow('imgage',img)
r,c=img.shape # 讀取元影像的 row column
x=np.zeros((r,c,8),dtype =np.uint8) #設定一個分析矩陣裡面都是0的 通道值==8

#分析位元平面
for i in range(8):
    x[:,:,i] =2**i #2位元矩陣  所以要有次方
r =np.zeros((r,c,8),dtype =np.uint8) 

#逐位元邏輯運算
for i in range(8):#主要要變成灰階 
    r[:,:,i] =cv.bitwise_and(img,x[:,:,i])
    mask =r[:,:,i]>0  
    r[mask] =255 # 1==255
    cv.imshow(str(i),r[:,:,i])
cv.waitKey()



'''影像加密及解密
        原始影像與金鑰影像 
            進行"互斥運算" 產生加密影像(encryption)
        加密影像與金鑰影像
            進行"互斥運算" 產生解密影像(deryption)
        
        a==原始資料(明文)
        b==金鑰
        c==加密 xor(a,b)

            xor(a,b)=c
            xor(c,b)=a
            
位元運算可實踐像素點加密
    通常需處理的像素點 為灰階值 ex像素值為216(明文)
    以178(此值由加密者自行決定)作為 加密金鑰
    將此二數值進行 互斥運算
    
    
    11011000  (216)--明文
xor)10110010  (178)--金鑰
-------------------------
    01101010  (106)---加密

bitwise_xor(216,178) =106  加密
bitwise_xor(106,178) =216  解密

    01101010  (106)
xor)10110010  (178)    
-----------------------
   11011000   (216) 
    
'''
#10
import cv2 as cv
import numpy as np
img =cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
cv.imshow('image',img)
r,c=img.shape
key =np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption =cv.bitwise_xor(img,key)
decryption =cv.bitwise_xor(encryption,key)
cv.imshow('img',img)
cv.imshow('key',key)
cv.imshow('encryption',encryption)
cv.imshow('decryption',decryption)
cv.waitKey()

'''浮水印(==資訊隱藏) # 不是一般所理解的浮水印!

        最低有效位(Least Significant Bit;LSB)
            二進位數字中的第0位(最低位) ==a^0
        將需要隱藏的二值影像嵌入載體影像的最低位有效位
        即將載體影像的LSB取代為需要隱藏的二值影像 以達到二值影像隱藏的目的
        
        "因二值影像處於載體影像的LSB上
         對載體影像影響非常不明顯 故具較高的隱蔽性"

#二值影像==二值化的影像為灰階影像
         
嵌入過程:
    將影像二值化(處理為灰階)
    灰階二值影像中 像素值 只有 0,255 表示 黑 白色
    將255轉為1可得到二進位的灰階影像 只用一個位元表達像素值
    
ex 版權認證 身分認證 
    
'''
#11
import cv2 as cv
import numpy as np
img =cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
watermark =cv.imread(r'C:\GitHub\python\PY-Learn\watermark.jpg',0)
w =watermark[:,:]>0#::== 只要大於0 的取出 (不是0就是255)所以取出255
watermark[w] =1#將灰階影像值為255的 轉為1 以方便嵌入
r,c =img.shape#取得原始影像的大小尺寸

t254 =np.ones((r,c),dtype=np.uint8)*254
# *254 為了要把255獨立出來==產生254的陣列
imgh7 =cv.bitwise_and(img, t254)#取得影像的高七位
e =cv.bitwise_or(imgh7,watermark)#再用 高七位用or做運算 把watermark 嵌入
#e ==已含載體的 圖片

t1=np.ones((r,c),dtype =np.uint8)#產生一個都是1的陣列
#用 and運算  把含有載體的e 跟
wm =cv.bitwise_and(e,t1)
#wm==從載體影像分析出來的浮水印影像
print(wm)
w =wm[:,:]>0
wm[w] =255

cv.imshow('img',img)
cv.imshow('watermark',watermark*255)
#要顯示圖片 就要把1轉乘255 才會有圖片 所以直接*255比較快
cv.imshow('e',e)
cv.imshow('wm',wm)
cv.waitKey()

#12
import cv2 as cv
import numpy as np
img =cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
#讀取原始影像的shape值
r,c =img.shape
mask =np.zeros((r,c),dtype =np.uint8)
mask[100:400,200:400] =1
#取得一個key(打碼與解碼所需要的金鑰)
key =np.random.randint(0, 256, size =[r,c], dtype =np.uint8)
#打碼臉部影像 使用金鑰key對原始影像加密
imgxorkey =cv.bitwise_xor(img,key)
#加密影像的臉部資訊
encryptface =cv.bitwise_and(imgxorkey, mask*255)
#將影像妹的臉部值 設定為0
noface1 =cv.bitwise_and(img,(1-mask)*255)
#取得 打碼影像
maskface =encryptface + noface1
#將打碼臉 解碼
extractoriginal =cv.bitwise_xor(maskface, key)
#將臉部打碼的影像與金樣進行互斥運算xor 得到臉部原始資訊
#將解碼的臉部 進行資料分析 extractoriginal
extractface =cv.bitwise_and(extractoriginal,mask*255)
#從臉打碼的影像分析沒有臉部資訊的影像
noface2 =cv.bitwise_and(maskface, (1-mask)*255)
#得到解碼影像
extractimg =noface2 + extractface
#顯示影像
cv.imshow('img',img)#原始影像
cv.imshow('mask',mask*255)#範本mask影像 白為1 黑為0 將1轉為255 方便顯示
cv.imshow('1-mask',(1-mask)*255)#範本mask影像的反色圖
cv.imshow('key',key)#金鑰影像
cv.imshow('imgxorkey',imgxorkey)#整體打碼臉部影像
cv.imshow('encryptface',encryptface)#從整體打碼影像中分析的臉部打碼影像
cv.imshow('noface1',noface1)#影像中分析的不包含臉部影像
cv.imshow('maskface',maskface)#打碼臉部影像
cv.imshow('extractoriginal',extractoriginal)#分析的初步原始影像
cv.imshow('extractface',extractface)#分析的臉部影像
cv.imshow('noface2',noface2)#不包含臉部資訊的影像
cv.imshow('extractimg',extractimg)#臉部解碼影像
cv.waitKey()

#----接續 0717的影像色彩

"""
Created on Fri Jul 17 16:51:25 2020

@author: Amanda Lu
"""
#0717 前為影像辨識 接續色彩

'''色彩空間類型轉換
        
    RGB色彩空間:
        
        R 紅           G 綠         B 藍
        三者為重要性相等  "但忽略亮度資訊"
        為硬體角度的色彩模型 以人眼觀看  存在一定的差異程度
        
    HSV(HSB)色彩空間:
        視覺感知的色彩模型 以心理學及視覺角度 指出人類視覺感知包含三部分:
            1.色調 2.飽和度 3.明度
            
        Hue色調(色相)
            光的顏色 範圍為 0~360
            
            基本款:
                0   紅色
                60  黃色
                120 綠色
                180 青色
                240 藍色
                300 品紅
        
        Saturation飽和度
            色彩顏色深淺程度 為一比例值  範圍 0~1
            是色彩純度值 與 最大純度值 之比值
            飽和度為0==灰階
            
        Value明暗 
            光的明暗程度  範圍 0~1
            
        
        
函數:                     src 原始影像
    色彩空間轉換  cvtColor(src,mode)
                                mode 色彩空間轉換

 
    *opneCV色彩模型為 "BGR"  與 RGB 不同
       RGB / BGR轉換到 GRAY灰階
        
       GRAY灰階=0.299*R + 0.587*G + 0.114*B
'''

#前12在影像辨識

#13
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[2,4,3],dtype =np.uint8)
rst =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('img =\n',img)
print('rst =\n',rst)
print('像素點(1,0) 直接計算得到的值 =',img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print('像素點(1,0) 使用公式cv.cvColor() 轉換值 = ',rst[1,0])
            
#==================================
#20200720

#ex01:

import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4],dtype=np.uint8)
rst = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
print('img = \n', img)
print('rst = \n', rst)    

"""
灰階 <-> BGR
=>當影像由GRAY彩色空間轉換到BGR色彩空間時,最後所有通道直視相同的

BGR <-> RGB
=>RGB與BGR互相轉換，R通道值與B通道值互換
=>BGR轉換為GRAY時，即為灰階影像，在將該影像轉換為BGR時，B、G、R值均相同，顯示結果為灰階
                                                ^_彩色__^
                                                ^_ BGR2GRAY
                                                ^_ GRAY2BGR
                                                ^_ BGR2RGB

=>色調H值設定範圍為 0~360, 8位元影像每個像素點能表示的灰階等級為2的8次方=256各，
  故8位元影像要以HSV表示時，必須將H值調整為0~255
  ->處理方式: 將 H值/2  得到 0~180之間的值  (適應8位元二進位儲存及表示)
  0:紅 30:黃 60:綠 90:青 120:藍 150:品紅

=>飽和度S值設定範圍為 0~1，因灰階影像之R,G,B值成分相等，相當於一種極度不飽和的色彩，
  故灰階影像其 飽和度 = 0
  灰階影像顯示時，較亮區域對應之色彩具有較高飽和度，及低飽和度，所得之色調值"不可靠"!

=>亮度V值設定範圍為0~1， 對應到 0~255
  BGRHSV

=>HSV色彩主要差異是在H通道，可對H通道進行篩選，已選出特定色彩
  ->inRange()函數:
      針對像素點之像素值判斷是否在某範圍內
      cv2.inRange(src,lower,upper)
                  ^影像 ^範圍下限 ^範圍上限
    若src值在範圍內，則傳回值中對應位置上之值為 255 否則為 0  

=>HSV色彩空間分析色彩時並非分析一特定值，而是分析依色彩區間
  如藍色H值為120，分析藍色時會以其附近值作為區間，通常附近值為10
  即120+10，120-10作為分析區間，S通道即V通道分析區間在100~255
  因飽和度、亮度太低時，得到的H值"不可靠" =>顏色判斷會失真
  
  HSV色彩區間: [H-10,100,100]~[H+10,255,255]
  紅色色彩的區間: [0,100,100]~[10,255,255]
  綠色色彩區間: [50,100,100]~[70,255,255]
  藍色色彩區間: [110,100,100]~[130,255,255]
  
=>膚色分析(HSV): 
    一般可設定為: 
        色調值: 5~170  (minHue,maxHue)
        飽和度: 25~166 (minSat,maxSat)

=>處理並設定HSV值，並將其設定為遮罩(mask:即掩模)，再將影像及遮罩座位元and運算，
  達到以遮罩控制影像顯示的目的
  
=>於RGB/BGR三通道後，在再加一通道，名為alpha，即透明度通道，即為4通道影像，
  為RGBA/BGRA色彩空間，設定範圍為: 0~1 or 0~255 (透明~不透明)
  BGR2BGRA
  
=>影像縮放:resize()函數:
    (src,dsize,fx,fy,interpolation)
    src:原始影像
    dsize:輸出影像大小
    fx:水平縮放比例
    fy:垂直縮放比例
    interpolation:內插方式
    影像執行幾何處理時，若無法直接透過對應值獲得像素點新值時，
    則採用內插處理(通常放大影像使用)
    內插處理:
        ->INTER_AREA ->區域內插      -- 鄰近、最接近區域
        ->INTER_NEAREST ->最鄰近內插  --^
        ->INTER_CUBIC ->三次樣得內插 --像點附近4*4區域 -->慢
        ->INTER_LINEAR ->線性內插 --預設 -->快

幾何轉換

#ex13:
原始影像大小:2行4列
resize後的大小:4行2列
結果的行數為原始的列數

shape屬性:
第一個值:行,第二個值:列
dsize屬性:
第一個值:列,第二個值:行   

=>影像翻轉:flip()
cv2.flip(src,flipcode)
src:原始影像
flipcode: 
    0: 繞X軸翻轉
    正數:繞Y軸翻轉(1)
    負數:繞X,Y軸翻轉(-1)    
    
#20200721
    
=>仿射轉換
透過幾何轉換執行平移，旋轉...，此轉換可以保持影像的平行性(平行線)及平直性(直線)
  warpAffine():仿射函數
  ->cv2.warpAffine(src,M,dsize,flags,borderMode,borderValue)
    src:影像
    M:轉換矩陣
    dsize:輸出影像大小
    flags:內插方法，預設INTER_LINEAR
    borderMode:框線模式 BORDER_CONSTANT
    borderValue:框線值，預設 0
    
    1.平移:透過3*3(或2*2)M矩陣執行轉換
       -->[1 0 tx]
    M->|           :將每一像點移到x+t,y+t
       -->[0 1 ty]
    M(11) = 1       M(21) = 0
    M(12) = 0       M(22) = 1
    M(13) = 100     M(23) = 200
    
    src(x*1+y*0+100,x*0+y*1+200)
    
    getRotationMatrix2D():
        產生已warpAffine()進行旋轉轉換時的轉換矩陣
        -> cv2.getRotationMatrix2D(center,angle,scale)
        center : 旋轉中心點
        angle　: 旋轉角度(逆時針為正)
        scale : 縮放比例
    以原點旋轉:(自訂矩陣)
    --              --
   |  cos0  -sin0  0  |
   |  sin0   cos0  0  | 
   |  0      0     1  |
    --              --
    以(x,y)旋轉:(自訂矩陣)
     --                         --
   |  cos0  -sin0  x-xcon0+ysin0  |
   |  sin0   cos0  y-xsin0-ycos0  | 
   |  0      0            1       |
    --                          --
    
  getAffineTransform():
      產生以warpAffine()進行仿射轉換時的轉換矩陣(以三個點進行轉換)
    ->cv2.getAffineTransform(src,dst)
    src:影像的三個點座標 -> 二維陣列
    dst:轉換的三個點座標 ->^
    
=>透視轉換:
    將矩形轉換為任意四邊形(無須維持平行性及平直性)
    warpPerspective()函數
    ->warpPerspective(src,M,dsize,flags,corderMode,borderValue)
      src:影像
      M:轉換矩陣
      dsize:輸出影像大小
      flags:內插方法，預設INTER_LINEAR
      borderMode:框線模式 BORDER_CONSTANT
      borderValue:框線值，預設 0
      
    getPerspectiveTransform():
      產生以 warpPerspective()執行時得轉換矩陣M
    ->cv2.getPerspectiveTransform(src,dst)
    src:原影像的四個點座標  --->任意四邊形，無須平行性，平直性
    dst:轉換影像的四個點座標 -->^

=>重對映:
    將影像中的像素點放到另一位置
    remap()函數
    ->cv2.remap(src,x,y,interpolation,corderMode,borderValue)
    src : 原始影像
    x : 對映的X座標
    y : 對映的Y座標
    
   (rst)
   目標陣列中的所有像素點均對映到原影像(img)中之第0行,第3列之像素點
   
   繞x軸翻轉:
       ->對映過程中->
                   x軸座標值不變
                   y軸座標值以x軸作為對稱軸進行交換
       
       ->對稱關係為:(行號索引自0開始)
                  目前行號+對稱行號 = 總行數-1      
       ->反映於X,Y上:(mapx,mapy)
                  mapx值保持不變,mapy=總行數-1-目前行號
    
    X,Y軸互換:
        mapx調整為所在的行號
        mapy調整為所在的列號
        若行列數量不相同，則無法完成對映的值會設為0
        .像點重對映
        .陣列複製(影像複製)
        .繞x軸翻轉
        .繞y軸翻轉
        .繞x,y軸翻轉
        .x,y軸互換
        .縮放
    
"""
#ex2:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
print('img = \n', img)
print('rgb = \n', rgb)  
print('bgr = \n', bgr)    

#ex3:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)

print('img.shape = ', img.shape)
print('gray.shape = ', gray.shape)  
print('bgr.shape = ', bgr.shape)

cv.imshow('img',img)
cv.imshow('gray',gray)  
cv.imshow('bgr',bgr)
print('bgr = \n',bgr)
cv.waitKey()

#ex4:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow('img',img)
cv.imshow('rgb',rgb)
cv.waitKey()

#ex5:
import cv2 as cv
import numpy as np
imgblue = np.zeros([1,1,3],dtype=np.uint8)
imgblue[0,0,0] = 255
Blue = imgblue
#測試藍色的HSV值
BlueHSV = cv.cvtColor(Blue,cv.COLOR_BGR2HSV)
print('Blue = \n',Blue)
print('BlueHSV = \n',BlueHSV)

imggreen = np.zeros([1,1,3],dtype=np.uint8)
imggreen[0,0,1] = 255
Green = imggreen
GreenHSV = cv.cvtColor(Green,cv.COLOR_BGR2HSV)
print('Green = \n',Green)
print('GreenHSV = \n',GreenHSV)

imgred = np.zeros([1,1,3],dtype=np.uint8)
imgred[0,0,2] = 255
Red= imgred
RedHSV = cv.cvtColor(Red,cv.COLOR_BGR2HSV)
print('Red = \n',Red)
print('RedHSV = \n',RedHSV)

#ex6:
import cv2 as cv
import numpy as np
img = np.random.randint(0,255,size=[5,5],dtype=np.uint8)
min = 100
max = 200
mask = cv.inRange(img,min,max)
print('img = \n',img)
print('mask = \n',mask)

#ex7:
import cv2 as cv
import numpy as np
img = np.ones([5,5],dtype=np.uint8)*9
mask = np.zeros([5,5],dtype=np.uint8)
mask[0:3,0] = 1
mask[2:5,2:4] = 1
roi = cv.bitwise_and(img,img,mask=mask)
print('img = \n',img)
print('mask = \n',mask)
print('roi = \n',roi)


#ex8:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\opencv-logo.png')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('img',img)

minBlue = np.array([110,50,50])
maxBlue = np.array([133,255,255])
mask = cv.inRange(hsv,minBlue,maxBlue)
blue = cv.bitwise_and(img,img,mask=mask)
cv.imshow('blue',blue)

minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
mask = cv.inRange(hsv,minGreen,maxGreen)
green = cv.bitwise_and(img,img,mask=mask)
cv.imshow('green',green)

minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
mask = cv.inRange(hsv,minRed,maxRed)
red = cv.bitwise_and(img,img,mask=mask)
cv.imshow('red',red)
cv.waitKey()

#ex9:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv)
minHue = 5
maxHue = 160
hueMask = cv.inRange(h,minHue,maxHue)
minSat = 25
maxSat = 160
satMask = cv.inRange(s,minSat,maxSat)
mask = hueMask & satMask
roi = cv.bitwise_and(img,img,mask=mask)
cv.imshow('img',img)
cv.imshow('ROI',roi)
cv.waitKey()

#ex10:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,3,3],dtype=np.uint8)
bgra = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
print('img',img)
print('bgra',bgra)
b,g,r,a = cv.split(bgra)
print('a = \n',a)
a[:,:] = 125
bgra = cv.merge([b,g,r,a])
print('bgra = \n',bgra)

#ex11:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
bgra = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
b,g,r,a = cv.split(bgra)
a[:,:] = 125
bgra125 = cv.merge([b,g,r,a])
a[:,:] = 0
bgra0 = cv.merge([b,g,r,a])
cv.imshow('img',img)
cv.imshow('bgra',bgra)
cv.imshow('bgra125',bgra125)
cv.imshow('bgra0',bgra0)
cv.waitKey()
cv.destroyAllWindows()
cv.imwrite(r'C:\GitHub\python\PY-Learn\bgra.png',bgra)
cv.imwrite(r'C:\GitHub\python\PY-Learn\bgra125.png',bgra125)
cv.imwrite(r'C:\GitHub\python\PY-Learn\bgra0.png',bgra0)

#ex12:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena_01.jpg')
cv.imshow('img',img)
hsv_low = np.array([0,0,0])
hsv_high = np.array([0,0,0])
def h_low(value):
    hsv_low[0] = value
def h_high(value):
    hsv_high[0] = value
def s_low(value):
    hsv_low[1] = value
def s_high(value):
    hsv_high[1] = value
def v_low(value):
    hsv_low[2] = value
def v_high(value):
    hsv_high[2] = value
cv.namedWindow('image')
cv.createTrackbar('H_low','image',0,250,h_low)
cv.createTrackbar('H_high','image',0,250,h_high)
cv.createTrackbar('S_low','image',0,250,s_low)
cv.createTrackbar('S_high','image',0,250,s_high)
cv.createTrackbar('V_low','image',0,250,v_low)
cv.createTrackbar('V_high','image',0,250,v_high)
while(1):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsv = cv.inRange(hsv,hsv_low,hsv_high)
    cv.imshow('hsv',hsv)
    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()


#ex13:
import cv2 as cv
import numpy as np
img = np.ones([2,4,3],dtype=np.uint8)
size = img.shape[:2]
rst = cv.resize(img,size)
print('img.shape = \n',img.shape)
print('img = \n',img)
print('rst.shape = \n',rst.shape)
print('rst = \n',rst) 


#ex14:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols=img.shape[:2]
size = (int(cols*0.9),int(rows*0.5))
rst = cv.resize(img,size)
print('img.shape = \n',img.shape)
print('rst.shape = \n',rst.shape)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()

#ex15:
import cv2 as cv
img1 = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
img2 = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
img3 = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
res1 = cv.resize(img1,None,fx=1.5,fy=1.5,interpolation=cv.INTER_AREA)
res2 = cv.resize(img2,None,fx=1.5,fy=1.5,interpolation=cv.INTER_LINEAR)
res3 = cv.resize(img3,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)
cv.imshow('img1',img1)
cv.imshow('res1',res1)
cv.imshow('res2',res2)
cv.imshow('res3',res3)
cv.imwrite(r'C:\GitHub\python\PY-Learn\lena512_A.jpg',res1)
cv.imwrite(r'C:\GitHub\python\PY-Learn\lena512_B.jpg',res2)
cv.imwrite(r'C:\GitHub\python\PY-Learn\lena512_C.jpg',res3)
while True:
    if(cv.waitKey() & 0xFF) == ord('q'):
        break
    else:
        pass
cv.destroyAllWindows()


#ex16:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
x = cv.flip(img,0)
y = cv.flip(img,1)
xy = cv.flip(img,-1)
cv.imshow('img',img)
cv.imshow('x',x)
cv.imshow('y',y)
cv.imshow('xy',xy)
cv.waitKey()

#20200721

#ex1:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
height,width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1,0,x],[0,1,y]])
move = cv.warpAffine(img,M,(width,height))
cv.imshow('img',img)
cv.imshow('move',move)
cv.waitKey()

#ex2:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
height,width = img.shape[:2]
M = cv.getRotationMatrix2D((width/2,height/2),45,0.6)
rotate = cv.warpAffine(img,M,(width,height))
cv.imshow('img',img)
cv.imshow('rotate',rotate)
cv.waitKey()

#ex3:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols,ch = img.shape
p1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2 = np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M = cv.getAffineTransform(p1,p2)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',img)
cv.imshow('result',dst)
cv.waitKey()

#ex4:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols = img.shape[:2]
print(rows,cols)
pts1 = np.float32([[150,50],[300,50],[60,450],[210,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(cols,rows))
cv.imshow('img',img)
cv.imshow('dst',dst)
cv.waitKey()

#ex5:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\opencv-logo.png')
rows,cols = img.shape[:2]
print(rows,cols)
pts1 = np.float32([[300,290],[500,290],[300,400],[500,400]])
pts2 = np.float32([[50,50],[rows-170,100],[50,cols+100],[rows-240,cols-200]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(cols,rows))
cv.imshow('img',img)
cv.imshow('dst',dst)
cv.waitKey()

#ex6:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)*3
mapy = np.ones(img.shape,np.float32)*0
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)


#ex7:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)
mapy = np.ones(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)


#ex7-1:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols = img.shape[:2]
mapx = np.ones(img.shape[:2],np.float32)
mapy = np.ones(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


#ex8:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)
mapy = np.ones(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)


#ex9:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)


#ex9-1:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


#ex10:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)

#ex10-1:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


#ex11:
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,6],dtype=np.uint8)
rows,cols = img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i)
        mapy.itemset((i,j),j)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img = \n',img)
print('mapx = \n',mapx)
print('mapy = \n',mapy)
print('rst = \n',rst)


#ex11-1:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\opencv-logo.png')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i)
        mapy.itemset((i,j),j)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


#ex12:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena_01.jpg')
rows,cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols<i<0.75*cols and 0.25*rows<j<0.75*rows:
            mapx.itemset((i,j),2*(j-cols*0.25)+0.5)
            mapy.itemset((i,j),2*(i-rows*0.25)+0.5)
        else:
            mapx.itemset((i,j),0)
            mapy.itemset((i,j),0)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


"""
影像平滑處理

=>平滑處理及影像濾波
    ->在儲存影像細節特徵之條件下，對影像進行雜訊(噪點)抑制

=>濾波的目的:
    ->清除(抑制)雜訊

=>均值濾波:
    以目前像素點周圍 n*n 範圍像素值之平均值
    均值:既平均值，將影像先找一個中心點，以n*n範圍的像素值，加總平均，寫入覆蓋原像素值.
        通常用於銳利度較高的影像，使其顯示較為自然
    blur()函數:均值濾波
    ->cv2.blur(src,ksize,anchor,borderType)
    src : 影像
    ksize : 濾波核大小，均值處理中鄰近範圍的高度、寬度
    anchor : 錨點，目前計算均值的點，位於該核中心點的位置，使用預設值即可(-1,-1)
    borderType : 變化樣式
    
    @@@ np.hstack : 水平方向堆疊
        np.vstack : 垂直方向堆疊
    
=>方框濾波:
    可自行設定濾波結果為平均值或加總覆蓋原像素值
    boxFilter()函數:
    ->cv2.boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
    src : 影像
    ddepth : 影像深度，每一像素能展示的顏色數，一般使用-1表示與原始像素採用相同的影像深度
    ksize : 濾波核大小，均值處理中鄰近範圍的高度、寬度
    anchor : 錨點，目前計算均值的點，位於該核中心點的位置，使用預設值即可(-1,-1)
    normlize : 1 : 即為均值濾波，功能同blur()，預設值.
               0 : 加總，若加總超過255(最大值)，則會得到白色影像
    borderType : 變化樣式

#20200723

=>高思濾波:
    每個像點尤其鄰近的像點及本身經過加權平均後計算得出，中心點加權值加強
    遠離中心點的加權值逐漸減少，將各像點加權平均加總.
    GaussianBlur()函數:
    ->cv2.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
    src : 原影像
    ksize : 濾波核大小(必須為奇數)
    sigmaX : 濾波核大小在水平方向之標準差，控制加權比例(不可省略)
    sigmaY : 濾波核大小在垂直方向之標準差，控制加權比例(可省略)
    若sigmaX,sigmaY均為0,則:
        sigmaX = 0.3 *[(ksize.width-1)*0.5-1]*0.8
        sigmaX = 0.3 *[(ksize.height-1)*0.5-1]*0.8
    
    標準差:
        測量一組數據之離散程度.(與平均值之分散程度)
        較大的標準差:大部分數值與平均值之間差異較大
        較小的標準差:大部分數值與平均值之間差異較小
        例如:2學生 => 100分  => 平均50分 => 標準差較大
                      0分

            2學生 => 50分  => 平均50分 => 標準差較小
                    50分
                    
=>中值濾波:
    以鄰近像點的中間值取代，目前像點的像素值
    medianBlur()函數:
    ->cv2.medianBlur(src,ksize)
    src : 原影像
    ksize : 濾波核大小(必須為比1大的奇數)

=>雙邊濾波:
  考慮空間資訊及色彩資訊的濾波方法,過程中可有效保護影像中的邊緣資訊
  bilateralFilter()函數:
  ->cv2.bilateralFilter(src,d,sigmaColor,sigmaSpace,borderType)
   src : 原影像
   d : 空間距離參數，表示以目前像點為中心點之直徑,建議d=5.
       d數越大,濾波速度越慢,雜訊較大的影像,可提高d值.
   sigmaColor : 濾波處理時，選取的顏色差值範圍，此值決定濾波時那些像點可加入到濾波中，
                與目前像素點差值小於sigmaColor值的像素點，可被加入到濾波.
                sigmaColor值越大，則有越多的像素點參與濾波處理
   sigmaSpace : 空間值，值越大，則有更多像點納入做濾波.

=>自訂濾波核:
    filter2D()函數:
    -> cv2.filter2D(src,ddepth,kernel,anchor,delta,borderType)
    src : 影像
    ddepth : 影像深度，每一像素能展示的顏色數，一般使用-1表示與原始像素採用相同的影像深度
    kernel : 濾波核大小，為通道陣列
    anchor : 錨點，目前計算均值的點，位於該核中心點的位置，使用預設值即可(-1,-1)
    delta : 修正值,修正濾波結果
    borderType : 變化樣式

"""


#ex13:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r5 = cv.blur(img,(5,5))
r30 = cv.blur(img,(30,30))
cv.imshow('img',img)
cv.imshow('r5',r5)
cv.imshow('r30',r30)
cv.waitKey()


#ex14: 影像加噪點
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',1)
rows, cols, ch = img.shape
for i in range(10000):
    x = np.random.randint(0,rows)
    y = np.random.randint(0,cols)
    img[x,y,:] = 255
cv.imshow('noise',img)
cv.imwrite(r'C:\GitHub\python\PY-Learn\lena512_noisy1.jpg',img)
cv.waitKey()



#ex14-1:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy1.jpg',1)
r5 = cv.blur(img,(5,5))
r30 = cv.blur(img,(30,30))
cv.imshow('img',img)
cv.imshow('r5',r5)
cv.imshow('r30',r30)
cv.waitKey()

#ex15:
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy1.jpg',1)
rst = cv.cvtColor(img,cv.COLOR_BGR2RGB)
final = cv.blur(rst,(5,5))
titles = ['Source','Blur']
images = [rst,final]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#ex16:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',1)
bl = np.hstack([cv.blur(img,(3,3)),cv.blur(img,(8,8)),cv.blur(img,(15,15))])
cv.imshow('img',img)
cv.imshow('result',bl)
cv.waitKey()


#ex17: #方框濾波 預設值
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r = cv.boxFilter(img,-1,(5,5))
cv.imshow('img',img)
cv.imshow('result',r)
cv.waitKey()

#ex18: #方框濾波 加總
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r = cv.boxFilter(img,-1,(5,5),normalize=0)
cv.imshow('img',img)
cv.imshow('result',r)
cv.waitKey()

#20200723

#ex1:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r = cv.GaussianBlur(img,(5,5),0,0)
cv.imshow('img',img)
cv.imshow('result',r)
cv.waitKey()

#ex2:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png')

bl = np.hstack([cv.GaussianBlur(img,(3,3),0),cv.GaussianBlur(img,(5,5),0),cv.GaussianBlur(img,(9,9),0)])

cv.imshow('img',img)
cv.imshow('GaussianBlur',bl)
cv.waitKey()


#ex3:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r = cv.medianBlur(img,3)
cv.imshow('img',img)
cv.imshow('result',r)
cv.waitKey()


#ex4:
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
for i in range(8000):
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(1,2,1),plt.imshow(img,'gray')
plt.subplot(1,2,2),plt.imshow(blur,'gray')


#ex5:
import cv2 as cv
import numpy as np
def dot(img,n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2: #img.ndim的大小(維度)
            img[j,i] = 255
        elif img.ndim == 3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
rst = dot(img,10000)
median = cv.medianBlur(rst,5)
cv.imshow('dot',rst)
cv.imshow('Median',median)
cv.waitKey()


#ex6:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
r = cv.bilateralFilter(img,25,100,100)
cv.imshow('img',img)
cv.imshow('result',r)
cv.waitKey()


#ex7:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
g = cv.GaussianBlur(img,(55,55),0,0)
b = cv.bilateralFilter(img,55,100,100)
cv.imshow('img',img)
cv.imshow('Gaussian',g)
cv.imshow('bilateral',b)
cv.waitKey()

#ex8:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy.png',0)
kernel = np.ones((9,9),np.float32)/81
r = cv.filter2D(img,-1,kernel)
cv.imshow('img',img)
cv.imshow('rst',r)
cv.waitKey()




"""
邊緣偵測
=>Canny演算法:
    ->低錯誤率:
          偵測的亮點大多屬於邊緣
      定位準確:
         標示的邊緣與實際的邊緣大致相同
      解析度高:
        邊緣線條細緻
    ->應用於灰階影像:
    ->演算法流程:
        1.去噪:欲處理圖片，使用高斯濾波
        2.計算影像梯度方向(影像強度，色彩方向之變化性)
        3.非極大值抑制
        4.確定邊緣
        
  ->Canny()函數:
      cv2.Canny(src,threshold1,threshold2,opertureSize,L2gradient)
      src : 原影像
      threshold1 : 第一個閥值 (低)
      threshold2 : 第二個閥值 (高)
      opertureSize : 梯度的運算孔徑大小
      L2gradient : 梯度幅度(預設False)


=>使用分類器Classifier:
    分類器:以訓練完成的各影像特徵(如人臉)，以檔案型式存在，為XML檔

=>辨識方法:
    1.自行訓練分類器(使用機器學習)
    2.使用以訓練完成的分類器，如openCV提供之特徵分類器
    
    =>opencv分類器:
        於opencv安裝資料夾中之data資料夾，包含以下的分類器:
            Haarcascades -> haar分類器
            HOG分類器 X 行人  紋理
            LBP分類器 (Local Binary Pattern)->臉部比對
    => Haar Classifier:(影像灰度變化)
        以黑白矩形作為mask，在影像上來回覆蓋，以提取特徵(學習臉部特徵)
        眼睛附近比臉頰附近皮膚顏色比對
    
    ->CascadeClassifier()函數:
        cv2.CascadeClassifier(filename)
        filename : 分類器檔案名稱及路徑 =>傳回的是分類器物件
        分類器物件.detectMultiScale(src,scaleFactor,minNeighbor,flag,minSize,maxSize)
        src : 原影像
        scaleFactor : 縮放比例 
        minNeighbor : 組成檢測目標的相鄰矩形最小個數(預設為3)
        flag : 使用舊版opencv時使用此參數
        minSize : 目標最小尺吋，小於此尺吋的目標物將被忽略
        maxSize : 目標最大尺吋，大於此尺吋的目標物將被忽略
               


"""

#ex9:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
r1 = cv.Canny(img,128,200)
r2 = cv.Canny(img,32,128)
cv.imshow('img',img)
cv.imshow('r1',r1)
cv.imshow('r2',r2)
cv.waitKey()

#ex10:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512_noisy1.jpg',0)
img = cv.GaussianBlur(img,(3,3),0)
canny = cv.Canny(img,50,150)
cv.imshow('img',img)
cv.imshow('Canny',canny)
cv.waitKey()



#ex11:
import cv2 as cv
def CannyThreshold(lowThreshold):
    detected_edges = cv.GaussianBlur(gray,(3,3),0)
    detected_edges = cv.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv.bitwise_and(img,img,mask = detected_edges)
    cv.imshow('canny',dst)
lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.namedWindow('canny')
cv.createTrackbar('threshold value','canny',lowThreshold,max_lowThreshold,CannyThreshold)
CannyThreshold(0)
if cv.waitKey(0) == 27:
    cv.destroyAllWindows()


#ex12:
import cv2 as cv
img_original = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg',0)
cv.namedWindow('Canny')
def nothing(x):
    pass
cv.createTrackbar('threshold1','Canny',50,500,nothing)
cv.createTrackbar('threshold2','Canny',100,500,nothing)
while(1):
    
    threshold1 = cv.getTrackbarPos('threshold1','Canny')
    threshold2 = cv.getTrackbarPos('threshold2','Canny')
    
    img_edges = cv.Canny(img_original,threshold1,threshold2)
    
    cv.imshow('original',img_original)
    cv.imshow('Canny',img_edges)
    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()


#ex13:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\coin.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cny = cv.Canny(blur,30,150)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('cny',cny)
cv.waitKey()


#ex-1:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\falt.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cny = cv.Canny(blur,30,150)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('cny',cny)
cv.waitKey()


#ex-2:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\keybo.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cny = cv.Canny(blur,30,150)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('cny',cny)
cv.waitKey()

#ex-3:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\pig.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cny = cv.Canny(blur,30,150)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('cny',cny)
cv.waitKey()


#ex-4:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\me.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cny = cv.Canny(blur,30,150)
cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('blur',blur)
cv.imshow('cny',cny)
cv.waitKey()



#ex14:
import numpy as np
#import argparse
import cv2 as cv
image = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
cv.imshow('Original',image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.int8(np.absolute(lap))

cv.imshow('Edge detection by Laplacaian',np.hstack([lap,gray]))

if(cv.waitKey(0) == 27):
    cv.destroyAllWindows()
    
    
#ex15:
import numpy as np
import cv2 as cv
image = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
cv.imshow('Original',image)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

sobelx = cv.Sobel(gray,cv.CV_64F,1,0) #sobel邊緣偵測
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombine = cv.bitwise_or(sobelx,sobely)
cv.imshow('Edge detection by Sobel',np.hstack([gray,sobelx,sobely,sobelcombine]))

if(cv.waitKey(0) == 27):
    cv.destroyAllWindows()

#ex16:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\lena512.jpg')
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=7,minSize=(5,5))
print(faces)
print('find {0} face!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey()

#ex16-1:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\person_3.jpg')
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=9,minSize=(5,5))
print(faces)                                                           #^改成大一點
print('find {0} face!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey()

#ex16-2:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\person_8.jpg')
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5))
print(faces)                                                           #^改成小一點
print('find {0} face!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2) #畫框

cv.imshow('img',img)
cv.waitKey()

#ex16-3:
import cv2 as cv
img = cv.imread(r'C:\GitHub\python\PY-Learn\person_8.jpg')
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5))
print(faces)                                                           #^改成小一點
print('find {0} face!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2) #畫圓

cv.imshow('img',img)
cv.waitKey()

#20200727
"""
影像辨識(機器)->速度、準確
(臉、物品、文字)  
=>影像分類器->載入影像進入辨識
   |  |         ^差異(角度、方向、訊訊、面積、色彩.....)
   |  |->經影像處理、運算....->不同的演算及處理方法-> 各自特色(分類器)
   |  |                      ^辨識結果:盡量提高90%以上
   |  |->產生分類器(調教個參數)------------------>^
   -> 自訓練分類->機器學習(深度學習)->各種機器/深度學習演算法
   
=>辨識流程:
    ->設定分類器檔案(*.xml)路徑位置
    ->建立分類器物件(載入上述位置)
    ->讀入待辨識影像
    ->由分類器物件執行偵測影像(人臉)->傳回偵測到的範圍
    ->繪製圖形標註偵測到的影像範圍
"""

#ex1:
import cv2 as cv
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
img = cv.imread(r'C:\GitHub\python\PY-Learn\person_3.jpg')
faces = faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=9,minSize=(30,30),flags = cv.CASCADE_SCALE_IMAGE)

cv.rectangle(img,(10,img.shape[0]-20),(110,img.shape[0]),(0,0,0),-1)
cv.putText(img,"find "+str(len(faces))+" face!",(10,img.shape[0]-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(128,255,0),2)
cv.namedWindow("facedetect")
cv.imshow('facedetect',img)
cv.waitKey()

#ex2:
import cv2 as cv
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml'
face_Cascade = cv.CascadeClassifier(pict)
img = cv.imread(r'C:\GitHub\python\PY-Learn\face_execuite.jpg')
faces = faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=2,minSize=(20,20))

cv.rectangle(img,(img.shape[1]-140,img.shape[0]-20),(img.shape[1],img.shape[0]),(0,255,255),-1)
        
cv.putText(img,"find "+str(len(faces))+" face!",(img.shape[1]-135,img.shape[0]-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv.namedWindow('Face',cv.WINDOW_NORMAL)  #視窗可調整大小
cv.imshow('Face',img)
cv.waitKey()


#ex3:
import cv2 as cv
pict = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml' #載入分類器
face_Cascade = cv.CascadeClassifier(pict)  #建立分類器物件(載入上述位置)
eyepict = r'C:\GitHub\python\PY-Learn\haarcascade_eye.xml' #載入分類器
eye_Cascade = cv.CascadeClassifier(eyepict)  #建立分類器物件(載入上述位置)

img = cv.imread(r'C:\GitHub\python\PY-Learn\Lena_01.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img,scaleFactor=1.15,minNeighbors=10,minSize=(20,20))


for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_Cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey()


#ex4:
import cv2 as cv
from PIL import Image #
case_path = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml' #載入分類器
faceCascade = cv.CascadeClassifier(case_path)  #建立分類器物件(載入上述位置)

imagename = r'C:\GitHub\python\PY-Learn\person_8.jpg'
image = cv.imread(imagename)
faces = faceCascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(5,5),flags = cv.CASCADE_SCALE_IMAGE)

count =1
for(x,y,w,h) in faces:
    cv.rectangle(image,(x,y),(x+w,y+h),(128,255,0),2)
    filename = str(count)+ '.jpg'
    image1 = Image.open(imagename)
    image2 = image1.crop((x,y,x+w,y+h)) 
                    #^裁切
    image3 = image2.resize((200,200),Image.ANTIALIAS)
                    #^重製大小               ^影像最佳化
    res = r'C:\GitHub\python\PY-Learn\face' + filename
    image3.save(res)
    count += 1    
cv.namedWindow('facedetect')
cv.imshow('facedetect',image)
cv.waitKey()


#ex5:
import cv2 as cv
from PIL import Image #
pictpath = r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml' #載入分類器
face = cv.CascadeClassifier(pictpath)  #建立分類器物件(載入上述位置)

img = cv.imread(r'C:\GitHub\python\PY-Learn\people_01.jpg')

faces = faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(10,10))

cv.rectangle(img,(img.shape[1]-140,img.shape[0]-20),(img.shape[1],img.shape[0]),(0,255,255),-1)
        
cv.putText(img,"Finded "+str(len(faces))+" face!",(img.shape[1]-135,img.shape[0]-5),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)

num =1
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    filename = str(num)+ '.jpg'
    image = Image.open(r'C:\GitHub\python\PY-Learn\people_01.jpg')
    imageCrop = image.crop((x,y,x+w,y+h)) 
                    #^裁切
    imageResize = imageCrop.resize((150,150),Image.ANTIALIAS)
                    #^重製大小               ^影像最佳化
    res = r'C:\GitHub\python\PY-Learn\face2_' + filename
    imageResize.save(res)
    num += 1    
cv.imshow('Face',img)
cv.waitKey()


#ex6:
import cv2 as cv
face_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_eye.xml')
mouth_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_mcs_mouth.xml')
nose_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_mcs_nose.xml')
leftear_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_mcs_leftear.xml')
rightear_cascade = cv.CascadeClassifier(r'C:\GitHub\python\PY-Learn\haarcascade_mcs_rightear.xml')
img = cv.imread(r'C:\GitHub\python\PY-Learn\Lena_01.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#face detect
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3)
for (x,y,w,h) in faces:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.3,minNeighbors=5,minSize=(30,30))
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    mouth = mouth_cascade.detectMultiScale(roi_gray,scaleFactor=1.4,minNeighbors=8,minSize=(10,10))    
    for (mx,my,mw,mh) in mouth:
        cv.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,0),2)
        
    nose = nose_cascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30))    
    for (nx,ny,nw,nh) in nose:
        cv.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(255,0,255),2)
        
    leftear = leftear_cascade.detectMultiScale(roi_gray,scaleFactor=1.01,minNeighbors=2,minSize=(30,30))    
    for (lx,ly,lw,lh) in leftear:
        cv.rectangle(roi_color,(lx,ly),(lx+lw,ly+lh),(0,0,0),2)

    rightear = rightear_cascade.detectMultiScale(roi_gray,scaleFactor=1.01,minNeighbors=2,minSize=(30,30))    
    for (rx,ry,rw,rh) in rightear:
        cv.rectangle(roi_color,(rx,ry),(rx+rw,ry+rh),(0,0,0),2)

cv.imshow('img',img)
cv.waitKey()


"""
Dlib:(C++函式庫)
=>用於機器學習，影像處理，影像辨識
=>人臉監測演算法:
    ->方向梯度直方圖(HOG)
    ->線性分類器(Linear Classifier)
    ->影像金字塔(image pyramid)
    ->滑動窗格(sliding window)
=>演算結果得到一分數值
  分數越大，越接近人臉
  分數越小，越接近誤判
  ----------------------
  建立python版本的環境:
  1.以Anaconda Navigator建立:
    Environments -> Create
  2.以命令列建立:
    a.  在 AnacondaPrompt系統管理員模式建立3.6環境 => conda create --name python_36 python=3.6
    b.  到Anaconda Navigator ，搜尋 uninstall spyder ，然後點選安裝spyder 3.6 
    c.  到Anaconda Navigator 開啟3.6命令列(Termanil)， 安裝dlib => pip install C:\GitHub\python\PY-Learn\dlib-19.8.1-cp36-cp36m-win_amd64.whl
    d.  繼續在3.6命令列(Termanil)，安裝openCV => pip install opencv-python

=> get_frontal_face_detector 函式
格式: 變數 = dlib.get_frontal_face_detector() 
     產生正面臉部偵測元件
     
     偵測人臉:
         結果 = 變數(待偵測影像,偵測參數,分數參數)
                             ^ 0 => 一般偵測
                               1 => 人臉範圍較小
    @安裝 imutils => pip install imutils (提供影像編輯功能)


"""

#ex7:
import dlib
import cv2 
import imutils
img = cv2.imread(r'C:\GitHub\python\PY-Learn\person_8.jpg')
img = imutils.resize(img,width=1280)
detector = dlib.get_frontal_face_detector()
face_rects = detector(img,1)

for i,d in enumerate(face_rects):
    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),4,cv2.LINE_AA)
cv2.imshow('Face_Detection',img)
cv2.waitKey()



#ex8:
import dlib
import cv2 
import imutils
img = cv2.imread(r'C:\GitHub\python\PY-Learn\face_trump01.jpg')
#img = cv2.imread(r'C:\GitHub\python\PY-Learn\face_execuite.jpg')
img = imutils.resize(img,width=1280)
detector = dlib.get_frontal_face_detector()
#偵測人臉,輸出分數
face_rects,scores,idx = detector.run(img,2,-0.1)

for i,d in enumerate(face_rects):
    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    text = "%2.2f(%d)" % (scores[i],idx[i])
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),4,cv2.LINE_AA)
    #標示分數
    cv2.putText(img,text,(x1,y1),cv2.FONT_HERSHEY_DUPLEX,0.7,(255,255,255),1,cv2.LINE_AA)
cv2.imshow('Face_Detection',img)
cv2.waitKey()


#==============================================================================
#20200728

#ex1  3.6
import dlib
import cv2 as cv
cap =cv.VideoCapture(r'C:\GitHub\python\PY-Learn\short_hamilton_clip.mp4')#.VideoCapture 開啟影片檔案
width =int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#把每秒影格畫面尺寸抓出 怕有小數點 所以前面放int轉整數
height =int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc =cv.VideoWriter_fourcc(*'XVID') #設定影片的編碼  XVID (很普及的)
out =cv.VideoWriter(r'C:\GitHub\python\PY-Learn\output.avi', fourcc, 20.0, (width,height))
#輸出影片檔 路徑檔名+avi格式 設定編碼 20.0==fps值 輸出時 依照每秒的影格數去做設定         
detector =dlib.get_frontal_face_detector()

while (cap.isOpened()):
    ret ,frame =cap.read()#cap.read() 讀出影格資訊 ==單一畫面 
    face_rects, scores, idx =detector.run(frame, 0)

    for i ,d in enumerate(face_rects):#d ==人臉的左右大小
        x1 =d.left()
        y1 =d.top()
        x2 =d.right()
        y2 =d.bottom()
        text ='%2.2f(%d)' % (scores[i],idx[i])
        cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),4,cv.LINE_AA)
    
    #標示分數
        cv.putText(frame, text, (x1,y1), cv.FONT_HERSHEY_DUPLEX,0.7,(255,255,255),1,cv.LINE_AA)
    out.write(frame)
    
    cv.imshow('Video face Detection', frame)
    if cv.waitKey(1) &0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()



"""
    用人臉框出 影片裡的人 就是先將影片  輸出依單一影格 並每一個每一個畫面去做處理
    

    FRS 每秒影格(畫面)數
        Frame/s 影格(畫面) (frame per second)
    人眼每秒可處理 10~12秒 靜態影像 ==即 <= 12fps值 人眼可分辨為靜止畫面
    
    16~24 fps 人眼便是為動態連續影像  即影片
    
    一般可分為 24 fps 標準速率 ex 電影,短片  
              30 fps 目前大都使用這個  ex電影 電視劇 新聞
              60 fps 運動
        
"""

#ex2   3.6
import dlib
import cv2 as cv
predictor_path =r'C:\GitHub\python\PY-Learn\shape_predictor_5_face_landmarks.dat'
face_path =r'C:\GitHub\python\PY-Learn\face_trumpfamily.jpg'

def rendrface(img,landmarks ,color =(0,255,0), radius =3):#在 landmark 上畫圓 把特徵點標示出來
    for p in landmarks.parts():
        cv.circle(img, (p.x,p.y), radius, color, -1)
    
detector =dlib.get_frontal_face_detector()#建立臉孔偵測元件
predictor =dlib.shape_predictor(predictor_path)#建立臉孔偵測元件

img =cv.imread(face_path)
dets =detector(img,1)#偵測臉孔

for k ,d in enumerate(dets):
    shape =predictor(img,d)#讀出外觀大小
    rendrface(img, shape) #標出特徵
    
cv.imshow('face-rendred', img)
cv.waitKey()



"""
    dlib模型
    
    5點模型:  shape_predictor_5_face_landmarks
    68點模型:shape_predictor_68_face_landmarks  ->模型過大 可以換使用5點模型
    
    可用來"校正"人臉辨識的準確度(face alignment)
    (臉部校正後 可提高辨識精準度)
    實作 步驟如下:
        1.取得雙眼 左右兩點 landmarks
        2.依landmarks 取得雙眼的中間點
        3.取得中間點　與　水平線的角度　
        4.重新取得較大的人臉區域 依步驟3 取得的角度旋轉 (校正)
        5.針對旋轉後的區域 重新取得人臉 即 alignment人臉
        
    =>人臉特徵偵點測:face,lamdmark,setection
     ->即人臉特徵定位:(即眼角、嘴角...)
     ->用途:
         1.改善人臉識別，使人臉識別演算法更有效
         2.人臉平均:將多張人臉進行融合、形成一新的平均人臉
         3.人臉交換:將兩張人臉進行無縫融合，形成換臉(A臉至B臉)
         4.人臉裝扮:人臉化妝，如美顏相機，美圖秀秀...等     

"""


#ex3:
import dlib
import cv2 
import imutils
from imutils.face_utils import FaceAligner
from imutils import face_utils

predictor_path =r'C:\GitHub\python\PY-Learn\shape_predictor_5_face_landmarks.dat'
face_path = r'C:\GitHub\python\PY-Learn\Lena_01.jpg'

detector =  dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
fa = FaceAligner(predictor,desiredFaceWidth=256)

image = cv2.imread(face_path)
image = imutils.resize(image,width=800)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Input',image)
rects = detector(gray,2)

for rect in rects:
    (x,y,w,h) = face_utils.rect_to_bb(rect)
    faceOrig = imutils.resize(image[y:y + h,x:x+w], width=256)
    faceAligned = fa.align(image,gray,rect)
    
    cv2.imshow('Original',faceOrig)
    cv2.imshow('Aligned',faceAligned)
    cv2.waitKey()
    


#ex4:
import numpy as np
import cv2  as cv
import dlib

predictor_path =r'C:\GitHub\python\PY-Learn\shape_predictor_68_face_landmarks.dat'
detector =  dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
img = cv.imread(r'C:\GitHub\python\PY-Learn\person_8.jpg')
img_gray = cv.cvtColor(image,cv2.COLOR_BGR2GRAY)
nums = detector(img_gray,2)

for i in range(len(nums)):
    landmarks = np.matrix([[p.x,p.y]for p in predictor(img,nums[i]).parts()])
    for idx, point in enumerate(landmarks):
        pos = (point[0,0],point[0,1])
        print(idx,pos)
        cv.circle(img,pos,3,color=(0,255,0))
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,str(idx+1),pos,font,0.4,(0,0,255),1,cv.LINE_AA)

cv.imshow('img',img)
cv2.waitKey()    
    
"""
LBPH 人臉辨識
=>Local Binary Pattern Histogram
  局部二值模式長條圖
=>將像素值與其最鄰近的8個像素值逐一比對
  若像素值 > 鄰近像素值，則得到 0
  若像素值 < 鄰近像素值，則得到 1
  將像素值得到的0,1值連接得到一個二進位序列值，再將二進位值轉為十進位，即為像素之LBP值
  列如: 128   36  251
        48   76    9
        11  213   99
    某像點值為76，其餘鄰近像點共8個
         1    0    1
         0         0
         0    1    1    
    由像點正上方起，順時針方向得到二進位的序列值 01011001 = 89
    每一像點均執行以上處理'
    
    face.LBPHFaceRecognizer_create()函數
    格式: (產生LBPH識別器模型)
        cv2.face.LBPHFaceRecognizer_create(
            rdius,半徑值(預設1)  #所有參數皆可省略
            neighbors,鄰近像點個數(預設8)
            grid_x,行方向的像素分組單位(預設8)
            grid_y,列方向的像素分組單位(預設8)
            threshold ) -> 閥值(限測試用，大於該值表示沒有影像)

    
用模型執行訓練
    為識別器模型物件   
    
    對影像進行計算 得到一向量值
    cv.face.LBPHFaceRecognizer.train(src,labels)
    src 原始影像
    labels 每個影像對應的標籤值
    
    
    cv.face.LBPHFaceRecognizer.predict(src)
    src 辨識影像
    
    對人臉進行判斷 我與目前影像最接近的人臉 找到則設為標籤
    (距離 為與 LBPH模型中之 threshold值之距離)
    
    傳回值 = label,confidence
    
    label 識別結果標籤
    
    confidence 可靠評分為識別結果 與 原有模型之間的距離
    0  完全符合
    50> 低於50 結果為比較好  
    80< 之間 >50 很勉強接受
    >80 不被接受



"""
    
#網頁套件_專門爬股票的套件
#https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html

"""
安裝 套件
        pip install twstock 

台灣股市程式，透過 twstock 簡單的查詢 各類股票之資訊以及即時的股票狀況。

#如果拒絕連線 就是因為證交所 可能收盤時間問題  等等後再重試

--------------------------------------------------------------------------------


檢視網頁 
    F12 或是 游標 移至想找的資料->右鍵->檢查 
    就會出來
    
    XHR資料 
    XMLHttpRequest  使網頁可不在刷新的情況下 更新資料

-------------------------------------------------------------------------------

ex 台灣證券交易所 -> 個股日成交資訊 ->選擇一個你有興趣的 ->爬下一整年度的
2884 玉山
2887 台新
2002 台積電
2633 高鐵

使用函式 
    convertDate 民國年月日 轉成西元年月日 的字串
    
def convertDate(date):
    str1 =str(date)
    yearst =str1[:3] #取出民國年
    ryear =str(int(yearst)+1911) #轉為西元元年
    firdate =ryear +str1 [4:6] +str1[7:9]
    return firdate
    



查詢時上面的標籤 network -> XHR 輸入年月查詢 -> 找到 STOCK_DAY?..
    由上述項目 按右鍵 ->open in new tab 
    開啟兩個視窗 去觀察網址內 json的網址 相關聯的地方 按順序
    ....data=20190101...
    ....data=20190201...
    ....data=20190301... 

"""

#查詢股票
import twstock 
stock =twstock.Stock('2002')#填入股票代號
# print('近31天的收盤價')
# print(stock.price)#近31個 收盤價
print('近6天的收盤價')
print(stock.price[-6:])#利用負的 去取得


#股價即時資料
rel =twstock.realtime.get('2002')
if rel['success']:
    print('股票即時資料')
    print(rel)
else:
    print('錯誤'+rel['rtmessage'])

print('目前股價:')
print(rel['realtime']['latest_trade_price'])
#           目前時間            及時股價

#==============================================================================
#==============================================================================
"""


取出個股年度個月資料網址 (先去找出有規律 連續的地方可以找出資料)
網址 分出前後 ....data=2019 "01"   前<- 從月份開始分前後 ->後 01...  
https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2884&_=1595922396478


"""



def twdigit(n):#取出框框的部分 ==將月份處理為兩位
    if (n<10):
        rstr ='0'+str(n)
    else:
        rstr =str(n)
    return rstr


url_1 = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=201901'
url_2 ='01&stockNo=2884&_=1595922396478'
    

for i in range(1,13):
    urlfin =url_1 +twdigit(i) +url_2
    print(urlfin) #抓到網址


#==============================================================================
#20200729
    
    
#01 單月的
def convertDate(date):
    str1 =str(date)
    yearst =str1[:3] #取出民國年
    ryear =str(int(yearst)+1911) #轉為西元元年
    firdate =ryear +str1 [4:6] +str1[7:9]
    return firdate    

import requests
import json,csv
import pandas as pd
import os #處理檔案的套件 文件系統
#----------------
# 顯示中文+製圖匯入
from matplotlib import pyplot as plt
font = {'family' : 'Microsoft JhengHei','weight':'bold','size':'11'}
# family: 字型 /Microsoft JhengHei 微軟正黑體，
# weight:字體
plt.rc('font', **font) # 設定py的繪圖系統的字型項目
plt.rc('axes',unicode_minus=False)#
#----------------


pd.options.mode.chained_assignment =None #取消顯示pandas 資料重設的警告 
filepath =r'C:\GitHub\python\PY-Learn\stockmonth01.csv'

if not os.path.isfile(filepath):#如果檔案不存在 就建立檔案 
    url_twse ='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2884&_=1595922396478'
    res =requests.get(url_twse)#取得 json資料
    jdata =json.loads(res.text)#解析 載入json資料
    
    outputf =open(filepath,'w',newline ='',encoding ='utf-8') #不要空行 所以要設定 newline =''
    outputw =csv.writer(outputf)
    outputw .writerow(jdata['fields'])
    for dataline in (jdata['data']):#逐筆資料寫入 再關閉
        outputw.writerow(dataline)
    outputf.close()
    
pdstock =pd.read_csv(filepath, encoding ='utf-8')#用pd讀取
for i in range(len(pdstock['日期'])):#讀取日期 並轉換格式
    pdstock['日期'][i] =convertDate(pdstock['日期'][i]) 
pdstock['日期'] =pd.to_datetime(pdstock['日期'])#轉換日期欄位 為格式

pdstock.plot(kind ='line',
             figsize =(12,6),
             x ='日期',
             y =['收盤價','最低價','最高價']
             
             )    
#打開檔案 如有亂碼 開一個新的excel匯入字串精靈 設定空格 即可儲存

'''前面的步驟為下


    建立網址中 月份為二進位的函式
    分析網址結構: 
        (檢視各月份網址內容)
        網址前段 +月份 +網址後段
        (網址前後段皆相同 差異在月份數值)
    程式:
        1.列出該年度12個月的網址資料
        2.繪製單月個股統計圖 並將依料儲存為 csv檔案
'''



#02 全年度的

def twodigit(n):
    if (n<10):
        restr ='0' +str(n)
    else:
        restr =str(n)
    return restr

def convertDate(date):
    str1 =str(date)
    yearst =str1[:3] #取出民國年
    ryear =str(int(yearst)+1911) #轉為西元元年
    firdate =ryear +str1 [4:6] +str1[7:9]
    return firdate   
import requests
import json,csv
import pandas as pd
import os #處理檔案的套件 文件系統
import time
#----------------
# 顯示中文+製圖匯入
from matplotlib import pyplot as plt
font = {'family' : 'Microsoft JhengHei','weight':'bold','size':'11'}
# family: 字型 /Microsoft JhengHei 微軟正黑體，
# weight:字體
plt.rc('font', **font) # 設定py的繪圖系統的字型項目
plt.rc('axes',unicode_minus=False)#
#----------------

pd.options.mode.chained_assignment =None #取消顯示pandas 資料重設的警告 
filepath =r'C:\GitHub\python\PY-Learn\stockmonth2017.csv'

url_front ='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=201901'
url_behind ='01&stockNo=2884&_=1595922396478'


if not os.path.isfile(filepath):#如果檔案不存在 就建立檔案 
    for i in range(1,13):
        url_twse =url_front +twodigit(i) +url_behind
        res =requests.get(url_twse)#取得 json資料
        jdata =json.loads(res.text)#解析 載入json資料
    
        outputf =open(filepath,'a',newline ='',encoding ='utf-8') #不要空行所以要設定 newline =''
        outputw =csv.writer(outputf)
        if i ==1:
            outputw .writerow(jdata['fields'])
        for dataline in (jdata['data']):#逐筆資料寫入 再關閉
            outputw.writerow(dataline)
        time.sleep(0.5)
    outputf.close()
    
pdstock =pd.read_csv(filepath, encoding ='utf-8')#用pd讀取
for i in range(len(pdstock['日期'])):#讀取日期 並轉換格式
    pdstock['日期'][i] =convertDate(pdstock['日期'][i]) 
pdstock['日期'] =pd.to_datetime(pdstock['日期'])#轉換日期欄位 為格式

pdstock.plot(kind ='line',
             figsize =(12,6),
             x ='日期',
             y =['收盤價','最低價','最高價']
             )    
#打開檔案 如有亂碼 開一個新的excel匯入字串精靈 設定空格 即可儲存



    
    
    
    
    
    