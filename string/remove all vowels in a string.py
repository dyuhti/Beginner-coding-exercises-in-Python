s1 = str(input("Enter a string"))
result = ""
for s in s1:
    if s not in "aeiouAEIOU":
        result += s
print(result)
