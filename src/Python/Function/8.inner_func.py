# ABS
print(-3, abs(-3), abs(3))

# ALL / ANY
list_a = [1, 2, 3, 0]
list_b = [1, 2, 3]
print(all(list_a), all(list_b), any(list_a), any(list_b), any([0,"", []]))

# CHR (ASCII to Char)
print(f'{chr(72)}{chr(69)}{chr(76)}{chr(76)}{chr(79)}')

# dir (객체, 자료형이 가지고 있는 내장함수 리스트 출력)
list_var = [1, 2, 3]
str_var = "ABC"
dict_var = {'key': "value"}
print(dir(list_var))
print(dir(str_var))
print(dir(dict_var))

# divmod (operates Divide and Modula)
def div_mod(in_a, in_b):
    return ((in_a // in_b),(in_a % in_b))

print(divmod(7, 3))
print(div_mod(7, 3))

# Enumerate (ENUM)
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval (실행 가능한 문자열을 입력받아 실행한 결과를 반환)
print(eval('11 + 22'))
print(eval('"hello" + " " +"world!!"'))
print(eval('divmod(7, 3) + (1, 2)'))
print(eval('div_mod(77,3)'))


# 리스트에 양수만 반환하는 함수
def rtn_positive(in_list):
    rtn_list = []
    for val in in_list:
        if val > 0:
            rtn_list.append(val)
    return rtn_list
print(rtn_positive([1, -1, 2, -2, 3, -3]))

# filter
# filter(함수이름, 함수에 들어갈 반복가능한 자료형): 함수의 반환 값이 참인 것만 묶어서 반환!
def func_positive(x):
    return x > 0
print(list(filter(func_positive, [7, 2, -3, -4, 1, 9, 0])))
print(list(filter(lambda x: x>0, [7, 2, -3, -4, 1, 9, 0])))
print(list(filter(lambda x: x*2, [7, 2, -3, -4, 1, 9, 0]))) #참인것만 반환하므로, 0이 아닌 모든 데이터 반환
print(list(map(lambda x: x*2, [7, 2, -3, -4, 1, 9, 0])))
# list comprehension (리스트 내포)
positive_value = [value for value in [7, 2, -3, -4, 1, 9, 0] if value > 0]
print(f'================{positive_value}')

two_times_values = lambda x: x*2
in_list = [7, 2, -3, -4, 1, 9, 0]
print(two_times_values(in_list))


# isinstance(object, class)
class Person:
    pass

class Student(Person):
    pass

class Male:
    pass

a = Person()
b = Student()
c = Male()
print(isinstance(a, Person))
print(isinstance(b, Person))
print(isinstance(b, Student))
print(isinstance(c, Person))

# map(함수, 함수의 인자(입력) 값)
# 함수가 수행한 결과를 묶어서 반환 (filter: 함수의 수행 결과에서 참인 부분만 반환)
def two_times(x): return x * 2
in_list = [1, 2, 3, 4]
print(list(map(two_times, in_list)))
print(list(map(lambda x: x * 2, in_list)))
twotimes_list = [values * 2 for values in in_list]
print(f'============={twotimes_list}')

# zip
list_1 = [1, 2, 3]
list_2 = [2, 4, 5]
list_3 = list(zip(list_1, list_2))
print(list_3, list_3[0][0] + list_3[0][1])
print(list(zip("abc", "def")))





