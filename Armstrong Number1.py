num = int(input("Enter a number"))
sum = 0
original_num = num
n = num
count = 0
while n != 0:
    n //= 10
    count = count + 1

while num != 0:
    digit = num % 10
    sum = sum + pow(digit, count)
    num = num // 10

if sum == original_num:
    print("It is Armstrong number")
else:
    print("It is not Armstrong number")
