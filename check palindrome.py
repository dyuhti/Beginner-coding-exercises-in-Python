num = int(input("Enter a number"))
n = num
rev = 0
while n != 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if rev == num:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
