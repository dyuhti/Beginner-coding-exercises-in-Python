num = int(input("Enter a number"))
count = 0
for i in range(num):
    if i % 5 == 0:
        count += 1
print(f"Count: {count}")
