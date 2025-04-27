n1 = input("Enter a binary number")
n2 = input("Enter another binary number")

sum = bin(int(n1, 2) + int(n2, 2))
print(f"The sum is: {sum[2:]}")
