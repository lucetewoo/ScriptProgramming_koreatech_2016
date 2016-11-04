#접두어 확인
def prefix(s1, s2) :
    #접두어확인위한 초기 빈 문자열
    pf = ''
    #길이에 따른 비교
    if len(s1) > len(s2) :
        #문자열 각각을 비교 후 같을 경우 빈 문자열에 삽입
        for i in range (len(s2)) :
            if(s1[i] == s2[i]) :
                pf = pf + s2[i]
            else :
                break
    else :
        for i in range (len(s1)) :
            if(s1[i] == s2[i]) :
                pf = pf + s1[i]
            else :
                break
    #비었던 문자열에 채워진 것을 반환
    return pf
            



s1 = input()
s2 = input()
print("문자열 %s와 %s의 최장 접두어는 %s입니다."%(s1, s2, prefix(s1,s2)))

