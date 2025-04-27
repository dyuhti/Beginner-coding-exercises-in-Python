my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky', 'nerdy', 'geek', 'love',
           'questions', 'words', 'life']
l = []
n = 5
for i in range(0, len(my_list), n):
    l.append( my_list[i:i + n])
print(l)