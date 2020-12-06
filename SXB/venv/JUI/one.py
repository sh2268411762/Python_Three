import tkinter
import tkinter.messagebox as mb
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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


def fun1():
    tkinter.messagebox.showinfo("登录测试", "登录成功！")


# 创建顶层窗口
topwin = tkinter.Tk()
# 初始化窗口大小
topwin.geometry('600x600')
# 设置窗口标题
topwin.title('枳洛淮南的小游戏')

# 创建一个图片对象，参数是包含文件地址的文件名
photo = tkinter.PhotoImage(file=r'D:\git Code\Python_Three\SXB\venv\奥特消消消\请坐.png')
# 创建Label组件
label = tkinter.Label(topwin,
                      text='WELCOME',
                      image=photo,
                      font=('黑体', 80), height=600, width=600, anchor="center",
                      fg='purple',
                      # 设置文本和图像的混合模式
                      compound=tkinter.CENTER
                      )


def fun2():
    mb.showinfo('注册', '登录')


def fun5():
    n = e1.get()
    p = e2.get()



    newPlayer = User(name=n, password=p)
    # 添加到session
    session.add(newPlayer)
    # 提交即保存到数据库
    session.commit()


def fun4():
    # 创建顶层窗口
    top = tkinter.Tk()
    # 初始化窗口大小
    top.geometry('230x180')
    # 设置窗口标题
    top.title('注册')
    # 创建标签
    tkinter.Label(top, text="姓名").grid(row=0)
    tkinter.Label(top, text="密码").grid(row=1, column=0)
    # 创建输入框
    global e1
    global e2
    e1 = tkinter.Entry(top)
    e2 = tkinter.Entry(top)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    # 创建按钮
    b1 = tkinter.Button(top, text='确定', command=fun5)
    b1.grid(row=3)
    b2 = tkinter.Button(top, text='退出', command=top.quit())
    b2.grid(row=3, column=1)
    top.mainloop()


def fun3():
    cursor.execute("select name_B,boun FROM bouns ORDER BY boun DESC")

    result = cursor.fetchall()
    t = tkinter.Tk()
    t.geometry('600x600')
    t.title('排行榜')

    s = "玩家名\t\t最高得分\n"
    l = ""
    for i in result:
        l += result[i][0] + "\t"
        l += result[i][1] + "\n"

    m = tkinter.Message(t, text=l, width=300)
    m.config(bg='lightgreen', font=('times', 18, 'italic'))
    m.pack()
    t.mainloop()


# 创建一个菜单
menubal = tkinter.Menu(topwin)

# 创建菜单项
menu1 = tkinter.Menu(topwin)
menu1.add_command(label='登录', command=fun2)
menu1.add_command(label='注册', command=fun4)

menu2 = tkinter.Menu(topwin)
menu2.add_command(label="排行榜", command=fun3)

# add_cascade 创建一个菜单项，label指明该菜单项的名称
#                           menu属性指明要把哪个菜单级联到该菜单项
menubal.add_cascade(label="登录/注册", menu=menu1)
menubal.add_cascade(label="排行榜", menu=menu2)
menubal.add_cascade(label="退出", command=topwin.quit)

topwin['menu'] = menubal
label.pack()
# 进入主循环，监听事件
topwin.mainloop()
# 关闭session
session.close()
