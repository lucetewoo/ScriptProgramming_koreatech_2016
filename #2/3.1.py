#3.1
#math모듈 import
import math
#길이 입력
r= eval(input("중심에서 한 점 까지의 길이를 입력하세요 : "))
#한 변의 길이 계산
s = 2*r*math.sin(math.pi/5)
#넓이 계산
A = (3*pow(3,1/2))/2*pow(s,2)
#결과출력
print("오각형의 넓이는 : ", A)
