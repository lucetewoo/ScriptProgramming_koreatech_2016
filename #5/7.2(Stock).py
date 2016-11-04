from Stock import Stock

#객체 생성
stock = Stock("INTC", "Intel Corporation", 200500, 20350)
print("%s의 가격 변동률은 %.2f입니다."%(stock.getName(), stock.getChangePercent()))
