l = [1, 2, 0]

for i in range(1, len(l) - 1):
    if l[i] > l[i+1] and l[i] > l[i-1]:
        print("Index of", l[i], "is", i)
