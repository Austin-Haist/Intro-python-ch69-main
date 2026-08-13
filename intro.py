print("Hello world from python!")
print(2)
print(5 + 3)
print(True) # this works

# SHORTCUTS:
# save file: ctrl + s windows| cmd+s mac
# up on arrow key gose to previous commands

# SINGLE LINE Comments

"""
Multi line make sure to use 3 quotes before and after 
"""
'''
this works too with single quotes
'''

# Variables and Concatenation
name = "Leo"
age = 28
print(name, age)

# cant concatinate an interger with a string
print("My name is " + name + " an I am " + str(age) + " years old.")


"""
Write a short story using variables.
1. Declare and initialize 5 variables (strings and numbers)
2. use print() and concatenation to tell a story
3. run the program in terminal
"""

place = "Disneyland"
activity = "riding the rollercoaster"
members = 5
print("The last time I went to " + place + ", i had a greate time " + activity + " with " + str(members) + " friends.")

# F-String
print(f"The last time I went to {place}, and i had a great time {activity}; with all {members} friends.")

# Multi-line f-string
print(f"""The last time I went to {place}, and i
                 had a great time 
{activity}; with all {members}

 friends.""")

# Type Function
print(type(name))  # string
print(type(age))   # int
print(type(False)) # bool

# Casting (changing data types)
print(20 + int("20"))
print(20 + age)

# User Input Function
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# input() always returns a sting
# print(type(input("Enter your name: ")))

# new_age = int(input("Enter your age: "))
# print(age + new_age)

"""
Pizza Calculator
1. Ask how many slices of pizza and how many people.
2. Use math operators to calculate variable = slices per person. (divide /)
3. Show the results with an f-string
"""

slices = int(input("How many silce of pizza you you want? "))
people = int(input("How many people are sharing the pizza? "))

slice_per_person = slices / people

print(f"Each person gets {slice_per_person} slices of pizza")
