#입력한 정수를 역으로 바꿔주는 reverse함수
def reverse (number) :
    return int(str(number)[::-1])
#reverse()함수를 활용해 대칭인지 아닌지 판별하는 함
def isPalindrome (number) :
    if( number == reverse(number)) :
        return True
    else :
        return False
#정수 입력
n = eval(input("정수를 입력하세요 : "))
#정수의 역
reverse(n)
#정수의 역판별 후 출력
print("입력한 정수 %d가 대칭이면 True, 대칭이 아니라면 False를 반환"%n)
print("입력한 수는 %d, 입력한 수의 역은 %d"%(n,reverse(n)))
print(isPalindrome(n))
