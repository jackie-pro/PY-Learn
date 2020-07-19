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













 












