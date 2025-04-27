even = 0
odd = 0
n = int(input("Enter a number"))
for num in range(n):
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even: ", even)
print("Odd: ", odd)
