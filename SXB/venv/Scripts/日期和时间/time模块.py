import time

# print("\ntime函数用于返回当前时间的时间戳：")
# now = time.time()
# print("当前时间时间戳：", now)
#
# print("\nlocaltime函数用于将当前时间戳格式化为本地时间（返回time_struct对象）：")
# print("有参数即传入时间戳则进行格式化，否则默认使用当前时间戳：")
# print("当前时间：", time.localtime())
# print("当前时间now：", time.localtime(now))
# print("0时间戳对应的时间：", time.localtime(0))
# print("localtime函数返回值类型：", type(time.localtime()))
#
# print("\ngmtime函数将一个时间戳转换为UTC时区（0时区）的time_struct对象：")
# print("参数为时间戳，f否则默认使用当前时间戳：")
# print("当前时间：", time.gmtime())
# print("当前时间now：", time.gmtime(now))
# print("0时间戳对应的时间：", time.gmtime(0))
#
# print("\nmktime函数接收time_struct对象或结构化时间作为参数，返回用秒数来表示的浮点数：")
# t = (2020, 10, 11, 19, 36, 1, 1, 1, 0)
# secs = time.mktime(t)
# print("结构化时间：%f" % secs)
# print("time_struct：%f" % time.mktime(time.localtime(secs)))
#
# print("\nasctime函数接收时间元组并返回一个可读的24个字符的字符串：")
# print("参数为9个元素的元组或time_struct：")
# tt = (2018, 7, 18, 17, 3, 1, 1, 1, 0)
# print("9个元素的时间元组：", time.asctime((2018, 7, 18, 17, 3, 1, 1, 1, 0)))
# print("time_struct对象：", time.asctime(time.localtime()))
#
# print("\nctime函数能把一个时间戳转换为time.asctime()形式：")
# print("参数未给或为None则默认time.time()为参数：")
# print("当前时间：%s" % time.ctime())
# print("0：%s" % time.ctime(0))
#
# print("\nsleep函数推迟调用线程的运行（参数为秒数）：")
# print("Start:%s" % time.ctime())
# time.sleep(5)
# print("End  :%s" % time.ctime())
#
#
# def fun():
#     time.sleep(5)
#
#
# print("反对警告:时间.时钟在Python 3.3中已被反对，并将从Python 3.8中删除:请改用time.perf_counter或time.process_time")
# print("\nclock函数返回当前CPU时间，用来衡量不同程序的时间：")
# t0 = time.perf_counter()
# fun()
# print("时间差（函数）：", time.perf_counter() - t0)
# t0 = time.time()
# fun()
# print("时间差（时间）：", time.time() - t0)
#
# print("\nstrftime函数用于接收时间元组，并返回以可读字符串表示的当地时间：")
# t = (2020, 10, 11, 19, 36, 1, 1, 1, 0)
# t = time.mktime(t)
# print(time.strftime("%w %b %d %Y %H:%M:%S", time.localtime(t)))
#
# print("\nstrptime函数能够根据指定的格式把一个时间字符串解析为时间元组（time_struct）对象：")
# s = time.strptime("0 Oct 11 2020 19:36:01", "%w %b %d %Y %H:%M:%S")
# print(s)
