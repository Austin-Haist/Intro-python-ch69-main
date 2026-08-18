"""
A while loop repeats a block of code as long as a conditoin is True.
BE CAREFUL - if the condition NEVER becomes FALSE, you'll get an INFINITE loop!

while condition:
    # Code block runs as long as the condition is True
"""

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1

print("-------------------------------------------")

# USING break to STOP the loop

count = 0 # initialize count at 0

while count <= 10:
    print(count)
    count += 1
    if count == 6:
        break

print("-------------------------------------------")

# using CONTINUE to SKIP an iteration
count = 0
while count <= 10:
    count += 1
    if count == 6:
        continue
    print(count)

print("-------------------------------------------")

# ELSE WITH WHILE
# The else block runs when the loop condition becomes FALSE (not by break)
count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop Finished!")


"""
-------------------------------
MINI CHALLENGE: WHILE LOOP
-------------------------------
Guess the Secret Number
1. Create a variable called secret_number
and set it equal to 7.
2. Ask the user to guess the number.
3. Use a while loop to keep asking until
they guess correctly.
4. If the guess is too low:
print "Too low!"
5. If the guess is too high:
print "Too high!"
6. When the user guesses correctly:
print "Correct!"
BONUS:
Count how many guesses the user needed.
"""













































