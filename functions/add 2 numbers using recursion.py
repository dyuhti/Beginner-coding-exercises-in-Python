def add_numbers_recursive(a, b):
    if b == 0:
        return a
    else:
        return add_numbers_recursive(a + 1, b - 1)

# Example usage:
num1 = 5
num2 = 3

result = add_numbers_recursive(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")