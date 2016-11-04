#난수 발생 모듈사용
import random
#최초 승리 0으로 초기화
victory = 0
#0부터 9999까지 10000번의 경
for i in range(0, 10000):
    #주사위 1,2 점수 0으로 초기
    dice1 = 0
    dice2 = 0
    score = 0
    #주사위 던지기
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #주사위 합
    diceSum = dice1 + dice2
    #7혹은 11일경우 승리
    if diceSum == 7 or diceSum == 11:
        victory += 1
    #2, 3, 12를 제외한 다른 숫자일 경우
    elif diceSum == 4 or diceSum == 5 or diceSum == 6\
         or diceSum == 8 or diceSum == 9 or diceSum == 10:
        #해당 값 점수로
        score = diceSum
        #다시던져서 7 혹은 같은 수가 나올때까지 던지기
        while 1:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            diceSum = dice1 + dice2
            #7일경우 패배
            if diceSum == 7:
                break
            #같을 경우 승리
            elif diceSum == score:
                victory += 1
                break
#최종 승리 출력
print("승리 횟수는 ", victory, "입니다.")
