#2.17 (건강 애플리케이션: BMI 계산하기) --> BMI 계산식 = 몸무게(Kg) / 키(m)^2


#무게 입력(파운드)
weight_pound = eval(input("몸무게를 파운드로 입력하세요"))
#키 입력(인치)
height_inch = eval(input("키를 인지로 입력하세요"))
 
#파운드 -> 킬로, 인치 -> 미터 변환
weight_kilo = 0.45359237 * weight_pound
height_meter = 0.0254 * height_inch

#BMI지수 계산 
BMI = weight_kilo / pow(height_meter,2)
 
print("BMI지수는", BMI)
