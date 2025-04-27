l1 = [1, 2, 3, 4, 45]

l2 = [3, 5, 87, 2, 3]
new_list = []
for num in l1:
    for n in l2:
        if num == n and n not in new_list:
            new_list.append(num)
print(new_list)
