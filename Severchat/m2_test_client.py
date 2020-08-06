# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:24:07 2020

@author: Jackie
"""
#Client

import socket
import threading
import tkinter as tk


address='122.116.118.222'   #服務器的ip地址
port=9000
buffsize=1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address,port))



def recv():
    while True:
        recvdata = client.recv(buffsize).decode('utf-8')
        gui.ListBox.insert(END, recvdata)
        print('\n' + recvdata + '\n')

class GUI:
    def __init__(self, root):
        self.root = root
        self.ListBox = Listbox(self.root)
        self.ListBox.pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        self.sendBtn = Button(self.root, text='發送', command=self.send)
        self.sendBtn.pack()

    def send(self):
        senddata = self.entry.get()
        client.send(senddata.encode())

def createGUI():
    global gui
    root = tk.Tk()
    gui = GUI(root)
    root.title('客戶端')
    root.mainloop()

if __name__ == '__main__':
    t1 = threading.Thread(target=recv, args=(), name='recv')
    t2 = threading.Thread(target=createGUI, args=(), name='gui')
 
    t1.start()
    t2.start()
