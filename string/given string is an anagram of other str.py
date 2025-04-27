s1 = str(input("Enter sting 1"))
s2 = str(input('Enter string 2'))

if len(s1) != len(s2):
    print("It is not an Anagram")
else:
    sort_s1 = sorted(s1, reverse=False)
    sort_s2 = sorted(s2, reverse=False)
    if sort_s1 == sort_s2:
        print("It is an Anagram!")
    else:
        print("It is not a anagram!")