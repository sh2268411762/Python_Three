import math


# 例 6-7
def circle(r):
    if r <= 0:
        return -1, -1
    area = math.pi * math.pow(r, 2)
    perimeter = 2 * math.pi * r
    return area, perimeter


print(circle(3))
cr, cp = circle(4)
print("半径为4的圆的面积为：", cr)
print("半径为4的圆的周长为：", cp)
cr, cp = circle(-1)
print("半径为4的圆的面积为：", cr)
print("半径为4的圆的周长为：", cp)
print("如果某个函数没有返回语句，则系统自动插入return None语句，返回None")
