a = [233, 2242, 41, 4332, 3456, 76652, 32, 56456, 5334]
size = len(a)
max=a[0]
for i in range(size):
    if max < a[i]:
        max = a[i]
print(max)
