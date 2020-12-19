# 导入pymysql模块
import pymysql


# 创建数据库操作类
class Sql_operation(object):
    '''
    数据库操作
    '''

    # 用构造函数实现数据库连接，并引入mydb参数，实现调用不同的数据库
    def __init__(self, mydb):
        # 实例变量
        self.mydb = mydb
        # 打开数据库连接
        self.db = pymysql.connect(host="localhost", user="root", password="123456", db=self.mydb, charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()

    # 定义查看数据表信息函数，并引入table_field、table_name参数，实现查看不同数据表的建表语句
    def FindAll(self, table_name):
        # 实例变量
        self.table_name = table_name
        # 定义SQL语句
        sql = "select * from %s" % (self.table_name)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)

    # 定义添加表数据函数
    def Insert(self, stu_name, stu_gender, stu_age, stu_cid, stu_classid, stu_phone):
        # 实例变量
        self.stu_name = stu_name
        self.stu_gender = stu_gender
        self.stu_age = stu_age
        self.stu_cid = stu_cid
        self.stu_classid = stu_classid
        self.stu_phone = stu_phone
        # 定义SQL语句
        sql = "insert into stu_info(stu_name,stu_gender,stu_age,stu_cid,stu_classid,stu_phone) values('%s','%s','%s','%s','%s','%s')" % (
        self.stu_name, self.stu_gender, self.stu_age, self.stu_cid, self.stu_classid, self.stu_phone)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 定义删除表数据函数
    def Del(self, stu_id):
        # 实例变量
        self.stu_id = stu_id
        # 定义SQL语句
        sql = "delete from stu_info where id=%d" % (self.stu_id)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 用析构函数实现数据库关闭
    def __del__(self):
        # 关闭数据库连接
        self.db.close()