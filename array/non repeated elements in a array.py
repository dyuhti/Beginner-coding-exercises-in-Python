size = int(input("Enter the size"))
my_list = []

for i in range(size):
    element = int(input("Enter element {}".format(i + 1)))
    my_list.append(element)
print(my_list)

for i in range(size - 1, 0, -1):
    if my_list[i] == my_list[i - 1]:
        my_list.pop(i)
print(my_list)
