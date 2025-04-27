
from functools import reduce

sentence = input("Enter a sentence")


def find(acc, word):
    return max(acc, len(word))


words = sentence.split()
max_length = reduce(find, words,0)
print(f"The length of the longest word in the sentence is: {max_length}")