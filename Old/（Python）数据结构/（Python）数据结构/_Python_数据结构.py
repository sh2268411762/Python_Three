#!/usr/bin/env python3
#-*- coding:utf-8 -*-


print("序列的索引下标可以超出真实的索引长度")
# 列表
x1 = [1,2,3,4]
print("列表")
print(x1 [0])
print(x1 [1])
print(x1 [-1])
print(x1 [-2])
print(x1 [0:3])
print(x1 [2:3])
print(x1 [-3:3])
print(x1 [3:100])
print(x1 [3:])
print(x1 [:3])
print(x1 [:])
print("\n")

print("----------------")
# 元组
x2 = (1,2,3,4)
print("元组")
print(x2 [0])
print(x2 [1])
print(x2 [-1])
print(x2 [-2])
print(x2 [0:3])
print(x2 [2:3])
print(x2 [-3:3])
print(x2 [3:100])
print(x2 [3:])
print(x2 [:3])
print(x2 [:])
print("\n")

print("----------------")
# 字符串
x3 = "1234"
print("字符串")
print(x3 [0:3])
print(x3 [2:3])
print(x3 [-3:3])
print(x3 [3:100])
print(x3 [3:])
print(x3 [:3])
print(x3 [:])
print("\n")


# 列表
xx1 = [1,2,3,4,5,6,7]
print("列表")
print(xx1 [1:5])
print(xx1 [1:5:1])
print(xx1 [1::2])
print(xx1 [1::3])
print(xx1 [5::-1])
print(xx1 [5::-2])
print("\n")

print("----------------")
# 元组
xx2 = (1,2,3,4,5,6,7)
print("元组")
print(xx2 [1:5])
print(xx2 [1:5:1])
print(xx2 [1::2])
print(xx2 [1::3])
print(xx2 [5::-1])
print(xx2 [5::-2])
print("\n")

print("----------------")
# 字符串
xx3 = "1234567"
print("字符串")
print(xx3 [1:5])
print(xx3 [1:5:1])
print(xx3 [1::2])
print(xx3 [1::3])
print(xx3 [5::-1])
print(xx3 [5::-2])
print("\n")

