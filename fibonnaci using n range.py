n = int(input("Enter a number"))
l = []
a = 0
b = 1
c = 0
l.append(a)
l.append(b)
for i in range(3, n + 1):
    c = a + b
    l.append(c)
    a = b
    b = c
print(l)