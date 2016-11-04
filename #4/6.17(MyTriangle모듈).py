#MyTriangle 모듈 불러오기
import MyTriangle
#삼각형의 세 변 입력
side1,side2, side3 = eval(input("삼각형의 세 변을 입력하세요 :"))
#삼각형의기준 확인
if MyTriangle.area(side1,side2,side3) == False :
    print("입력된 세 변이 삼각형의 기준에 맞지 않습니다.")
else :
    print("삼각형의 넓이는 %.1lf입니다."%MyTriangle.area(side1,side2,side3))
