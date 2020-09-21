#if语句
x1 = []
x2 = [1,2]
if x1:
    print("x1")
if x2:
    print("x2")

x3 = ()
x4 = (1,2,3)
if x3:
    print("x3")
if x4:
    print("x4")

x5 = {}
x6 = {"孙豪","二球"}
if x5:
    print("x5")
if x6:
    print("x6")
#空列表，空元素，空字符串，空字典，0 ，None 都是“False”
x = 49
if x > 90:
    print("优秀")
elif x > 80:
    print("良好")
elif x > 60:
    print("及格")
else:
    print("不及格")

#while循环（可接else）
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("二球")

#for循环(可接else)
for x in range(10):
    print(x)
else:
    print("二球")
for x in range(1,10,2):
    print(x)
else:
    print("二球")
#break
for i in range(10):
    if i > 5:
        break
    print(i)
#continue
for i in range(10):
    if i == 5:
        continue
    print(i)
#pass语句：没有任何操作，用来保持程序结构的完整性，通常用来占位控制缩进
for i in range(10):
    if i == 3:
        pass
    else:
        print(i)
