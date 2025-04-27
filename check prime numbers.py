from sympy import isprime

num = int(input("Enter the interval"))
for i in range(2, num+1):
    if isprime(i):
        print(i)