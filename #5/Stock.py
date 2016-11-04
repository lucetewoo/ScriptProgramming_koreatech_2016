#Stock 클래스
class Stock :
    #생성자
    def __init__(self, symbol, name, previousClosingPrice , currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    #종목 반환
    def getSymbol(self):
        return self.__symbol
    #이름 반환
    def getName(self):
        return self.__name 
    #전일 가격 반환
    def getpreviousClosingPrice(self):
        return self.__previousClosingPrice
    #현재가격 반환
    def getCurrentPrice(self):
        return self.__currentPrice
    #전일 가격 설정
    def setPreviousPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    #현재가격 설정
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
    #변화율 반환
    def getChangePercent(self):
        ChangePercnt = (self.__currentPrice - self.__previousClosingPrice) * 100 / self.__previousClosingPrice
        return ChangePercnt

