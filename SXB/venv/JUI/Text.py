import tkinter

topwin = tkinter.Tk()
# 初始化窗口大小
# topwin.geometry('600x600')
topwin.title('Text组件测试')
# 设置Text组件，height设置为5行，width设置为35列
t1 = tkinter.Text(topwin, width=35, height=5)
t1.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 创建滚动条
s1 = tkinter.Scrollbar(topwin)
s1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# 将滚动条绑定到Text编辑器上
s1.config(command=t1.yview)
t1.config(yscrollcommand=s1.set)
# 索引号INSERT表示输入光标所在的位置，初始化后的输入光标在左上角
t1.insert(tkinter.INSERT, '赋得古原草送别\n')
# 索引号END表示最后
t1.insert(tkinter.END, '白居易\n')
t1.insert(tkinter.END, '离离原上草，一岁一枯荣。\n')
t1.insert(tkinter.END, '野火烧不尽，春风吹又生。\n')
t1.insert(tkinter.END, '远芳侵古道，晴翠接荒城。\n')
t1.insert(tkinter.END, '又送王孙去，萋萋满别情。')
# 进入主循环
topwin.mainloop()
