# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:34:03 2020

@author: Jackie
"""


# -*- coding: utf-8 -*-
import sys
import socket
from PyQt5 import QtWidgets
from socket_chatbot import Ui_MainWindow

# HOST & PORT
HOST = '192.168.43.176'
PORT = 8001


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textBrowser.append('<font color="#FF0000">Server: Hello! I will repeat what you said!</font>')
        self.HOST = HOST
        self.PORT = PORT

        self.ui.pushButton.clicked.connect(self.buttonEvent)

    def buttonEvent(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.clear()
        self.ui.textBrowser.append('User: '+text)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.HOST, self.PORT))
        self.client.sendall(text.encode())

        # Server message
        serverMessage = str(self.client.recv(1024), encoding='utf-8')
        self.ui.textBrowser.append('<font color="#FF0000">Server: '+serverMessage+'</font>')
        self.client.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
