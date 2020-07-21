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
    boxFilter()函數
    ->cv2.boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
    src : 影像
    ddepth : 影像深度，每一像素能展示的顏色數，一般使用-1表示與原始像素採用相同的影像深度
    ksize : 濾波核大小，均值處理中鄰近範圍的高度、寬度
    anchor : 錨點，目前計算均值的點，位於該核中心點的位置，使用預設值即可(-1,-1)
    normlize : 1 : 即為均值濾波，功能同blur()，預設值.
               0 : 加總，若加總超過255(最大值)，則會得到白色影像
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