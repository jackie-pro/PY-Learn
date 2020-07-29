# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:54:21 2020

@author: Jackie
"""


import socket

HOST = '192.168.43.176'
PORT = 8001
clientMessage = 'Hello!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(clientMessage.encode())

serverMessage = str(client.recv(1024), encoding='utf-8')
print('Server:', serverMessage)

client.close()