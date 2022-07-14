# Variable Test (기본 사용법: Assignment '=' 기호 사용)
a = 1
b = "Python"
print(a, b)
a, b = 1, "Python"
print(a, b)

# 변수에 assign 할 경우, 대입되는 값에 해당하는 객체의 값들이 메모리에 할당, 변수는 해당 주소를 가리키고 있음
a = [1, 2, 3]
#아래와 같이 복사 할 경우, 사실 b 또한 list [1,2,3]이 할당된 메모리를 참조하고 있음
b = a
print(a, b, a is b, id(a), id(b))
a[2] = ['1', '2']
print(a, b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b, a is b, id(a), id(b))

# 복사
a = [1, 2, 3]
b = a[:] # 리스트 슬라이싱을 사용하면 새로운 객체를 생성하고 b는 새로 생성된 객체의 주소를 참조

c = a.copy()
print(id(a), id(b), id(c), c)

# 변수 만드는 여러가지 방법
a, b = ("coding", "life")
(a, b) = ("coding", "life")
[a, b] = ['coding', 'life']
print(type(a), type(b), a, b)

# 아래와 같이 하면 a라는 변수는 tuple 형이됨
a = ("coding", "life")
print(type(a))
a = "coding", "life"
print(type(a))

# Swap
a, b = 3, 10
print(a, b)
a, b = b, a
print(a, b)