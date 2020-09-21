import math
#1
f = float(input("请输入要转换的华氏温度："))
c = (f - 32) * 5 / 9
print("华氏温度为：%.2f，则摄氏温度为：%.2f" % (f, c))
print("华氏温度为", f, ",摄氏温度为", round(c,2))

#2
b = input("请输入矩形的长和宽：")
l, k = map(float, b.split())
s = l * k
print("长为：%.2f宽为：%.2f的矩形面积为：%.2f" % (l, k, s))
print("矩形面积为：", round(s, 2))

#3
l = input("请输入三个学生的成绩：")
l1, l2, l3 = map(float, l.split())
n = l1 + l2 + l3
i = float(n / 3)
print("三个学生的成绩平均值为：%.2f" % i)
print("三个学生的成绩平均值为：", round(i, 2))

#4
l = input("请输入三门课的成绩：")
c, m, e = map(float, l.split())
if (c in range(60, 101) and m in range(60, 101) and e in range(60, 101)):
    print("三门课程都及格")
if (c in range(60, 101) or m in range(60, 101) or e in range(60, 101)):
    print("至少一门课程及格")
if (c in range(60, 101) and (m in range(60, 101) or e in range(60, 101))):
    print("语文及格且数学或者英语及格")

#6
ll = input("请输入月利率：")
l2 = ll
l2 = float(l2)
l2 = 1 + l2
x = 50000 / pow(l2, 120)
print("月利率为：" + str(ll) + "投资金额为：%.2f" %x + "时，孩子可以在10周岁时取回50000")
