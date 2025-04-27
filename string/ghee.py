s1 = "ghee"
l = len(s1)


def char_frequency(s):
    freq_dict = {}
    for char in s1:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


d = char_frequency(s1)

for key, value in d.items():
    c = 1
    for i in range(0, value):
        print("next letter after", key, "is", chr(ord(key) + c))
        c += 1
