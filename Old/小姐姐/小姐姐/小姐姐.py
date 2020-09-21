
#画图
import turtle as t
t.goto(100,0)
for i in range(50):
            t.left(160)
            t.fd(200)
            t.left(270)
            t.fd(210)

#风车
import turtle as t
t.goto(100,0)
for i in range(100):
            t.left(80)
            t.fd(100)
            t.left(135)
            t.fd(165)
            t.left(125)
            t.fd(115)

#彩色漩涡
import turtle
q = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors = ["red","orange","yellow","green","cyan","blue","purple"]
for x in range(360):
            q.pencolor(color[x%sides])
            q.forward(x*3/sides+x)
            q.left(360/sides+1)
            q.width(x*sides/200)


#猜数游戏
import random  #生成一个随机数
number = int(input("请输入一个0到9之间的数字"))
secret = random.randint(0,9)

if number == secret:
    print("恭喜，答对了\n")
else:
    print("抱歉，答错了\n")
    print("正确答案是：-->",secret)



#树
import turtle#导入模块

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)#前进banchLen长度
        t.right(20)#画笔右倾20度
        tree(branchLen-15,t)#调用自身
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)#回到原来位置
        
def main():
    t =turtle.Turtle()
    myWin = turtle.Screen()
    
    t.left(90)#这几步主要为了调整初始画笔的位置，让树落在窗口中间
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    
    tree(75,t)#初始主干为75
    myWin.exitonclick()
    
main()