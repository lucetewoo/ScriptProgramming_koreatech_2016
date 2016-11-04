class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    #기본 생성자
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    #팬의 속도 반환
    def getSpeed(self):
        return self.__speed
    #팬의 반지름 반환
    def getRadius(self):
        return self.__radius
    #팬의 색상 반환
    def getColor(self):
        return self.__color
    #팬의 전원 여부 반환
    def isOn(self):
        return self.__on
    #팬의 속도 설정
    def setSpeed(self, speed):
        self.__speed = speed
    #팬의 반지름 설정
    def setRadius(self, radius):
        self.__radius = radius
    #팬의 색상 설정
    def setColor(self, color):
        self.__color = color
    #팬의 전원 여부 설정
    def setOn(self, on):
        self.__on = on



