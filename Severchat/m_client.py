# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:12:18 2020

@author: Jackie
"""
#client端

import socket 
import threading 
outString = '' 
inString = '' 
nick = '' #發送信息的函數 
def DealOut(sock): 
    global nick,outString #聲明為全局變量，進行賦值,這樣才可以生效 
    while True: 
        outString = input() #輸入 
        if outString == 'q':
            client.close()
            break
        else:
            outString = nick+':'+outString
            client.sendall(bytes(outString, encoding='utf-8'))#發送 #接收信息 

   
        
def DealIn(sock):
    global inString 
    while True: 
        try: 
            inString = str(client.recv(1024), encoding='utf-8')
            if not inString: 
                break 
            
            if outString != inString: 
                print(inString) 
        except: 
            break 
        
nick = input('請輸入你的名字:')#名字 
HOST = '122.116.118.222' #ip地址 
PORT = 28018
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(bytes(nick, encoding='utf-8')) #接收信息 發送信息 
thin = threading.Thread(target=DealIn,args=(client,))#調用threading 創建一個接收信息的線程'
thin.start() 
thout = threading.Thread(target=DealOut,args=(client,))#創建一個發送信息的線程，聲明是一個元組 
thout.start()
