# # 51
# # IPV4地址
# while True:
#     x = input()
#     if x == "":
#         break
#     else:
#         x1, x2, x3, x4 = map(int, x.split("."))
#         if x1 in range(1, 256) and x2 in range(0, 256) and x3 in range(0, 256) and x4 in range(0, 256):
#             print("True")
#         else:
#             print("False")


# # 52
# # 合法的日期格式
# import time
#
# while True:
#     x = input()
#     if x == "":
#         break
#     else:
#         try:
#             flag = False
#             if "-" in x:
#                 time.strptime(x,"%Y-%m-%d")
#                 flag = True
#                 print(flag)
#             elif "." in x:
#                 time.strptime(x,"%Y.%m.%d")
#                 flag = True
#                 print(flag)
#             elif "/" in x:
#                 time.strptime(x,"%Y/%m/%d")
#                 flag = True
#                 print(flag)
#             else:
#                 print(flag)
#         except:
#             flag = False
#             print(flag)


# # 53
# # 分词与副词
# while True:
#     x = input()
#     if x == "":
#         break
#     if len(x) < 3:
#         print(x)
#     else:
#         if x[-3:] == "ing":
#             l = x + "ly"
#         else:
#             l = x + "ing"
#         print(l)


# # 54
# # 公式计算
# l1 = input()
# l2 = input()
#
# x, y, z = map(int, l2.split())
# print(l1, "=", eval(l1), sep="")


# # 55
# # 合法的电话号码
# while True:
#     num = input()
#     if num == "":
#         break
#     l = ['13', '14', '15', '18', '17', '19']
#     flag = False
#     if num[:2] in l and len(num) == 11:
#         flag = True
#     else:
#         flag = False
#     print(flag)


# # 56
# # 交换逗号和小数点
# x = input()
# l = [',', '.']
# count1 = 0
# count2 = 0
# ll = []
# for i in range(0, len(x)):
#     if x[i] == l[0]:
#         count1 += 1
#     if x[i] == l[1]:
#         count2 += 1
#     ll.append(x[i])
#
# if l[0] in ll and l[1] in ll and count1 == count2:
#     for i in range(0, len(ll)):
#         if ll[i] == l[0]:
#             ll[i] = l[1]
#         elif ll[i] == l[1]:
#             ll[i] = l[0]
# x = "".join(ll)   # join只接收str类型参数，不能传数字
# print(x)


# # 57
# # 同义词
# import re
#
# while True:
#     x = input()
#     if x == '':
#         break
#     pattern = re.compile(r'not *[a-z]* *poor')
#     x1 = pattern.sub('good', x)
#     print(x1)


# # 58
# # 提取字符串
# while True:
#     x = input()
#     if x == "":
#         break
#     if len(x) < 2:
#         print(x)
#     else:
#         y = x[0:2] + x[-2:]
#         print(y)


# # 59
# # 删除字符
# while True:
#     x = input()
#     if x == "":
#         break
#     l1 = []
#     for i in range(0, len(x)):
#         l1.append(x[i])
#     l2 = []
#     for i in range(0,len(l1)):
#         if i % 2 == 0:
#             l2.append(l1[i])
#     s = "".join(l2)
#     print(s)


# # 60
# # 单词
# x = input()
# l = x.split()
# l.sort(key=len)
# print(l[0])
# print(l[-1])
