# # 1
# print("Hello World")


# # 2
# a = int(input())
# b = int(input())
# print(a + b)


# # 3
# a = float(input())
# b = int(input())
# print(round(a,b))


# # 4
# a = int(input())
# b = int(input())
# print(bin(a), bin(a), a & b, end=" ")


# # 5
# a = int(input())
# c = input()
# print(chr(a), ord(c), end=" ")


# # 6
# num = int(input())
# print(oct(num), hex(num), bin(num), sep=",")


# # 7
# num = int(input())
# print('{: <10}'.format(num))
# print('{: >10}'.format(num))
# n = abs(num)
# print('{: <10}'.format("+%d" % n))
# print('{: >10}'.format("+%d" % n))


# # 8
# f = float(input())
# print(round(f, 6), round(f, 2), round(f, 8), '{:.6e}'.format(f), format(f, ','), sep="/")


# # 9
# num = int(input())
# print('{0:b}'.format(num), '{0:o}'.format(num), oct(num), '{0:x}'.format(num), hex(num), '{0:#X}'.format(num), sep=',')


# # 10
# def to_bin(value, num):  # 十进制数据，二进制位宽
#     bin_chars = ""  # str
#     temp = value
#     for i in range(num):
#         bin_char = bin(temp % 2)[-1]
#         temp = temp // 2
#         bin_chars = bin_char + bin_chars
#     return bin_chars
#
#
# m = int(input())
# n = int(input())
# print(to_bin(m, n))


# 11
# import math
#
# x = int(input())
# y = int(input())
# x1 = math.sqrt((math.pow(x, 2) + math.pow(y, 2)))
# y1 = math.atan(y / x)
# print("%.4f" % x1, "%.4f" % y1, sep=",")

# import math
#
# x = int(input())
# y = int(input())
# if x != 0:
#     x1 = math.sqrt((math.pow(x, 2) + math.pow(y, 2)))
#     y1 = math.atan(y / x)
#     print("%.4f" % x1, "%.4f" % y1, sep=",")
# else:
#     print("除数不可以为0")


# # 12
# import math
#
# v = float(input())
# T = float(input())
# W = 13.12 + 0.6215 * T - 11.35 * math.pow(v, 0.16) + 0.3965 * T * math.pow(v, 0.16)
# print(round(W))


# # 13
# import fractions
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# num1 = fractions.Fraction(a, c)
# num2 = fractions.Fraction(b, d)
# temp = num1 + num2
# print("(", num1, ")+(", num2, ")=", temp, sep='')
# temp = num1 - num2
# print("(", num1, ")-(", num2, ")=", temp, sep='')
# temp = num1 * num2
# print("(", num1, ")*(", num2, ")=", temp, sep='')
# temp = num1 / num2
# print("(", num1, ")/(", num2, ")=", temp, sep='')


# # 14
# person_age = float(input())
# if person_age <= 2:
#     dog_age = 10.5 * person_age
# else:
#     dog_age = (person_age - 2) * 4 + 10.5 * 2
# print(int(dog_age))


# # 15
# f = float(input())
# n = int(input())
# print(round(f, n))


# # 16
# import math
#
# h = float(input())
# r = float(input())
# V = math.pi * math.pow(r, 2) * h
# S = 2 * math.pi * math.pow(r, 2) + 2 * math.pi * r * h
# print("%.4f" % V, round(S, 4), sep="\n")


# # 17
# import math
#
# a = int(input())
# b = int(input())
# # c1 = math.sqrt((math.pow(a, 2) + math.pow(b, 2)))  # 斜边
# max = a if a >= b else b
# min = a if a < b else b
# # c2 = math.sqrt((math.pow(max, 2) - math.pow(min, 2)))
# #
# # if c1 < (a + b) and a < (b + c1) and b < (a + c1):
# #     print("c")
# # else:
# #     print("non")
# #
# # if a < (b + c2) and b < (a + c2) and c2 < (a + b):
# #     if c2 > min:
# #         print("b")
# #     else:
# #         print("a")
# # else:
# #    print("non")
#
# if max <= 0 or min <= 0:
#     print("non")
# else:
#     for c in range(int(math.sqrt((math.pow(max, 2) - math.pow(min, 2)))),
#                    int(math.sqrt((math.pow(max, 2) + math.pow(min, 2)))) + 1):
#         if math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2):
#             print("c")
#         elif math.pow(a, 2) == math.pow(c, 2) + math.pow(b, 2):
#             if c > b:
#                 print("b")
#             else:
#                 print("a")
#         elif math.pow(b, 2) == math.pow(a, 2) + math.pow(c, 2):
#             if c > a:
#                 print("a")
#             else:
#                 print("b")

# # 18
# import fractions
#
# f = float(input())
# f = int(f * 10)
# a = 10
# num = fractions.Fraction(f, a)
# print(num)
