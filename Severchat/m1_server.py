# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:28:19 2020

@author: Jackie
"""
"""
Server
localhost：Server的IP，str
port: Server port，int
"""

#服务端开放的ip和端口号port
#HOST = ''
#PORT = 28018
 
import socketserver
 
#創建MysServer類
class MyServer(socketserver.BaseRequestHandler):
 
    #定義handle方法，函數名只能是handle
    def handle(self):
        conn = self.request
        conn.sendall(bytes("歡迎光臨！\n 按q结束聊天哦！", encoding='utf-8'))
        while True:
            ret_nik = str(conn.recv(1024), encoding='utf-8')
            if ret_nik == 'q':
                break
            else:
                conn.sendall(bytes("我已經收到：" + ret_nik, encoding='utf-8'))
                print(ret_nik)
                
            ret = str(conn.recv(1024), encoding='utf-8')
            if ret == 'q':
                break
            else:
                conn.sendall(bytes("我已經收到：" + ret, encoding='utf-8'))
                print(ret)                
 
 
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('', 28018), MyServer)
    server.serve_forever()