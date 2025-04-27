s = str(input("Enter a string"))
size = len(s)
m = size//2
m1 = m-1
m2 = m+1
c = s[m1]+s[m]+s[m2]
print(c)
