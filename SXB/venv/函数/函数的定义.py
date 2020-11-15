# 例 6-1
def sayHello():  # 函数定义
    print("Hello World!")  # 函数体


sayHello()  # 函数调用


# 例 6-2
def sayHello1(s):  # 函数定义
    print(s)  # 函数体


sayHello1("Hello!")  # 函数调用
sayHello1("How are you?")


# 例 6-3
def fac(num):
    if num == 1:
        return 1
    elif num < 1:
        return 0
    else:
        ret = 1
        while num > 1:
            ret *= num
            num -= 1
        return ret


print(6, "!=", fac(6), sep="")
print(16, "!=", fac(16), sep="")
print(26, "!=", fac(26), sep="")
print(0, "!=", fac(0), sep="")
print(1, "!=", fac(1), sep="")
