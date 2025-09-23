# Sara Sulokoka
# Unit 3 Assignment - Question 2
# Program to handle division by zero using if/elif/else

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check for division by zero
if num2 == 0:
    # If the second number is zero, show an error message
    print("Error: You cannot divide by zero. Please enter a non-zero second number.")
else:
    # If the second number is not zero, perform division
    result = num1 / num2
    print("Result:", result)
