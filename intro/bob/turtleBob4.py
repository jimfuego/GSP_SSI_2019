#!/usr/bin/env python
import turtle

# define a function to make a square
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# instantiate object
bob = turtle.Turtle()

# call function with bob as a parameter
square(bob)

turtle.mainloop()
