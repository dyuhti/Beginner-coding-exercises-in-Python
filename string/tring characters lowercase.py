s = str(input("Enter a string"))


def custom_sort(char):
    return char.islower(), char


r = ''.join(sorted(s, key=custom_sort))
print(r)
