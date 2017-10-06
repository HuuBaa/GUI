# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput=Entry(self)
#         self.nameInput.pack()
#         self.alertButton=Button(self,text='Quit',command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name=self.nameInput.get() or 'world'
#         messagebox.showinfo('Message','Hello, %s'%name)
#
# app=Application()
# app.master.title('Huu')
# app.mainloop()
#
#

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()