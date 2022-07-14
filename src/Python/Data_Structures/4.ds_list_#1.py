# list
list1 = [1, 2, 3, 0.1]
print(f'{list1}')
list2 = [30, 3, ["study", "bed", "game"], "1층", "3억"]
print(list2)
list3 = []
list3.append("1")
list3.append(32)
print(list3, type(list3[0]), type(list3[1]))

# list indexing/slicing
print(f'Start index of the List=%d, first data of a list3 = {list3[0]}' % 0)
print(list2[-3])
print("1+2=%d" % (list1[0] + list1[1]))
str2 = f'My house area is {list2[0]}, there are {len(list2[-3])} rooms and \n' \
       f'l like the {list2[-3][2]} room!\n' \
       f'{list2[-2:]} are shown in web site!'
print(str2)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(f'list 3 length is {len(list3)}: {list3}')