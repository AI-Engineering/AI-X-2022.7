a = {
    'name': ['kim', 'cha', 'lee', 'jeon', 'cho', 'shin', 'kang'],
    'ID': [210100, 210101, 210102, 210103, 210104, 210105]
}
list_tmp = ['name', 'ID']
print(a)
# list처럼 사용할 수 있다는 것은 값을 가지고 올 수 있다. (리스트의 값을 가지고 오는 것 처럼)
dict_keys = a.keys()
for i in a.keys():
    print(i)
for i in list_tmp:
    print(i)
list_tmp.append('Phone-Number')
# dict_keys.append <<- 존재하지 않음 (관련 내장함수가 존재하지 않음)

# list 형으로 변경 (형변환)
dict_list = list(a.keys())
dict_list.append('phone-Number')
# list 뿐만 아니라 원하는 자료형으로 형은 변환 할 수 있음
b = "123"
c = int(b)
print(type(b), type(c), b, c)
print(dict_list[0])
print(f'{dict_keys}\n{dict_list}\n{list_tmp}')

# dict.value, dict.item value: key에 해당하는 value 값 반환 (dict_value type), item의 경우, Pair로 반환
print(a.values(), type(a.values()))
print(a.items(), type(a.items()))

dict_values_list = list(a.values())
dict_items_list = list(a.items())
print(dict_values_list, f'\n{dict_values_list[0][0]}')

# clear, in, get..
# Clear를 수행하기 전에 복사
a['phone-number'] = ["010-xxxx-xxxx"]
print(a)
b = a
copy_a = a.copy() # a = b (변수 파트에서 다시 설명)
print(b)
a.clear()
print(a, b, copy_a)
# copy_a = a.copy()
# print(copy_a)
# copy_a.clear()
# print(a, f'\n{copy_a}')

# in example
print('name' in a, 'addr' in a)

# get() example
print(a.get('name'), a.get('addr'))
print(a['name']) # Error: 없는 key 값에 해당하는 value를 반환하려고 하면... 반면에, get()함수는 None을 출력
'''
get() 함수사용 시 없는 키에 해당하는 value 값은 당연히 없으므로, None을 출력
None 대신해서 다른 것을 출력하고 싶을때
'''
print(a.get('addr', 'Default'))




