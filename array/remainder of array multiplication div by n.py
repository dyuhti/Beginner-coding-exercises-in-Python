arr = [100, 10, 5, 25, 35, 14]
n = 11
mul = 1
size = len(arr)
for i in range(size):
    mul = mul * arr[i]
result = mul % n
print(result)
