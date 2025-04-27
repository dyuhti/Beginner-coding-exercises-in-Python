s = "ygtygnu"
r = 0
for c in s:
    if c.isdigit():

        continue
    else:
        r = 1
if r == 1:
    print("No digits")
else:
    print("Contains digits")
