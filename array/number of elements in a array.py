size = int(input("Enter the size of array "))
list = []

for i in range(size):
    element = input("Enter element {}: ".format(i + 1))
    list.append(element)
print(list)
print("\nLength is ", len(list))
