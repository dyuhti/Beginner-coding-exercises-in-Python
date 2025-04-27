num = int(input("Enter a number"))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
sum1 = 0
while num > 0:
    m = num % 10
    sum1 = sum1 + m
    num = num // 10
if sum == sum1:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
