#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('Test')
#设置大小和位置
win.geometry('400x400+500+200')

#<Button-1>鼠标左键
#<Button-3>鼠标右键
#<Button-2>鼠标中键
#<Double-Button-1>鼠标左键双击
#<Double-Button-3>鼠标右键双击
#<Double-Button-2>鼠标中键双击
#<Triple-Button-1>鼠标左键三击
#<Triple-Button-3>鼠标右键三击
#<Triple-Button-2>鼠标中键三击
def func(event):
    print event.x, event.y

button1 = tkinter.Button(win, text='leftmouse button')
#bind    给控件绑定事件
button1.bind('<Triple-Button-1>', func)
button1.pack()






win.mainloop()