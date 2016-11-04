#피라미드의 높이 입력
n = eval(input("pyramid height : "))

#피라미드 그리기
for i in range(0,n +1) :
#앞의 줄 만큼 띄우기 end = " " ==> 한줄에 결과값 출력하기 위함
    for j in range(n - i) :
        print(" "*5, end = " ")
#피라미드의 앞쪽        
    for j in range(1, i) :
        print("%5d"%pow(2,j-1), end = " ")
#피라미드의 뒤쪽        
    for i in range(i,0,-1) :
        print("%5d"%pow(2,i-1), end = " ")
#줄 변환
    print("\n")
