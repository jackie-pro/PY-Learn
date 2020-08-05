# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:42:04 2020

@author: Jackie
"""

#Server 測試連線
import socket

HOST = '' #遠端Server IP :122.116.118.222 ,防火牆已開port,因為要接收外部連線所以用''空字串
PORT = 28018  #port

# AF_INET => IPV4, SOCK_STREAM => TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind 遠端IP 和port
server.bind((HOST, PORT))

#開啟5個queqe
server.listen(5)

#用while迴圈 不停地等待回應
while True:
    # conn => 新的socket , addr => client的IP, accept() => server端地等待連接
    conn, addr = server.accept() 
    #recv接收client來的文字並由二進位轉成文字
    clientName = str(conn.recv(1024), encoding='utf-8')
    clientMessage = str(conn.recv(1024), encoding='utf-8') 
    #印出連線的過來的IP
    print('Connect form :', clientName)
    #印出client來的文字
    print('%s message is: %s' % (clientName,clientMessage))
    #設定Server要回覆的文字
    serverMessage = '連線測試正常!'
    #將Server回覆文字轉成二進位,send給client
    conn.sendall(serverMessage.encode())
    #關閉socket連結
    conn.close()
    