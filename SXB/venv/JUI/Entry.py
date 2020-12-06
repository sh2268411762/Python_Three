import tkinter

topwin = tkinter.Tk()
# 初始化窗口大小
topwin.geometry('600x600')
# 设置窗口标题
topwin.title('枳洛淮南的小游戏')
# 创建标签
tkinter.Label(topwin, text='用户名：').grid(row=0)
tkinter.Label(topwin, text='密码  ：').grid(row=1, column=0)
# 创建输入框
e1 = tkinter.Entry(topwin)
e2 = tkinter.Entry(topwin)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
topwin.mainloop()
