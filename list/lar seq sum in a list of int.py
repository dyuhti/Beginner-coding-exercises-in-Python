def largest_sequence(arr):
    max_sum=0
    
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


input_list = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = largest_sequence(input_list)
print(f"Largest sequence sum: {result}")