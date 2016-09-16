#2.19 (금융 애플리케이션: 미래 투자가치 계산하기)


#투자금 입력
investment = eval(input("투자금을 입력하세요. "))
#연이율 입력
year_rate = eval(input("연이율을 입력하세요. "))
#연수 입력
year = eval(input("년수를 입력하세요. "))
#투자가치 계산
investment_value = investment * pow((1+year_rate/(12*100)),year*12)


print("누적된 투자가치는 ",investment_value,"입니다.")
