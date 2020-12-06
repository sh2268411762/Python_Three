import tkinter
import tkinter.messagebox


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
                      text='点这里',
                      image=photo,
                      font=('黑体', 20), height=600, width=600, anchor="center",
                      fg='lightgreen',
                      # 设置文本和图像的混合模式
                      compound=tkinter.CENTER
                      )

# 创建按钮
button1 = tkinter.Button(topwin, text="登录", command=fun1)
button1.pack(side=tkinter.LEFT)
# state参数设置按钮状态
button2 = tkinter.Button(topwin, text='禁用', state=tkinter.DISABLED)
button2.pack(side=tkinter.LEFT)
button3 = tkinter.Button(topwin, text='退出', command=topwin.quit)
button3.pack(side=tkinter.RIGHT)
# 填充到界面，指定布局方法，否则组件将不会显示
label.pack()
# 进入主循环，监听事件
topwin.mainloop()
