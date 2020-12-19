import os

student_list=[]

student_dict={}




#学生管理系统界面
def jiemian():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print("                           ")
    print("      1:添加学生"            )
    print("      2:删除学生"            )
    print("      3:修改学生"            )
    print("      4:查询学生"            )
    print("      5:显示所有学生"         )
    print("      6:保存数据"            )
    print("      7:退出系统"            )
    print("                           ")
    print("---------------------------")


#添加学生
def add():
    name=input("请输入录入学生姓名:")
    cls=input("请输入学生班级:")
    age=input("请输入录入学生年龄:")
    phone=input("请输入录入学生手机号:")
    addr=input("请输入录入学生家庭住址:")

    student_dict={"name":name,"class":cls,"age":age,"phone":phone,"address":addr}

    student_list.append(student_dict)
    print()
    print("-----添加学生信息界面-----")
    print()
    print("姓名\t\t","班级\t\t","年龄\t\t","电话号\t\t","家庭住址\t\t")
    for student_dict_1 in student_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s" %(student_dict_1["name"],
                                             student_dict_1["class"],
                                             student_dict_1["age"],
                                             student_dict_1["phone"],
                                             student_dict_1["address"]))
    print()
    print("录入成功!")
    print()

#删除学生
def dele():
    name_del=input("请输入想要删除的学生姓名:")
    for student_dict_1 in student_list:
        if name_del in student_dict_1["name"]:
            student_list.remove(student_dict_1)
            print()
            print("删除%s信息成功!" % name_del)
            print()
            break
    else:
        print()
        print("您输入的学生姓名错误，请重新输入")
        print()
#修改学生
def xiugai():
    name_xiugai=input("请输入想要修改的学生姓名:")


    for student_dict_1 in student_list:

        if name_xiugai == student_dict_1["name"]:
            print()
            print("-----修改界面-----")
            print()
            print("姓名\t\t", "班级\t\t", "年龄\t\t", "电话号\t\t", "家庭住址\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s" %(student_dict_1["name"],
                                                 student_dict_1["class"],
                                                 student_dict_1["age"],
                                                 student_dict_1["phone"],
                                                 student_dict_1["address"]))
            #回车不修改

            student_dict_1["name"]=new_input(student_dict_1["name"],"请输入修改后的学生姓名[回车不修改]:")
            student_dict_1["class"]=new_input(student_dict_1["class"],"请输入修改后的学生班级[回车不修改]:")
            student_dict_1["age"]=new_input(student_dict_1["age"],"请输入修改后的学生年龄[回车不修改]:")
            student_dict_1["phone"]=new_input(student_dict_1["phone"],"请输入修改后的学生手机号[回车不修改]:")
            student_dict_1["address"]=new_input(student_dict_1["address"],"请输入修改后的学生家庭地址[回车不修改]:")
            print()
            print("修改成功!")
            print()
            break
    else:
        print()
        print("您输入的学生姓名错误，请重新输入")
        print()

#查找学生
def find():
    find_name=input("请输入需要查找的学生姓名:")
    for student_dict_1 in student_list:

        if find_name == student_dict_1["name"]:
            print()
            print("-----查询结果界面-----")
            print()
            print("姓名\t\t", "班级\t\t", "年龄\t\t", "电话号\t\t", "家庭住址\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (student_dict_1["name"],
                                                  student_dict_1["class"],
                                                  student_dict_1["age"],
                                                  student_dict_1["phone"],
                                                  student_dict_1["address"]))
        else:
            print()
            print("-----查询结果界面-----")
            print()
            print("无此学生信息")

#显示所有学生信息
def showall():

    if len(student_list)>0:
        print()
        print("-----显示所有学生信息-----")
        print()
        print("姓名\t\t", "班级\t\t", "年龄\t\t", "电话号\t\t", "家庭住址\t\t")
        for student_dict_1 in student_list:

            print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (student_dict_1["name"],
                                                  student_dict_1["class"],
                                                  student_dict_1["age"],
                                                  student_dict_1["phone"],
                                                  student_dict_1["address"]))
    else:
        print()
        print("暂无数据！")
        print()
#设置用户不输入内容返回原值，输入内容返回新内容
def new_input(yuanzhi,message):
    input_str=input(message)

    if len(input_str)>0:
        return input_str
    else:
        return yuanzhi


#保存数据至文件中
def save_file():

    f = open("student.txt", 'w', encoding='utf-8')
    f.write(str(student_list))
    f.close()
    print("数据保存至student.txt文件成功！")


#将数据读取至变量中
def read_file():

     if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        ret = f.read()
        global student_list
        student_list=eval(ret)
        f.close()
        print("数据读取成功!")
