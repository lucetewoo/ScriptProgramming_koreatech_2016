class LinearEquation :
    #생성자
    def __init__(self, a, b, c, d, e, f) :
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    #a반환
    def geta(self) :
        return self.__a
    #b반환
    def getb(self) :
        return self.__b
    #c반환
    def getc(self) :
        return self.__c
    #d반환
    def getd(self) :
        return self.__d
    #e반환
    def gete(self) :
        return self.__e
    #f반환
    def getf(self) :
        return self.__f
    #연립방정식 해가 존재하는지 확인
    def isSolvable(self) :
        if self.__a*self.__d-self.__b*self.__c == 0 :
            return False
        else :
            return True
    #x값 반환    
    def getX(self) :
        return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    #y값 반
    def getY(self) :
        return (self.__a*self.__f-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
