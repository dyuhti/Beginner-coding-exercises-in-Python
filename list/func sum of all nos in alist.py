def add(l, s):
    sum=0
    for i in range(0, s):
        sum = sum + l[i]
    return sum


list = [8, 2, 3, 0, 7]
size = len(list)
print(add(list, size))
