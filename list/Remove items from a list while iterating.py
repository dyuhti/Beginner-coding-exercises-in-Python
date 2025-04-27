number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(number_list)
i=0
while i< n:
    if number_list[i] >50:
        number_list.pop()
        n=n-1
    else:
        i=i+1
print(number_list)