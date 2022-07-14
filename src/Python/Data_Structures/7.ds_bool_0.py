# bool 자료형 사용
a = True
b = False
print(type(a), type(b), f'1과 1은 같나요?{1 == 1}, 1과 2는 같나요?{1 == 2}'
                        f'1은 2보다 작나요?{1 < 2}')

# str_t = ""가 되면 False가 되어 While문에서 빠져 나옴.
str_t = "Hello"
idx = 1
while str_t:
    print(idx, len(str_t), str_t)
    str_t = str_t[:len(str_t) - idx]

# 해당 표를 조금 더 쉽게?
if 1:
    print("True")

if []:
    print("True")
else:
    print("False")

if [1, 2, 3]:
    print("True")
else:
    print("False")

# Bool 내장함수 (자료형의 참과 거짓을 판별할 수 있는 내장함수)
print(f'{bool("Python")}, {bool("")}')
print(bool(''), bool(()))


