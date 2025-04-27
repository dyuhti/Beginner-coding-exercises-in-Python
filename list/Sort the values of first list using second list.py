x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = []
    for _, x in sorted(zipped_pairs):
        z.append(x)
    return z


print(sort_list(x, y))
