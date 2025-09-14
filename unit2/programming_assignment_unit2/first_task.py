# Function to calculate and print the circumference of a circle

# This function calculates the circumference of a circle.
# Formula: circumference = 2 * pi * r
# pi is taken as 3.14159 (rounded to five decimal places).
# The function prints the calculated circumference.

def print_circum(radius):

    
    pi = 3.14159   # value of pi
    circumference = 2 * pi * radius   # formula
    print(f"The circumference of a circle with radius {radius} is {circumference}")

# Calling the function three times with different radius values
print_circum(5)    # Example radius 1
print_circum(10)   # Example radius 2
print_circum(2.5)  # Example radius 3

# Output:
# The circumference of a circle with radius 5 is 31.4159
# The circumference of a circle with radius 10 is 62.8318  
# The circumference of a circle with radius 2.5 is 15.70795
