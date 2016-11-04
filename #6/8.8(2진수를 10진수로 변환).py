#2진수를 10진수로 변환하는 함수 1
def binaryToDecimal(binaryString) :
    #내장 되어있는 함수사용
    Decimal = int(binaryString,2)
    return Decimal

#2진수를 10진수로 변환하는 함수 2
def binaryToDecimal2(binaryString) :
    #2진수를 10진수로 바꾸는 계산식 코드
    value = 0
    for i in range (len(binaryString)-1,-1,-1):
            value = value + int(binaryString[i])*pow(2,len(binaryString)-1-i)                     
    return value
    
        
binary = input("2진수를 입력하세요.")
print("함수1 : 2진수 %s를 10진수로 변환하면 %d입니다."%(binary, binaryToDecimal(binary)))
print("함수2 : 2진수 %s를 10진수로 변환하면 %d입니다."%(binary, binaryToDecimal2(binary)))
