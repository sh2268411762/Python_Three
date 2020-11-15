# 例 6-4
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


def sum(n):
    ret = 0
    while n > 0:
        ret += fac(n)
        n -= 1
    return ret


print("1! + 2! + 3! + 4! + 5! = ", sum(5));
