# 例 6-24
def fac(n):
    if n == 1:
        return 1
    if n <= 0:
        return -1
    return fac(n - 1) * n


def fac1(n):
    if n > 0:
        if n == 1:
            return 1
        return fac1(n - 1) * n
    if n == 0:
        return 0
    if n < 0:
        if n == -1:
            return -1
        return fac1(n + 1) * n


a = eval(input("请输入数字："))
print(str(a) + "!=", fac(a))
a = eval(input("请输入数字："))
print(str(a) + "!=", fac1(a))


# 例 6-25
# 猴子吃桃子
def fun1():
    x = 1
    for i in range(6):
        x = (x + 1) * 2
    return x


def fun2(n):
    if n == 7:
        return 1
    return 2 * (1 + fun2(n + 1))


print(fun1())
print(fun2(1))


def han(n, a, b, c):
    if n == 1:
        print(n, "from", a, "to", b)
    else:
        han(n - 1, a, b, c)
        print(n, "from", a, "to", b)
        han(n - 1, c, b, a)


a = int(input("请输入数字："))
han(a, "A", "B", "C")
