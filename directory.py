#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename

def selectPath():
    path_ = askopenfilename()
    path.set(path_)

root = Tk()
path = StringVar()

Label(root,text = "目标路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)

root.mainloop()