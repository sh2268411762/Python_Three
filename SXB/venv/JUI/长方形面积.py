import tkinter


def fun():
    l = eval(e1.get())
    w = eval(e2.get())
    e3.insert(0, l * w)


topwin = tkinter.Tk()
# 初始化窗口大小
topwin.geometry('600x600')
# 设置窗口标题
topwin.title('枳洛淮南的小游戏')
# 创建标签
tkinter.Label(topwin, text='长度：').grid(row=0)
tkinter.Label(topwin, text='宽度：').grid(row=1)
tkinter.Label(topwin, text='面积：').grid(row=2)
tkinter.Label(topwin, text='cm').grid(row=0, column=2)
tkinter.Label(topwin, text='cm').grid(row=1, column=2)
tkinter.Label(topwin, text='cm * cm').grid(row=2, column=2)
# 创建输入框
e1 = tkinter.Entry(topwin)  # 长度
e2 = tkinter.Entry(topwin)  # 宽度
e3 = tkinter.Entry(topwin)  # 面积
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
# 创建按钮
b1 = tkinter.Button(topwin, text='计算', command=fun)
b1.grid(row=3)
b2 = tkinter.Button(topwin, text='退出', command=topwin.quit)
b2.grid(row=3, column=1)
# 进入主循环
topwin.mainloop()
