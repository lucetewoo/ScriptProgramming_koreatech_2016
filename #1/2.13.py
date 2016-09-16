#2.13 (숫자 분할하기) --> 역순이 아니라 정순. 예외상황은 없다.


#숫자 입력
number = eval(input("4자리 숫자를 입력하세요."))
#천의자리 출력
print(number//1000)
#백의자리 출력
print((number%1000)//100)
#십의자리 출력
print((number%100)//10)
#일의자리 출력
print(number%10)
