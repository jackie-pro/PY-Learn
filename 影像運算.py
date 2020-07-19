影像運算
=>影像加法運算
  →灰階影像中,像素以8位元表示,像素值範圍為0~255
  →影像加法:
      兩影像對應的像素值相加<=255→直接相加
      兩影像對應的像素值相加>255→直接相加結果 mod 256 得出結果(255+58)%256=57
  →add():影像像素相加
           格式:(CV2,add(影像1,影像2))
  =>影像加法:
      使用 + → 變暗
      使用add()→ 變亮
        
ex1:
import numpy as np
img1 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1 = \n',img1)
print('img2 = \n',img2)
print('img1 + img2 = \n',img1 + img2)


ex2:
import cv2 as cv
import numpy as np
img1 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1 = \n',img1)
print('img2 = \n',img2)
img3 = cv.add(img1 , img2)
print('cv.add(img1 , img2) = \n', img3)


ex3:
import cv2 as cv
img = cv.imread(r'C:\Users\ASUS\Desktop\python\lena.jpg' , 0)
a = img
result1 = a + img
result2 = cv.add(img , a)
cv.imshow('image',img)
cv.imshow('image1',result1)
cv.imshow('image2',result2)
cv.waitKey()

影像加權和:
=>計算影像像素值和並加入加權值計算
=>使用函數:addWeighted
addWeighted(src1,a,src2,b,c)
#src1:影像1
#a:影像1加權
#src2:影像2
#b:影像2加權
#c:亮度調節
=>公式:src1 * a + src2 * b + c


ex4:
import cv2 as cv
import numpy as np
img1 = np.ones((3,4,3),dtype = np.uint8)*100
img2 = np.ones((3,4,3),dtype = np.uint8)*10
a = 3
img3 = cv.addWeighted(img1 , 0.6 , img2 , 5 , a)
print(img3)



ex5:(合併影像)
import cv2 as cv    
img1 = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\landscape.jpg')
img2 = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\Lena512.jpg')
result = cv.addWeighted(img1,0.6,img2,0.4,0)
cv.imshow('image1',img1)
cv.imshow('image2',img2)
cv.imshow('image3',result)
cv.waitKey()

※兩影像大小及類型必須相同
=>ROI:Region of Interest感興趣區域於程式中
自行設定所需要處理的區域範圍


ex6:(臉部合併)
import cv2 as cv    
img = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\lena_01.jpg',1)
US1 = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\US1_600.jpg',1)
cv.imshow('image',img)
cv.imshow('banknote',US1)
img_face = img[80:230,250:370] #人臉ROI
US1_face = US1[80:230,240:360] #鈔票ROI
add = cv.addWeighted(img_face,0.6,US1_face,0.4,0) #將人像和鈔票的ROI執行運算,設定給app變數
US1[80:230,240:360] = add #設定合併影像ROI區域
cv.imshow('result',US1)
cv.waitKey()

 
逐位元邏輯運算
=>bitwise_and:且
  bitwise_and:或
  bitwise_xor:互斥
  bitwise_not:反向

=>and運算:
    兩個運算元(邏輯值)都為真其結果為真
+>函數:bitwise_and
bitwise_and(src1,src2)

=>任何數值n與數值 0 and 運算,結果為0
=>任何數值n與數值255做and運算,結果為數值n本身

以上述定裡可建立掩膜影像(只有兩個值)


ex7:
import cv2 as cv
import numpy as np
img1 = np.random.randint(0,255,(5,5),dtype = np.uint8) 
img2 = np.zeros((5,5),dtype = np.uint8) #掩膜影像,透過numpy的zero影像
img2[0:3 , 0:3] = 255 #掩膜影像,行列位置設置255
img2[4 , 4] = 255 #掩膜影像最右下角的位置設置255
a = cv.bitwise_and(img1 , img2) #做and運算,全為0
print("img1 = \n" , img1)
print("img2 = \n" , img2)
print("a = \n" , a)


=>or運算:
    兩個運算元(邏輯值)有一個為真結果為真
=>函數:bituise_or(src) 

=>xor運算:
    兩個運算元都不相同,結果為真
    ->函數:bitwise_xor
    bituise_xor(src1 , src2)


    11000110(198)
xor)11011011(219)
__________________
    00011101(29)

=>add函數:
    add(src1,src2,mask)

#==============================================
    
位元平面分解

=>將灰階影像中同一個位元上的二進位像素值進行組合,
可得到一個二進位影像,「該影像撐為灰階影像的位元平面」,
其組合過程稱為位元平面分解。

=>灰階影像中,每依像素使用8位元二進位值表示,
值的範圍為0~255,表示為: 
    a7 * 2**6 + a5 * 2**5 + a4 * 2**4 + a3 * 2**3 +
    a2 * 2**2 + a1 * 2**1 + a0 * 2**0
    

a1~a0的值為0或1
a7值對影像影響最大
a0值對影像影響最小
a7加權最高,其位元平面與原影像相關性最高
與原影像最類似

a0.......最低,...............
                         最低
                         
該位元平面最雜亂

=>執行步驟:
    ->影像前置處理
    ->建置分析矩陣
    ->分析位元平面
    ->設定值處理
    ->顯示影像

ex8
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\lena512.jpg' , 0)
cv.imshow('image' , img)
r,c = img.shape
x = np.zeros((r , c , 8) , dtype = np.uint8)

for i in range(8):
    x[:,:,i] = 2 ** i
r = np.zeros((r , c , 8) , dtype = np.uint8)

for i in range(8):
    r[:,:,i] = cv.bitwise_and(img , x[:,:,i])
    mask = r[:,:,i] > 0
    r[mask] = 255
    cv.imshow(str(i) , r[:,:,i])
cv.waitKey()    


#=====================================
影像加密及解密
=>原始影像與金鑰影像
進行互斥運算,產生加密影像(emcryption)

=>加密影像與金鑰影像
進行互斥運算,產生解密影像(decryption)

=>a:原始資料(明文) , b:金鑰 ,c:加密(xor(a,b))
xor(a , b) = c , xor(c , b) = a

=>位元運算可實踐像素點加密,通常須處理的像素點為灰階值,
如某像素點值為216(明文),以178(此值由加密者自行決定)作為加密金鑰,
將此二數值進行互斥運算。

    11011000(216) ->明文
xor)10110010(178) ->金鑰
____________________
    01101010(106) ->加密

bitwise_xor(216,178) = 106加密
bitwise_xor(106,178) = 216解密


ex9:
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\Lena512.jpg',0)
cv.imshow('image' , img)
r,c = img.shape
key = np.random.randint(0,256,size=[r,c],dtype = np.uint8)
encryption = cv.bitwise_xor(img,key)
decryption = cv.bitwise_xor(encryption,key)
cv.imshow('image',img)
cv.imshow('key',key)
cv.imshow('encryption',encryption)
cv.imshow('decryption',decryption)
cv.waitKey()


浮水印(資訊隱藏)
=>最低有效位(Least Significant Bit; LSB)
    ->二進位數字中的第0位(最低位)
    
=>將需要隱藏的二值影像嵌入載體影像的最低有效位,
即將載體影像的LSB取代為需要隱藏的目的
因二值影像處於載體影像的LSB上,對載體影像影響非常不明顯,故具較高的隱蔽性。
嵌入過程:
    ->將影像二值化(處理為灰階),輝接二值影像中,像素值只有0,255,表示為黑色,白色
    ->將255轉為1,可得到二進位的灰階影像,只用一個位元表達像素值


import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\Lena512.jpg',0)
watermark = cv.imread(r'C:\Users\ASUS\Desktop\python\20200717\watermark.jpg',0)
w = watermark[:,:] > 0
watermark[w] = 1
r,c = img.shape

t254 = np.ones((r,c),dtype = np.uint8)*254
imgh7 = cv.bitwise_and(img , t254)
e = cv.bitwise_or(imgh7 , watermark)

t1 = np.ones((r,c),dtype = np.uint8)
wm = cv.bitwise_and(e , t1)
print(wm)
w = wm[:,:] > 0
wm[w] = 255
cv.imshow('image',img)
cv.imshow('watermark',watermark*255)
cv.imshow('e',e)
cv.imshow('wm',wm)
cv.waitKey()    




ex12
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\Python\20200717\Lena512.jpg',0)

r,c = img.shape
mask = np.zeros((r,c),dtype = np.uint8)
mask[100:400,200:400] = 1

key = np.random.randint(0,256,size = [r,c],dtype = np.uint8)
imgxorkey = cv.bitwise_xor(img, key)
encryptFace = cv.bitwise_and(imgxorkey,mask*255)
noface1 = cv.bitwise_and(img, (1-mask)*255)
maskface = encryptFace + noface1
extractOriginal = cv.bitwise_xor(maskface, key)
extractFace = cv.bitwise_and(extractOriginal,mask*255)
noface2 = cv.bitwise_and(maskface, (1-mask)*255)
extractimg = noface2 + extractFace


cv.imshow('img' , img)
cv.imshow('mask' ,mask*255)
cv.imshow('1-mask', (1-mask)*255)
cv.imshow('key', key)
cv.imshow('imgxorkey' , imgxorkey)
cv.imshow('encryptFace' ,encryptFace)
cv.imshow('noface1' ,noface1)
cv.imshow('maskface' ,maskface)
cv.imshow('extractOriginal',extractOriginal)
cv.imshow('extractFace',extractFace)
cv.imshow('noface2' ,noface2)
cv.imshow('extractimg' ,extractimg)
cv.waitKey()



色彩空間類型轉換
=>函數: cvtColor()
cvtColor(src , mode) #src原始影像,mod色彩空間轉換
openCV色彩模型為BGR,與RGB不同。
RGB/BGR轉換到GRAY(灰階)
GRAY = 0.299 * R + 0.587 * G + 0.114 * B




import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size = [2,4,3],dtype = np.uint8)
rst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('img = \n' , img)
print('rst = \n' , rst)
print('像素點(1,0) 直接計算得到的值 =' , 
      img[1,0,0]*0.114 + img[1,0,1]*0.587 + img[1,0,2]*0.299)
print('像素點 (1,0) 使用公式 cv.cvtColor() 轉換值 =', rst[1,0])








   