# 文件的打开与关闭
print("打开一个文件用open(name[,mode[,buffering]])函数，name为文件路径，mode参数提供文件打开方式，\nbuffering可控制文件读写时是否需要缓冲"
      "，若取0（或False）则无缓冲，直接将数据写入磁盘文件，若取1（或True）则有行缓冲，碰到换行就将数据写入磁盘，否则数据先不写入磁盘，除非使用"
      "flush()或close()方法强制将缓冲区内容写入磁盘，\n若取大于1的数，该数则为所取缓冲区中的字节数，若取负数，则表示使用默认缓冲区的大小\n"
      "如果不提供参数，则buffering默认为1，如果buffering的值大一1或负数，缓冲区不满时数据不会写入磁盘，直到缓冲区满"
      "或使用flush()方法或close()方法强制将缓冲区内容写入磁盘")

print(r"打开方式有三种：1、f = open(r'd:\test.txt')    2、f = open('d:\\test.txt')    3、f = open('d:/test.txt')")
print("Python中的文本对象有3种常用属性：closed属性用于判断文件是否关闭，若文件处于打开状态，则返回False。\n"
      "mode属性返回文件的打开模式。\n"
      "name属性返回文件的名称")
print("在文件读写完毕之后，要注意使用f.closed()方法关闭文件，把缓存区的数据写入磁盘，释放内存资源供其他持续使用")

# 文本文件的写入
print("以 w 模式打开文件(原文件内容被清空)：")
print("向文件写入数据用：write(),writelines()方法：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'w')
f.write('12345678\n')
f.write('abcdefgh\n')
l = ['defghighk\n', '45688888\n']
f.writelines(l)
f.close()  # 强制将缓冲区内的数据写入磁盘

# 文本文件的读取
print("以 r 模式打开文件(原文件内容被清空)：")
print("读取文件数据用：read(),readline(),readlines()方法：")
print("reda()方法中，不指定读取长度则将文件中全部字符作为一个字符串返回，若提供数字，则一次读取指定数量字节的字符"
      "\n若从当前光标位置到最后字符不足传入参数个，则返回所有字符")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
print(f.read(3))  # 光标移动3个字符
print(f.read(2))  # 光标移动2个字符
print(f.read())  # 剩余全部
f.close()
print()

f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
print("readline()方法中，若无参数则实现逐行读取文件，若传入参数，则返回一行中对应数量的字符，若数字大于这一行的字符数，则读取这一行的所有字符")
print(f.readline())  # 输出一行
print(f.readline(4))  # 输出一行中的4个字符
print(f.readline(6))  # 输出一行中的6个字符，不足6个则全部输出
f.close()
print()

f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
print("readlines()方法将一个文件中的所有行进行读取，并将其作为一个列表返回，每一行信息作为一个字符串元素")
print(f.readlines())
f.close()

print("替代readlines()方法：\n1、组合使用循环结构与readline()方法，逐行读取文本内容：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()

print("\n2、利用iter(文件对象)返回一个迭代器，降低对计算机内存的占用：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
for i in iter(f):
    print(i, end='')
f.close()

print("\n3、利用文件对象迭代功能，逐行读取信息：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
for i in f:
    print(i, end='')
f.close()

print("将迭代器转换为列表：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作.txt", 'r')
l = list(f)
print(l)
f.close()
