#Turtel모듈 임포트
import turtle

#터틀 크기 3
turtle.pensize(3)
#터틀 올리기
turtle.penup()
#터틀 (-120,-120)으로 이동
turtle.goto(-120, -120)
#터틀 내리기(그림시작)
turtle.pendown()
#터틀 속도 10(최대)
turtle.speed(10)
#터틀 색깔 검정색으로
turtle.color("Black")


#-120부터 90까지 60씩 이동 반복
for i in range(-120, 90, 60):
    #-120부터 120까지 이동 반복
    for j in range(-120, 120, 60):
        turtle.penup()
        turtle.goto(j, i)
        turtle.pendown()

       #작게 그린 사각형 칠하기(시작)     
        turtle.begin_fill()
        for k in range(4):
            #30픽셀 앞으로 이동
            turtle.forward(30)
            #터틀 90도 방향전환
            turtle.left(90)
        #작게 그린 사각형 칠하기(끝)
        turtle.end_fill()

        
#중간 그림그리기 -90부터 120까지 60씩 이동 반복
for i in range(-90, 120, 60):
    #-90부터 120까지 60씩 이동 반복
    for j in range(-90, 120, 60):
        #터틀 올리기
        turtle.penup()
        
        turtle.goto(j, i)
        turtle.pendown()

       #작게 그린 사각형 칠하기(시작)     
        turtle.begin_fill()
        for k in range(4):
            #30픽셀 앞으로 이동
            turtle.forward(30)
            #터틀 90도 방향전환
            turtle.left(90)
        #작게 그린 사각형 칠하기(끝)
        turtle.end_fill()
#터틀 올리기
turtle.penup()
#터틀 초기위치로 이동
turtle.goto(-120, -120)
#터틀 내리기
turtle.pendown()

#외부 선 그리기
for i in range(4):
    #240픽셀 이동
    turtle.forward(240)
    #90도 회전
    turtle.left(90)

#터틀 모양 숨기기
turtle.hideturtle()
#터틀 완료
turtle.done() 
