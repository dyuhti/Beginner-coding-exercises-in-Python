num = int(input("Enter a number"))
rev = 0
original = num
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if rev == original:
    print("It is a palindrome")
else:
    print("It is not a palindrome")