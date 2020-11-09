# str与bytes类型转换
print("字符串编码")
str1 = "我"
print("str1的类型为", type(str1))

str2 = str1.encode('gbk')
print("将str1转换为bytes类型，gbk编码格式 ：", str2)
print("str2的类型为", type(str2))

str3 = str1.encode('utf-8')
print("将str1转换为bytes类型，utf-8编码格式：", str3)
print("str3的类型为", type(str3))

str4 = str2.decode('gbk')
print("使用gbk进行解码：", str4)

str5 = str3.decode('utf-8')
print("使用utf-8进行解码：", str5)

print("中文字符不可以使用ASCII编码，英文可以")
# str6 = str1.encode('ascii')错误
str6 = 'ABC'.encode('ascii')
print(str6)

str7 = '浮世三千，吾爱有三'
print("str7的类型为", type(str7))

str8 = bytes(str7, encoding='gbk')
print(str8)
print("str8的类型为", type(str8))

str9 = bytes(str7, encoding='utf-8')
print(str9)
print("str9的类型为", type(str9))

str10 = str(str8, encoding='gbk')
print(str10)
print("str10的类型为", type(str10))

str11 = str(str9, encoding='utf-8')
print(str11)
print("str11的类型为", type(str11))

import sys

print("Python3.x完全支持中文字符，解析器默认采用UTF-8解析源程序，无论是数字字符、英文字母或汉字都按一个字符来对待和处理")
print(sys.getdefaultencoding())
s1 = '一二三'
print(len(s1))
s2 = 'iiiij 一二三 uuu'
print(len(s2))
一二 = 12
print(一二)
print("Python3.x中支持用中文作为标识符")

print("字符串构造")
print("使用单引号或双引号构造字符串必须成对出现：")
print("如果代码中包含了单引号且未使用转义字符则字符串必须用双引号构造，反之亦然")
print("c:\test\net")
print("在字符串前加上r或R表示原始字符串，所有的字符都是原始的本义而不会被转化：", r"c:\test\net")
print("使用\\\\表示反斜杠让t和n不形成转义：", "c:\\test\\net")
print("三重引号字符串：保留所有字符串的格式信息，可以跨越多行，行与行之间的回车符等都会被保存:")
print('''"11111
22222
33333"''')

# 例5-1
print("单引号：  ", 'Let\'s say:"Hello World!"')
print("双引号：  ", "Let's say:\"Hello World!\"")
print("三重引号：", '''Let's say:"Hello World!"''')

print("字符串格式化（分为格式和格式化）：")
print("格式：以%开头")
print("格式化运算符用%表示用对象代替格式化字符串中的格式，最终得到一个字符串")

print("最小宽度和精度：")
print("最小宽度是转换后的值所保留的最小字符个数（如果不足则左边补空格）：")
print("精度是结果中应该包含的小数位数：")
a = 3.1416
print('%6.2f' % a)
print("单独的%%f默认保留6位小数：%f" % 3.1415)
print("指定保留2位小数：%.2f" % 3.1416)
print("7位宽度，保留两位小数，空位补空格：%7.2f" % 3.1416)
print("7位宽度，保留两位小数，空位补0  ：%07.2f" % 3.1416)
print("7位宽度，保留两位小数，正数加正号，空位补0  ：%+07.2f" % 3.1416)
print("7位宽度，保留两位小数，左对齐输出，空位补空格  ：%-7.2f" % 3.1416)

print("进位制和科学计数法：")
print("把一个数转换成不同的进制位，也可按科学计数法进行转换：")
a = 123456
print("转换为八进制串：%o" % a)
print("转换为八进制串（前面加0o）：%#o" % a)
print("转换为十六进制串：%x" % a)
print("转换为十六进制串（前面加0x）：%#x" % a)
print("转换为科学计数法传，基底e:%e" % a)

# 5-2 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %-4d" % (i, j, i * j), end=" ")
    print()

print("format（）方法格式化字符串：")
print("format()方法是通过用{}和：来代替传统%方式：")
print("我叫{},今年{}岁".format('张三', 34))
print("我叫{0},今年{1}岁".format('张三', 34))
print("我叫{1},今年{0}岁".format(34, '张三'))
l = ['张三', 34]
print("我叫{},今年{}岁".format(*l))
print("我叫{0[0]},今年{0[1]}岁".format(l))

print("{0:.2f}".format(2 / 3))
print("{0:b}".format(8))  # 二进制
print("{0:o}".format(8))  # 八进制
print("{0:x}".format(18))  # 十六进制
print("{0:#x}".format(18))  # 十六进制加0x
print("{0:,}".format(123456789))  # 千分位用，分隔
print("{0:*>10}".format(18))  # 右对齐
print("{0:&>10}".format(18))  # 右对齐
print("{0:*<10}".format(18))  # 左对齐
print("{0:&<10}".format(18))  # 左对齐
print("{0:*^10}".format(18))  # 居中对齐
print("{0:&^10}".format(18))  # 居中对齐
print("{0:*=10}".format(-18))  # 将填充字符放在符号与数字之间

print("Formatted String Literals格式化字符串")
name = "张三"
age = 18
print(f"我叫{name},今年{age}岁")

print("字符串截取：")
import this

lists = ["Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.",
         "Complex is better than complicated."]
d1 = int(input("第一个位置："))
d2 = int(input("第二个位置："))
for s in lists:
    print("字符串:%s,长度为%d,子串为%s" % (s, len(s), s[d1 - 1: d2]))
    print("字符串：{}，长度为{}，子串为{}".format(s, len(s), s[d1 - 1:d2]))

print("字符串常用内置函数：")
s = 'qwertyuiop asdfghjkl'
print("len()表示字符串长度            ：", len(s))
print("max()表示字符串最大字符        ：", max(s))
print("min()表示字符串最小字符        ：", min(s))
print("ords()表示获取该字符的Unicode码：", ord('M'))
print("chr()表示将编码转换为对应字符   ：", chr(77))
print(ord('好'))
print(chr(22909))

# 例5-4
songs = ["优美旅程", "Fantasy", "406", "IRAKIRA梦"]
for s in songs:
    print("%s:" % s)
    for i in s:
        print(i, "->", ord(i), end=" ")
    print()

for s in songs:
    print(s)
    for i in s:
        print("字符%c的Unicode编码为%d" % (i, ord(i)))
    print()

print("只显示歌曲名字符串下标为奇数：")
for s in songs:
    print(s)
    for i in range(len(s)):
        if i % 2 != 0:
            print("字符%c的Unicode编码为%d" % (s[i], ord(s[i])))
    print()

# 例5-5
s = input("请输入一个字符串：")
c1, c2, c3, c4 = 0, 0, 0, 0  # c1大写字母，c2小写字母，c3数字，c4其他
for i in s:
    if 'A' < i < 'Z':
        c1 += 1
    elif 'a' < i < 'z':
        c2 += 1
    elif "0:" < i < "9":
        c3 += 1
    else:
        c4 += 1
print("大写字母为%d个" % c1)
print("小写字母为%d个" % c2)
print("数字为%d个   " % c3)
print("其他字母为%d个" % c4)

print("大写字母为{0}个：小写字母为{1}个：数字为{2}个：其他字母为{3}个：".format(c1, c2, c3, c4))

print(f"大写字母为{c1}个：小写字母为{c2}个：数字为{c3}个：其他字母为{c4}个：")
