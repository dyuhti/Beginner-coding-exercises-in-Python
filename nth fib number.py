num = int(input("Enter a number"))
a = 0
b = 1
c = 0
for i in range(0, 100):
    c = a + b
    if num == 1:
        print(f"{num}th Fib is 0")
        break
    elif num == 2:
        print(f"{num}th Fib is 1")
        break
    elif i == num - 3:
        print(f"{num}th Fib is {c}")
        break
    else:
        a = b
        b = c
