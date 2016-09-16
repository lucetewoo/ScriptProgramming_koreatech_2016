#2.9 (과학: 체감온도)(과학: 체감온도)


#온도 입력
temperature = eval(input("화씨 -58도와 41도 사이의 온도를 입력하세요."))
#풍속 입력
wind = eval(input("풍속을 시간당 마일 단위로 입력하세요."))
#체감 온도 계산
temperature_feel = 35.74 + 0.6215*temperature - 35.75*pow(wind,0.16) + 0.4275*temperature*pow(wind,0.16)

print("체감온도는",temperature_feel)
