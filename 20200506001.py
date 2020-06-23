# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#===========================================================
"""
#20200506 - 第一個測試

a=1
b=100
print("sum=",a+b)
print("Hello World")

"""
#===========================================================
#輸入2個數字,求最大公因數
num1 = int(input('請輸入第一個數值:')) #num1=變數 int=資料型態(整數) input=
num2 = int(input('請輸入第二個數值:'))
if num1 < num2: #if=條件式 
    tmp_num = num1
    num1 = num2
    num2 = tmp_num
while num2 != 0 : #while=迴圈 (如果上面條件成立才執行)
    tmp_num = num1 % num2
    num1 = num2
    num2 = tmp_num
print('最大公因數',num1) #print=輸出 (格式字串 % 資料)

#===========================================================
"""
Python程式檔格式: *.py
jupyter程式檔格式: *.ipynb
Jupyter檔案放置於本機端 使用者下 (C:\Users\Jackie\.ipynb_checkpoints)
"""
