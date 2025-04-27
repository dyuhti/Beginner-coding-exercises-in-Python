def common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common_chars = set1.intersection(set2)

    return common_chars


# Example usage:
string1 = "hello"
string2 = "world"

result = common_characters(string1, string2)

if result:
    print(f"Common characters between '{string1}' and '{string2}': {result}")
else:
    print(f"There are no common characters between '{string1}' and '{string2}'.")
