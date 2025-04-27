l = [10, 20, 30, 40, 50]
l1=[]
sum=0

for i in range(1,len(l)+1):
    sum = sum+l[i-1]
    l1.append(sum)
print(l1)
