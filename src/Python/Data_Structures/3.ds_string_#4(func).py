str1 = """
Spread out before him that April day was the largest flotilla Communist-ruled China had ever put to sea at one time,
 48 ships, dozens of fighter jets, more than 10,000 military personnel.
"""

cnt_a = str1.count("ships")
print(cnt_a)
print(str1.find("jets"), str1.find("h"), str1.index("h"), str1.find("korea"))
print(str1.upper())
print(str1.lower())

str1 = "12345"
print(",".join(str1))

str_list = "Life is too short"
print(str_list.replace("short", "long"))
print(str_list)

str_list = str_list.split()
print(str_list, type(str_list))

str_list = "    ".join(str_list)
print(str_list, type(str_list))






