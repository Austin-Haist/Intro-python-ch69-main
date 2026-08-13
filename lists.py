"""
List store multiple items in a sinlge variable
List are crated using = []
"""

my_list = [10, 20, 30, 40, 50]
print(my_list)

# Can contain different data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing items by INDEX
# indexing starts at 0

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
print(fruits[0])

# You can use NEGATIVE indexs to count from the END
print(fruits[-1])
print(fruits[-3])

# Modifiying List items
fruits[1] = "mango" # changes banana -> mango
print(fruits)

# Adding items
fruits.append("orange") # adds ONE item to the END of list
print(fruits)

fruits.insert(1, "kiwi") # adds before the index
print(fruits)

fruits.extend(["grape", "pear", "apple"]) # adds MULTIPLE items to the end of list
print(fruits)

# Removing Items
fruits.remove("apple")  # removes by exact VALUE (the first match it finds)
print(fruits)

fruits.pop()    # Removes the LAST item in list
print(fruits)

fruits.pop(3)   # can also remove from specific index
print(fruits)

#fruits.clear()  # Deletes the whole list leaving it empty []
#print(fruits)

# Looping through a list
for x in fruits:
    print(x)

# Checks if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

# List length
print(len(fruits)) # Number of items in list

# Slicing a list
# Slicing lets you grab a RANGE of items using [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  #index 2 - 5
print(numbers[:4])   #start from the very beginning up to index 4
print(numbers[6:])   #starts at index 6 till the end of list
print(numbers[-3:])  #returns last 3 items
print(numbers[::2])  #step skips every 2nd item

# useful list methods
numbers = [4, 2, 9, 1, 7]

print(numbers.count(2)) # counts number of times the item is in the list
print(numbers.index(9)) # Returns the index where the item first appears

numbers.sort()          # Sorts the list in place (smallest to largest)
print(numbers) 

numbers.sort(reverse=True)# Sorts the list in place (largest to smallest)
print(numbers)

numbers.reverse() # flips current order of the list
print(numbers)

number_copy = numbers.copy() # makes a real COPY of the list
print(number_copy)



# -------------------------------
#  MINI CHALLENGE: THE GROCERY LIST
# -------------------------------
# You're building a grocery list app.

# 1. Create a list called "groceries" with at least 5 items.
# 2. Print the first and last item using indexing.
# 3. Use slicing to print just the first 3 items.
# 4. Add "eggs" to the end of the list using append().
# 5. Insert "milk" at the very beginning of the list.
# 6. Remove one item using remove().
# 7. Check if "bread" is in the list — print a message either way.
# 8. Sort the list alphabetically and print it.
# 9. Print how many items are in the final list.

