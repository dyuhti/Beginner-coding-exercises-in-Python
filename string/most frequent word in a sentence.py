def most_frequent_word(sentence):
    words = sentence.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    most_common_word = max(word_counts, key=word_counts.get)
    frequency = word_counts[most_common_word]

    return most_common_word, frequency


sentence = "This is a sample sentence. Sample sentence with a repeated word."
most_common_word, frequency = most_frequent_word(sentence)

print(f"The most frequent word is '{most_common_word}' with a frequency of {frequency} times.")
