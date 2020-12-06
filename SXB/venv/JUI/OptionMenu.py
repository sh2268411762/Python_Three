import tkinter

# 创建顶层窗口
topwin = tkinter.Tk()
# 初始化窗口大小
topwin.geometry('350x50')
# 设置窗口标题
topwin.title('枳洛淮南的小游戏')

# 内容列表
content = ['李白', '杜甫', '白居易']
variable = tkinter.StringVar()
variable.set(content[1])  # 默认选中的值
om = tkinter.OptionMenu(topwin, variable, *content)
om.pack()

# 进入主循环
topwin.mainloop()
