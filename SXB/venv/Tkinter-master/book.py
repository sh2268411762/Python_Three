# author = liuwei  date = 2017-06-02
from datetime import *  # 导入日期模块

__metaclass__ = type


class Book:
    '''一个书本信息类，包括书本名字，作者名字和书本简单信息'''

    def __init__(self, bookName="", author="", content=""):
        self.bookName = bookName  # 书本名字
        self.author = author  # 作者名字
        self.content = content  # 书本信息
        self.add_date = date.today()  # 书本添加日期

    def setBookName(self, name):
        self.bookName = name

    def getBookName(self):
        return self.bookName

    def setAuthor(self, author):
        self.author = author

    def getAuthor(self):
        return self.author

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content

    def getAddDate(self):
        return self.add_date


if __name__ == "__main__":
    mybook = Book()
    print(mybook.add_date)
