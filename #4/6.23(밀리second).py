#밀리초를 시,분,초로 변환하는 함수
def convertMillis(millis) :
    
    conSec = millis // 1000
    Hour = conSec // 3600
    Min = (conSec % 3600) //60 
    Sec = conSec % 60
    return Hour, Min, Sec

millis = eval(input("밀리초를 입력하세요. : " ))
#함수 사용 변수에 반환
Hour, Min, Sec = convertMillis(millis)
#출력
print("%d밀리 세컨드는 %d시간 %d분 %d초 입니다."%(millis,Hour,Min,Sec))
