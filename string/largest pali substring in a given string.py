def is_plai(substring):
    return substring == substring[::-1]


def longest_plai(s):
    n = len(s)
    max_length = 0
    max_pali = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if is_plai(substring) and len(substring) > max_length:
                max_length = len(substring)
                max_pali = substring
    return max_pali


s = str(input("Enter a string"))
result = longest_plai(s)
print(f"The longest palindrome substring is: {result}")
