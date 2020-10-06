import fibs
import sys

print("模块导入", fibs)
print("__name__变量可用来访问模块的模块名", fibs.__name__)
print("当前模块名：", __name__)
print("dir函数可以列出对象的模块标识符：", dir(fibs))
print("如果不提供参数，它返回当前模块中定义的名称列表：", dir())
print("使用模块：")
fibs.fib(6)
ret2 = fibs.fib2(6)
print(ret2)

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
