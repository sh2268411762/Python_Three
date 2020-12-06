import pymysql
import pprint

host = "localhost"
username = "root"
password = "sunhao2268411762"
db_name = "python"

# 创建connect对象
connect = pymysql.connect(host, username, password, db_name)

# 获取游标对象
cursor = connect.cursor()

cursor.execute("select name_B,boun FROM bouns ORDER BY boun DESC")
result = cursor.fetchall()
print(type(result))
print(type(result[0]))
print(type(result[0][1]))
print(result[0][0])
pprint.pprint(result)

cursor.close()
connect.close()
