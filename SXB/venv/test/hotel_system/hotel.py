# hotel.py
# 客户信息管理项目，要求带操作界面，并完成每项操作：
# ＋－－－－－－－－－－－－－－－－－－－－－－＋
# ｜　１）添加客户信息　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　２）显示所有客户的信息　　　　　　　　　　　　　　　　　｜
# ｜　３）删除客户信息　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　４）修改客户信息　　　　　　　　　　　　　　　　　　　　　　｜
# ｜ ５）查询客户信息                        ｜
# ｜ 6）按客户房间号高－低显示客户信息　　　　　　　　　｜
# ｜ 7）按客户年龄高－低显示客户信息　　　　　　　　　｜
# ｜ ９）保存客户信息到文件（students.txt)      ｜
# ｜ １０）从文件中读取数据（students.txt)      ｜
# ｜ 退出：其他任意按键＜回车＞                 ｜
# ＋－－－－－－－－－－－－－－－－－－－－－－＋               　　　　　　　　　｜

def meun():
    menu_info = '''＋－－－－－－－－－－－－－－－－－－－－－－＋
｜ １）添加客户信息(输入名字时为空时结束添加)  ｜
｜ ２）显示所有客户的信息                     ｜
｜ ３）删除客户信息                           ｜
｜ ４）修改客户信息                           ｜
｜ ５）查询客户信息                        ｜
｜ 6）按客户房间号高－低显示客户信息　　　　　　　　　｜
｜ 7）按客户年龄高－低显示客户信息　　　　　　　　　｜
｜ 8）保存客户信息到文件（guest.txt)      ｜
｜ 9）从文件中读取数据（guest.txt)      ｜
｜ 退出：其他任意按键＜回车＞                 ｜
＋－－－－－－－－－－－－－－－－－－－－－－＋
'''
    print(menu_info)


# 以下二个函数用于sorted排序，　key的表达式函数
def get_age(*l):
    for x in l:
        return x.get("age")


def get_room(*l):
    for x in l:
        return x.get("room")


# １）添加客户信息
def add_guest_info():
    L = []
    while True:
        _name = input("请输入名字：")
        if not _name:  # 名字为空　跳出循环
            break
        try:
            #_name = str(input("请输入姓名："))
            _age = int(input("请输入年龄："))
            _SID = str(input("请输入身份证号："))
            _number =str(input("请输入电话号码："))
            _room = str(input("请输入房间号："))
        except:
            print("输入无效，不是正确数值．．．．重新录入信息")
            continue
        info = {"name": _name, "age":_age, "SID":_SID, "number":_number,"room":_room}
        L.append(info)
    print("客户信息录入完毕！！！")
    return L


# ２）显示所有客户的信息
def show_guest_info(guest_info):
    if not guest_info:
        print("无数据信息．．．．．")
        return
    print("姓名".center(8), "年龄".center(4), "身份证".center(18),"电话号码".center(15),"房间号".center(8))
    for info in guest_info:
        print(info.get("name").center(10), str(info.get("age")).center(5), str(info.get("SID")).center(18),str(info.get("number")).center(15),str(info.get("room")).center(8))


# ３）删除学生信息
def del_guest_info(guest_info, del_name=''):
    if not del_name:
        del_name = input("请输入删除的客户姓名：")
    for info in guest_info:
        if del_name == info.get("name"):
            return info
    raise IndexError("客户信息不匹配,没有找到%s" % del_name)


# ４）修改学生信息
def mod_guest_info(guest_info):
    mod_name = input("请输入修改的客户姓名：")
    for info in guest_info:
        if mod_name == info.get("name"):
            _age = int(input("请输入年龄："))
            _SID = str(input("请输入身份证号："))
            _number = str(input("请输入电话号码："))
            _room = str(input("请输入房间号："))
            info = {"name": mod_name, "age": _age, "SID": _SID,"number": _number,"room":_room}
            return info
    raise IndexError("客户信息不匹配,没有找到%s" % mod_name)



# 5)查询客户信息
def search_guest_info(guest_info):
    searchSID = input("请输入你要查询客户的身份证号:")
#验证是否有此身份号
    #for info in guest_info:
    for info in guest_info:
      if info['SID'] == searchSID:
         print("找到此客户，信息如下：")
         print("身份证号：%s\n姓名：%s\n年龄：%s\n电话号码：%s\n房间号：%s\n" % (info['SID'], info['name'], info['age'],info['number'],info['room']))
    raise IndexError("客户信息不匹配,没有找到%s" %searchSID)

# ５）按房间号高－低显示客户信息

def room_reduce(guest_info):
    print("按客户房间号高－低显示")
    mit = sorted(guest_info, key=get_room, reverse=True)
    show_guest_info(mit)


# ６）按客户年龄低－高显示客户信息
def age_rise(guest_info):
    print("按学生成绩低－高显示")
    mit = sorted(guest_info, key=get_age)
    show_guest_info(mit)


# ９）保存学生信息到文件（students.txt)
def save_info(guest_info):
    try:
        guest_txt = open("guest.txt", "a")  # 以写模式打开，并清空文件内容
    except Exception as e:
        guest_txt = open("guest", "x")  # 文件不存在，创建文件并打开
    for info in guest_info:
        guest_txt.write(str(info) + "\n")  # 按行存储，添加换行符
    guest_txt.close()


# １０）从文件中读取数据（guest.txt)
def read_info():
    old_info = []
    try:
        guest_txt = open("guest.txt")
    except:
        print("暂未保存数据信息")  # 打开失败，文件不存在说明没有数据保存
        return
    while True:
        info = guest_txt.readline()
        if not info:
            break
        # print(info)
        info = info.rstrip()  # 去掉换行符
        # print(info)
        info = info[1:-1]  # 去掉｛｝
        # print(info)
        guest_dict = {}  # 单个学生字典信息
        for x in info.split(","):  # 以，为间隔拆分
            # print(x)
            key_value = []  # 开辟空间，key_value[0]存key,key_value[0]存value
            for k in x.split(":"):  # 以：为间隔拆分
                k = k.strip()  # 去掉首尾空字符
                # print(k)
                if k[0] == k[-1] and len(k) > 2:  # 判断是字符串还是整数
                    key_value.append(k[1:-1])  # 去掉　首尾的＇
                else:
                    key_value.append(int(k))
                # print(key_value)
            guest_dict[key_value[0]] = key_value[1]  # 客户信息添加
        # print(guest_dict)
        old_info.append(guest_dict)  # 所有客户信息汇总
    guest_txt.close()
    return old_info


def main():
    guest_info = []
    while True:
        # print(student_info)
        meun()
        number = input("请输入选项：")
        if number == '1':
            guest_info = add_guest_info()
        elif number == '2':
            show_guest_info(guest_info)
        elif number == '3':
            try:
                guest_info.remove(del_guest_info(guest_info))
            except Exception as e:
                # 客户姓名不匹配
                print(e)
        elif number == '4':
            try:
                guest = mod_guest_info(guest_info)
            except Exception as e:
                # 客户姓名不匹配
                print(e)
            else:
                # 首先按照根据输入信息的名字，从列表中删除该客户信息，然后重新添加该客户最新信息
                guest_info.remove(del_guest_info(guest_info, del_name=guest.get("name")))
                guest_info.append(guest)
        elif number == '5':
            try:
                guest_info.index(search_guest_info(guest_info))
            except Exception as e:
                # 客户姓名不匹配
                print(e)
        elif number == '6':
            room_reduce(guest_info)
        elif number == '7':
            age_rise(guest_info)
        elif number == '8':
            save_info(guest_info)
        elif number == '9':
            guest_info = read_info()
        else:
            break
        input("回车显示菜单")



main()

