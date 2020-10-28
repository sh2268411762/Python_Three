# # 读文件
# print("read()方法可以用来读取整个文件并保存到字符串中：")
# file_name = "readme.txt"
# f = open(file_name)
# txt1 = f.read()
# print(txt1)
# f.close()
# print("read()方法可以传递参数用于指定读取多少个字符：")
# f = open(file_name)
# txt2 = f.read(20)
# print(txt2)
# f.close()
# f = open(file_name)
# txt3 = f.read(200)
# print(txt3)
# f.close()

# # 写文件
# from datetime import datetime
#
# print("write()方法可以将任意字符串写入文件中，返回字符串长度：")
# f = open("readme.txt", "w")
# txt4 = "2020年10月8日\n"
# print(f.write(txt4))
# f.close()
# print("返回字符串长度说明成功写入！")
# print("\na后续追加写入：")
# f = open("readme.txt", "a")
# txt5 = "是我带你混我的圈子\n然后你开始对我说话冲了\n是我混差了还是狗养大了？\n是你飘了还是觉得我不动刀了？\n"
# print(f.write(txt5))
# txt6 = str(datetime.now()) + "\n"
# f.write(txt6)
# f.close()

# # 按行读文件
# print("readline()函数可以逐行读取文件内容：")
# f = open("readme.txt", "r")
# for i in range(0, 7):
#     print(f.readline())
# f.close()
# f = open("readme.txt", "r")
# print("readlines函数用于读取整个文件，并将其按行切割返回一个列表对象，保留换行符：")
# for line in f.readlines():
#     print(line)
# f.close()
# print("直接迭代文件（惰性读取）：")
# f = open("readme.txt", "r")
# for line in f:
#     print(line)
# f.close()

# # 按行写文件
# print("writelines方法用于按行输入（接收列表作为参数）：")
# f = open("readme.txt", "a")
# lines1 = ["遇到困难就放弃\n然后呢\n再放弃？\n总有一天你会退无可退的\n"]
# f.writelines(lines1)
# print("close()方法用来关闭文件")
# f.close()
# f = open("readme.txt", "r")
# txt7 = f.read()
# print(txt7)

# # with语句关闭文件
# with open("readme.txt", "r") as f:
#     txt8 = f.read()
#     print(txt8)


# # IO
# # String IO
# from io import StringIO
#
# print("写入读取：")
# f = StringIO()
# f.write("Hello")
# f.write(" ")
# f.write("World")
# f.write("!")
# print("获取写入后的str：", f.getvalue())
# f.close()
#
# print("初始化读取：")
# f = StringIO("Hello!\nWorld!\nWelcome!")
# while True:
#     s = f.readline()
#     if s == "":
#         break
#     print(s.strip())
# f.close()
# f = StringIO("Hello!\nWorld!\nWelcome!")
# for i in f.readlines():
#     print(i)
# f.close()


# # BytesIO
# from io import BytesIO
#
# f = BytesIO()
# f.write("杯中倒满无情酒、心中再无意中人、\n看尽人生红尘梦、尝尽人间疾苦情。\n本是青灯不归客、却因浊酒恋红尘，\n星光不问赶路人、岁月不负有心人。\n借最烈的酒、浇最忧的愁。\n".encode("utf-8"))
# print("由于写入的是经过UTF-8编码的bytes，直接访问会出错：", f.getvalue())
# print("UTF-8编码访问：\n", f.getvalue().decode("utf-8"))
# f.close()
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read().decode("utf-8"))


# # 序列化与反序列化
# # pickle 模块
# import pickle
#
#
# class Student:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# print("pickle模块中的dumps方法可以把对象序列化成bytes：")
# stu1 = Student("孙豪", 21, "男")
# stu2 = Student("王翔", 20, "男")
# stu3 = Student("刘辰鑫", 20, "男")
# stu4 = Student("杨致远", 20, "男")
# stu5 = Student("李梓豪", 20, "男")
# print(pickle.dumps(stu1))
#
# with open("student.data.txt", "wb") as f:
#     pickle.dump(stu1, f)
#     pickle.dump(stu2, f)
#     pickle.dump(stu3, f)
#     pickle.dump(stu4, f)
#     pickle.dump(stu5, f)
# with open("student.data.txt", "rb") as f:
#     for i in range(0, 5):
#         line = pickle.load(f)
#         print("姓名：", line.name)
#         print("年龄：", line.age)
#         print("性别：", line.gender)


# # JSON 序列与反序列化
# import json
#
# stu6 = {
#     "姓名": "小明",
#     "年龄": 25,
#     "性别": "男"
# }
# print(json.dumps(stu6))
#
# with open("student1.data.txt", "w") as f:
#     json.dump(stu6, f)
# with open("student1.data.txt", "r") as f:
#     stu7 = json.load(f)
#     print(stu7)

