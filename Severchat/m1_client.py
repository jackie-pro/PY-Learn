# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:28:36 2020

@author: Jackie
"""



#Client

 
import socket

HOST = '122.116.118.222' #遠端Server IP,防火牆已開port
PORT = 28018 #port
#創建socket對象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 連接Server
client.connect((HOST, PORT))
 
# 通信
print(str(client.recv(1024), encoding='utf-8'))
while True:
    nik = input("請輸入你的暱稱：")
    client.sendall(bytes(nik, encoding='utf-8'))
    if nik == 'q':
        break
    else:
        print(str(client.recv(1024), encoding='utf-8'))    
        
    inp = input("請輸入：")
    client.sendall(bytes(inp, encoding='utf-8'))
    if inp == 'q':
        break
    else:
        print(str(client.recv(1024), encoding='utf-8'))
# 關閉連結
client.close()