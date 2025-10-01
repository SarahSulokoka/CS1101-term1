# Part 2: Celsius to Fahrenheit Function
# Using incremental development


# Stage 1: Start with simple calculation
celsius = 0
fahrenheit = celsius * 9/5
print("Stage 1: Celsius to Fahrenheit without adding 32:", fahrenheit)
# Output: 0.0

# Stage 2: Add 32 to complete the formula
fahrenheit = celsius * 9/5 + 32
print("Stage 2: Celsius to Fahrenheit completed:", fahrenheit)
# Output: 32.0

# Stage 3: Wrap the calculation into a function
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return c * 9/5 + 32

# Stage 4: Test the function with three different inputs
print("Test 1: celsius_to_fahrenheit(0) =", celsius_to_fahrenheit(0))     # Output: 32.0
print("Test 2: celsius_to_fahrenheit(25) =", celsius_to_fahrenheit(25))   # Output: 77.0
print("Test 3: celsius_to_fahrenheit(-10) =", celsius_to_fahrenheit(-10)) # Output: 14.0
