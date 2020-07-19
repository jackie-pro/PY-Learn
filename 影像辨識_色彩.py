# -*- coding: utf-8 -*-
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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
             






'''







































































































