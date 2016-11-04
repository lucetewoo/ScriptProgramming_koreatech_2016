#패스워드 생성 규칙확인
def PasswordCorrect(password) :
    #문자 수
    character = 0
    #숫자수
    number = 0
    #길이 8자 이상인지 확인
    if len(password) >= 8 :
        for i in range(len(password)):
            #문자 와 숫자로 구성되어 있는지 확인
            if 48<= ord(password[i]) < 58 :
                number += 1
            else :
                character +=1
        #모든조건을 만족하면 올바른 패스워드
        if number > 1 and  character > 0:
                print("올바른 패스워드입니다.")
        #하나라도 만족하지 않으면 올바르지 않은 패스워드
        else :
                print("올바르지 않은 패스워드입니다.")
    else:
        print("올바르지 않은 패스워드입니다.")




#확인 받을 패스워드 입력
password = input()
PasswordCorrect(password)
