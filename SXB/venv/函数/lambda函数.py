print("lambda表达式又称匿名函数，可以接收任意多个参数，但只返回一个表达式的值，不能包含多个表达式")
print("lambda函数的定义格式：lambda 形参:表达式")
print("形参可以有多个，用逗号隔开，表达式只有一个，返回表达式的结果\n")

print("可以给lambda表达式命名：")
f = lambda x, y: x + y
print(f(5, 10))

print("lambda表达式通常以匿名方式出现：")
x = list(range(10))
print(x)
y = list(filter(lambda i: i % 2 == 0, x))
print(y)
