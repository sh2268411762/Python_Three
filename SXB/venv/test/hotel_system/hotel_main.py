import hotel_tools

user=['xuyating']
pwd=['123456']

#登录
def denglu():
    users = input("请输入您的用户名:")
    pwds = input("请输入您的密码:")
    if users in user and pwds in pwd:
        student()
    else:
        print("账号或密码不正确，请重新输入")

#注册
def zhuce():
    users=input("请输入您要注册的用户名:")
    pwds=input("请输入您要注册的密码:")
    user.append(users)
    pwd.append(pwds)
    print()
    print("注册成功!")
    print()

#登录界面
def dljiemian():

    while True:
        print("---------------------------")
        print("    学生管理系统登陆界面 V1.0  ")
        print("                           ")
        print("        1:登   录           ")
        print("        2:注   册           ")
        print("        3:退   出           ")
        print("                           ")
        print("---------------------------")
        xx=input("请输入您的选择:")
        #1.登录
        if xx=='1':
            denglu()
        elif xx=='2':
        #2.注册
            zhuce()
        elif xx=='3':
        #3.退出
            print()
            print("成功退出!")
            print()
            break
        else:
            print("输入错误，请重新输入")


#学生管理系统
def student():
    while True:
        #调用student_tools模块中的界面函数
        hotel_tools.jiemian()
        #调用student_tools模块中的读取文件函数
        hotel_tools.read_file()
        x=input("请输入您的选择:")
        #添加学生
        if x=='1':
            hotel_tools.add()
        #删除学生
        elif x=='2':
            hotel_tools.dele()
        #修改学生
        elif x=='3':
            hotel_tools.xiugai()
        #查询学生
        elif x=='4':
            hotel_tools.find()
        #显示所有学生
        elif x=='5':
            hotel_tools.showall()
        #保存数据至文件中
        elif x=='6':
            hotel_tools.save_file()
        #退出学生管理系统,返回上一层登录界面系统
        elif x=='7':
            print()
            print("成功退出学生管理系统!")
            break
        else:
            print()
            print("输入错误，请重新输入")
            print()

#调用最先执行的登录界面函数
dljiemian()
