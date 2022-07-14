t1 = (1, 2, "a", "b")
# t1.insert(0, 1) # insert 메서드 없음
# del t1[0] # 삭제 불가능

print(t1[0], t1[1], t1[2]) # 인덱스로 접근
# t1[0] = "c"

t2 = t1[0:2]
print(t2)

t3 = t2 + (3, 4) # Concatenate
t4 = t2 * 2 # 반복
print(t3, t4)

