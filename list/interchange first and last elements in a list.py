a = [1, 2, 3, 4, 5, 6, 7]
size = len(a)
first = a[0]
last = a[size - 1]
a[0] = last
a[size - 1] = first
print(a)
