#연도와 요일을 입력
year, day = eval(input("연도와 요일을 입력해주세요 : "))
#요일 7이상일 경우 나머지로 대입
if day > 6:
    day = day % 7

#1월 부터 12월까지 
for month in range(1, 13):
    print()
    print("\n%d년 %d월"%(year, month))
    print("---------------------------------------")
    print(" 일   월   화   수   목   금   토")
    #1, 3, 5, 7, 8, 10, 12월 이면 31일까지
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        date = 31
     #4, 6, 9, 11월이면 30일까지.
    elif month == 4 or month == 6 or month == 9 or month == 11: #4, 6, 9, 11월이면 30일을 저장한다.
        date = 30
    #윤년일 경우 29일을 아니면 28일까지
    elif month == 2: 
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            date = 29
        else:
            date = 28

    #시작위치 띄우기
    if day != 6:
        print('     ' * day, end = '     ')
    #일별로 한줄 출력    
    for i in range(1, date+1):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print("%2d"%i, end = '   ')
            #1주일이 넘어갈 경우 밑줄로 내리기
            if i == 6 - day:
                print()
            elif i % 7 == 6 - day:
                print()
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("%2d"%i, end = '   ')
            if i == 6 - day:
                print()
            elif i % 7 == 6 - day:
                print()
        elif month == 2:
            print("%2d"%i, end = '   ')
            if i == 6 - day:
                print()
            elif i % 7 == 6 - day:
                print()
    #월별 처리
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = day + 3
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = day + 2
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            day = day + 1
    if day > 6:
        day = day % 7
 

