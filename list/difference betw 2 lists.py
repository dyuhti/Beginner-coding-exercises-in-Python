list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))

print("Difference1",diff1)
print("Difference2",diff2)