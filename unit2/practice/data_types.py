
#INTEGERS

a = 9
b = a * a - a -1
c = a * b
print(c)

if (a<0):
    print ("a<0")
    print(c)
else:
    print("a is not less than 0")
    print(c-a)

print("OK")


# //STRING


a = "My first test string"
b = 'Another test string that I have defined'
c = "This is Sal's string"
d = 'My favorite word is "asparaus" , what is yours?'
math_string = " 3 + 4 * 2"
expression_string = "a + '  ' + b + 'tiger' "

print(len(a))
print(len(math_string))

a_with_b = a + b

print(a_with_b)

math_string + expression_string

# b.split(' ')

# print(b)

parts = b.split("t")
print(parts)


print(b)

string_found = math_string.find('*')
print(string_found)


replaced_string = c.replace('i', 'o')
print(replaced_string)


eval(math_string)   #evaluates string as python codes
print(eval(math_string))
