s1 = str(input("Enter a string"))


def char_frequency(s):
    freq_dict = {}

    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


result = char_frequency(s1)
print("Character Frequency")
for char, count in result.items():
    print(f"{char}: {count}")
