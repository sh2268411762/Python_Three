import re
import random
import string

print("大多数字母和字符一般都会和自身匹配，如果在字符串前面加了r，表示对字符串不进行转义"
      "。有些字符比较特殊，它们和自身并不匹配，而是表明应该和一些特殊的东西匹配，或者会影响重复次数，这些特殊的字符称之为元字符")

print("re模块中的findall()方法以列表的形式返回所有能匹配的子串，如果没有找到匹配的，则返回空列表：")
s = r'aab'
print("无匹配：", re.findall(s, 'aasasasassa'))
print("三处匹配：", re.findall(s, 'sssssaabaabaab'))
s = r'\n'
print(re.findall(s, r'\nHi\n'))
print(re.findall(s, '\nHi\n'))


print(" . 表示除换行符以外的任意字符， \S 表示不是空白的任意字符")
s = r'hi,i am a student.my name is Hilton.'
print("匹配所有的i:", re.findall(r'i', s))
print("匹配 .    ：", re.findall(r'.', s))
print("匹配i后面跟着除换行符以外的任意字符的形式：", re.findall(r'i.', s))
print("匹配i后面跟着不是空白符的任意字符的形式  ：", re.findall(r'i\S', s))


print("[]指定字符集：")
print("[0-9][a-z][A-Z]用来指定一个字符集")
print("在[]中元字符不起作用,如[m.]中 。不起作用")
print("中括号内^表示补集，即匹配不在区间范围内的字符")
s = 'map mit mee mwt meqwt'
print(re.findall(r'me', s))
print("匹配m后面跟i或w再跟t形式：", re.findall(r'm[iw]t', s))
print("元字符放在[]中，不起作用：", re.findall(r'm[.]', s))
s = '0x12x3x567x8xy'
print(re.findall(r'x[0-9]x', s))
print("x后面跟不为3的字符再跟x：", re.findall(r'x[^3]x', s))


print("^匹配行首，匹配以^后面的字符开头的字符串：")
s = 'hello hello world hello Mary hello John'
print(re.findall(r'hello', s))
print(re.findall(r'^hello', s))
print(re.findall(r'world', s))
print(re.findall(r'^world', s))
print(re.findall(r'^he', s))


print("$匹配行尾，匹配以$之前的字符结束的字符串：")
s = 'hello hello world hello Mary hello John'
print(re.findall(r'hello$', s))
s = 'hello hello world hello Mary hello John hello'
print(re.findall(r'hello$', s))
s = 'map mit mee mwt meqwt$'
print("匹配ma，mi，mw结尾的字符串：", re.findall(r'm[aiw]$', s))
print("$在[]找那个作为普通字符：", re.findall(r'm[aiw$]', s))
print("$在[]找那个作为普通字符：", re.findall(r'm[aiw$]$', s))


print("\后面的可以加不同的字符以表示不同的特殊意义：")
print(r"\b表示匹配单词头或单词尾")
print(r"\B表示匹配非单词头或单词尾")
print(r"\d表示匹配任何十进制数：相当于[0-9]")
print(r"\D表示匹配任何非数字字符：相当于[^0-9]")
print(r"\s表示匹配任何空白字符：相当于[\t\n\r\f\v]")
print(r"\S表示匹配任何非空白字符：相当于[^\t\n\r\f\v]")
print(r"\w表示匹配任何字母、数字或下划线字符：相当于[a-zA-Z0-9]")
print(r"\W表示匹配任何非字母、数字和下划线字符：相当于[^a-zA-Z0-9]")
print(r"\\,\[ 用于取消所有的元字符")
print("这些特殊字符可以包含在[]中")


print(" * 匹配位于 * 之前的字符或子模式的0次或多次出现")
s = 'a ab abbbbb abbbbbxa'
print("a后面跟重复0次或多次的b：", re.findall(r'ab*', s))


print(" + 匹配位于 + 之前的字符或子模式的一次或多次出现")
print("a后面跟重复1次或多次的b：",re.findall(r'ab+', s))


print(" ? 匹配位于 ? 之前的0个或1个字符")
print("当 ? 紧随其他限定符（*、+{n}，{n，}，{n，m}）之后时，匹配模式是“非贪心的”")
print("非贪心模式匹配搜索到尽可能短的字符串，而默认“贪心的”模式匹配搜索到的尽可能长的字符串")
print("最大模式，贪心模式  ：", re.findall(r'ab+', s))
print("最小模式，非贪心模式：", re.findall(r'ab+?', s))


print("{m,n}表示至少有m个重复，至多有n个重复。m和n都为十进制数：")


# 例5-14
s = 'hi,i am a student .my name is Hilton'
print("贪心  ：", re.findall(r'i.*e', s))
print("非贪心：", re.findall(r'i.*?e', s))



# 例5-15
l = []
x = string.ascii_letters + string.digits + "_.#%"
for i in range(10):  # 产生10个
      y = [random.choice(x) for i in range(random.randint(1, 25))]  # 随机放入1-25个元素
      l.append(''.join(y))
print("列表：", l)
print("满足要求的表达式：")
s = r'^[a-zA-Z]{1}[a-zA-Z0-9._]{4,19}$'
for i in l:
      if re.findall(s, i):
            print(i)

