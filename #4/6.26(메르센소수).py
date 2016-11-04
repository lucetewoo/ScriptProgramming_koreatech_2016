#소수 판별 함수
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

#메르센 소수 판별 함수
def mersenn_prime(p):
    if (is_prime(pow(2,p)-1) == True) :
        return True
    else :
        return False
    
#메르센 소수 출력
print("    p                 2^p-1\n")
for i in range(1,32) :
        if(mersenn_prime(i) == True) :
            print("%5d %20d"%(i,(pow(2,i)-1)))
        else :
            continue
