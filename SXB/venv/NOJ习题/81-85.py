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