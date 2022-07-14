str_txt = "vehicle 10 10 50 50 vehicle 50 50 250 250"
str_tmp = str_txt.split()
print(str_tmp)

"""
Process
"""
for idx in range(0, len(str_tmp)):
    if idx % 5 == 0:
        obj = str_tmp[idx]
        x = str_tmp[idx + 1]
        y = str_tmp[idx + 2]
        w = str_tmp[idx + 3]
        h = str_tmp[idx + 4]
        print(idx, obj, x, y, w, h)
        if obj == "vehicle":
            if int(w)-int(x) > 100:
                str_tmp[idx] = "truck"
"""
Assign
"""
str_txt = ""
for i in range(0, len(str_tmp)):
    str_txt += str_tmp[i]
    str_txt = str_txt + " "
print(str_txt)

# str_txt = "vehicle 10 10 50 50 vehicle 50 50 250 250 "
data = ["vehicle", [10, 10, 50, 50], "vehicle", [50, 50, 250, 250], "pedestrian", [100, 100, 64, 128]]
print(data)
cnt_vd = int(len(data) / 2)
print(cnt_vd)
for idx in range(0, cnt_vd):
    obj = data[idx*2]
    x = data[idx * 2 + 1][0]
    y = data[idx * 2 + 1][1]
    w = data[idx * 2 + 1][2]
    h = data[idx * 2 + 1][3]
    print(obj, x, y, w, h)
    if obj == "vehicle":
        if w-x > 100:
            data[idx * 2] = "Truck"
    else:
        print(f'{obj} is not interest value!\n')
print(data)

str_txt = "vehicle 10 10 50 50 vehicle 50 50 250 250 "
str_tmp = str_txt.split()
print(str_tmp)

"""
Process
"""
for idx in range(0, len(str_tmp)):
    if idx % 5 == 0:
        obj = str_tmp[idx]
        x = str_tmp[idx + 1]
        y = str_tmp[idx + 2]
        w = str_tmp[idx + 3]
        h = str_tmp[idx + 4]
        print(idx, obj, x, y, w, h)
        if obj == "vehicle":
            if int(w)-int(x) > 100:
                str_tmp[idx] = "truck"
"""
Assign
"""
str_txt = ""
for i in range(0, len(str_tmp)):
    str_txt += str_tmp[i]
    str_txt = str_txt + " "
print(str_txt)