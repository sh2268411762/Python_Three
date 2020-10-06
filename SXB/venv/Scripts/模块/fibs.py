def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


def fib2(n):
    ret = []
    a, b = 0, 1
    while b < n:
        ret.append(b)
        a, b = b, a + b
    return ret
