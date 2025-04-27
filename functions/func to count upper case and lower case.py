def count(s1):
    upper = 0
    lower = 0
    for c in s1:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
    print("Uppercase:",upper)
    print("Lowercase:",lower)


s = "The quick Brow Fox"
count(s)
