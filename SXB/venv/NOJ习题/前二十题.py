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
# max = a if a > b else b
# min = a if a < b else b
#
#
# def isTriangle(a, b, c):  # 判断是否三角形
#     if a + b > c and a + c > b and b + c > a and abs(a - b) < c and abs(a - c) < b and abs(c - b) < a:
#         return True
#     else:
#         return False
#
#
# condition1 = int(math.sqrt(math.pow(max, 2) - math.pow(min, 2)))  # 直角边
# condition2 = int(math.sqrt(math.pow(max, 2) + math.pow(min, 2)))  # 斜边
# if (isTriangle(min, max, condition2) and math.pow(min, 2) + math.pow(max, 2) == math.pow(condition2,
#                                                                                          2) and condition2 > max):
#     print("c")
# elif isTriangle(min, max, condition1) and math.pow(min, 2) + math.pow(condition1, 2) == math.pow(max, 2):
#     if condition1 < min:
#         print("a")
#     if max > condition1 > min:
#         print("b")
# else:
#     print("non")
#
#
# def isTriangle(a, b, c):
#     if a + b < c:
#         return False
#     if a + c < b:
#         return False
#     if b + c < a:
#         return False
#     if abs(a - b) > c:
#         return False
#     if abs(a - c) > b:
#         return False
#     if abs(c - b) > a:
#         return False
#     return True

# # 18
# import fractions
#
# f = float(input())
# f = int(f * 10)
# a = 10
# num = fractions.Fraction(f, a)
# print(num)


# # 19
# def rgb2hsv(R, G, B):
#     R, G, B = R / 255.0, G / 255.0, B / 255.0  # R,G,B在 0 到 1 之间
#     Max = max(R, G, B)  # 最大值
#     Min = min(R, G, B)  # 最小值
#     m = Max - Min
#     V = Max
#
#     if V == 0:
#         S = 0
#     else:
#         S = m / Max
#
#     if Max == Min:
#         H = 0
#     elif Max == R:
#         H = ((G - B) / m) * 60
#     elif Max == G:
#         H = ((B - R) / m) * 60 + 120
#     elif Max == B:
#         H = ((R - G) / m) * 60 + 240
#
#     if H < 0:
#         H = H + 360
#
#     return H, S, V
#
#
# r = int(input())
# g = int(input())
# b = int(input())
#
# h, s, v = rgb2hsv(r, g, b)
# print("%.4f" % h, "%.4f%%" % (s * 100), "%.4f%%" % (v * 100), sep=",")


# 20
# import math
#
#
# def get_distance(L1, L2):
#     lon1 = math.radians(float(L1[0]))
#     lon2 = math.radians(float(L1[1]))  # 经度
#     lat1 = math.radians(float(L2[0]))
#     lat2 = math.radians(float(L2[1]))  # 纬度
#     lo = lon1 - lon2
#     la = lat1 - lat2
#
#     a = math.pow(math.sin(la / 2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(lo / 2), 2)
#     D = 2 * math.asin(math.sqrt(a)) * 6371
#     return D
#
#
# w1 = input()  # 西安纬度
# j1 = input()  # 西安经度
# w2 = input()  # 莫斯科纬度
# j2 = input()  # 莫斯科经度
#
# l1 = [j1, j2]  # 经度集合
# l2 = [w1, w2]  # 纬度集合
# d = get_distance(l1, l2)
# print("%.4fkm" % d)
