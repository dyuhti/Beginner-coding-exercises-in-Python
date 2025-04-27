num = int(input("Enter a number"))
mul = 1
if num == 0:
    print("1")
elif num < 0:
    print("Not defined")
else:
    for i in range(2, num + 1):
        mul = i * mul
    print(mul)
