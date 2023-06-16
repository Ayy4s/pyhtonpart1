list1 = ["lion", "monkey", "dog", "fish"]
tuple1 = ("lion", "monkey", "dog", "fish")
set1 = {"lion", "monkey", "dog", "fish"}
dict1 = {"lion": "land", "monkey": "land", "dog": "land", "fish": "water"}

# Iterate through list1
print("Elements of list1:")
for item in list1:
    print(item)

# Iterate through tuple1
print("\nElements of tuple1:")
for item in tuple1:
    print(item)

# Iterate through set1
print("\nElements of set1:")
for item in set1:
    print(item)

# Iterate through dict1 and print elements living on land
print("\nElements living on land in dict1:")
for key, value in dict1.items():
    if value == "land":
        print(key + " lives in " + value)
