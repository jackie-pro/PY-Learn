# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:10:57 2020

@author: Jackie
"""

#Server端

import socket 
import threading 

def clientThreadIn(conn,nick):
    global data 
    while True:
        try:
            temp = str(conn.recv(1024), encoding='utf-8')#客戶端發過來的消息
            if not temp:
                conn.close()
                return
            
            NotifyAll(temp) 
            print(data) 
            
        except: 
            NotifyAll(nick+' 離開聊天室了!')#出現異常就退出 
            print(data) 
            return 
    
def clientThreadOut(conn,nick):
    global data 
    while True:
        if con.acquire():
            con.wait()#堵塞，放棄對資源的占有等待通知運行後面的代碼 
            if data: 
                try: 
                    conn.sendall(bytes(data, encoding='utf-8')) 
                    con.release() 
                except: 
                    con.release()
                    return 

def NotifyAll(sss): 
    global data 
    if con.acquire(): 
        data = sss
        con.notifyAll()#當前線程放棄對資源的占有，通知所有等待x線程 
        con.release()
         
con = threading.Condition()#條件    
HOST = '' # ip地址 
PORT = 28018
data = '' 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))  
server.listen(5) 
print('Server 程式已啟動 !')
print('Server 正在等待連線中...')    

while True:
    conn,addr = server.accept()#接受連接 
    print('連線來源IP: '+addr[0]+' PORT:'+str(addr[1])) 
    nick = str(conn.recv(1024), encoding='utf-8')#獲取用戶名 
    NotifyAll('歡迎 '+nick+' 進入聊天室!') 
    print(data)
    print('現在有 '+ str((threading.activeCount()+1)/2)+' 人在線上!') 
    conn.sendall(bytes(data, encoding='utf-8'))  
    threading.Thread(target=clientThreadIn,args=(conn,nick)).start()
    threading.Thread(target=clientThreadOut,args=(conn,nick)).start()

