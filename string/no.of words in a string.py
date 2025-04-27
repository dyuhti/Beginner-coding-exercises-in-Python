def count_words(input_string):
    words = input_string.split()
    return len(words)

# Example usage:
input_string = "This is an example sentence."
word_count = count_words(input_string)

print(f"The number of words in the given string is: {word_count}")