
##!/usr/bin/env python3
## _*_ coding:utf-8 _*_

#x = True
#if x:
#    print("It's True")

#x = False
#if x:
#    print("It's False")
##无法输出，x为False，无法执行if语句

#x = 18
#if x:
#    print("x is",x)

#x = 0
#if x:
#    print("x is",x)
##不输出


#x = "HELLo"
#if x:
#    print("x is",x)

#x = ""
#if x:
#    print("x is")
##不输出

#x1 = []
#x2 = [1,2]
#if x1:
#    print("x1")#不输出

#if x2:
#    print("x2")


#x3 =()
#x4 =(15,3)
#if x3:
#    print("x3")#不输出

#if x4:
#    print("x4")


#x5 = {}
#x6 = {"HELLO","二球"}
#if x5:
#    print("x5")

#if x6:
#    print("x6")


#x = 0
#if x:
#    print("x不是0")
#else:
#    print("x是0")


#x = 49
#if x>90:
#    print("优")
#elif x>80:
#    print("良")
#elif x>60:
#    print("及格")
#else:
#    print("不及格")

#x = 1
#while x<=10:
#    print(x)
#    x += 1#不能省略，否则死循环



#for x in (1,2,3,4,5,6,7,8,9,10):
#    print(x)

#for x in (0,1,2):
#    print("Hello World!")

#for x in range(10):
#    print(x)
#print("\n")

#for x in range(1,10):
#    print(x)
#print("\n")

#for x in range(1,10,2):
#    print(x)
#print("\n")

#for i in range(10):
#    if i > 5:
#        break
#    print(i)
#print("\n")

#for i in range(10):
#    if i == 5:
#        continue
#    print(i)
#print("\n")


##pass语句
#for i in range(10):
#    if i == 3:
#        pass
#    else:
#        print(i)
#print("\n")

#count = 0
#while count < 5:
#    print(count,"is less than 5")
#    if count == 3:
#        break#不执行else语句
#    count = count + 1
#else:
#    print(count,"is no less than 5")


for count in range(5):
    print(count,"in for segment")
    if 3 == count:
        break
else:
    print(count + 1,"int else segment")

