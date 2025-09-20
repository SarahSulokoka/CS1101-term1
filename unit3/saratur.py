import turtle

# def square(t):
#     for i in range(4):
#         t.forward(100)   # move forward 100 units
#         t.left(90)       # turn left 90 degrees

# sara = turtle.Turtle()
# square(sara)

# turtle.done()



def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()
square(bob, 150)   # try different lengths
