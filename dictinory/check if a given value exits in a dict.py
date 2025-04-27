dictonary = {"e": 5, "f": 6, "g": 7, "a": 1, "b": 2, "c": 3, "d": 4}
flag = 1
for value in dictonary.values():
    if value == 9:
        print("Element present")
    else:
        flag = 0

if flag == 0:
    print("Element not present")
