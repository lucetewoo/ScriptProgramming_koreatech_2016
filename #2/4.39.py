#turtle모듈 임포트
import turtle
#math 모듈 임포트
import math


#원1 과 원2 의 정보를 입력
x1, y1, r1 = eval(input("원1의 중심과 반지름 입력  : "))
x2, y2, r2 = eval(input("원2의 중심과 반지름 입력  : "))

#원1 과 원2 의 중심점 거리를 구한다.
d= math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
#펜을 올린다
turtle.up()
#원의 중심으로 이동한다.
#이 때 반지름 만큼 y값을 이동시키는 이유는 (x,y)점이 
#turtle이 원을 그리는 시작점의 위치이기 때문이다.
turtle.goto(x1,y1-r1)
turtle.down()
#원1 그리기
turtle.circle(r1)

#펜을 올린다
turtle.up()
#원2의 중심으로 이동
turtle.goto(x2,y2-r2)
turtle.down()
#원2 그리기
turtle.circle(r2)

turtle.hideturtle()


#두 원의 위치를 판별하여 출력
if d > r1 + r2 :
    turtle.write("원 2는 원 1과 겹치지 않습니다.")
elif d == r1 + r2:
    turtle.write("원 2는 원 1과 접합니다.")
elif d < r1 + r2:
    if d < r1 - r2:
        turtle.write("원 2는 원 1의 내부에 있습니다.")
    else:
        turtle.write("원 2는 원 1과 겹칩니다.")
