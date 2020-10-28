# # 41
# # 因数分解
# def fun(a, t=2):
#     count = 0
#     if a < t:
#         return count
#     else:
#         for i in range(t, int(a / 2) + 1):
#             if a % i == 0:
#                 temp = a // i
#                 if temp >= i:
#                     count += 1
#                     count += fun(temp, i)
#         return count
#
#
# num = int(input())
# print(fun(num) + 1)


# # 42
# # 有效运动
# def fun1(x, y):
#     return x + y, y
#
#
# def fun2(x, y):
#     return x, x + y
#
#
# l = input()
# x1, y1, x2, y2 = map(int, l.split())
# m1 = x1
# n1 = y1
# isTrue1 = False
# isTrue2 = False
# while m1 < x2 and n1 < y2:
#     if y2 < x2:
#         m1, n1 = fun2(m1, n1)
#         if n1 == y2:
#             isTrue1 = True
#             if m1 == x2:
#                 isTrue2 = True
#             else:
#                 while m1 < x2:
#                     m1, n1 = fun1(m1, n1)
#                 if m1 == x2:
#                     isTrue2 = True
#     else:
#         m1, n1 = fun1(m1, n1)
#         if m1 == x2:
#             isTrue1 = True
#             if n1 == y2:
#                 isTrue2 = True
#             else:
#                 while n1 < y2:
#                     m1, n1 = fun2(m1, n1)
#                 if n1 == y2:
#                     isTrue2 = True
# if isTrue1 and isTrue2:
#     print("true")
# else:
#     print("false")


# # 43
# # 卡塔兰数
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# def fun(n):
#     ret = fac(2 * n) / (fac(n + 1) * fac(n))
#     return ret
#
#
# num = int(input())
# print(int(fun(num)))


# # 44
# # 扩展欧几里得算法
# def gcd(x, y):
#     i = x
#     while i > 1:
#         if x % i == 0 and y % i == 0:
#             return i
#         i -= 1
#     else:
#         return 1
#
#
# def fun(x, y):
#     t = gcd(x, y)
#     i = 0
#     j = 0
#     while True:
#         j = (t - x * i) // y
#         if t == x * i + y * j:
#             return i, j
#         i += 1
#
#
# x = input()
# a, b = map(int, x.split())
# ret1, ret2 = fun(a, b)
# print(ret1, ret2, sep=" ")


# # 45
# # 考拉兹猜想：每一个正整数，如果它是奇数，则对它乘3再加1，如果它是偶数，则对它除以2，如此循环，最终都能够得到1
# def fun(n):
#     l1 = [n]
#     while True:
#         if n == 1:
#             break
#         if n % 2 == 0:
#             n = n // 2
#             l1.append(n)
#         else:
#             n = 3 * n + 1
#             l1.append(n)
#     return l1
#
#
# num = int(input())
# l0 = fun(num)
# for i in range(0, len(l0) - 1):
#     print(l0[i], ",", sep="", end="")
# print(l0[-1], end="")


# # 46
# # 非负累加（重写）
# def fun(num, val):
#     count = 0
#     t = 0
#     if num == 0 and t == val:
#         count += 1
#     else:
#         for i in range(0, val):
#             t += fun(num - 1, val)
#     return t
#
#
# x = input()
# n, v = map(int, x.split())
# count = 0
# for i in range(0, v + 1):
#     for ii in range(0, v + 1):
#         for iii in range(0, v + 1):
#             for iiii in range(0, v + 1):
#                 for iiiii in range(0, v + 1):
#                     if (i + ii + iii + iiii + iiiii) == v:
#                         count += 1
# print(count)


# # 47
# # 霍夫斯塔德序列
# def F(n):
#     if n == 0:
#         return 1
#     else:
#         ret = n - M(F(n - 1))
#         return ret
#
#
# def M(n):
#     if n == 0:
#         return 0
#     else:
#         ret = n - F(M(n - 1))
#         return ret
#
#
# num = int(input())
# if num >= 0:
#     f = F(num)
#     m = M(num)
#     print(f, m, sep=" ")


    # # 48
    # # 分苹果
    # def fun(m, n):
    #     if m == 0 or n == 1:  # 碟子为 1 或苹果为 0 则只有一种方法
    #         return 1
    #     if n > m:  # 碟子数量大于苹果
    #         return fun(m, m)
    #     else:
    #         return fun(m, n - 1) + fun(m - n, n)
    #
    #
    # x = input()
    # M, N = map(int, x.split())
    # if M >= 1 and N <= 10:
    #     print(fun(M, N))


# # 49
# # 配尔数
# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return 2 * fun(n - 1) + fun(n - 2)
#
#
# num = int(input())
# print(fun(num))


# # 50
# # 倒序二进制
# num = int(input())
# s = str(bin(num))
# l = []
# for i in range(0, len(s) - 2):
#     l.append(s[i + 2])
# l.reverse()
# for i in range(0, len(l)):
#     print(l[i], end="")
