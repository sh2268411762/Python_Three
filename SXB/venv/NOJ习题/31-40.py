# # 31
# # 长安
# l1 = []
#
#
# def fun(m, n):
#     t1 = 1
#     t2 = 1
#     t3 = n
#     t4 = m
#     while t3 > 0:  # t1
#         t1 *= t4
#         t4 -= 1
#         t3 -= 1
#     t3 = n
#     while t3 > 0:  # t2
#         t2 *= t3
#         t3 -= 1
#     return t1 // t2
#
#
# while True:
#     x = input()
#     bi, bj, pi, pj = map(int, x.split(","))
#     if bi < 0 or bj < 0 or pi < 0 or pj < 0:
#         break
#     else:
#         a = fun((bi + bj), bj)
#         b = fun((pi + pj), pj)
#         c = fun((abs(bi - pi) + abs(bj - pj)), abs(bj - pj))
#         if b == 1 or c == 1:
#             d = a
#         else:
#             d = a - b * c
#         l1.append(d)
# for i in range(0, len(l1)):
#     print(l1[i])


# import math
#
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     elif x % 2 == 1:
#         print(0)
#     else:
#         ret = (x + int(math.pow(x, 2)) // 2 - 1) % 100003
#         print(ret)


# # 32
# # 乘方
# while True:
#     x = input()
#     a, b = map(int,x.split())
#     if a <= 0 or b <= 0:
#         break
#
#     temp = 1
#     a %= 10
#     while b > 1:
#         if b & 1:
#             temp = (temp * a) % 10
#         a = (a * a) % 10
#         b >>= 1
#     ret = (temp * a) % 10
#     print(ret)


# # 33
# # 上楼梯
# def fun(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     return fun(n - 1) + fun(n - 2) + fun(n - 3)
#
#
# while True:
#     num = int(input())
#     if num <= 0:
#         break
#
#     ret = fun(num)
#     print(ret)


# # 34
# # 铺地砖
# def floor(n):
#     if n % 2 == 1:
#         return 0
#     f = [0 for i in range(n + 1)]
#     f[0] = 1
#     f[2] = 3
#     for i in range(4, n + 1, 2):
#         f[i] = f[i - 2] * 4 - f[i - 4]
#     return f[n] % 100003
#
#
# n = int(input())
# while n != 0:
#     print(floor(n))
#     n = int(input())

# 35
# # 小木棍
# def fun1(num):
#     l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#     if num < 10:
#         ret = l[num]
#     elif 10 <= num < 100:
#         ret = l[num % 10] + l[num // 10]
#     elif 100 <= num < 1000:
#         ret = l[num % 10] + l[(num // 10) % 10] + l[num // 100]
#     else:
#         ret = l[num % 10] + l[(num // 10) % 10] + l[num // 100 % 10] + l[num // 1000]
#     return ret
#
#
# def fun2(n):
#     count = 0
#     n -= 4
#     for i in range(1000):
#         for j in range(1000):
#             if fun1(i) + fun1(j) + fun1(i + j) == n + 4:
#                 count += 1
#     return count
#
#
# num = int(input())
# if num <= 24:
#     if num <= 4:
#         print(0)
#     else:
#         num -= 4
#         print(fun2(num))


# 36
# 吃糖果
def F(n):
    a = 1
    b = 2
    if n == 1 or n == 2:
        return n
    else:
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
        return c


n = int(input())
while n > 0:
    print(F(n))
    n = int(input())


