# Program to do operations on the name "Sara Sulokoka"

# Step 1: store my name
name = "Sara Sulokoka"

# Step 2: Ask the user how many letters from the left they want to see
n = int(input("Enter the number of letters to show from the left: "))

# Step 3: Show the first n letters using a loop
first_n_letters = ""
for i in range(n):
    first_n_letters += name[i]

print("First", n, "letters:", first_n_letters)


# Step 4: Count how many vowels are in my name
vowels = "aeiouAEIOU"
count = 0
for letter in name:
    if letter in vowels:
        count += 1
print("Number of vowels in my name:", count)

# Step 5: Show my name backwards using a loop
reversed_name = ""  # Start with an empty string

# Go through each letter in the name from the end to the start
for i in range(len(name)-1, -1, -1):
    reversed_name += name[i]  # Add each letter to the new string

print("My name reversed:", reversed_name)

