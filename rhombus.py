num = 3

for i in range(1, num + 1):
    print(" " * (num - i), end="")
    print("* " * i)

for i in range(num - 1, 0, -1):
    print(" " * (num - i), end="")
    print("* " * i)