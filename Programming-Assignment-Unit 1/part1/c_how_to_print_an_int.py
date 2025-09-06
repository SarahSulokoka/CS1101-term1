print(09)
print(9)

# RESULT
# $ python c_how_to_print_an_int.py
#   File "C:\Users\Sarah\Desktop\CS1101-UNIT1\Programming-Assignment-Unit 1\part1\c_how_to_print_an_int.py", line 1
#     print(09)
#           ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# Explanation of Why the Error Happened
# The error occurs because, in Python, an integer literal (a number written directly in your code) cannot have leading zeros (a 0 at the beginning), with one specific exception.
# 1. The Problem with 09
# Python sees the integer 09 and gets confused. Here's why:
#     The leading 0 historically had a special meaning in programming languages: it signified that the number was an octal (base-8) number, not a decimal (base-10) number.
#     In the octal number system, only digits from 0 to 7 are valid. The digit 9 is invalid in octal.
#     So, when Python sees 09, it thinks you are trying to write an octal number because it starts with 0, but then it immediately sees the invalid digit 9 and throws a SyntaxError.
# The Key Reason: The digit 9 is out of range for the octal number system that the leading zero implies.

# 2. Why print(9) Works
# The integer 9 is a standard decimal integer literal. It has no leading zero to confuse the interpreter, so Python understands it perfectly and prints the value 9.

# How to "Fix" It (And What You Learned)
# If I want to display the number 09 (for example, to represent the day of the month or a sports jersey number), I cannot do it as an integer. I must represent it as a string by putting it in quotes. A string can contain any character, including leading zeros
# What I learned: This experiment teaches me about Python's syntax rules for writing numbers. Integers are for mathematical values, and their written form in code has specific rules. If I need to preserve formatting like leading zeros, I must use a string, even if the characters are digits. This is a crucial distinction between numeric data (used for calculations) and string data (used for text and display).