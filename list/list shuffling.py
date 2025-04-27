s1 = "welcome"
s2 = "homely"
l1 = list(s1)
p = len(s1)
q = len(s2)
c = 0
for i in range(0, p + q):
    if i % 2 != 0:
        l1.insert(i, s2[c])
        c += 1
v = 0
for i in l1:
    print(i, end="")
    if i in "aeiouAEIOU":
        v += 1
print(v)
