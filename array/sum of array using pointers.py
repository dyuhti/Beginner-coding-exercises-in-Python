size = int(input("Enter size of array"))
my_list = []
sum = 0

for i in range(size):
    ele = int(input("Enter a element {}".format(i + 1)))
    my_list.append(ele)
    sum = sum + ele

print("Sum", sum)
