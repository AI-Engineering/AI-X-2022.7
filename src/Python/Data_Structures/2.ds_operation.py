
num1 = 3
num2 = 4.23

sumR = f'{num1+num2}'
print(sumR, f'{num1*num2}, {num1/num2}')

num1 = 7
num2 = 4

# 나누기 몫
print(num1//num2)

# **연산자 (승수 계산)
result = 2**8
print(result)

# % 연산자: 나눗셈 후 나머지 반환
print((8 % 3), (7 % 3))

# range: start ~ end - 1
for x in range(1, 10):
    print(x)

# 소수 판단
# testNum = 17 #12
while(1):
    testNum = input()
    if (testNum.isdigit()):
        break

testNum = int(testNum)
for i in range(2, testNum):
    if (testNum % i) == 0:
        print(f'{testNum} is not prime Number')
        break
    print(f'{testNum} is Prime Number')

# 소수 판단
testNum = 112397
decision = "False"
for i in range(2, testNum):
    if (testNum % i) == 0:
        print(f'{testNum} is not prime Number')
        break
    else:
        decision = "True"
if decision == "True":
    print(f'{testNum} is Prime Number')

