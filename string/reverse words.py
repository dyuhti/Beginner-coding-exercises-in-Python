

def rev(sen):
    words = sen.split(" ")
    new_word = [word[::-1] for word in words]
    r = " ".join(new_word)
    return r

s = 'My Name is Jessa'
print(rev(s))