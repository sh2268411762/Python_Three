import tkinter as tk
import tkinter.messagebox as msg
import search
from tkinter import ttk
import pymysql


def frame():
    window = tk.Tk()
    window.title('管理员')
    window.geometry('900x700')
    lable0 = tk.Label(window, text='欢迎来到梓豪图书馆', bg='pink', font=('微软雅黑', 50)).pack()  # 上

    lable1 = tk.Label(window, text='请选择操作:', font=('微软雅黑', 20)).place(x=80, y=400)  # 下
    tk.Button(window, text='进购图书', font=('微软雅黑', 15), width=10, height=2, command=purchase).place(x=350, y=250)
    tk.Button(window, text='注销图书', font=('微软雅黑', 15), width=10, height=2, command=cancel).place(x=350, y=350)
    tk.Button(window, text='信息查询', font=('微软雅黑', 15), width=10, height=2, command=search.frame).place(x=350, y=450)
    window.mainloop()


def purchase():  # 进购图书
    global win
    win = tk.Tk()
    win.title('管理员')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='请填写进购图书的信息:', font=('微软雅黑', 20)).place(x=30, y=100)

    tk.Label(win, text='图书类目：', font=('宋体', 12)).place(x=30, y=200)
    global list  # 这个是一个下拉页表项，只能从下面的list['values']里边选
    comvalue = tk.StringVar()
    list = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('全部', '人文', '艺术', '计算机', '科技', '杂志')
    list.current(0)  # 默认显示'全部'

    global b_name
    tk.Label(win, text='书名：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(win, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='作者：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    global price
    tk.Label(win, text='价格：', font=('宋体', 12)).place(x=460, y=200)
    price = tk.Entry(win, font=('宋体', 12), width=10)
    price.place(x=510, y=200)

    global amount
    tk.Label(win, text='数量：', font=('宋体', 12)).place(x=560, y=200)
    amount = tk.Entry(win, font=('宋体', 12), width=5)
    amount.place(x=610, y=200)

    tk.Button(win, text='确认添加', font=('宋体', 12), width=10, command=add).place(x=700, y=195)


def add():  # 添加图书信息到数据库中
    sql = "INSERT INTO book VALUES('%s','%s','%s','%s','%s')" % (
    list.get(), b_name.get(), author.get(), price.get(), amount.get())
    db = pymysql.connect("localhost", "root", "sunhao2268411762", "library")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    db.close()
    msg.showinfo(title='成功！', message='新书已入库！')


def cancel():  # 撤销图书
    global win
    win = tk.Tk()
    win.title('管理员')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='请填写注销图书的信息:', font=('微软雅黑', 20)).place(x=30, y=100)

    tk.Label(win, text='图书类目：', font=('宋体', 12)).place(x=30, y=200)
    global list
    comvalue = tk.StringVar()
    list = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('全部', '人文', '艺术', '计算机', '科技', '杂志')
    list.current(0)

    global b_name
    tk.Label(win, text='书名：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(win, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='作者：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    tk.Button(win, text='确认注销', font=('宋体', 12), width=10, command=delete).place(x=600, y=195)


def delete(): #删除图书
    sql = "DELETE FROM book WHERE type='%s' AND name='%s' AND author='%s'" % (list.get(), b_name.get(), author.get())
    db = pymysql.connect("localhost", "root", "sunhao2268411762", "library")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    msg.showinfo(title='成功！', message='该书已删除！')

