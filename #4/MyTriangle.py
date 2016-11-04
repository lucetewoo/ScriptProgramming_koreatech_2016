#math모듈 사용
import math
#세 변의 길이를 확인해, 삼각형의 조건에 맞는지 확인하는 함수
def  isValid(side1, side2, side3) :
    if(side1 <=0 or side2 <=0 or side3 <=0) :
        False
    lis = [0,0,0]
    lis[0] = side1
    lis[1] = side2
    lis[2] = side3
    lis.sort()
    if lis[2] < (lis[0] + lis[1]) :
        return True
    else :
        return False
#삼각형 조건이 True이면, 삼각형의 넓이를 구하는 함수
def area(side1, side2, side3) :
    if isValid(side1, side2, side3) == True :
        s=(side1 + side2 + side3) / 2
        Area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
        return Area
    else :
        return False
