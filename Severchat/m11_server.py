# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:44:58 2020

@author: Jackie
"""



#服务端开放的ip和端口号port
LOCALHOST = '192.168.43.176'
PORT = 9999
 
import socketserver
 
#創建MysServer類
class MyServer(socketserver.BaseRequestHandler):
 
    #定義handle方法，函數名只能是handle
    def handle(self):
        conn = self.request
        conn.sendall(bytes("歡迎光臨！\n 按q结束聊天哦！", encoding='utf-8'))
        while True:
            clientMessage = str(conn.recv(1024), encoding='utf-8')
            
            if clientMessage == 'q':
                break
            else:
                conn.sendall(bytes("我已經收到：" + clientMessage, encoding='utf-8'))
                print('Client message is:', clientMessage)
                
 
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer((LOCALHOST, PORT), MyServer)
    server.serve_forever()