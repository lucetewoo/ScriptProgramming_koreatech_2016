#calendar모듈 임포트
import calendar

#년 월을 입력
year, month = eval(input("년, 월을 입력하세요 : "))

#calendar모듈에 있는 monthrange함수를 활용해서 마지막날 변수에 대입
last_day = calendar.monthrange(year,month)

#출력
print("%d년 %d월은 %d일까지 있습니다."%(year, month, last_day[1]))
