string = "heeh"
flag = 1
size = len(string)
for i in range(size // 2):
    if string[i] != string[size - i - 1]:
            flag = 0
            break
if flag == 1:
    print("It is a palindrome")
if flag == 0:
    print("It is not a palindrome")
