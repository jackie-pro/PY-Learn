# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:24:07 2020

@author: Jackie
"""
#Client

from socket import *
import threading
from tkinter import *


address='192.168.43.176'   #服務器的ip地址
port=9000
buffsize=1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address,port))
 


def recv():
    while True:
        recvdata = s.recv(buffsize).decode('utf-8')
        gui.listBox.insert(END, recvdata)
        print('\n' + recvdata + '\n')

class GUI:
    def __init__(self, root):
        self.root = root
        self.listBox = Listbox(self.root)
        self.listBox.pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        self.sendBtn = Button(self.root, text='發送', command=self.send)
        self.sendBtn.pack()

    def send(self):
        senddata = self.entry.get()
        s.send(senddata.encode())

def createGUI():
    global gui
    root = Tk()
    gui = GUI(root)
    root.title('客戶端')
    root.mainloop()

if __name__ == '__main__':
    t1 = threading.Thread(target=recv, args=(), name='recv')
    t2 = threading.Thread(target=createGUI, args=(), name='gui')
 
    t1.start()
    t2.start()
