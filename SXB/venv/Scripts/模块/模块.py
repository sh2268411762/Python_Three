import fibs
import sys
import os
import math
import random

print("模块导入", fibs)
print("__name__变量可用来访问模块的模块名", fibs.__name__)
print("当前模块名：", __name__)
print("dir函数可以列出对象的模块标识符：", dir(fibs))
print("如果不提供参数，它返回当前模块中定义的名称列表：", dir())
print("使用模块：")
fibs.fib(6)
ret2 = fibs.fib2(6)
print(ret2)

# sys
print("识别操作系统：", sys.platform)
print("处理命令行参数：", sys.argv)
# if len(sys.argv) <= 1:
#     print("缺少参数，程序退出：")
#     sys.exit(1)
print("path存储了python结束其需要搜索的所有路径：")
for path in sys.path:
    print(path)
print("查找已导入的模块：")
print(sys.modules.keys)
print(sys.modules.values())
print(sys.modules["os"])

# os
print("获取当前文件所在目录：")
print("Python内置变量：", __file__)
print("当前文件的位置：", os.path.dirname(__file__))
print("获取当前路径以及切换当前路径：")
print("获取当前执行程序的路径：", os.getcwd())
print("切换当前路径（os.chdir）：")
os.chdir("c:\\")
print("获取当前执行程序的路径：", os.getcwd())
print("重命名文件（os.rename）:")
print("查看指定的路径是否存在：", os.path.exists("c:\Windows"))
print("判断给出的路径是否是一个文件：", os.path.isfile("c:\\aow_drv.log"))
print("判断给出的路径是否是一个目录：", os.path.isdir("c:\\$WinREAgent"))
print("获取系统环境变量：")
for k, v in os.environ.items():
    print(k, "=>", v)
# print("创建单层目录：", os.mkdir("d:\\test"))
# print("创建多层目录：", os.makedirs("d:\\test1\\test2\\test3"))


# math
print("math库中的常量：圆周率PI = ", math.pi, "，自然对数e = ", math.e)
print("math库中的运算函数：")
print("向上取整（ceil） ：1.7 -> ", math.ceil(1.7), "      -1.7 -> ", math.ceil(-1.7))
print("向下取整（floor）：1.7 -> ", math.floor(1.7), "      -1.7 -> ", math.floor(-1.7))
print("指数运算（pow）：15^3 = ", math.pow(15, 3), "\t29^-1 = ", math.pow(29, -1))
print("对数运算（默认底数为e，可用第二个参数改变底数）：log(math.e) = ", math.log(math.e), "log(100,10) = ", math.log(100, 10))
print("平方根计算（sqrt）：sqrt(4) = ", math.sqrt(4), "\tsqrt(100)", math.sqrt(100))
print("三角函数：sin(pi/2) = ", math.sin(math.pi / 2), "\tcos(pi) = ", math.cos(math.pi), "\ttan(0) = ", math.tan(0))
print("弧度转角度：", math.degrees(math.pi), "\t角度转弧度：", math.radians(90))

# random  随机数
print("random.random用于生成一个随机数（0<=n<1.0）：", random.random(), random.random())
print("random.uniform用于生成一个指定范围的随机数（1,150）：", random.uniform(1, 150))
print("random.uniform用于生成一个指定范围的随机整数（1,150）：", random.randint(1, 150))
s1 = [1, 2, 3, 4, 5, 6, 7, 8]
s2 = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
print("random.choice用于从指定序列中随机获取一个元素：", random.choice(s1), random.choice(s2))
print("random.shuffle用于打乱一个序列，不能为元组：")
print("打乱前：")
print(s1, "\n", s2)
random.shuffle(s1)
random.shuffle(s2)
print("打乱后：")
print(s1, "\n", s2)
