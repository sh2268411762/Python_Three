# input()函数无论输入什么内容，该函数都会返回字符串类型，自动忽略换行符
# x = input("请输入x的值：")
# print(x)
# print(type(x))

# int()函数
# 1 int([x])：截取数字的整数部分或将字符串转换成一个整数，不给定参数则返回0
import math

print(int())
print(int(23.44))
print(int(-7.99))
print(int('44'))
print(int('-77'))
# 不接受带小数的数字字符串
# 2 int(x,base=10)：把base进制的字符串x转换成十进制，base为可选的基数，默认为10（base为0和2——36）
print(int('1001001', 2))
print(int('2ef', 16))
print(int('27', 8))
print(int('0b110', base=0))
print(int('110', base=2))
print(int('110', 2))

# float()：将一个数字或字符串转换成浮点数
print(float(5))
print(float(5.99))
print(float('5'))
print(float('5.99'))
print(float('inf'))  # 无穷大，INF不区分大小写

# eval(source,globals = None,locals = None,/)函数：将source当做一个Python表达式进行解析和计算，返回计算结果
x = 3
print(eval('x+1'))
print(eval('3+8'))
print(eval('[1,2,3,4]'))
print(eval('(1,2,3)'))
print(eval('{1:23,2:32}'))
print(eval("__import__('os').getcwd()"))
m = input("请输入z，y值：")
m.split()
z, y = map(str, m.split())
print(z)
print(y)

num = input("请输入股票代码：")
name = input("请输入股票名称：")
highest = float(input("请输入当天最高价："))
lower = float(input("请输入当天最低价："))
diff = highest - lower  # 差值
print("股票代码 + 股票名称：", num, name)
print("最高价：", highest, " 最低价：", lower, " 差值：", diff)

print("用 ，分隔")
nn = input("请输入股票代码和名称：")
num, name = map(str, nn.split(','))
hl = input("请输入当天最高价和最低价：")
highest, lower = map(float, hl.split(','))
diff = highest - lower
print("股票代码 + 股票名称：", num, name)
print("最高价：%.2f, 最低价：%.2f, 差值：%.2f:" % (highest, lower, diff))


#复数
a = input("请输入复数的实部：")
b = input("请输入复数的虚部：")
c = math.sqrt(float(a) ** 2 + float(b) ** 2)
print("输入的复数为：" + a + "+" + b + "j", "模为：" + str(c))
x = input("请输入复数的实部和虚部：")
a, b = map(float, x.split())
c = math.sqrt(a ** 2 + b ** 2)
print("输入的复数为：" + str(a) + "+" + str(b) + "j", "模为：" + str(c))
x = input("请输入复数的实部和虚部：")
a, b = map(float, x.split())
m = complex(a, b)
c = abs(m)
print("输入的复数为：" + str(m), " 模为：" + str(c))

