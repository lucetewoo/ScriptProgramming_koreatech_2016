#컴퓨터와 가위바위보를 하기위해 random모듈 임포트
import random

#플레이어의 입력에 따라 가위, 바위, 보 결정
player = eval(input("가위 (0), 바위(1), 보(2) : " ))
if (player == 0):
    player = "가위"
elif (player == 1):
    player = "바위"
elif (player == 2) :
    player = "보"
 
#컴퓨터의 입력에 따라 가위, 바위, 보 결정
computer = random.randint(0,2)
if (computer == 0):
    computer = "가위"
elif (computer == 1):
    computer = "바위"
elif (computer == 2):
    computer = "보"
 
    
 
#결과 출력
if (player == computer):
    print ("컴퓨터는 %s입니다. 당신도 %s입니다. 비겼습니다."%(computer,player))
elif (player == "바위") :
    if (computer == "보"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 졌습니다."%(computer,player))
    elif (computer == "가위"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 이겼습니다."%(computer,player))
elif (player == "보"):
    if (computer == "바위"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 이겼습니다."%(computer,player))
    elif (computer == "가위"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 졌습니다."%(computer,player))
elif (player == "가위"):
    if (computer == "바위"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 졌습니다."%(computer,player))
    elif (computer == "보"):
        print ("컴퓨터는 %s입니다. 당신은 %s입니다. 당신이 이겼습니다."%(computer,player))

        
