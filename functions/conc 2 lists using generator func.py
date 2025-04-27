def concatenate_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item


# Example usage:

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

concatenated_list = list(concatenate_lists(list_a, list_b))

print("Concatenated List:", concatenated_list)
