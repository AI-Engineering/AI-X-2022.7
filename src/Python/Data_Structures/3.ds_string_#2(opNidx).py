# String Operation
str1 = "Hi Everyone"
str2 = "My name is james"
str3 = "************" # Comment Block
print(f'{str3*10}\n{str1+str2},\n'
      f'This Block is comment block\n'
      f'{str3*10} ')

# print(str1-str2)

# indexing/Slicing
lenStr2 = len(str2)
# j --> "J"
print(str2[-5])
# str2[-5] = "J" # Error
print(id(str2))
str2 = str2[:-5]+"J"+str2[lenStr2-4:]
print(str2, id(str2))

a = 10
b = 10

print(id(a), id(b), id(a+b))



str2 = "20210308Sunny"
print('Today weather is ' + '\"' + str2[8:] + '\"')

print(str2[:-5] + str2[-5].upper() + str2[-4:])

