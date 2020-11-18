# 二进制文件的写入
print("二进制文件的写入有两种常用的方法：一种是通过struct.Struct对象的pack方法将数据转换成二进制的字节串，然后用write方法写入文件"
      "。\n另一种方法是用pickle模块的dump方法将数据转换为二进制的字节串并直接写入文件")
print("方法一：1、导入struct包 2、创建struct.Struct对象 3、利用struct.Struct对象的pack方法将数据转换为二进制的字节串 4、将二进制的字节串写入准备好的文件对象")
# 例 7-1
import struct

values = (9, b'abc', 5.6, True)
s = struct.Struct('I3sf?')
packed_data = s.pack(*values)
f = open("d://git Code//Python_Three//Sxb//venv//文件操作二进制1.dat", 'wb')
f.write(packed_data)
f.close()

print("方法二：")
# 例 7-2
import pickle

s = '一二三四'
l = [1, 2, '五六七八', 4.5]
d = {1: 10, 2: 20}
x = 8
y = 8.8
f = open("d://git Code//Python_Three//Sxb//venv//文件操作二进制2.dat", 'ab+')
pickle.dump(s, f)
pickle.dump(l, f)
pickle.dump(d, f)
pickle.dump(x, f)
pickle.dump(y, f)
f.close()

# 二进制文件的读取
print("根据写入的方法，二进制的读取也有两种常用方法：")
print("方法一：针对通过struct.Struct对象的pack方法将数据转换为二进制的字节串，然后用write写入的方法，\n"
      "首先打开文件，读取文件内容，然后利用struct.unpack将字节串转换为原对象：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作二进制1.dat", 'rb')
s = f.read()
t = struct.unpack('I3sf?', s)
print(t)
for i in t:
    print(i)
f.close()

print("方法二：利用pickle.load每次读取一个对象的内容，并自动转换为相应的对象：")
f = open("d://git Code//Python_Three//Sxb//venv//文件操作二进制2.dat", 'rb')
try:
    while True:
        x = pickle.load(f)
        print(x)
except EOFError:
    print("读取完毕")
f.close()
