dictonary = {"e": 5, "f": 6, "g": 7, "a": 1, "b": 2, "c": 3, "d": 4}


def char_frequency(dictonary):
    freq_dict = {}

    for char in dictonary.keys():
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


result = char_frequency(dictonary)
for char,count in result.items():
    print(f"{char}: {count}")