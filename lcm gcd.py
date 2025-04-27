def lcm(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while True:
        if (greater % n1 == 0) and (greater % n2 == 0):
            lcm = greater
            break
        greater += 1
    print("LCM",lcm)


def gcd(n1, n2):
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    print("GCD ",hcf)


x = int(input("Enter a number"))
y = int(input("Enter a number"))
lcm(x, y)
gcd(x, y)
