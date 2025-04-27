sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
list = []
size = len(sample_list)
for i in range(0, size):
    for j in range(0,size-i-1):
        if sample_list[i] == sample_list[j - 1]:
            if sample_list[i] not in list:
                list.append(sample_list[i])
list.remove(sample_list[0])


print(list)
