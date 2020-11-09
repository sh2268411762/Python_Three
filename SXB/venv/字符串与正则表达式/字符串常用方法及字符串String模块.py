print("字符串常用方法：")
print("由于字符串是不可变序列，常用方法中涉及返回字符串的都是新字符串，原字符串对象不变")

print("参数部分：width->指定宽度\tfillchar->以这个字符填充，默认为空格：")
print("center()居中对齐，ljust()右对齐，rjust()左对齐：")
print("功能：返回一个宽度为width的新字符串，原字符串各种对齐出现在新字符串中，如果width大于原字符串长度，则使用fillchar填充：")
print('张三'.center(10))  # 居中对齐，以空格填充
print('张三'.center(10, '*'))  # 居中对齐，以*填充
print('张三'.ljust(10, '!'))  # 右对齐，以！填充
print('张三'.rjust(10, '-'))  # 左对齐，以-填充

# 例5-6
# 9 9 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0} * {1} = {2}".format(i, j, i * j).ljust(8), end="\t")
    print()

print("lower()方法用于将大写字母转换为小写字母，其他字符不变，返回新字符串")
print("upper()方法用于将小写字母转换为大写字母，其他字符不变，返回新字符串")
s = 'ssssYUIOJshydkk***hsss9877uuIo'
print(s)
print("大->小     ：", s.lower())
print("原字符串不变：", s)
print("小->大     ：", s.upper())
s1 = s.lower()
print(s1)
s1 = s.upper()
print(s1)

# 例5 - 7
names = ["风云Th", "Brown", "飘然12345", "云S", "thomas", "青山依旧QSYJ"]
name = input("请输入用户名：")
for i in names:
    if name.lower() == i.lower():
        print("找到了")
        break
else:
    print("未找到")



print("capitalize()方法将字符串首字母转换为大写，其余字母转换为小写")
print("title()方法将单词首字母转换为大写，其余字母转换为小写")
print("swapcase()方法将字符串大小写互换")
print("上述三个方法均返回新字符串，不对原字符串产生影响：")
s = 'merry days will cOme,beLieve'
print("原字符串", s)
print("s.capitalize:", s.capitalize())
print("原字符串不变：", s)
print("s.title()   :", s.title())
print("s.swapcase():", s.swapcase())

print("islower()用于判断字符串是否为小写")
print("isupper()用于判断字符串是否为大写")
print("isdigit()用于判断字符串是否为数字")
s = 'oooooiiuu'
print(s.islower())
print(s.isupper())
print(s.isdigit())
print()
s = "SSSSS"
print(s.islower())
print(s.isupper())
print(s.isdigit())
print()
s = '1234'
print(s.islower())
print(s.isupper())
print(s.isdigit())
print()
s = '1234.6'
print(s.islower())
print(s.isupper())
print(s.isdigit())
print()
s = 'SSSjjj'
print(s.islower())
print(s.isupper())
print(s.isdigit())
print("浮点数和大小写都有则全False")

# 例 5-8
s = input("请输入一个字符串：")
c1, c2, c3, c4 = 0, 0, 0, 0
for i in s:
    if i.islower():
        c2 += 1
    elif i.isupper():
        c1 += 1
    elif i.isdigit():
        c3 += 1
    else:
        c4 += 1
print("大写字母{0}个，小写字母{1},数字{2}个，其他字符{3}个".format(c1, c2, c3, c4))


print("find()和rfind()方法用来查找sub子串是否在字符串内并返回其索引，若无该字符则返回-1：")
print("find()从左向右查看，rfind()从右向左查看：")
print("格式：S.find(sub,[,start[,end]]),S.rfind(sub,[,start[,end]])")
s = 'Heart is living in tomorrow'
print(s.find('Heart'))
print(s.find('is'))
print(s.find('heart'))
print("不存在则返回-1")
print(s.find('i'))
print(s.find('i', 7, 16))
print("从右边查看：")
print(s.rfind('i', 0, 16))


print("index()和rindex()方法与find和rfind方法类似，但这两个方法无法查询则抛出异常：")
try:
    s = 'Heart is living in tomorrow'
    print(s.index('Heart'))
    print(s.index('is'))
    print(s.index('heart'))
    print("不存在则返回-1")
    print(s.index('i'))
    print(s.index('i', 7, 16))
    print("从右边查看：")
    print(s.rindex('i', 0, 16))
except Exception as e:
    print(e)


print("count()方法用于统计一个子串在字符串内出现的次数，可指定前后索引，不存在则返回0：")
s = 'Heart is living in tomorrow'
print(s.count('i'))
print(s.count('i', 4, 10))
print(s.count('i', 7, 9999))


print("split()方法以指定字符为分隔符，从左往右将字符串分隔开来，并将分割后的结果组成列表返回：")
print("rsplit()从右向左分隔，两种方法均可指定最大分割次数：")
s = 'Heart is living in tomorrow'
l = s.split()                             # 通过空格分隔
print(l)
l = s.split(',')                          # 通过 , 分隔
print(l)
s = 'Heart\tis\nliving\tin\ttomorrow'     # 通过空白字符分隔
l = s.split()
print(l)


# 例 5-9
s = input("请输入最近几天的温度，用逗号分隔：")
l = s.split(',')
t = 0
ss = 0
for i in l:
    ss += float(i)
    t += 1
num = ss / t
print("最近几天的平均气温为：%.2f" % num)

c = list(map(float, l))
print("最近几天的平均气温为：%.2f" % (sum(c) / len(c)))


print("join()方法可用来连接序列中的元素，并在两个字符之间插入指定字符，返回一个字符串：")
s = 'Heart is living in tomorrow'
print('+'.join(s))   # 字符串中，每个字符为一个元素
s1 = ['Heart', 'is', 'living', 'in', 'tomorrow']
print('+'.join(s1))  # 列表中，每个字符串为一个元素
s2 = 'Heart', 'is', 'living', 'in', 'tomorrow'   # 元组
print(type(s2))
print(','.join(s2))


# 例5-10
s = input("请输入英文单词，用空格分隔：")
l = s.split()
f = [i.title() for i in l]
ss = ' '.join(f)
print("首字母大写：", ss)

ss = s.title()
print("首字母大写：", ss)


print("replace(old,new,count=-1)方法查找字符串中old子串并用new子串来替换。"
      "参数count默认为-1，表示替换所有匹配项，否则最多替换count次。返回替换后的新字符串")
s = 'Heart is living in tomorrow'
print("原字符串    :", s)
print("replace() :", s.replace('i', 'I'))
print("原字符串不变：", s)
s1 = '中国北京，北京地铁，地铁沿线，沿线城市'
s2 = s1.replace('北京', 'Beijing')  # 替换所有项
print(s2)
s3 = s1.replace('666', 'Beijing')
print("原字符串无666，则不替换：", s3)
s4 = s1.replace('北京', 'Beijing', 1)  # 指定最大替换次数为1
print(s4)


print("maketrans()方法用于生成字符映射表")
print("translate()方法用于根据字符映射表替换字符")
print("两种方法联合使用可以一次性替换多个字符")
t = ''.maketrans('iort', 'mn24')         # 两个序列中的元素按照次序一一对应于替换
s = 'Heart is living in tomorrow'
print(s.translate(t))


import random

l = []
i = 0
while i < 10:
    c = chr(random.randint(ord('a'), ord('z')))
    if c not in l:
        l.append(c)
        i += 1
t = ''.maketrans('abcdefg', '1234567')
print("原列表:", l)
s1 = ','.join(l)
s2 = s1.translate(t)
l2 = list(s2.split(','))
print("新列表：", l2)
for i in l2:
    print("%s" % i, end=' ')


print("strip()方法用于去除字符串两侧的空白字符或指定字符，并返回新的字符串")
s = "     Heart is living in tomorrow   \n\n"
print(s.strip())
s1 = "HHwHeart is living in tomorrowHww"
print(s1.strip('Hw'))  # 从两端去除H和w

print("去除字符串中的空格")
s = "Heart is living in tomorrow"
print(s)
print(s.replace(' ', ''))


import string

print("string模块：")
print("string模块定义了Formatter类，Template类，capwords函数和常量，可用来简化某些字符串的操作")

# 例5-12
print("capwords()函数把字符串中每一个英语单词首字母变为大写，其他字母变为小写，返回新字符串：")
s = input("请输入字符串：")
print("单词首字母大写：", string.capwords(s))

# 例5-13
l1 = []
i = 0
while i < 10:
    c = random.choice(string.ascii_lowercase)
    if c not in l1:
        i += 1
        l1.append(c)
print(l1)

print("choice()方法用来在一个非空的序列中随机选择一个元素")
print("ascii_lowercase是string模块中的常量（小写字母）：")
print(string.ascii_lowercase)
