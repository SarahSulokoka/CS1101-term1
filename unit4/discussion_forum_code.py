# Debugging in Python
# According to the book, if a function is not working there are 3 main reasons:
# 1. The arguments are wrong (precondition is violated).
# 2. The function logic itself is wrong (postcondition is violated).
# 3. The return value is correct, but the caller uses it in the wrong way.

# -----------------------------------
# 1) Precondition violated (bad arguments)
def divide(a, b):
    # precondition: b must not be 0
    return a / b

print(divide(10, 0))  
# This crashes with ZeroDivisionError because the caller gave b=0.
# The function assumed the precondition (b != 0) was true, but it was not.

# Safer version with precondition check:
def divide_safe(a, b):
    if b == 0:
        print("Error: precondition violated, b must not be 0")
        return None
    return a / b

print(divide_safe(10, 0))  
# This prints an error message and returns None instead of crashing.


# -----------------------------------
# 2) Postcondition violated (bug inside the function)
def get_max(nums):
    # postcondition: should return the maximum number in the list
    max_val = nums[0]
    for x in nums:
        if x < max_val:   # BUG: wrong sign, this actually finds the minimum
            max_val = x
    return max_val

print(get_max([3, 7, 2, 9]))  
# Wrong result -> 2, because the function logic is broken.
# The postcondition "returns max" is not true.

# Fixed version:
def get_max_fixed(nums):
    max_val = nums[0]
    for x in nums:
        if x > max_val:   # correct sign now
            max_val = x
    return max_val

print(get_max_fixed([3, 7, 2, 9]))  
# Correct result -> 9


# -----------------------------------
# 3) Wrong usage of return value
def split_name(fullname):
    # This function returns a list of words, e.g. ["Alice", "Smith"]
    return fullname.strip().split()

print(split_name("Alice Smith").upper())  
# ERROR: AttributeError, because .upper() works on strings, not on lists.
# The function worked fine, but the caller used the return value incorrectly.

# Correct usage:
parts = split_name("Alice Smith")
print(parts[0].upper())  
# This prints "ALICE" which makes sense.
