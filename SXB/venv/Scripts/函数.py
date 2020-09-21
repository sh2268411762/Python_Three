#必须参数：函数定义的参数调用时必须传入，并且调用时数量和顺序必须和定义函数时的参数保持一致
def add(a,b):
    print("a + b = ",a+b)
add(1,2)

#关键字参数：可以不按函数定义时的参数的顺序来调用函数，Python解释器能够根据函数定义时的参数名来匹配函数
def hello(name,age):
    print("姓名：",name)
    print("年龄：",age)
#按顺序传递参数
hello(name = "孙豪",age = 20)
#不按顺序传递参数
hello(age = 19,name = "张莎")

#默认参数：在定义函数时可以给参数添加默认值，如果调用函数时没有传入参数，函数就会使用默认值，并且不会像参数那样报错
#       默认参数必须定义在最后，而且在默认参数之后定义必须参数会报错
def fun1(name,age = 10):
    print("姓名：",name)
    print("年龄：",age,"岁")
fun1(name = "孙豪")
def fun2(name,s = 60,l = "ShanXi"):
    print("姓名：",name)
    print("成绩：",s,"分")
    print("地区：",l)
print("-------传入所有参数-------")
fun2("孙豪",100,"ShanXi")
print("-------不传最后一个参数-------")
fun2("牛娃",80)
print("-------不传成绩-------")
fun2("二球",l = "BeiJing")
print("-------只传必须参数-------")
fun2("王翔")
print("-------只传关键字参数-------")
fun2(name = "辰鑫")

#可变参数：在定义函数时不能确定参数的内容和数量
def fun3(*args):# *args 参数获取到的是一个元组
    print(args)
fun3()
fun3(1,2,3,4)
fun3("孙豪","欣欣")
def fun4(**kwargs):# **kwargs获取的是一个字典
    print(kwargs)
fun4()
fun4(name = "孙豪",age = 18)
def add(*args,**kwargs):
    s = 0
    for i in args:
        s += i
    print("输入的数字之和为：",s)
    for k,v in kwargs.items():
        print(k,"：",v)
add(1,2,3,4,5,6,7,8,9,10,姓名 = "孙豪",年龄 = 22,性别 = "男")

#变量
x = "函数体外"
def fun5():
    x = "函数体内"
    print(x)
fun5()
print(x)

x = "函数体外"
def fun6():
    global x  #global关键字可以在函数体内修改全局变量
    x = "函数体内"
    print(x)
fun6()
print(x)


#返回值
def no_return():
    print("无return")
def no_value():
    print("有return无返回值")
    return
def has_reurn():
    x = "局部变量"
    print("有return")
    return x

ret1 = no_return()
print(ret1)    #None
ret2 = no_value()
print(ret2)    #None
ret3 = has_reurn()
print(ret3)    #value

def fun6():
    r1 = "一"
    r2 = "二"
    r3 = "三"
    r4 = "四"
    r5 = "五"
    return r1,r2,r3,r4,r5   #返回一个元组
s = fun6()
print(s)

#匿名函数 Lambda表达式：一般在需要一个函数，但名字不重要
def fun7(x,y):
    return x+y
fun8 = lambda x,y:x+y   #以lambda开头，表示这是一个lambda表达式，：前是参数，：后是返回值
print(fun8)
ret4 = fun8(6,7)
print(ret4)
#文档字符串
def Add(x,y):
    """

返回参数x和y的两数之和

Parameters
---------------
x:int
第一个参数
y:int
第二个参数

Returns
--------------

int
返回x+y
    """
    return x+y
ret5 = Add(88,9)
print(ret5)
print(Add.__doc__) #__doc__可以用来获取文档字符串
help(Add)
def fun9(name:"名字",age:"年龄",id:"手机号")->"手机号":
    return id
ret6 = fun9(name = "孙豪",age = 21,id = 18710870197)
print(ret6)
print(fun9.__annotations__)  #获取函数注释