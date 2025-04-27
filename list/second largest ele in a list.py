list = [3, 1, 4, 7, 2, 8, 5]
largest = list[0]
second_largest = 0
for num in list:
    if num > largest:
        second_largest = largest
        largest = num
print(second_largest)