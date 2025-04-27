size = int(input("Enter the size of array "))
my_list = []

for i in range(size):
    element = input("Enter element {}: ".format(i + 1))
    my_list.append(element)
print(my_list)

ele = input("Enter element which you want to delete")
my_list.remove(ele)

print("Updated list: ", my_list)
