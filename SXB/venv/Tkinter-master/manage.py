import tkinter as tk
import tkinter.messagebox as msg
import pymysql
import os
import login

BACK_PATH = "resources" + os.sep + "background6.gif"
BACK_PATH2 = "resources" + os.sep + "background4.gif"


def check_book():
    db = pymysql.connect("localhost", "root", "zyj19991116", "library")
    cursor = db.cursor()
    a = input_book.get()
    sql = "SELECT * FROM book WHERE bname = '%s'" % (a)
    cursor.execute(sql)
    results = cursor.fetchone()
    if results:
        root3 = tk.Tk()
        root3.title('查询到的书')
        val = "您要查询的书号为：%s" % (results[0])
        print2 = tk.Label(root3, text=val)
        print2.grid(row=1, column=0, padx=10, pady=5)
        val = "您要查询的书的作者为：%s" % (results[1])
        print3 = tk.Label(root3, text=val)
        print3.grid(row=2, column=0, padx=10, pady=5)
        val = "您要查询的书的库存量为：%s" % (results[2])
        print4 = tk.Label(root3, text=val)
        print4.grid(row=3, column=0, padx=10, pady=5)
        val = "您要查询的书名为：%s" % (results[3])
        print5 = tk.Label(root3, text=val)
        print5.grid(row=4, column=0, padx=10, pady=5)
        val = "您要查询的书的出版日期为：%s" % (results[4])
        print6 = tk.Label(root3, text=val)
        print6.grid(row=5, column=0, padx=10, pady=5)
    else:
        msg._show(title='错误', message='没有查到您要查询的记录')
    db.close()


def book_print():
    db = pymysql.connect("localhost", "root", "******", "library")
    cursor = db.cursor()
    sql = "SELECT bname FROM book WHERE num=0"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print("库存量不足的书名为：" + i[0])
    db.close()


def delete_end():
    db = pymysql.connect("localhost", "root", "*******", "library")
    cursor = db.cursor()
    name = input4.get()
    sql = "UPDATE book SET num=0 WHERE bname= '%s'" % (name)
    try:
        cursor.execute(sql)
        db.commit()
        msg._show(title='成功', message='下架成功')
    except:
        db.rollback()
        msg._show(title='系统故障', message='下架失败')
    db.close()


def borrow_end():
    global root3
    root3 = tk.Tk()
    root3.title("借阅记录查询：")
    db = pymysql.connect("localhost", "root", "*******", "library")
    cursor = db.cursor()
    name = input5.get()
    sql = "SELECT lid,bname,btime,rtime FROM borrow,reader,book WHERE borrow.bid=book.bid AND borrow.rid=reader.rid AND rname='%s'" % (
        name)
    cursor.execute(sql)
    results = cursor.fetchall()
    cur = 0
    for i in results:
        tk.Label(root3, text="记录号为：%s 书名为：%s 借阅时间为：%s 还书时间为：%s" % (i[0], i[1], i[2], i[3]), justify=tk.LEFT,
                 font=36).grid(row=cur, column=0)
        cur = cur + 1
    db.close()


def book_delete():
    global root2
    root2 = tk.Tk()
    root2.title("下架图书")
    v1 = tk.StringVar()
    global input4
    labe1 = tk.Label(root2, text="请输入要下架的图书名：", font=36).grid(row=0, column=0)
    input4 = tk.Entry(root2, textvariable=v1)
    input4.grid(row=1, column=0)
    tk.Button(root2, text='确认', width=10, command=delete_end).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root2, text='取消', width=10, command=exit_login3).grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)


def donate_end():
    db = pymysql.connect("localhost", "root", "*******", "library")
    cursor = db.cursor()
    name = input10.get()
    amount = input11.get()
    write = input12.get()
    tim = input13.get()
    sql = "SELECT num FROM book WHERE bname='%s'" % (name)
    cursor.execute(sql)
    results = cursor.fetchone()
    if results:
        sql = "UPDATE book SET num=num+%s WHERE bname='%s'" % (amount, name)
        try:
            cursor.execute(sql)
            db.commit()
            msg._show(title="成功", message="新进图书更新成功")
        except:
            msg._show(title="系统故障", message="新进图书更新失败")
            db.rollback()
    else:
        sql = "INSERT INTO book(writer,num,bname,ptime) VALUES ('%s',%s,'%s','%s')" % (write, amount, name, tim)
        try:
            cursor.execute(sql)
            db.commit()
            msg._show(title="成功", message="新进图书更新成功")
        except:
            msg._show(title="错误", message="输入信息有误")
            db.rollback()
    db.close()


def borrow_select():
    global root2
    root2 = tk.Tk()
    root2.title("查询借阅记录")
    v1 = tk.StringVar()
    global input5
    labe1 = tk.Label(root2, text="请输入要查询的读者姓名：", font=36).grid(row=0, column=0)
    input5 = tk.Entry(root2, textvariable=v1)
    input5.grid(row=1, column=0)
    tk.Button(root2, text='确认', width=10, command=borrow_end).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root2, text='取消', width=10, command=exit_login3).grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)


def book_select():
    v1 = tk.StringVar()
    global root2
    root2 = tk.Tk()
    root2.title("查询图书")
    global input_book
    labe1 = tk.Label(root2, text="请输入您要查询的图书名：", font=36).grid(row=0, column=0)
    input_book = tk.Entry(root2, textvariable=v1)
    input_book.grid(row=0, column=1)
    tk.Button(root2, text='确认', width=10, command=check_book).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root2, text='取消', width=10, command=exit_login3).grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)


def book_in():
    global root2
    root2 = tk.Tk()
    root2.title("新进图书")
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    v3 = tk.StringVar()
    v4 = tk.StringVar()
    global input10, input11, input12, input13
    labe1 = tk.Label(root2, text="请输入您要新进的图书名：", font=36).grid(row=0, column=0)
    labe12 = tk.Label(root2, text="请输入您要新进的图书的数量：", font=36).grid(row=1, column=0)
    labe13 = tk.Label(root2, text="请输入您要新进的作者：", font=36).grid(row=2, column=0)
    labe4 = tk.Label(root2, text="请输入您要新进的图书的出版时间：", font=36).grid(row=3, column=0)
    input10 = tk.Entry(root2, textvariable=v1)
    input10.grid(row=0, column=1)
    input11 = tk.Entry(root2, textvariable=v2)
    input11.grid(row=1, column=1)
    input12 = tk.Entry(root2, textvariable=v3)
    input12.grid(row=2, column=1)
    input13 = tk.Entry(root2, textvariable=v4)
    input13.grid(row=3, column=1)
    tk.Button(root2, text='确认', width=10, command=donate_end).grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root2, text='取消', width=10, command=exit_login3).grid(row=4, column=1, sticky=tk.E, padx=10, pady=5)


def success_tip(id):
    global root1
    root.destroy()
    root2.destroy()
    root1 = tk.Tk()
    root1.title('YTU图书管理系统')
    # root1.geometry("280x250")
    labe1 = tk.Label(root1, text="欢迎来到YTU图书管理系统，请选择您要进行的操作：", font=36).grid(row=0, column=0)
    tk.Button(root1, text='打印缺书单', width=50, height=2, command=book_print).grid(row=1, column=0)
    tk.Button(root1, text='下架图书', width=50, height=2, command=book_delete).grid(row=5, column=0)
    tk.Button(root1, text='查询借阅记录', width=50, height=2, command=borrow_select).grid(row=3, column=0)
    tk.Button(root1, text='新进图书', width=50, height=2, command=book_in).grid(row=4, column=0)
    tk.Button(root1, text='查询图书信息', width=50, height=2, command=book_select).grid(row=2, column=0)
    tk.Button(root1, text='退出', width=50, height=2, command=exit_loginx).grid(row=6, column=0)


def exit_loginx():
    root1.destroy()
    frame()


def exit_login2():
    root1.destroy()


def login_check():
    db = pymysql.connect("localhost", "root", "*******", "library")
    cursor = db.cursor()
    id = input_id.get()
    name = input2.get()
    sql = "SELECT mpassward FROM mpass WHERE mid='%s'" % (id)
    cursor.execute(sql)
    results = cursor.fetchone()
    if results:
        if name == results[0]:
            success_tip(id)
        else:
            msg._show(title='错误！', message='账号密码输入错误！')
    else:
        msg._show(title='错误！', message='您输入的用户不存在！')
    db.close()


def auto_login():
    global root2
    root2 = tk.Tk()
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    root2.title("登入")
    labe1 = tk.Label(root2, text="职工号：", font=36).grid(row=0, column=0)
    label2 = tk.Label(root2, text="密码：", font=36).grid(row=1, column=0)
    global input_id, input2
    input_id = tk.Entry(root2, textvariable=v1)
    input_id.grid(row=0, column=1, padx=10, pady=5)
    input2 = tk.Entry(root2, textvariable=v2, show='*')
    input2.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root2, text='登录', width=10, command=login_check).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    tk.Button(root2, text='退出', width=10, command=exit_login3).grid(row=3, column=1, sticky=tk.E, padx=10, pady=5)


def exit_login():
    root.destroy()
    login.frame()


def exit_login3():
    root2.destroy()


def frame():
    global root
    root = tk.Tk()
    root.title('YTU图书管理系统登录')
    root.geometry("280x250")
    photo = tk.PhotoImage(file=BACK_PATH)
    theLabel = tk.Label(root, image=photo, compound=tk.CENTER, fg="white").grid(row=2, column=0)
    tk.Button(root, text='登入', width=10, height=2, command=auto_login).grid(row=0, column=0)
    tk.Button(root, text='退出', width=10, height=2, command=exit_login).grid(row=1, column=0)
    root.mainloop()
