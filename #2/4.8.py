#세 정수 입력
a,b,c = eval(input("세 정수를 입력하세요 : "))
#리스트 자료형
r = [0, 0, 0]
#리스트에 대입
r[0] = a
r[1] = b
r[2] = c
 
#리스트 정렬 함수 사용
r.sort()
#출력
print("%d\n%d\n%d"%(r[0],r[1],r[2]))
