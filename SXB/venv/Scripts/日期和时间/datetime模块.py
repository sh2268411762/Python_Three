import datetime
import time

# date对象
# date = datetime.date(2020,10,19)
# print(date)

# today = datetime.date.today()
# print(today)

# t1 = datetime.date.today()
# t2 = t1.weekday()
# t3 = t1.isoweekday()
# print(t2)
# print(t3)

# date = datetime.date(2018,7,2)
# print(date.isoformat())

# date = datetime.date(2020, 10, 19)
# print(date.strftime("%Y-%m-%d"))
# print(date.strftime("%y,%b-%d"))


# time对象
# time1 = datetime.time()
# time2 = datetime.time(hour=9, minute=59, second=59)
# print(time1)
# print(time2)

# print(datetime.time.min)
# print(datetime.time.max)

# time3 = datetime.time(hour=10,second=45)
# print(time3.isoformat())

# time4 = datetime.time(hour=10,minute=4,second=6)
# print(time4.strftime("%H:%M:%S"))
# print(time4.strftime("%p %I:%M:%S:%f"))


# # datetime对象
# dt = datetime.datetime(year=2020,month=10,day=19,hour=10,minute=6,second=44)
# print(dt)

# today = datetime.datetime.today()
# print(today)
# today = datetime.datetime.now()
# print(today)
# today = datetime.datetime.utcnow()
# print(today)

# time5 = datetime.datetime.fromtimestamp(time.time() - 86000)
# print(time5)

# now = datetime.datetime.now()
# print(now.date())
# print(now.time())

# date = datetime.date(1999,8,27)
# time = datetime.time(6,6,6)
# dt = datetime.datetime.combine(date,time)
# print(dt)
# print(dt.strftime("%Y-%m-%d %H:%M:%S"))
# print(dt.strftime("%y-%m-%d %a %I:%M:%S"))



# timedelta对象
# dt1 = datetime.datetime(2020, 10, 19)
# dt2 = dt1 + datetime.timedelta(days=-14)
# print(dt1)
# print(dt2)
# print(dt1 - dt2)
# print(dt2 - dt1)



# # tzinfo对象
# u1_now = datetime.datetime.now(datetime.timezone.utc)
# u2_now = datetime.datetime.utcnow()
# print(u1_now)
# print(u2_now)
#
# china_timezone = datetime.timezone(datetime.timedelta(hours=10))
# utc_timezone = datetime.timezone(datetime.timedelta(hours=0))
# china_time = datetime.datetime.now(china_timezone)
# utc_time = datetime.datetime.now(utc_timezone)
#
# print(china_time)
# print(utc_time)
