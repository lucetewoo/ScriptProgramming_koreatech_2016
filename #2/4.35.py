import turtle

x0, y0 = eval(input("p0의 x, y좌표를 입력하세요 : "))
x1, y1 = eval(input("p1의 x, y좌표를 입력하세요 : "))
x2, y2 = eval(input("p2의 x, y좌표를 입력하세요 : "))

#펜올리기
turtle.shape("circle")
turtle.up()
#p0점으로 이동
turtle.goto(x0,y0)
#p0점 위치저장
turtle.stamp()
#p0점에 대한 정보 기록
turtle.write("    p0 : %d,%d"%(x0,y0))
#펜 내리기(선 긋기)
turtle.down()
#p1점으로 이동
turtle.goto(x1,y1)
#p1점 위치저장
turtle.stamp()
#p1점에 대한 정보 기
turtle.write("    p1 : %d,%d"%(x1,y1))
#펜 올리기
turtle.up()

#p2점으로 이동
turtle.goto(x2, y2)


#기울기를 활용해 점의 위치파악
slope1 = (y1-y0)/(x1-x0)
slope2 = (y2-y0)/(x2-x0)

if slope1 < slope2:
    turtle.write("    p2 : %d,%d\n\n     p2는 직선의 왼쪽에 있습니다."%(x2,y2))
elif slope1 > slope2:
    turtle.write("    p2 : %d,%d\n\n     p2는 직선의 오른쪽에 있습니다."%(x2,y2))
else:
    turtle.write("    p2 : %d,%d\n\n     p2는 직선 위에 있습니다."%(x2,y2))
 
