n = 5
for i in range(n + 1):
    for j in range(n - i):
        print(' ', end=' ')

    c = 1
    for j in range(1, i + 1):
        print(c, ' ', sep=' ', end=' ')
        c = c * (i - j) // j
    print()
