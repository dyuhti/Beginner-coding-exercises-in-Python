my_list = ["python is best for coders", "python is fun", "python is easy to learn"]
li = " ".join(my_list)
l = li.split()

freq_dict = {}
for word in l:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

for word, freq in freq_dict.items():
    if freq == 1:
        print(word)
        break