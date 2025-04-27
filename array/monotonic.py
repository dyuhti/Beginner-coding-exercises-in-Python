arr = [5, 15, 20, 10]
c = 0
for i in range(1):
    for j in range(1):
        if i < j + 1:
            c = 1
        else:
            c = 2


def check(c, ar):
    for i in range(len(ar)-1):
        if c == 1 and ar[i] > ar[i + 1]:
            return False
        elif c == 0 and ar[i] < ar[i + 1]:
            return False
    return True


print(check(c, arr))
