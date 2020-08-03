# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:12:18 2020

@author: Jackie
"""
#socket 服務端和客戶端 服務端監聽 客戶端的請求 連結確認 
import socket 
import threading 
outString = '' 
inString = '' 
nick = '' #發送信息的函數 
def DealOut(sock): 
    global nick,outString #聲明為全局變量，進行賦值,這樣才可以生效 
    while True: 
        outString = input() #輸入 
        outString = nick+':'+outString#拼接cd
        sock.send(outString)#發送 #接收信息 
        
def DealIn(sock):
    global inString 
    while True: 
        try: 
            inString = sock.recv(1024) 
            if not inString: 
                break 
            
            if outString != inString: 
                print(inString) 
        except: 
            break 
        
        nick = input('input your nickname:')#名字 
        ip = input('input your server ip address:')#ip地址 
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#創建套接字,默認為ipv4 
        sock.connect((ip,1111))#發起請求，接收的是一個元組 
        sock.send(nick) #多線程 接收信息 發送信息 
        thin = threading.Thread(target=DealIn,args=(sock,))#調用threading 創建一個接收信息的線程'
        thin.start() 
        thout = threading.Thread(target=DealOut,args=(sock,))#創建一個發送信息的線程，聲明是一個元組 
        thout.start()
