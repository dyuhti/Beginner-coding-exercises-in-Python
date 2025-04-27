def remove_nth_occurrence(word_list, word, N):
    count = 0
    index_to_remove = None

    for i, w in enumerate(word_list):
        if w == word:
            count += 1
            if count == N:
                index_to_remove = i
                break

    if index_to_remove is not None:
        del word_list[index_to_remove]


list1 = ["geeks", "for", "geeks"]
remove_nth_occurrence(list1,"geeks",2)
print(list1)