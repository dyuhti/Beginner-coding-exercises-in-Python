s = "Hello, this is a sample striq1ng."
sub = "sample"

index = s.find(sub)
if index!=-1:
    print(f"Substring '{sub}' found at index {index}.")
else:
    print(f"Substring '{sub}' not found.")