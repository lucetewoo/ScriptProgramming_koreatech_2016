#2.5 (금융 애플리케이션: 팁 계산하기)


#가격과 팁 비율 입력
price, tip = eval(input("소계와 팁 비율(%)을 입력하세요(,로 구분)"))
#팁가격
tip_price = (price * tip)/100                 
#전체가격     
total_price = price * (1+tip/100)
print("팁은",tip_price,"총액은",total_price)
