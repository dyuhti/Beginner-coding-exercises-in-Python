capitals = {
            "USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# Access values of a particular key
print(capitals.get("India"))

# check
if capitals.get("Japan"):
    print("That capital exits")
else:
    print("That capital dosent exist")

# Add a new key
capitals.update({"Germany": "Berlin"})
print(capitals)

# modify a key-value
capitals.update({"USA": "Detroit"})

# del a key value
capitals.pop("China")

# del the last element in a dict
capitals.popitem()

# clear dictionary
capitals.clear()

# To get only keys
keys = capitals.keys()

# Iterate over all keys
for key in capitals.keys():
    print(key)

# To get only values
values = capitals.values()

# Iterate over all values
for value in capitals.values():
    print(value)

# Returns a dict with a 2D list of tuples
items = capitals.items()

# iterate
for key, value in capitals.items():
    print(f"{key}:{value}")
