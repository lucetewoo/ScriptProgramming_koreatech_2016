from LinearEquation import LinearEquation
#객체 생성
ex1 = LinearEquation(1, 1, 1, 1, 1, 1)
ex1.isSolvable()
if(ex1.isSolvable() == False):
    print("이 방정식은 해가 없습니다.")
else :
    print("x = %d, y = %d"%(ex1.getX(), ex1.getY()))
