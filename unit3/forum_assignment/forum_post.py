# Conditionals control the flow of a program by executing different blocks of code depending on certain conditions.
# There are different types of conditionals, like chained and nested conditionals, which we can use depending on the situation.

# Chained conditional: uses if, elif, and else to check multiple conditions one after another.
# Only one branch will run, the first one that evaluates to True. For example:

temperature = 15
if temperature > 30:
    print("It is hot")
elif temperature > 20:
    print("It is warm")
elif temperature > 10:
    print("It is cool")
else:
    print("It is cold")

# Output (with temperature = 15):
# It is cool
# Python checks the first condition (> 30) → false, then the next (> 20) → false, then (> 10) → true, so it prints “It is cool.”

____________________________________________________________________________________

# Nested conditional: one conditional inside another. For example:

age = 25
if age >= 18:
    if age < 65:
        print("Adult (working age)")

# Output: Adult (working age)
# Explanation: The first check age >= 18 is true, so Python goes inside and checks age < 65, which is also true. 
# That’s why it prints “Adult (working age).”
# Nested conditionals can get messy because adding more layers makes code harder to read.

____________________________________________________________________________________

# Simplifying nested conditionals with logical operators:

age = 25
if age >= 18 and age < 65:
    print("Adult (working age)")

# This produces the same output but is shorter and easier to read.

____________________________________________________________________________________

# In summary, chained conditionals are useful when checking multiple distinct options, 
# while nested conditionals can be simplified with logical operators to improve readability.

# Discussion Question:
# When designing conditionals, how do you decide whether to use a chained structure or logical operators to simplify your code?
