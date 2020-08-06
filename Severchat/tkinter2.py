# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:57:00 2020

@author: Jackie
"""

import tkinter as tk
a = 1
def set(x):
    global a
    print(x+a)
    a += x
window = tk.Tk()
btn = tk.Button(window, command= lambda x=1: set(x))