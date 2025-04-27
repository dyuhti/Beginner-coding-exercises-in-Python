num = int(input("Enter a number"))
a = 0
b = 1
print(f"{a}\n{b}")
for i in range(2, num):
    c = a + b
    print(f"{c}")
    a = b
    b = c
