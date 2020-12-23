'''一个图书管理系统，能够实现增加书籍，删除书籍，
修改书籍和查看图书详情，基于mysql数据库和
wxPython'''

import wx
from book import *
from dbhelper import *

__metaclass__ = type

class AddFrame(wx.Frame):
    '''添加书籍弹出的小窗口'''

    def __init__(self, parent, title):
        '''初始化该小窗口的布局'''

        self.mainframe = parent
        #生成一个300*300的框
        wx.Frame.__init__(self, parent, title = title, size = (400, 250))

        self.panel = wx.Panel(self, pos = (0, 0), size = (400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")                              #背景为白色

        #三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label = "书名:", pos = (5, 8), size = (35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos = (40, 5), size = (340, 25))
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label = "作者:", pos = (5, 38), size = (35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos = (40, 35), size = (340, 25))
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label = "内容:", pos = (5, 68), size = (340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos = (40, 65), size = (340, 100), style = wx.TE_MULTILINE)
        self.content = content_text

        save_button = wx.Button(self.panel, label = "保存书籍", pos = (160, 170))
        self.Bind(wx.EVT_BUTTON, self.saveBook, save_button)

        #需要用到的数据库接口
        self.dbhelper = DBHelper()


    def saveBook(self, evt):
        '''第一步：获取text中文本；第二步，连接数据库；第三步插入并获得主键；第四步添加到ListCtrl中'''
        bookName = self.name.GetValue()
        author = self.author.GetValue()
        content = self.content.GetValue()

        print("书名:"+bookName)
        if bookName == "" or author == "" or content == "":
            print("进来了")
            warn = wx.MessageDialog(self, message = "所有信息不能为空！！！", caption = "错误警告", style = wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()                                                             #提示错误
            warn.Destroy()
            return
        else:
            print("开始插入到数据库中")
            book = Book(bookName, author, content)
            book_id = self.dbhelper.insertBook(book)
            self.mainframe.addToList(book_id, book)

        self.Destroy()


class UpdateFrame(wx.Frame):
    def __init__(self, parent, title, select_id):
        '''初始化更新图书信息界面总布局'''

        wx.Frame(parent, title = title, size = (400, 250))

        #用来调用父frame,便于更新
        self.mainframe = parent
        #生成一个300*300的框
        wx.Frame.__init__(self, parent, title = title, size = (400, 250))

        self.panel = wx.Panel(self, pos = (0, 0), size = (400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")                              #背景为白色

        #三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label = "书名:", pos = (5, 8), size = (35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos = (40, 5), size = (340, 25))
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label = "作者:", pos = (5, 38), size = (35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos = (40, 35), size = (340, 25))
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label = "内容:", pos = (5, 68), size = (340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos = (40, 65), size = (340, 100), style = wx.TE_MULTILINE)
        self.content = content_text

        save_button = wx.Button(self.panel, label = "保存修改", pos = (160, 170))
        self.Bind(wx.EVT_BUTTON, self.saveUpdate, save_button)

        #选中的id和bookid
        self.select_id = select_id
        self.bookid = self.mainframe.list.GetItem(select_id, 0).Text             #获取第select_id行的第0列的值
        print(select_id, self.bookid)
        #需要用到的数据库接口
        self.dbhelper = DBHelper()
        self.showAllText()                     #展现所有的text原来取值


    def showAllText(self):
        '''显示概述本原始信息'''
        data = self.dbhelper.getBookById(self.bookid)                      #通过id获取书本信息

        self.name.SetValue(data[0])                                        #设置值
        self.author.SetValue(data[1])
        self.content.SetValue(data[2])

    def saveUpdate(self, evt):
        '''保存修改后的值'''
        bookName = self.name.GetValue()                                    #获得修改后的值
        author = self.author.GetValue()
        content = self.content.GetValue()

        print("书名:"+bookName)
        if bookName == "" or author == "" or content == "":
            print("进来了")
            warn = wx.MessageDialog(self, message = "所有信息不能为空！！！", caption = "错误警告", style = wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()                                                             #提示错误
            warn.Destroy()
            return
        else:
            print("开始将修改后的数据保存到数据库中")
            book = Book(bookName, author, content)                         #将数据封装到book对象中
            self.dbhelper.saveUpdate(self.bookid, book)
            self.mainframe.list.SetItem(self.select_id, 1, bookName)

        self.Destroy()                                                     #修改完后自动销毁


class ShowFrame(wx.Frame):
    '''用来显示书籍的信息'''

    def __init__(self, parent, title, select_id):
        '''初始化该小窗口的布局'''

        #便于调用父窗口
        self.mainframe = parent

        #生成一个300*300的框
        wx.Frame.__init__(self, parent, title = title, size = (400, 250))

        self.panel = wx.Panel(self, pos = (0, 0), size = (400, 250))
        self.panel.SetBackgroundColour("#FFFFFF")                              #背景为白色

        #三个编辑框，分别用来编辑书名，作者，书籍相关信息
        bookName_tip = wx.StaticText(self.panel, label = "书名:", pos = (5, 8), size = (35, 25))
        bookName_tip.SetBackgroundColour("#FFFFFF")
        bookName_text = wx.TextCtrl(self.panel, pos = (40, 5), size = (340, 25))
        bookName_text.SetEditable(False)
        self.name = bookName_text

        author_tip = wx.StaticText(self.panel, label = "作者:", pos = (5, 38), size = (35, 25))
        author_tip.SetBackgroundColour("#FFFFFF")
        author_text = wx.TextCtrl(self.panel, pos = (40, 35), size = (340, 25))
        author_text.SetEditable(False)
        self.author = author_text

        content_tip = wx.StaticText(self.panel, label = "内容:", pos = (5, 68), size = (340, 25))
        content_tip.SetBackgroundColour("#FFFFFF")
        content_text = wx.TextCtrl(self.panel, pos = (40, 65), size = (340, 100), style = wx.TE_MULTILINE)
        content_text.SetEditable(False)
        self.content = content_text

        #选中的id和bookid
        self.select_id = select_id
        self.bookid = self.mainframe.list.GetItem(select_id, 0).Text             #获取第select_id行的第0列的值

        #需要用到的数据库接口
        self.dbhelper = DBHelper()
        self.showAllText()                     #展现所有的text原来取值

    def showAllText(self):
        '''显示概述本原始信息'''
        data = self.dbhelper.getBookById(self.bookid)                      #通过id获取书本信息

        self.name.SetValue(data[0])                                        #设置值
        self.author.SetValue(data[1])
        self.content.SetValue(data[2])



class LibraryFrame(wx.Frame):
    def __init__(self, parent, title):
        '''初始化系统总体布局，包括各种控件'''

        #生成一个宽为400，高为400的frame框
        wx.Frame.__init__(self, parent, title=title, size=(400, 400))

        #定一个网格布局,两行一列
        self.main_layout = wx.BoxSizer(wx.VERTICAL)


        #生成一个列表
        self.list = wx.ListCtrl(self, -1, size = (400,300), style = wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES) #| wx.LC_SINGLE_SEL
        #列表有散列，分别是书本ID,书名，添加日期
        self.list.InsertColumn(0, "ID")
        self.list.InsertColumn(1, "书名")
        self.list.InsertColumn(2, "添加日期")
        #设置各列的宽度
        self.list.SetColumnWidth(0, 60)                                         #设置每一列的宽度
        self.list.SetColumnWidth(1, 230)
        self.list.SetColumnWidth(2, 92)

        #添加一组按钮，实现增删改查,用一个panel来管理该组按钮的布局
        self.panel = wx.Panel(self, pos = (0, 300), size = (400, 100))

        #定义一组按钮
        add_button = wx.Button(self.panel, label = "添加", pos = (10, 15), size = (60, 30))    #, size = (75, 30)
        del_button = wx.Button(self.panel, label = "删除", pos = (110, 15), size = (60, 30))    #, size = (75, 30)
        update_button = wx.Button(self.panel, label = "修改", pos = (210, 15), size = (60, 30)) #, size = (75, 30)
        query_button = wx.Button(self.panel, label = "查看", pos = (310, 15), size = (60, 30))  #, size = (75, 30)
        #w为按钮绑定相应事件函数，第一个参数为默认参数，指明为按钮类事件，第二个为事件函数名，第三个为按钮名
        self.Bind(wx.EVT_BUTTON, self.addBook, add_button)
        self.Bind(wx.EVT_BUTTON, self.delBook, del_button)
        self.Bind(wx.EVT_BUTTON, self.updateBook, update_button)
        self.Bind(wx.EVT_BUTTON, self.queryBook, query_button)

        #将列表和panel添加到主面板
        self.main_layout.Add(self.list, 3)
        self.main_layout.Add(self.panel, 1)

        self.SetSizer(self.main_layout)

        #添加数据库操作对象
        self.dbhelper = DBHelper()
        datas = self.dbhelper.getAllBook()

        for data in datas:
            index = self.list.InsertItem(self.list.GetItemCount(), str(data[0]))
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])


    def addBook(self, evt):
        '''添加书籍按钮，弹出添加书籍框'''
        add_f = AddFrame(self, "添加书籍窗口")
        add_f.Show(True)


    def delBook(self, evt):
        '''删除书籍按钮，先选中,然后删除'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message = "未选中任何条目！！！", caption = "错误警告", style = wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()                                                             #提示错误
            warn.Destroy()
            return
        else:
            bookid = self.list.GetItem(selectId, 0).Text                                 #得到书本id
            self.list.DeleteItem(selectId)                                               #先在listctrl中删除选中行
            self.dbhelper.deleteBook(bookid)



    def updateBook(self, evt):
        '''修改按钮响应事件，点击修改按钮，弹出修改框'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message = "未选中任何条目！！！", caption = "错误警告", style = wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()                                                             #提示错误
            warn.Destroy()
            return
        else:
            update_f = UpdateFrame(self, "修改书籍窗口", selectId)
            update_f.Show(True)

    def queryBook(self, evt):
        '''查看按钮响应事件'''
        selectId = self.list.GetFirstSelected()
        if selectId == -1:
            warn = wx.MessageDialog(self, message = "未选中任何条目！！！", caption = "错误警告", style = wx.YES_DEFAULT | wx.ICON_ERROR)
            warn.ShowModal()                                                             #提示错误
            warn.Destroy()
            return
        else:
            show_f = ShowFrame(self, "修改书籍窗口", selectId)
            show_f.Show(True)

    def addToList(self, id, book):
        index = self.list.InsertItem(self.list.GetItemCount(), str(id))
        self.list.SetItem(index, 1, book.getBookName())
        self.list.SetItem(index, 2, str(book.getAddDate()))



AppBaseClass = wx.App

class LibraryApp(AppBaseClass):
    def OnInit(self):
        frame = LibraryFrame(None, "library-system")
        frame.Show()

        return True


#类似于c中的main函数，但被其他模块导入时，__name__值不是"__main__"
if __name__ == "__main__":
    app = LibraryApp()
    app.MainLoop()
