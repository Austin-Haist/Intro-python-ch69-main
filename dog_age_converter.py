# Dog Age Converter

# Ask the user for their dog's age and convert the input to an integer
dogAge = int(input("Enter your dog's age in human years: "))

# Multiply the dog's age by 7 to calculate the age in dog years
dogYears = dogAge * 7

# Display the result using an f-string
print(f"Your dog is {dogYears} years old in dog years!")