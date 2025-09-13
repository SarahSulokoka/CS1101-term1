# Example 1: Define a function that takes an argument, call it, identify argument vs. parameter

#Explanation:
# Parameter: name is the placeholder in the function definition that will receive a value when the function is called.
# Argument: "Alice" is the actual value passed to the function when calling it.

# Function definition: 'name' is the parameter
def greet(name):
    print("Hello, " + name + "! Welcome to Python.")

# Function call: "Alice" is the argument
greet("Alice")

output: Hello, Alice! Welcome to Python.




_______________________________________________________________________________________________________

# Example 2: Call the function three times with different kinds of argumentsExplanation:
# Literal: Direct value "Bob"
# Variable: user_name stores the value "Charlie"
# Expression: "D" + "aisy" evaluates to "Daisy"

# Calling the function with a value (literal)
greet("Bob")  # Argument is a literal value

# Calling the function with a variable
user_name = "Charlie"
greet(user_name)  # Argument is a variable

# Calling the function with an expression
greet("D" + "aisy")  # Argument is an expression

# output for each: 
# Hello, Bob! Welcome to Python.
# Hello, Charlie! Welcome to Python.
# Hello, Daisy! Welcome to Python.


# _______________________________________________________________________________________________________________

#Example 3: Function with a local variable
#Explanation:
# result is a local variable, meaning it only exists inside add_five.
# Accessing it outside the function causes a NameError because Python cannot find result in the global scope.

def add_five(number):
    result = number + 5  # 'result' is local to the function
    print("Inside function:", result)

    add_five(10)
    

# output: Inside function: 15


# Trying to use 'result' outside the function
# print(result)  causes an error, I get nothing

________________________________________________________________________________________________

# Example 4: Function with a uniquely named parameter
# Explanation:

# num_to_square is the parameter and exists only inside the function.You cannot “call” or access num_to_square itself outside the function. You have to return a value or store it in a global variable.

# Using it outside the function scope leads to an error because Python treats it as local to the function.

def square(num_to_square):
    squared_value = num_to_square ** 2
    print("Squared value:", squared_value)

square(4)

# output: Squared value: 16


# Trying to access 'num_to_square' outside the function
# print(num_to_square)  # This will cause an error


___________________________________________________________________________________________________

# Example 5: Variable outside vs. inside the function with the same name
# Explanation:

# Inside the function, value refers to the local variable 100.

# Outside, value still refers to the global variable 50.

# Local variables shadow global variables inside the function, but do not change the global value unless explicitly declared global.


value = 50  # Global variable

def change_value():
    value = 100  # Local variable with same name
    print("Inside function:", value)

change_value()
print("Outside function:", value)

# output : 
# Inside function: 100
# Outside function: 50



# How can confusing local and global variables cause unexpected results in a program, and what are some best practices to manage variable scope effectively?

# Personally, I find this a bit confusing because I am more used to Java, which provides more protection when dealing with local and global variables. I hope that as I gain more experience with coding in Python, these concepts will become clearer.



# outputs:

# Hello, Alice! Welcome to Python.
# Hello, Bob! Welcome to Python.
# Hello, Charlie! Welcome to Python.
# Hello, Daisy! Welcome to Python.
# Inside function: 15
# name 'result' is not defined
# Squared value: 16
# name 'num_to_square' is not defined
# Inside function: 100
# Outside function: 50
