original_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
unique_list = []

for element in original_list:
    if element not in unique_list:
        unique_list.append(element)
print(unique_list)