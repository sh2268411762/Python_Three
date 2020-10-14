# # 21
# # 阶乘末尾 0 的个数
# # def fac(n):
# #     temp = 1
# #     while n > 0:
# #         temp *= n
# #         n -= 1
# #     return temp
# #
# #
# # def deter(n):
# #     temp1 = fac(n)
# #     temp2 = float(temp1)
# #     count = 0
# #     while (temp1 // 10 * 10) == temp2:
# #         count += 1
# #         temp1 /= 10
# #         temp2 /= 10
# #     return count
# #
# #
# # num = int(input())
# # print(deter(num))
#
#
# num = int(input())
# temp = 1
# while num > 0:
#     temp *= num
#     num -= 1
#
# n = 0
# for i in range(len(str(temp))):
#     if '0' == str(temp)[len(str(temp)) - i - 1]:
#         n += 1
#     else:
#         break
# print(n)


# 22
# 回文数
# def isPalindrome(n):
#     temp1 = n
#     temp2 = 0
#     while temp1 > 0:
#         temp2 = temp1 % 10 + temp2 * 10
#         temp1 //= 10
#     if n == temp2:
#         return True
#     else:
#         return False
#
#
# num = int(input())
# if isPalindrome(num):
#     print("Yes")
# else:
#     print("Not")


# # 23
# # 操作数
# def sum(n):
#     temp1 = 0
#     while n > 0:
#         temp1 = n % 10 + temp1
#         n //= 10
#     return temp1
#
#
# def sub(n):
#     temp = sum(n)
#     n = n - temp
#     return n
#
#
# num = int(input())
# count = 0
# while num > 0:
#     count += 1
#     num = sub(num)
# print(count)


# # 24
# # 斐波那契数列
# def fib(n):
#     t1 = 1
#     t2 = 1
#     t3 = t1 + t2
#     temp = n
#     while n > 3:
#         t1 = t2
#         t2 = t3
#         t3 = t1 + t2
#         n -= 1
#     return t3
#
#
# num = int(input())
# print(fib(num))


# # 25
# # 组合数
# num = int(input())
# count = 0
# for a in range(0, 10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             for d in range(0, 10):
#                 if (a + b + c + d) == num:
#                     count += 1
# print(count)


# # 26
# # 平行
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())
# x4 = int(input())
# y4 = int(input())
#
# k1 = (y1 - y2) / (x1 - x2)
# k2 = (y3 - y4) / (x3 - x4)
#
# if abs(k1) == abs(k2):
#     print("Yes")
# else:
#     print("No")


# # 27
# # 整数组合
# n = int(input())
# m = int(input())
# sum = 0
# temp = n
# while m > 0:
#     sum += n
#     n = n * 10 + temp
#     m -= 1
# print(sum)


# # 28
# # 圆
# import math
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# x3 = int(input())
# y3 = int(input())
# a = 2 * (x2 - x1)
# b = 2 * (y2 - y1)
# c = 2 * (x3 - x2)
# d = 2 * (y3 - y2)
# e = x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1
# f = x3 * x3 + y3 * y3 - x2 * x2 - y2 * y2
# x = (b * f - d * e) / (b * c - d * a)
# y = (c * e - a * f) / (b * c - d * a)
# r = math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
# print("{:.3f}".format(r), "{:.3f}".format(x), "{:.3f}".format(y), sep=",")


# # 29
# # 方程组
#
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())
#
# if e != 0 and b != 0 and (a * e - b * d) != 0:
#     if (d / e) == (a / b):
#         print("error")
#     else:
#         x = (c * e - b * f) / (a * e - b * d)
#         y = (c - a * x) / b
#     print("%.3f" % x, "%.3f" % y, sep=" ")
# else:
#     print("error")


# # 30
# # 对称数
#
# def len_n(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n //= 10
#     return count
#
#
#  def find(m):
# #     n = len_n(m)
# #     nums = n % 2 * list('018') or ['']
# #     while n > 1:
# #         n -= 2
# #         nums = [a + num1+ b for a, b in '00 11 88 69 90 96'.split()[n < 2:] for num1 in nums]
#     #        print(nums)
#     if str(m) in nums:
#         return print("Yes")
#     else:
#         return print("No")
#
#
# num = int(input())
# find(num)
