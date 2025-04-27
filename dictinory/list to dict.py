l = ['a', 1, 'b', 2, 'c', 3]
dict = {}
for i in range(0, len(l), 2):
    dict[l[i]] = l[i + 1]
print(dict)
