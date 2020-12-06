import tkinter

# 创建顶层窗口
topwin = tkinter.Tk()
# 初始化窗口大小
topwin.geometry('280x100')
# 设置窗口标题
topwin.title('枳洛淮南的小游戏')
# 创建列表框，允许多项选择
listbox = tkinter.Listbox(topwin, selectmode=tkinter.MULTIPLE)
listbox.pack()
# 内容列表
content = ['李白', '杜甫', '白居易']
# 添加下拉列表项
for item in content:
    listbox.insert(tkinter.END, item)

# 进入主循环
topwin.mainloop()
