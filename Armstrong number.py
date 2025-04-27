num = int(input("Enter a number"))
original_num=num
sum=0
count = 0

while original_num > 0:
    count +=1
    original_num //=10
original_num = num

while original_num > 0:
    m = original_num % 10
    sum=sum+pow(m,count)
    original_num//= 10

if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
