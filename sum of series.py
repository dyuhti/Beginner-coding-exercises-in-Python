#Python Program for Program to find the sum of a Series 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
n = int(input("Enter a number"))
r = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    r = r + (i / fact)
print(r)
