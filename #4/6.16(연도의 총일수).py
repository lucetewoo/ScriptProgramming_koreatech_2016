#calendar모듈 사용
import calendar
#지정된 연도의 총 일수를 반환하는 함수 지정
def numberOfDaysInYear(year) :
    DaysInYear = 0
    #월 별 마지막 날을 더하기
    for month in range (1,13) :
        monthinfo = calendar.monthrange(year,month)
        DaysInYear = DaysInYear + monthinfo[1]
    return DaysInYear

#해당 년도의 총 일수 출력
for i in range(2010,2021) :
    print("%d년의 총 일수는 %d일입니다."%(i,numberOfDaysInYear(i)))
