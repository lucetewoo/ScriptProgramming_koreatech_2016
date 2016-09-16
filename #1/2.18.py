#2.18 (현재 시간)


#시간 모듈 임포트
import time

currentTime = time.time() #현재시간을 얻어온다.

#1970년 1월1일 자정이후로의 전체 초 값을 얻어온다.
totalSeconds = int(currentTime)
#현재 시간의 초 값을 계산
currentSecond = totalSeconds % 60
#전체 분 값을 계산
totalMinutes = totalSeconds // 60
#현재 시간의 분 값을 계산
currentMinute = totalMinutes % 60
#전체 시 값을 계산
totalHours = totalMinutes // 60
#현재 시간의 시 값을 계산
currentHour = totalHours %24

#시간대 차이 입력
time_offset = eval(input("GMT와 시간대 차이를 입력하세요 : "))
#시간대 차이
time_zone_offset = (currentHour + time_offset) %24

#현재 시간 출력
print("GTM시간 : ",currentHour, ":", currentMinute, ":", currentSecond)
#현재 위치 시간 출력
print("현재 위치의 시간 : ",time_zone_offset, ":", currentMinute, ":", currentSecond)
