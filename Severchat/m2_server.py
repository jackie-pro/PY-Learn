# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:04:50 2020

@author: Jackie
"""
#Server

from tkinter import *
import socket
import threading
 

address='192.168.43.176'
port=9000
buffsize=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address,port))
s.listen(5)     #最大連接數
conn_list = []
conn_dt = {}

def tcplink(sock,addr):
    while True:
        try:
            recvdata=sock.recv(buffsize).decode('utf-8')
            print(recvdata, addr)
            gui.infoList.config(state=NORMAL)
            gui.infoList.insert(END, addr, 'name')
            gui.infoList.insert(END, '：\t')
            gui.infoList.insert(END, recvdata, 'conment')
            gui.infoList.insert(END, '\n\n')
            gui.infoList.config(state=DISABLED)
            if not recvdata:
                break
        except:
            sock.close()
            print(addr,'offline')
            _index = conn_list.index(addr)
            gui.listBox.delete(_index)
            conn_dt.pop(addr)
            conn_list.pop(_index)
            break
 
def recs():
    while True:
        clientsock,clientaddress=s.accept()
        if clientaddress not in conn_list:
            conn_list.append(clientaddress)
            conn_dt[clientaddress] = clientsock
            gui.listBox.insert(END, clientaddress)
        print('connect from:',clientaddress)
        #在這里創建線程，就可以每次都將socket進行保持
        t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))
        t.start()


class GUI:
    def __init__(self, root):
        self.root = root
        self.leftFrame = Frame(self.root, width=20, height=30)
        self.leftFrame.grid(row=0, column=0)
        self.rightFrame = Frame(self.root, width=20, height=30)
        self.rightFrame.grid(row=0, column=1)
        Label(self.leftFrame, text='在線IP地址列表').grid(row=0, column=0)
        self.listBox = Listbox(self.leftFrame, width=15, height=10)
        self.listBox.grid(row=1, column=0)
        self.entry = Entry(self.rightFrame, font=('Serief', 18), width=30)
        self.entry.grid(row=0, column=0)
        self.sendBtn = Button(self.rightFrame, text='發送', command=self.send, width=10)
        self.sendBtn.grid(row=0, column=1)
        Label(self.rightFrame, text='聊天信息').grid(row=1, columnspan=2)
        self.infoList = Text(self.rightFrame, width=40, height=12)
        self.infoList.grid(row=2, columnspan=2)
        self.infoList.tag_config('name', background='yellow', foreground='red')
        self.infoList.tag_config('conment', background='black', foreground='white')

 
    def send(self):
        _index = self.listBox.curselection()
        conn_dt[self.listBox.get(_index)].sendall(self.entry.get().encode('utf-8'))
        self.entry.delete(0, END)

def createGUI():
    global gui
    root = Tk()
    gui = GUI(root)
    root.title('Server')
    root.mainloop()

if __name__ == '__main__':
    t1 = threading.Thread(target=recs, args=(), name='rec')
    t2 = threading.Thread(target=createGUI, args=(), name='GUI')

    t1.start()
    t2.start()