#1부터 10000까지
for i in range(1,10001) :
    #변수 total선언
    total = 0
    #완전수 계산할때 나누는 수는 i/2+1까지
    for j in range(1, i//2+1) :
        #나머지가 0이면 total값에 넣기
        if i%j ==0 :
            total = total + j
    #total값이 i와 같으면 완전수라는 말 출력        
    if total == i :
        print(i,"= 완전수")
    #아니면 반복문 계속진행     
    else :
        continue
