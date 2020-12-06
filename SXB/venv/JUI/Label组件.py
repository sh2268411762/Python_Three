import tkinter

topwin = tkinter.Tk()
topwin.geometry('600x600')
topwin.title('Label组件显示文本测试')
label = tkinter.Label(topwin, text='Hello World!', font=('华文行楷', 30), fg="red", height=20, width=20, anchor="center")
# 填充到界面。指定布局方法，否则组件将不会被显示
label.pack()
# 进入主循环
topwin.mainloop()
