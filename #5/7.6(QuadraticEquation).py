from QuadraticEquation import QuadraticEquation

#입력
a, b, c = eval(input("2차 방정식 a^2 + bx + c = 0에 대한 a, b, c를 입력하세요.\n"))
#객체 생성
equation = QuadraticEquation(a, b, c)


if equation.getDiscriminant() < 0 : 
    print("이 방정식은 해가 없습니다.\n")
elif equation.getDiscriminant() == 0 :
    print("이 방정식의 해는 %f입니다\n"%equation.getRoot1())
else: 
    print("이 방정식의 해는 %.1f와 %.1f입니다.\n"\
          %(equation.getRoot1(), equation.getRoot2()))
