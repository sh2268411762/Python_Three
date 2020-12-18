import tkinter
import tkinter.messagebox as mb
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from Game import *

# 创建对象的基类
Base = declarative_base()


# 定义USer对象
class User(Base):
    # 数据库中表的名字
    __tablename__ = 'user'
    # 数据库表结构对应的字段
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    password = Column(String(20))
    boun = Column(Integer())


# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:sunhao2268411762@localhost:3306/python?charset=utf8')

# 创建DBSession类型
Dbsession = sessionmaker(bind=engine)
session = Dbsession()


# import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog    #askstring()

################################################################
# 注册窗口
class Application_zc(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('注册')
        self.master.geometry('600x600')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Command3.TButton', font=('宋体', 9))
        self.Command3 = Button(self.top, text='注册', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.383, rely=0.504, relwidth=0.211, relheight=0.095)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='', textvariable=self.Text2Var, font=('宋体', 9))
        self.Text2.place(relx=0.209, rely=0.367, relwidth=0.698, relheight=0.072)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='', textvariable=self.Text1Var, font=('宋体', 9))
        self.Text1.place(relx=0.209, rely=0.183, relwidth=0.698, relheight=0.072)

        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='用户名：', style='Label1.TLabel')
        self.Label1.place(relx=0.087, rely=0.183, relwidth=0.089, relheight=0.072)

        self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
        self.Label2 = Label(self.top, text='  密 码：', style='Label2.TLabel')
        self.Label2.place(relx=0.07, rely=0.367, relwidth=0.107, relheight=0.072)


class Application_ZC(Application_zc):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command3_Cmd(self, event=None):
        # TODO, Please finish the function here!
        n = self.Text1.get()
        p = self.Text2.get()

        if session.query(User).filter(User.name.in_([n])).all():
            ret = session.query(User).filter_by(name=n).first()
            tkinter.messagebox.showinfo("注册", "该用户已注册！")
        else:
            tkinter.messagebox.showinfo("注册", "注册成功，进入游戏！")
            print(n + "进入游戏")
            global top
            top.destroy()
            main()
        newPlayer = User(name=n, password=p)
        # 添加到session
        session.add(newPlayer)
        # 提交即保存到数据库
        session.commit()


##################################################
class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('登录')
        self.master.geometry('600x600')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='用户名：', style='Label1.TLabel')
        self.Label1.place(relx=0.087, rely=0.183, relwidth=0.089, relheight=0.072)

        self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
        self.Label2 = Label(self.top, text='  密 码：', style='Label2.TLabel')
        self.Label2.place(relx=0.07, rely=0.367, relwidth=0.107, relheight=0.072)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, text='', textvariable=self.Text1Var, font=('宋体', 9))
        self.Text1.place(relx=0.209, rely=0.183, relwidth=0.698, relheight=0.072)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top, text='', textvariable=self.Text2Var, font=('宋体', 9))
        self.Text2.place(relx=0.209, rely=0.367, relwidth=0.698, relheight=0.072)

        self.style.configure('Command1.TButton', font=('宋体', 9))
        self.Command1 = Button(self.top, text='注册', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.035, rely=0.917, relwidth=0.141, relheight=0.049)

        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.top, text='退出', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.8, rely=0.917, relwidth=0.159, relheight=0.049)

        self.style.configure('Command3.TButton', font=('宋体', 9))
        self.Command3 = Button(self.top, text='登录', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.383, rely=0.504, relwidth=0.211, relheight=0.095)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        # TODO, Please finish the function here!
        top1 = Tk()
        Application_ZC(top1).mainloop()
        top1.destroy()

    def Command2_Cmd(self, event=None):
        # TODO, Please finish the function here!
        self.quit()

    def Command3_Cmd(self, event=None):
        # TODO, Please finish the function here!
        n = self.Text1.get()
        p = self.Text2.get()

        if session.query(User).filter(User.name.in_([n])).all():
            ret = session.query(User).filter_by(name=n).first()
            print(ret.name + "进入游戏")
            if ret.password == p:
                tkinter.messagebox.showinfo("登录", "登录成功！")
                global top
                top.destroy()
                ret = main()
                print(ret)
            else:
                tkinter.messagebox.showinfo("登录", "登录失败，请检查密码！")
        else:
            tkinter.messagebox.showinfo("登录", "登录失败，没有该用户，请注册！")
        session.commit()
        session.close()


'''test'''
if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
