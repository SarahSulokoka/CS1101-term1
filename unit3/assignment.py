# Sara Sulokoka
# Unit 3 Assignment - Question 1
# Recursive countdown and countup functions

def countdown(n):
    """Counts down from n to Blastoff!"""
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    """Counts up from n to Blastoff!"""
    if n >= 0:
        print("Blastoff!")
    else:
        print(n)
        countup(n + 1)

# Main program
num = int(input("Enter a number: "))

if num > 0:
    countdown(num)
elif num < 0:
    countup(num)
else:
    countdown(num)  # zero → Blastoff!
