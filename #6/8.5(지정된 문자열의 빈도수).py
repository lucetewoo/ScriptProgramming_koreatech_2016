#문자열확인
def count(s1, s2) :
    #카운트메소드 사용
    cnt = s1.count(s2)
    return cnt


s1 = input("문자열s1을 입력하세요 : ")
s2 = input("문자열s2를 입력하세요 : ")

print("문자열 %s내에서 %s는 %d번 출력됩니다."%(s1,s2, count(s1,s2)))
