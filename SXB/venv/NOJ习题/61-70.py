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


# # 61
# # 重复字符
# s = input()
# l = []
# for i in range(0, len(s)):
#     count = 0
#     for j in range(0, len(s)):
#         if s[i] == s[j]:
#             count += 1
#     if count > 1:
#         if s[i] not in l:
#             print(s[i], count, sep=" ")
#             l.append(s[i])


# # 62
# # 元素相乘
#
# x = input()
# l = x.split(" ")
#
# sum = 1
# for i in range(0, len(l)):
#     sum *= int(l[i])
# print(sum)


# # 63
# # 排序3
# x = input()
# ll = x.split(";")
# l1 = []
# for i in range(0, len(ll)):
#     s = str(ll[i]).strip("\'")
#     s = s.strip("(")
#     s = s.strip(")")
#     m, n = map(int, s.split(","))
#     t = (m, n)
#     l1.append(t)
#
# l2 = sorted(l1, key=lambda x: (x[1]))
# print(l2)


# # 64
# # 排序2
# x = input()
# ll = x.split(",")
# l1 = []
# for i in range(0, len(ll)):
#     s = str(ll[i]).strip("\'")
#     s = s.strip("a")
#     s = int(s)
#     l1.append(s)
# l1.sort()
# l2 = []
# for i in range(0, len(l1)):
#     s = 'a' + str(l1[i])
#     l2.append(s)
# for i in range(0, len(l2)):
#     print(l2[i], end=' ')


# # 65
# # 反转元组
# x = input()
# ll = x.split(" ")
# l1 = []
# for i in range(0, len(ll)):
#     s = int(ll[i])
#     l1.append(s)
# l1.reverse()
# l2 = list(reversed(l1))
# for i in range(0, len(l2)):
#     l2[i] = l1[i] + l2[i]
# t = tuple(l2)
# print(t)


# # 66
# # 循环相同
# x = input()
# l1 = x.split()
# ll1 = l1
# y = input()
# l2 = y.split()
# ll2 = l2
# l3 = []
# l4 = []
# if len(l1) == len(l2):
#     l = len(l1)
#     for i in range(0, l):
#         if i > 0:
#             s = ll1.pop(0)
#             ll1.append(s)
#         str1 = ''.join(ll1)
#         l3.append(str1)
#
#     for i in range(0, l):
#         if i > 0:
#             s = ll2.pop(0)
#             ll2.append(s)
#         str2 = ''.join(ll2)
#         l4.append(str2)
#
#     isTrue = True
#     for i in range(0, l):
#         for j in range(0, l):
#             if l3[i] == l4[j]:
#                 break
#             if j == (l - 1):
#                 isTrue = False
#     print(isTrue)


# # 67
# # 列表差异
# x = input()
# l1 = x.split()
# y = input()
# l2 = y.split()
# l3 = []
# for i in range(0, len(l1)):
#     for j in range(0, len(l2)):
#         if l2[j] == l1[i]:
#             break
#         if len(l2) - 1 == j:
#             l3.append(l1[i])
# for i in range(0, len(l2)):
#     for j in range(0, len(l1)):
#         if l1[j] == l2[i]:
#             break
#         if len(l1) - 1 == j:
#             l3.append(l2[i])
# for i in range(len(l3)):
#     print(l3[i], end=" ")


# # 68
# # 排序1
# x = input()
# list = x.split()
# l1 = []
# for i in range(0, len(list)):
#     s = int(list[i])
#     l1.append(s)
# l1.sort(reverse=True)
# for i in range(0, len(l1)):
#     print(l1[i], end=" ")


# # 69
# # 重复元素
# num = int(input())
# x = input()
# l1 = x.split()
# l2 = []
# for i in range(0, len(l1)):
#     s = int(l1[i])
#     l2.append(s)
# t1 = tuple(l2)
# count = 0
# for i in range(0, len(t1)):
#     if num == t1[i]:
#         count += 1
# print(count)


# # 70
# # 列表切片
# x = input()
# m, n = map(int, x.split())
# y = input()
# l1 = y.split()
# l2 = []
# for i in range(0, len(l1)):
#     s = int(l1[i])
#     l2.append(s)
# l3 = l2[m:n]
# print(l3)
