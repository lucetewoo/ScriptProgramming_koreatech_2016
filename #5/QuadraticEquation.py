#클래스
class QuadraticEquation:
    #생성자
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    #a값 반환
    def getA(self):
        return self.__a
    #b값 반환
    def getB(self):
        return self.__b
    #c값 반환
    def getC(self):
        return self.__c
    #판별식 계산값 반환
    def getDiscriminant(self):
        return self.__b * self.__b - 4 * self.__a * self.__c
    #해1 반환
    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return False
        else:
            return (-self.__b + self.getDiscriminant()) / (2 * self.__a)
    #해2 반환
    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return False
        else:
            return (-self.__b - self.getDiscriminant()) / (2 * self.__a)


