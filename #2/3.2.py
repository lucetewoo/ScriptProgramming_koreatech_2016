
#math함수 사용을 위한 모듈 임포트
import math

#60분법 각으로 입력
x1, y1 = eval(input("첫번째 점(위도와 경도)을 60분법 각으로 입력하세요 :"))
x2, y2 = eval(input("두번째 점(위도와 경도)을 60분법 각으로 입력하세요 :"))

#60분법의 각을 라디안 값으로 변환
rx1, ry1, rx2, ry2 = math.radians(x1), math.radians(y1),\
                     math.radians(x2), math.radians(y2)

#지구의 평균 반지름
r = 6370.01

#두 점 사이의 대권거리 입력
d = r * math.acos((math.sin(rx1)*math.sin(rx2))\
                       + (math.cos(rx1)*math.cos(rx2)*math.cos(ry1-ry2)))

#두 점 사이의 대권거리 출
print("두 점 사이의 거리는", d,"km입니다.")

