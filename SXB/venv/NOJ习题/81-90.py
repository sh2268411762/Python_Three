# # 81
# # 和为0
# class A:
#     def __init__(self):
#         pass
#
#     def add_zero(self, l):
#         t = []
#         for i in range(0, len(l)):
#             for j in range(i + 1, len(l)):
#                 for k in range(j + 1, len(l)):
#                     s = []
#                     if (l[i] + l[j] + l[k]) == 0:
#                         v = [l[i], l[j], l[k]]
#                         v.sort()
#                         s.append(v)
#                         t.extend(s)
#         return t
#
#
# x = input()
# l1 = x.split()
# for i in range(0, len(l1)):
#     l1[i] = int(l1[i])
# a = A()
# l2 = a.add_zero(l1)
# print(l2)


# # 82
# # 矩形类
# class Rectangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w
#
#     def area(self):
#         return self.l * self.w
#
#
# x = input()
# l, w = map(int, x.split())
# r = Rectangle(l, w)
# print(r.area())


# # 83
# # 罗马数字转整数 2
# class RomanInt:
#     def __init__(self, s):
#         self.s = s
#
#     # def toInt(self):
#     #     temp = 0
#     #     for i in range(0, len(self.s)):
#     #         if self.s[i] == 'I':
#     #             temp += 1
#     #         elif self.s[i] == 'V':
#     #             temp += 5
#     #         elif self.s[i] == 'X':
#     #             temp += 10
#     #         elif self.s[i] == 'L':
#     #             temp += 50
#     #         elif self.s[i] == 'C':
#     #             temp += 100
#     #         elif self.s[i] == 'D':
#     #             temp += 500
#     #         elif self.s[i] == 'M':
#     #             temp += 1000
#     #         else:
#     #             temp += 0
#     #     return temp if 1 < temp <3999 else False
#
#     def fun(self):
#         d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         result = 0
#         for i in range(len(self.s) - 1):
#             if d[self.s[i]] < d[self.s[i + 1]]:
#                 result -= d[self.s[i]]
#             else:
#                 result += d[self.s[i]]
#         result += d[self.s[len(self.s) - 1]]
#         return result if 1 < result < 3999 else False
#
#
# x = input()
# a = RomanInt(x)
# print(a.fun())


# # 84
# # 闭合括号
# def fun(s):
#     b = []
#     flag = True
#     for i in s:
#         if i == "(" or i == "[" or i == "{":
#             b.append(i)
#         elif i == ")":
#             if len(b) == 0 or b.pop() != "(":
#                 return False
#         elif i == "]":
#             if len(b) == 0 or b.pop() != "[":
#                 return False
#         elif i == "}":
#             if len(b) == 0 or b.pop() != "{":
#                 return False
#     if len(b) != 0:
#         flag = False
#     return flag
#
#
# l = list()
# while True:
#     x = input()
#     if x != "":
#         l.append(x)
#     else:
#         break
# for i in range(0, len(l)):
#     print(fun(l[i]))


# # 85
# # 罗马数字1
# class Roman_Int:
#     def __init__(self, n):
#         self.n = n
#
#     def to_Int(self):
#         if 1 <= self.n <= 3999:
#             i1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#             s = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#             ret = ""
#             for i in range(0, len(i1)):
#                 while self.n >= i1[i]:
#                     self.n -= i1[i]
#                     ret += s[i]
#             return ret
#
#
# num = int(input())
# r = Roman_Int(num)
# print(r.to_Int())


# # 86
# # 圆类
# import math
#
#
# class Circle:
#
#     def __init__(self, _r):
#         self.r = _r
#         self.PI = 3.14
#
#     def area(self):
#         return self.PI * math.pow(self.r, 2)
#
#     def perimeter(self):
#         return 2 * self.PI * self.r
#
#
# r = float(input())
# c = Circle(r)
# print(c.area(), c.perimeter(), sep=" ")


# # 87
# # 唯一子集
# from math import pow
#
#
# class A:
#     def __init__(self, _s):
#         self.s = _s
#
#     def fun(self):
#         Len = len(self.s)
#         ll = []
#         for ii in range(0, int(pow(Len, 2) - 1)):
#             lll = []
#             for j in range(Len):
#                 if (ii >> j) % 2:
#                     lll.append(self.s[Len - j - 1])
#             lll.sort()
#             ll.append(lll)
#         if ll[-1] != self.s:
#             ll.append(self.s)
#         return ll
#
#
# x = input()
# l1 = x.split()
# for i in range(0, len(l1)):  # 变为int
#     l1[i] = int(l1[i])
#
# s1 = set(l1)
# l1 = list(s1)  # 去重
# l1.sort(reverse=False)  # 排序
# a = A(l1)
# print(a.fun())

# l1.sort(reverse=True)  # 排序
# print(l1)
# a = A(l1)
# print(a.fun())

# # 88
# # 特定目标
# class A:
#     def __init__(self, _s):
#         self.s = _s
#
#     def fun(self, n):
#         for i in range(0, len(self.s)):
#             isTrue = False
#             for j in range(0, len(self.s)):
#                 if i == j:
#                     break
#                 else:
#                     if self.s[i] + self.s[j] == n:
#                         print(self.s[j], "+", self.s[i], "=", n, sep=" ")
#                         isTrue = True
#                         break
#             if isTrue:
#                 break
#
#
# x = input()
# l1 = x.split()
# num = int(input())
# for i in range(0, len(l1)):
#     l1[i] = int(l1[i])
# a = A(l1)
# a.fun(num)


# # 89
# # 反向字符串
# class A:
#     def __init__(self, _s):
#         self.s = _s
#
#     def fun(self):
#         l1 = self.s
#         l1.reverse()
#         ll = []
#         for i in range(0, len(l1)):
#             s = ""
#             s = l1[i]
#             ll.append(s)
#         return ll
#
#
# x = input()
# l1 = x.split()
# a = A(l1)
# l1 = a.fun()
# for i in range(0, len(l1)):
#     print(l1[i], end=" ")


# # 90
# # Pow方法
# class A:
#     def __init__(self, _x):
#         self.x = _x
#
#     def fun(self, n):
#         ret = 1
#         isTrue = False
#         if n < 0:
#             n = abs(n)
#             isTrue = True
#         if n > 0:
#             while n > 1:
#                 if n & 1 == 1:
#                     ret *= self.x
#                 self.x *= self.x
#                 n = n >> 1
#             if isTrue:
#                 return 1 / (ret * self.x)
#             return ret * self.x
#         elif n == 0:
#             return 1
#
#     def fun1(self, n, l):
#         ret = 1
#         isTrue = False
#         if n < 0:
#             n = abs(n)
#             isTrue = True
#         if n > 0:
#             while n > 1:
#                 if n & 1 == 1:
#                     ret *= self.x
#                 self.x *= self.x
#                 n = n >> 1
#             if isTrue:
#                 r = 1 / (ret * self.x)
#             r = ret * self.x
#         elif n == 0:
#             r = 1
#         return r % l
#
#
# s = input()
# x, num = map(int, s.split())
# a = A(x)
# print(a.fun(num))
