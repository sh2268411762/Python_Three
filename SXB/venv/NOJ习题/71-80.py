# # 71
# # 差集
# x = input()
# l1 = x.split()
# y = input()
# l2 = y.split()
#
# s1 = set(l1)
# s2 = set(l2)
# s3 = s1.difference(s2)
# l3 = list(s3)
# for i in range(0, len(l3)):
#     print(l3[i], end=' ')


# # 72
# # 字典相加
# x = input()
# l1 = x.split(",")
# y = input()
# l2 = y.split(",")
# k1 = []
# v1 = []
# k2 = []
# v2 = []
# for i in range(0, len(l1)):
#     s = str(l1[i])
#     kk1, vv1 = s.split(":")
#     k1.append(kk1)
#     v1.append(vv1)
# for i in range(0, len(l2)):
#     s = str(l2[i])
#     kk2, vv2 = s.split(":")
#     k2.append(kk2)
#     v2.append(vv2)
# for i in range(0, len(k1)):
#     for j in range(0, len(k2)):
#         if k1[i] == k2[j]:
#             temp1 = int(v1[i])
#             temp2 = temp1 + int(v2[j])
#             v1[i] = temp2
#         if k2[j] not in k1:
#             k1.append(k2[j])
#             v1.append(int(v2[j]))
# for i in range(0, len(k1)):
#     v1[i] = int(v1[i])
#
# d1 = dict(zip(k1, v1))
# print(d1)


# # 73
# # 字典最大值与最小值
# x = input()
# l1 = x.split(",")
# k1 = []
# v1 = []
# for i in range(0, len(l1)):
#     s = str(l1[i])
#     kk1, vv1 = s.split(":")
#     k1.append(kk1)
#     vv1 = int(vv1)
#     v1.append(vv1)
# d1 = dict(zip(k1, v1))
# Max = v1[0]
# Min = v1[0]
# for i in d1.values():
#     if i > Max:
#         Max = i
#     if i < Min:
#         Min = i
# print(Max, Min, sep=" ")


# 74
# 生成字典嵌套字典
# # 1可用，不能过
# x = input()
# l1 = x.split()
# d0 = dict()
# d1 = dict()
# for i in range(0, len(l1)):
#     d1 = dict.fromkeys(l1[len(l1) - 1 - i], d0)
#     d0 = d1
#
# print(d1)
# # 可用可过
# from functools import reduce
#
# x = input()
# l1 = x.split()
# d1 = dict()
# reduce(lambda l1, b: l1.setdefault(b, dict()), l1, d1)
# print(d1)
# # 可用来换d1
# d2 = {}
# d2 = reduce(lambda x, y: {y: x}, reversed(l1), {})
# print(d2)


# # 75
# # 并集
# x = input()
# l1 = x.split()
# y = input()
# l2 = y.split()
# s1 = set(l1)
# s2 = set(l2)
# # s3 = s1.union(s2)
# s3 = s1 | s2
# l3 = list(s3)
# l3.sort(key=str)
# for i in range(0, len(l3)):
#     print(l3[i], end=' ')


# # 76
# # 对称差集
# x = input()
# l1 = x.split()
# y = input()
# l2 = y.split()
# s1 = set(l1)
# s2 = set(l2)
# s3 = s1.symmetric_difference(s2)
# l3 = list(s3)
# l3.sort(key=str)
# for i in range(0, len(l3)):
#     print(l3[i], end=" ")


# # 77
# # 交集
# x = input()
# l1 = x.split()
# y = input()
# l2 = y.split()
# s1 = set(l1)
# s2 = set(l2)
# s3 = s1.intersection(s2)
# l3 = list(s3)
# l3.sort(key=str)
# for i in range(0, len(l3)):
#     print(l3[i], end=" ")


# # 78
# # 生成字典1
# import math
#
# n = int(input())
# d1 = dict()
# for i in range(1, n + 1):
#     d1[i] = int(math.pow(i, 2))
# print(d1)


# # 79
# # 字典排序
# d1 = dict()
# while True:
#     x = input()
#     if x == "":
#         break
#     l = x.split()
#     d1[l[0]] = l[1]
# d2 = sorted(d1.items(), key=lambda x: x[1], reverse=False)
# print(d2)
# d2 = sorted(d1.items(), key=lambda x: x[0], reverse=True)
# print(d2)


# # 80
# # 生成字典2
# x = input()
# l1 = x.split()
# y = input()
# v1 = y.split()
# d1 = dict(zip(l1, v1))
# print(d1)
