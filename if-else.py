"""
An if-else statement in python is a conditionsal control structure that lets you 
decide which block of code to run depending on wheather a condition is True or False.

The if block runs only if the condition evaluates to True.
- If the condition is False, the else block runs instead
- You can also add elif (else if) blocks to check multiple conditions in a sequence

if condtition:
    - Code block runs if condition is true
elif another_condition:
    - Code block runs if the first condition is False
    - and this condition is True
else:
    - Code block always runs if none of the above conditions are True
"""

x = 7

if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short Hand IF statements
if x > 5: print("x is greater than 5")

# Short hand IF...ELSE
print("Even") if x % 2 == 0 else print ("Odd")

# Nested IF statements
x = 21
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions
age = 19

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")

"""
Mini challenge

1. Ask the user to enter a number from 0-100 and store it in a variable called "score".
2. If the score is 90 or above, print "Grade: A".
3. If the score is between 80-89, print "Grade: B".
4. If the score is between 70-79, print "Grade: C".
5. Otherwise, print "Grade: F".

6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
 BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"

"""

score = float(input("number"))
if score >= 90:
    print("90")
elif score >= 80:
    print("80")