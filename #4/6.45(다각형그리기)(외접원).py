import turtle
import math
#x좌표, y좌표, 반지름, 다각형의 종류
x, y, radius,numberOfSides = eval(input("x, y, radius,numberOfSides : "))
 
#원 그리기 
def drawCircle(x=0, y=0, radius = 50, numberOfSides =3) :
    turtle.speed(10)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)
    
#다각형 그리기
def drawPolygon(x=0, y=0, radius = 50, numberOfSides =3) :
    #다각형에서 한 각
    numberOfSides_angle = (numberOfSides-2)*180/numberOfSides
    #turtle이 회전할 각
    turn_angle = 90-numberOfSides_angle/2
    #turtle이 이동할 길이
    numberOfSides_go = math.cos(math.radians(numberOfSides_angle/2))*radius*2
    turtle.showturtle()
    turtle.setup()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    #turtle이동 -> 그리기 
    for i in range(0,numberOfSides) :
        if i == 0 :
            turtle.left(turn_angle)
            turtle.forward(numberOfSides_go)
        else :
            turtle.left(180 - numberOfSides_angle)
            turtle.forward(numberOfSides_go)
    turtle.hideturtle()

#원그리기
drawCircle(x,y,radius,numberOfSides)
#다각형 그리기
drawPolygon(x,y,radius,numberOfSides)


