l = [3, 5, 1, 4, 1, 5, 8, 4, 9]
for num in reversed(l):
    if num % 2 == 0:
        l.remove(num)
print(l)
