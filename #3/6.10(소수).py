#exit함수 사용을 위한 sys모듈 임포트
import sys 

#소수판별함수
def is_prime(n):
    #2혹은 3은 True
    if n == 2 or n == 3: return True
    #2보다 작거나 2로나누웠을 때 나머지가 0이면 False
    if n < 2 or n%2 == 0: return False
    #위의 조건에 이어 9보다 작은경우 True
    if n < 9: return True
    #3으로 나뉘어지면 False
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

#번호에 따른 검색, 출력, 종료기능 
print("10000 이하의 숫자 중에서 소스를 찾는 프로그램\n")
print("1 : 10000이하의 소수 모두 출력\n2 : 숫자 입력 시 소수인지 판별\n그 외의번호 : 종료\n")
n = eval(input("숫자를 입력하세요 : "))
#1을 입력할 경우 10000까지의 소수 출력
if n == 1 :
    for i in range (0 ,10000) :
        if(is_prime(i) == True) :
            #한줄 출력
            print("%5d"%i,end = '')
        else :
            continue
#2를 입력할 경우 입력한 추가로 입력한 수가 소수인지 아닌지 판별
elif n == 2:
    fn = eval(input("숫자 입력 : "))
    if(is_prime(fn) == True) :
        print(is_prime(fn))
    else :
        print("False")
#1 혹은 2가 아닌 다른 수를 입력시 종료
else :
    sys.exit()
