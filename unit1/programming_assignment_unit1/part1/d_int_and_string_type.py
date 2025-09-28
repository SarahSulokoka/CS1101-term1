print('67')
print(67)

print(type(67))
print(type('67'))

# Explanation of the Difference
# Although the output looks identical, Python treats the two values in a fundamentally different way.
# The difference is that '67' is a string (text), while 67 is an integer (a number).

#     '67': The quotation marks tell Python, "This is a piece of text." You cannot perform mathematical operations on it. '67' + 1 would cause an error.

#     67: This is a numerical value. Python understands it as a number that you can use in calculations. 67 + 1 would give the result 68.

# Justification with Code

# The type() function proves this difference, which is what the assignment asks for.
# python

# print(type('67'))
# print(type(67))

# Output:
# text

# <class 'str'>
# <class 'int'>

#     <class 'str'> means the value is a string.

#     <class 'int'> means the value is an integer.

# What I Learned
# I learned that the presence or absence of quotation marks changes how Python interprets data. The visual output can be the same, but the data type underneath is completely different. This is crucial because it determines what operations you can perform on the value. You can do math with int, but you can only do things like concatenation (e.g., '67' + '1' = '671') with str.
