#tan()사용을 위한 math모듈 임포트
import math
#클래스
class RegularPolygon :
    #생성자
    def __init__(self, n = 3, side = 1.0, x = 0.0, y = 0.0) :
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    #n각형 반환
    def getn(self) :
        return self.__n
    #한 변의 길이 반환
    def getside(self) :
        return self.__side
    #n각형의 중심 x좌표 반환
    def getx(self) :
        return self.__x
    #n각형의 중심 y좌표 반환
    def gety(self) :
        return self.__y
    #n각형 설정
    def setn(self,n) :
        self.__n = n
    #한 변의 길이 설정
    def setside(self,side) :
        self.__side = side
    #n각형의 중심 x좌표 설정
    def setx(self,x) :
        self.__x = x
    #n각형의 중심 y좌표 설정
    def sety(self,y) :
        self.__y = y
    #n각형의 둘레  반환
    def getPerimeter(self) :
        return self.__n * self.__side
    #n각형의 넓이 반환
    def getArea(self) :
        return (self.__n*pow(self.__side,2)) / (4*math.tan(math.radians(180/self.__n)))
    

