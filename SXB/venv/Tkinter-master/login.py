import tkinter as tk
import tkinter.messagebox as msg
import pymysql
import os
import user
import manage

BACK_PATH = "resources" + os.sep + "background.gif"


def exit1():
    root.destroy()
    user.frame()


def exit2():
    root.destroy()
    manage.frame()


def frame():
    global root
    root = tk.Tk()
    root.title('YTU图书系统')
    photo = tk.PhotoImage(file=BACK_PATH)
    root.geometry("700x260")
    theLabel = tk.Label(root, image=photo, compound=tk.CENTER, fg="white").grid(row=0, column=0)
    labe1 = tk.Label(root, text="欢迎来到YTU图书系统，请选择用户类型：", font=36).grid(row=0, column=1)
    tk.Button(root, text='普通用户', width=10, height=2, command=exit1).grid(row=1, column=1, )
    tk.Button(root, text='管理员', width=10, height=2, command=exit2).grid(row=2, column=1)
    root.mainloop()


if __name__ == '__main__':
    frame()
