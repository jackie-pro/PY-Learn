# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:01:14 2020

@author: Jackie
"""


import tkinter as tk
win=tk.Tk() #建立視窗容器物件
win.title('Tk GUI')
label=tk.Label(win, text='測試視窗介面!') #建立標籤物件
label.pack() #顯示元件
button=tk.Button(win, text='確定')
button.pack() #顯示元件
win.mainloop()

# 引入套件
import tkinter as tk

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
top_frame = tk.Frame(window)

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

# 建立事件處理函式（event handler），透過元件 command 參數存取
def echo_Red():
    print('這是"紅色"按鈕!')

def echo_Green():
    print('這是"綠色"按鈕!')

def echo_Blue():
    print('這是"藍色"按鈕!')

def echo_Black():
    print('這是"黑色"按鈕!')

# 以下為 top 群組
left_button = tk.Button(top_frame, text='Red', fg='red', command=echo_Red)
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='Green', fg='green', command=echo_Green)
middle_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='Blue', fg='blue', command=echo_Blue)
right_button.pack(side=tk.LEFT)

# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_Black)
# 讓系統自動擺放元件（靠下方）
bottom_button.pack(side=tk.BOTTOM)

# 運行主程式
window.mainloop()



#=============================

import tkinter as tk
import math

window = tk.Tk()
window.title('BMI App')
window.geometry('400x120')
window.configure(background='white')

def calculate_bmi_number():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height, 2), 2)
    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text=result)

def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'

header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（m）')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)
calculate_btn.pack()

window.mainloop()