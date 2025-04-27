input_string = "This is an example sentence with long words."

words = input_string.split()

# Using max function with key=len to find the longest word
longest_word = max(words, key=len)

length_of_longest_word = len(longest_word)

print(f"The length of the longest word in the given string is: {length_of_longest_word}")
