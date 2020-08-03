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
            temp = conn.recv(1024)#客戶端發過來的消息
            if not temp:
                conn.close()
                return
            
            NotifyAll(temp) 
            print(data) 
        except: 
            NotifyAll(nick+'leaves the room')#出現異常就退出 
            print(data) 
            return 
    
def clientThreadOut(conn,nick):
    global data 
    while True:
        if conn.acquire():
            conn.wait()#堵塞，放棄對資源的占有 等待通知運行後面的代碼 
            if data: 
                try: 
                    conn.send(data) 
                    conn.release() 
                except: 
                    conn.release 
                    return 

def NotifyAll(conn,ss): 
    global data 
    if conn.acquire():#獲取鎖 
        data = ss 
        conn.notifyAll()#當前線程放棄對資源的占有，通知所有等待x線程 
        conn.release()
         
    conn = threading.Condition()#條件    
    Host = input('input the server ip address:') # ip地址 
    print(Host)
    port = 1111
    data = '' 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#創建套接字 
    print('Socket created') 
    s.bind((Host,port)) #把套接字綁定到ip地址 
    s.listen(5) 
    print('Socket now listening')
    
    while True:
        conn,addr = s.accept()#接受連接 
        print('Connected with'+'' +addr[0]+':'+str(addr[1])) #字符串拼接 
        nick = conn.recv(1024)#獲取用戶名 
        NotifyAll('Welcome'+' '+nick+' to the room!') 
        print(data) 
        print(str((threading.activeCount()+1)/2)+'person(s)') 
        conn.sendall(data) 
        threading.Thread(target=clientThreadIn,args=(conn,nick)).start()
        threading.Thread(target=clientThreadOut,args=(conn,nick)).start()

