#author = liuwei date = 2017-06-02
#数据库帮助类
import pymysql
from book import *

__metaclass__ = type
class DBHelper:
    def getCon(self):
        '''获取操作数据库的curcor即游标，首先的建立连接，需要服务器地址，端口号，用户名，密码和数据库名'''
        #为了能用中文，得加上编码方式
        conn = pymysql.connect(host = "localhost", port = 3306, user = "root", password = "201392260", db = "library", charset = "utf8")

        return conn

    def insertBook(self, book):
        '''向数据库中book表插入书本信息，book为Book类对象，包含书本基本信息'''
        sql = "insert into book(name, author, content, add_date) values(%s, %s, %s, %s)"

        conn = self.getCon();
        if conn ==None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (book.getBookName(), book.getAuthor(), book.getContent(), book.getAddDate()))

        conn.commit()
        cursor.close()
        conn.close()

        new_id = cursor.lastrowid
        print("新插入键值id为:", new_id)

        return new_id

    def getAllBook(self):
        '''返回数据库中，book表中所有的书本信息'''
        sql = "select *from book"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        rownum = cursor.execute(sql)              #执行并返回找到的行数

        #获取查询结果
        rows = cursor.fetchall()
        list = []

        for item in rows:
            bitem = (item[0], item[1], str(item[4]))

            list.append(bitem)

        conn.commit()
        cursor.close()
        conn.close()

        return list

    def getBookById(self, bookid):
        '''根据书本id值来寻找书本信息'''

        sql = "select book.name, book.author, book.content from book  where id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (bookid, ))                     #参数以元组形式给出
        row = cursor.fetchone()                             #取到第一个结果

        conn.commit()
        cursor.close()
        conn.close()

        return row                                          #返回该书本信息


    def saveUpdate(self, bookid, book):
        '''用book对象来修改id为bookid的书本信息'''
        sql = "update book set book.name=%s, book.author=%s, book.content=%s where book.id=%s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (book.getBookName(), book.getAuthor(), book.getContent(), bookid))

        conn.commit()
        cursor.close()
        conn.close()

    def deleteBook(self, bookid):
        '''根据书本id来删除书籍'''
        sql = "delete from book where book.id = %s"

        conn = self.getCon()
        if conn == None:
            return

        cursor = conn.cursor()
        cursor.execute(sql, (bookid, ))

        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    db = DBHelper()
    #book = Book("秦腔", "贾凹平", "讲的是大西北夏家和白家的事情，由引生口述。")
    #db.insertBook(book)
    list = db.getAllBook()
    for item in list:
        print(item)

