"""
A function is a block of code that only runs when its called.
We can pass data to functions (parameters), and they can return data as a result.

def function_name(parameters):
    Code block (indented)
    Prefom actions using the parameters
    return value # optional
"""

# Simple function without parameters
# It wont run until we CALL the function by its name
def my_function():
    print("This is my function") # This is the line that runs when the function is called

# calling the function
my_function()

# Functions with parameters
# Parameters allow us to pass information into a function
def print_full_name(fname, lname):
    print(f"The name is: {fname} {lname}")

print_full_name("Leo", "Flores")

# Functions that return values
# Instead of just printing, functions can send back (return) data

def print_full_name(fname, lname):
    return f"{fname} {lname}" # sends back the full name as text

full_name = print_full_name("Leo", "Flores")
print(full_name)


# Functions with default parameters
# A default parameter means the funcion will use that value
# if no argument is provided when calling the function.

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

# Calling with no argument update -> uses the default
greet()

# calling with an argument -> overrides the default
greet("Leo")






































