
sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for char in sentence:
    if char.lower() in "aeiouAEIOU":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
