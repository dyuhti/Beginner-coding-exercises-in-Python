s = "This is a sample string . It's string"
s1 = s.split()

freq_dict = {}
for char in s1:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

freq = sorted(freq_dict.items())
val = freq[len(freq) - 1][1]
f = dict(freq)
print(f)

for key, value in reversed(f.items()):
    if value < val:
        print("The 2nd most frequent char is:", key)
        break
