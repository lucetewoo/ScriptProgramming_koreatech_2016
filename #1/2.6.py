#2.6 (정수의 자릿수 합산하기)

#숫자 입력
number = eval(input("0부터 1000사이의 숫자를 입력하세요."))
#백의 자리
number_100 = number //100
#십의자리
number_10 = (number%100) // 10
#일의자리
number_1 = number %10
#자리수 합계
number_sum = number_100 + number_10 + number_1

print("각 자릿수의 합은 " ,number_sum, "이다")
