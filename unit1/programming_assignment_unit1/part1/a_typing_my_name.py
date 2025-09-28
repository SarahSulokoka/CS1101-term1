print("Sara Sulokoka")

# Output would be : Sara Sulokoka since the command is correct


# print(Sara Sulokoka")
      
# I get a warnning since a quotation is missing , no output given. 

#     print(Sara Sulokoka")
# SyntaxError: unterminated string literal (detected at line 6)
# [Done] exited with code=1 in 0.358 seconds.

# Why this happened: In this line, I forgot the opening quotation mark before Sara. Python reads the code and sees Sara Sulokoka"). It interprets Sara as a variable name and Sulokoka") as another variable or command. Since this sequence of words and parentheses doesn't follow any valid Python grammar rules, the interpreter throws a SyntaxError. It essentially says, "This code is grammatically incorrect and I cannot understand it." The suggestion about a missing comma is the interpreter's best guess, but the real mistake is the missing quotation mark.

# What I learned : This experiment demonstrates a fundamental rule in Python and most programming languages: text must be enclosed in quotation marks to be distinguished from code. Without them, the interpreter tries to execute the text as if it were a command or a variable name, leading to errors. The type of error (SyntaxError vs. NameError) helps a programmer diagnose the specific nature of the mistake.
