s1 = input("Enter a string")
s2 = input("Enter another string")

if len(s1) != len(s2):
    print("It is not Anagram")
else:
    sorted_s1 = sorted(s1, key=str.lower, reverse=False)
    sorted_s2 = sorted(s2, key=str.lower, reverse=False)

    if sorted_s1 == sorted_s2:
        print("It is a anagram")
    else:
        print("It is not a anagram")
