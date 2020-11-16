# 例 6-23
# 斐波那契数列
def fib1(n):
    i, a, b = 0, 0, 1
    l = []
    while i < n:  # i是个数-1
        l.append(a)
        a, b = b, a + b
        i += 1
    return l


def fib2(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


n = int(input("请输入个数："))
l = fib1(n)
print(type(l))
for i in l:
    print(i, end="\t")
l = fib2(n)
print("\n", type(l))
for i in l:
    print(i, end="\t")

print("\nPython中使用了yield的函数返回生成器对象，此函数称为生成器函数，只能用于迭代操作"
      "\n。在调用函数过程中，每次遇到yield语句时，函数会暂停执行，并保存当前所有的运行状态信息，返回yield后面的值"
      "，\n并在下一次执行next()方法时从当前位置继续运行，生成器函数返回的是一个生成器对象")
