num = int(input("Enter a number"))
print("0 \n1")
a = 0
b = 1
c = 0
for i in range(3, num):
    c = a + b
    print(c)
    a=b
    b=c