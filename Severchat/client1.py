# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:54:21 2020

@author: Jackie
"""

#Client測試連線
import socket

HOST = '122.116.118.222' #遠端Server IP,防火牆已開port
PORT = 28018 #port
#client傳回去的文字
clientname = 'Client_1'
clientMessage = 'Hello!'


# AF_INET => IPV4, SOCK_STREAM => TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect() => 連接Server
client.connect((HOST, PORT))
#將client文字轉成二進位,send 過去給server
client.sendall(clientname.encode())
client.sendall(clientMessage.encode())
#將Server send過來的文字 從二進位轉成字串
serverMessage = str(client.recv(1024), encoding='utf-8')
#印出Server send過來的文字
print('Server:', serverMessage)

#關閉socket連結
client.close()