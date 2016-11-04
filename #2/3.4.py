#math함수 입력을 위한 모듈 임포트
import math

#한 변의 길이 입력
s = eval(input("한 변의 길이를 입력하세요 : "))

#넓이 구하는 공식 사용
A = (5 * pow(s,2)) / (4* math.tan(math.pi/5))

#넓이 출력
print("오각형의 넓이는", A, "입니다.")
