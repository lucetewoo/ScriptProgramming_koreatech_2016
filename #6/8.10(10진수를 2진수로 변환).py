#10진수를 2진수로 변환하는 함수 1
def decimalToBinary(value) :
    #내장 되어있는 함수 사용
    binary = bin(value)
    return binary

#10진수를 2진수로 변환하는 함수 2
def decimalToBinary2(value) :
    #10진수를 2진수로 바꾸는 계산식 코드
    result = ""
    while value != 0:
        bit = value % 2;
        #앞쪽에 문자열 넣기
        result = str(bit) + result
        value = value // 2
    return result

decimal = eval(input())
print("함수1 : 10진수 %d를 2진수로 변환하면 %s입니다."\
      #bin함수는 0bxxxx라고 출력되므로 스트링값을 [2:]로 출력 범위를 지정
      %(decimal,decimalToBinary(decimal)[2:]))
print("함수2 : 10진수 %d를 2진수로 변환하면 %s입니다."\
      %(decimal,decimalToBinary2(decimal)))
