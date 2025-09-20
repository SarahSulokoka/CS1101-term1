import turtle

def square(t):
    for i in range(4):
        t.forward(100)   # move forward 100 units
        t.left(90)       # turn left 90 degrees

sara = turtle.Turtle()
square(sara)

turtle.done()
