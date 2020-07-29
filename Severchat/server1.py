# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:42:04 2020

@author: Jackie
"""


import socket
HOST = '192.168.43.176'
PORT = 8001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    print('Client message is:', clientMessage)

    serverMessage = '測試正常!'
    conn.sendall(serverMessage.encode())
    conn.close()