p = float(input("Enter the principal amount"))
r = float(input("Enter the annual interest rate"))
n = int(input("Enter number of times that interest is compounded per unit"))
t = int(input("The money that is invested or borrowed for, in years"))
nt = n*t
P=p(1+(r/n))
c = pow(P,nt)
print("Compound Interest",c)
