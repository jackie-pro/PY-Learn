# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:13:19 2020

@author: Jackie
"""


#=========================額外練習
import os
entries = os.scandir('c:\\GitHub\\test\\')
print(entries)




import os
srt = []
with os.scandir('c:\\GitHub\\test\\') as entries:
    for entry in entries:
        info = entry.stat()
        print(info.st_mtime)
        lst = srt.append(entry.st)
if srt >= 5:
    
print(srt)  
print(len(srt))
