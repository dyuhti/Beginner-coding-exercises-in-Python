num = int(input("Enter a number"))
a = 0
b = 1

for i in range(2, 101):
    c = a + b
    if c == num:
        print("Yes it is a fib number")
        break
    else:
        a = b
        b = c
