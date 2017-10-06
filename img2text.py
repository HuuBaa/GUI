#!/usr/bin/env python
#-*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.openpath = StringVar()
        self.savepath = StringVar()
        self.char_list="#*abcdeogqp;:',. "
        self.pack()
        self.create_widgets()

    def selectOpenFilename(self):
        openpath_=askopenfilename()
        self.openpath.set(openpath_)

    def selectSaveDirectory(self):
        savepath_=askdirectory()
        self.savepath.set(savepath_)

    def get_char(self,r,g,b,alpha=256):
        if alpha==0:
            return ' '
        length=len(self.char_list)
        gray=int(0.2126*r+0.7152*g+0.0722*b)
        unit=(256/length)
        return self.char_list[int(gray/unit)]

    def img2text(self):
        from PIL import Image
        import os
        img_openpath=self.OpenEntry.get()
        img_savepath=self.SaveEntry.get()

        try:
            img=Image.open(img_openpath)
        except Exception:
            messagebox.showinfo("failed", "请选择正确格式图片！")
            return

        img_name = img_openpath.split('/')[-1].split('.')[0]
        WIDTH = 120
        x,y=img.size
        HEIGHT=int(WIDTH/x*y)
        img=img.resize((WIDTH,HEIGHT),Image.NEAREST)
        txt=''
        for j in range(HEIGHT):
            for i in range(WIDTH):
                txt+=self.get_char(*img.getpixel((i,j)))
            txt+='\n'

        if img_savepath == '':
            savepath = os.path.join('/'.join(img_openpath.split('/')[:-1]), '%s.txt' % img_name)
            messagebox.showinfo('info', "未选路径,保存到图片路径目录下")
        else:
            savepath = os.path.join(img_savepath, '%s.txt'%img_name)

        try:
            with open(savepath,'w') as f:
                f.write(txt)
            messagebox.showinfo("success","转换成功！")
        except Exception:
            messagebox.showinfo("failed","转换出现错误，请重试！")


    def create_widgets(self):
        self.OpenLabel=Label(self,text="选择图片：")
        self.OpenLabel.grid(row=0,column=0)

        self.OpenEntry=Entry(self,textvariable=self.openpath,width=45)
        self.OpenEntry.grid(row=0,column=1)

        self.OpenButton=Button(self,text="选择图片",command=self.selectOpenFilename)
        self.OpenButton.grid(row=0,column=2)

        self.SaveLabel=Label(self,text="选择保存路径：")
        self.SaveLabel.grid(row=1,column=0)

        self.SaveEntry=Entry(self,textvariable=self.savepath,width=45)
        self.SaveEntry.grid(row=1,column=1)

        self.SaveButton = Button(self, text="选择保存路径", command=self.selectSaveDirectory)
        self.SaveButton.grid(row=1, column=2)

        self.ChangeButton=Button(self,text="开始转换",command=self.img2text)
        self.ChangeButton.grid(row=2,column=2)

        self.Quit=Button(self,text="退出",command=root.destroy,fg="red")
        self.Quit.grid(row=2,column=0)

root=Tk()
root.title("图片转字符画")
root.geometry("600x100")
app=Application(master=root)
app.mainloop()