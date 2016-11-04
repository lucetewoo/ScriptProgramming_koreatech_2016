import math

print("10개의 숫자를 입력하세요 :")
lst = [0,0,0,0,0,0,0,0,0,0]
for i in range (0,10) :
    n = eval(input())
    lst[i] = n
 
#평균을 반환하는 함수 
def average(lst) :
    return sum(lst) / len(lst)

#표준편차를 반환하는 함수 
def standardDeviation(lst):

  sigma = 0
  sum = 0
  averagelst = average(lst)

  for i in range(0, len(lst)):
    diff = lst[i] - averagelst
    sum += diff * diff
  sigma = math.sqrt(sum / len(lst))
  return sigma
print(lst)
print("평균은 %f이다."%average(lst))
print("표준편차는 %f이다"%standardDeviation(lst))
