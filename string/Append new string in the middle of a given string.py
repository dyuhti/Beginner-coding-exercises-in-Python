s1 = str(input("Enter a string"))
s2 = str(input("Enter a string"))
size = len(s1)
mid = size//2
str1 = s1[:mid]
str2 = s1[mid:]
concat = str1+s2+str2
print(concat)