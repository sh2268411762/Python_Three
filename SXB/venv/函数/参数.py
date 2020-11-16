# 例 6-10
# 位置参数
def printChars(ch1, ch2, number):
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        count += 1
        if count % number != 0:
            print(" % 4s" % chr(i), end=' ')
        else:
            print(" % 4s" % chr(i))  # 整除换行


printChars("!", "9", 8)

# 例 6-11
# 默认参数
print("函数定义时，形参中非默认参数可以与默认参数共存，但是非默认参数之前不可以有默认参数")


# n表示行数，m表示将s打印几遍
def sayHello2(s="Hello!", n=2, m=1):
    for i in range(1, n + 1):
        print(s * m)


print("形参没有赋予新值，采用默认值：")
sayHello2()

print("\n按照顺序依次赋予新值：")
sayHello2("Ha!", 4, 5)

print("\n只给s赋予新值：")
sayHello2("Ha")


# 例 6-12
# 关键字参数
def sayHello3(s, n=2, m=1):
    for i in range(1, n + 1):
        print(s * m)


print("关键字传参可以不按顺序，而采用变量名=值的形式来进行赋值：")
sayHello3(m=3, s="Ha!")


# 例 6-13
# 可变长参数
def print_all(*args):
    print(args)


print_all("a")
print_all("a", 2)
print_all("a", 1, 2, 3, 4, 5, 6)
print("函数定义中，参数形式前有一个 * 表示参数可以接收不定个数的参数，且传入参数以元组形式保存")


# 例 6-14
def add(*args):
    ret = 0
    for i in range(0, len(args)):
        if type(args[i]) == int:
            if 0 <= args[i] <= 9:
                ret += args[i]
        elif args[i].isdigit():
            ret += int(args[i])
    return ret


print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, "4", "5"))
print(add(1, 2, "3", "4", "a"))

# 例 6-15
print("可变长参数也可以与其他普通参数联合使用，这时一般将可变长参数放在最后：")


def print_6_15(a, b, *args):
    print(a)
    print(b)
    print(args)


print_6_15(1, 2, 3, 3, 3, 3, 3, 34, 4, 5, 5, )
print_6_15("aba", 'a', 'e', 'r', 3, 4, 7)

# 例 6-16
print("在Python的函数形参中提供了前面加标识符 ** 的方式，用来引用一个字典"
      "。函数调用者必须以关键值参数的形式为其赋值，形参得到一个以以关键值参数中"
      "变量名为key，右边表达式值为value的字典")


def print_6_16(**args):
    print(args)


print_6_16(x="a", y="b", z=2)
print_6_16(m=3, n=4)


# 例 6-17
def print_6_17(**args):
    print(args)
    ret = 0
    for i in args.keys():
        if type(args[i]) == int:
            ret += args[i]
        elif args[i].isdigit():
            ret += int(args[i])
    return ret


print("\n\n", print_6_17(x=1, y=2, z=3))
print(print_6_17(x=1, y=2, z="3", a="4"))
print(print_6_17(x=1, y=2, z="3", a="a"))

# 例 6-18
print("多种参数混合时，普通参数在最前，其次是以 * 为前缀的可变长度参数，其次是以 ** 为前缀的可变长度参数")


def print_6_18(a, b, *aa, **bb):
    print(a)
    print(b)
    print(aa)
    print(bb)


print_6_18(1, 2, 3, 4, 5, xx="a", yy="b", zz=2)

# 例 6-19
print("序列和字典作为参数的要求：")
print("1、函数中形参也是序列")
print("2、如果函数中形参是n个单变量，则在实参的序列变量名前加 * ，要求实参序列中的元素个数与单变量形参个数相同；\n"
      "如果实参中普通变量与序列变量混用，则以 * 为前缀的序列变量放置在实参的最后")


def sun1(args):
    print(args)
    s = 0
    for i in args:
        s += i
    return s


def sun2(args):
    print(args)
    s = 0
    for i in args.keys():
        s += args[i]
    return s


print("sun1:")
aa = [1, 2, 3]  # 列表
print(sun1(aa))
print(sun1([4, 5]))  # 列表
bb = (1, 2, 3, 4)
print(sun1(bb), "\n")

print("sun2:")
cc = {'x': 1, 'y': 2, 'c': 3}  # 字典
print(sun2(cc))
print(sun2({'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}))  # 字典
