import json
import pickle
import random
import glob
import os

f = open("lib_example.txt", "wb")
data = {1: 'python',
        2: 'you need'
        }
pickle.dump(data, f)
f.close()

f = open("lib_example.txt", "rb")
data = pickle.load(f)
print(data, type(data))

print(random.random())
print(random.randint(1, 10))
data_rnd = [1, 2, 3, 4, 5]
random.shuffle(data_rnd)
print(data_rnd)

def refined_data(path):
        f = open(path)
        json_data = json.load(f)

        img = json_data["Image"]
        objects = json_data["Object"]
        mask = list(filter(lambda objects: objects["level"] == 0 and objects["class"] != "Dontcare", objects))

        for idx, val in enumerate(mask):
                if val["class"] == "Truck" or val["class"] == "Car":
                        mask[idx]["class"] = "Vehicle"
        f.close()

        rtn_data = {}
        rtn_data['Image'] = img
        rtn_data['Object'] = []
        # for idx in range(len(tmp)):
        for idx, _ in enumerate(mask):
                rtn_data['Object'].append(mask[idx])

        return rtn_data



dir = "D:/0.2022/002.강의/1학기/1.월_인공지능프로그래밍/0509"
files = glob.glob(dir + "/" + "CAM_FRONT/*.json")
file = files[0]
# print(file, len(files))
for idx, file in enumerate(files):
        data = refined_data(file)
        filename = os.path.basename(file)
        path = dir + "/CAM_FRONT/" + "modified_" + filename
        f = open(path, "w")
        json.dump(data, f, indent=2)
        f.close()
#
# f = open(file)
# f = open("CAM_FRONT/000000.json")
# filename = os.path.basename(file)
# print(filename)
# json_data = json.load(f)
#
#
# img = json_data["Image"]
# objects = json_data["Object"]
# # print(objects, len(objects))
# tmp = list(filter(lambda objects: objects["level"] == 0 and objects["class"] != "Dontcare", objects))
#
# for idx, val in enumerate(tmp):
#         print(idx, val)
#         if val["class"] == "Truck" or val["class"] == "Car":
#                 tmp[idx]["class"] = "Vehicle"
#
# print(tmp[0], len(tmp), tmp[0]["class"])
# f.close()
#
# file_path = "CAM_FRONT/" + "modified_" + filename
# print(file_path)
# # f = open("CAM_FRONT/modified_000000.json", "w")
# f = open(file_path, "w")
# # print(img)
# data_img = {}
# data_img['Image'] = img
# data_img['Object'] = []
# # for idx in range(len(tmp)):
# for idx, _ in enumerate(tmp):
#         data_img['Object'].append(tmp[idx])
# json.dump(data_img, f, indent=2)
# f.close()





