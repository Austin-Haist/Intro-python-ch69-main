# Assignment 2
# Lists and Dictionaries


# --------------------
# LIST
# --------------------

# Create a new list
animals = ["dog", "cat", "rabbit", "hamster"]
print("Original list:", animals)
print("List length:", len(animals))


# Access an item by index
print("Item at index 1:", animals[1])
print("List:", animals)
print("List length:", len(animals))


# Replace a value
animals[2] = "parrot"
print("After replacing rabbit with parrot:", animals)
print("List length:", len(animals))


# Remove an item by value
animals.remove("hamster")
print("After removing hamster:", animals)
print("List length:", len(animals))


# --------------------
# DICTIONARY
# --------------------

# Create a new dictionary
pet = {
    "name": "Kira",
    "age": 5,
    "breed": "Shiba Inu"
}

print("Original dictionary:", pet)
print("Dictionary length:", len(pet))


# Access a value using a key
print("Pet name:", pet["name"])
print("Dictionary:", pet)
print("Dictionary length:", len(pet))


# Add a new key
pet["color"] = "red"
print("After adding color:", pet)
print("Dictionary length:", len(pet))


# Update an existing value
pet["age"] = 6
print("After updating age:", pet)
print("Dictionary length:", len(pet))


# Remove a key
pet.pop("color")
print("After removing color:", pet)
print("Dictionary length:", len(pet))