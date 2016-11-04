#sqrt()함수 사용을 위해 math모듈 임포트
import math

#이차방정식의 항 입력
a,b,c = eval(input("a, b, c를 입력하세요 : "))

#판별식
D = pow(b,2) - 4*a*c


#판별식을 조건에 따라 출력

#판별식이 0보다 작을경우
if D < 0 :
    print("이 방정식은 실근이 존재하지 않습니다")

#판별식이 0일경우
elif D == 0 :
    r = -b / 2*a
    print("실근은",r,"입니다")
    
#판별식이 0보다 클 경우 
else :
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("실근은", r1, "이고", r2,"입니다.")
    
