# 집합 자료형 사용방법
s1 = set([3, 1, 2, 4]) # set() 괄호 안에 list 형태로 작성하거나
s2 = set("Hello") # 문자열을 입력하여 만들 수 있음
print(s1, s2) # s2의 경우, 중복되는 것이 빠져있는 것을 확인 할 수 있음

# Point: 중복 허용하지 않으며, 순서가 없음. ==> 인덱싱 등 사용 불가능 ==> 사용하고 싶으면 형변환
s1_tuple = tuple(s1)
# set 출력 값을 바탕으로 형 변환
print(type(s1_tuple), s1_tuple, s1_tuple[0], s1_tuple[1])

# Set Function (교집합, 합집합, etc.)
s1 = set([1, 2, 3, 4, 5])
s2 = ([2, 3, 5, 6])
print(f'교집합={s1.intersection(s2)}, 합집합={s1.union(s2)}, 차집합={s1.difference(s2)}')

# 관련합수
# set에 값 하나 추가
s1 = set([1, 3, 4])
s1.add("5")
print(s1)

# set에 여러개의 값을 추가하기
s1 = set([1, 3, 4, 5])
s1.update(['1', '3', '4', '5']) # Set() 괄호 내에 리스트 형태로 표현, list를 추가할 수는 없음
print(s1)

# 특정 값 삭제
s1.remove(1)
s1.remove('1')
print(s1)
