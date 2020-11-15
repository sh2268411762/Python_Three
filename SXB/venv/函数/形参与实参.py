# 例 6-5
def fdiv(x, y):
    if x < y:
        x, y = y, x
    r = x % y
    while r != 0:
        x, y = y, r
        r = x % y
    return y


print("25和45的最大公约数为 ", fdiv(25, 45))
m, n = 36, 24
print(m, "和", n, "的最大公约数为 ", fdiv(m, n), sep="")


# 例6-6
def future_value(money, year_Rate, year):
    month_Rate = year_Rate / 12  # 月回报率
    ret = money * (1 + month_Rate) ** (year * 12)
    return ret


money = 1000
year_Rate = float(input("请输入年回报率："))
year_Rate = year_Rate / 100
print("年份", "投资的未来价值")
for i in range(1, 11):
    x = future_value(money, year_Rate, i)
    print("%2d" % i, "%10.2f" % x)
