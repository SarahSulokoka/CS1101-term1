# --------------------------------------
# Part 1: Hypotenuse Function
# Using incremental development (beginner-friendly)
# --------------------------------------

# Stage 1: Start with squaring the numbers
a = 3
b = 4
print("Stage 1: Squares of a and b are:", a**2, b**2)
# Output: 9 16

# Stage 2: Add the squares together
sum_squares = a**2 + b**2
print("Stage 2: Sum of squares is:", sum_squares)
# Output: 25

# Stage 3: Take the square root of the sum using **0.5
hyp = sum_squares ** 0.5
print("Stage 3: Hypotenuse is:", hyp)
# Output: 5.0

# Stage 4: Wrap the calculation into a function
def hypotenuse(a, b):
    """Return the length of the hypotenuse of a right triangle"""
    return (a**2 + b**2) ** 0.5

# Stage 5: Test the function with three different calls
print("Test 1: hypotenuse(3,4) =", hypotenuse(3,4))    # Expected 5.0
print("Test 2: hypotenuse(5,12) =", hypotenuse(5,12))  # Expected 13.0
print("Test 3: hypotenuse(8,15) =", hypotenuse(8,15))  # Expected 17.0
