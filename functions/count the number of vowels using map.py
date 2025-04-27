def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_counts = map(lambda char: char in vowels, s)
    total_vowels = sum(vowel_counts)
    return total_vowels

input_string = "Hello, World!"
result = count_vowels(input_string)
print(f"The number of vowels in the given string is: {result}")