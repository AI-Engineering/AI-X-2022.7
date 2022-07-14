# list add/delete
list_a = [1, "2", 4]
print(f'{list_a}', id(list_a))
list_a[1] = 4
print(f'{list_a}', id(list_a))
list_a = list_a + [5, 6]
print(list_a)
del list_a[2]
print(list_a)

str_1 = "123"
print(str_1[0], str_1[1], str_1[2])
# str_1[2] = "3"
# str_1 = str_1[:2]+"4"
# print(str_1)

# list append / sort
test_list = [1, 2, 3]
test_list.append([4, 8, 6, 7, 9])
test_list.append("string")
print(test_list)
test_list[3].sort()
test_list[3].reverse()

print(test_list, test_list[3])
test_list = [1, 2, 3, 'd', 'c', 'a']
tmp = test_list[3:]
tmp.sort()
print(test_list[3:], tmp)

# list reverse
tmp_list = ['a', 'd', 'c']
tmp_list.reverse()
print(tmp_list)
print(tmp_list.index('d'))
# print(tmp_list.index('p'))

# list insert/remove
print("====================\n")
print(tmp_list)
tmp_list.insert(0, [1, 2, 3])
print(tmp_list)
tmp_list[0].insert(3, 4) ##tmp_list[0]번째, [1, 2, 3]리스트의 3번째 인덱스에 4를 삽입 ==> [1, 2, 3, 4]
print(f'===>{tmp_list}')
tmp_list[0].remove(1) # tmp_list에서 값(value) 1을 삭제 (제일 먼저 나오는 값만 삭제)
print(tmp_list) ## [ [2, 3, 4], c, d, a ]

# pop / count /extend
tmp_list.pop() ## pop (remove last index of list: a) [ [2, 3, 4], c, d ]
print(f"===>{tmp_list}")
tmp_list.pop(2) ## remove 2nd index of list: d (0: [2, 3, 4], 1: c, 2: d) ==> [ [2, 3, 4], c ]
print(f"====>{tmp_list}, {tmp_list.count('c')}")
tmp_list.extend([4, 5]) # 리스트에 리스트를 더하는 함수 (append와 다름. tmp_list += [4, 5]와 동일)
print(tmp_list)
