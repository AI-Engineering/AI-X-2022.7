# Practice 1
a = {1: 'a', 2: 'b'}
a[3] = 'c'
print(a)
a['name'] = ["Shin", "Park", "Kim"]
print(a)
del a[1] # Dictionary a에서 key가 1인 key:value 쌍을 삭제한다.
print(a)
a = {"Dept": ["AI-Engineering", "Smart Electronic"], "StudentNum": [22, 60]}
print(a['Dept'], a['StudentNum'])
a = {'1': 'a', '2': 'b', '3': 'c'}
# Key를 중복해서 사용하면 하나만 남기고 나머지는 무시
a['1'] = 'aa'
a['1'] = 'aaa'
print(a)

# Error Case  키는 고유값이므로 변하는 자료형을 사용하면 안됨.
a = {
#    ['name', 'age']: (["Shin", "Kim", "Park"], [22, 23, 25])
    ('name', 'age'): (["Shin", "Kim", "Park"], [22, 23, 25])
}
print(a)
