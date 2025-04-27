num = int(input("Enter your choice"))
m = 0
sum = 0
while num > 0:
    m = num % 10
    sum = sum + m + 1
    num = num // 10
print(f"Sum is {sum}")
