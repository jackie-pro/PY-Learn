# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:28:36 2020

@author: Jackie
"""


"""
Client
IP:Server IP，str
port：Server port，int
"""
 
import socket
 
#創建socket對象
client_sk = socket.socket()
 
# 連接Server
client_sk.connect(('192.168.43.176',9999))
 
# 通信
print(str(client_sk.recv(1024), encoding='utf-8'))
while True:
    inp = input("請輸入：")
    client_sk.sendall(bytes(inp, encoding='utf-8'))
    if inp == 'q':
        break
    else:
        print(str(client_sk.recv(1024), encoding='utf-8'))
# 關閉連結
client_sk.close()