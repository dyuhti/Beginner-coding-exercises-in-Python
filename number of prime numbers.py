from sympy import isprime

count = 1
num = int(input("Enter a range"))
for i in range(2, num + 1):
    if isprime(i):
        print(i)
        count += 1
print("The number of prime numbers are ", count)
