#!/usr/bin/env python
import turtle

# define a function to make a square
def polygon(t, numSides, length):
    angle = 360 / numSides
    for i in range(numSides):
        t.fd(length)
        t.lt(angle)

# instantiate object
bob = turtle.Turtle()

# call function with bob as a parameter
polygon(bob, 7, 70)

# polygon(bob, 7, 80)
#
# polygon(bob, 7, 90)

# stay with us, bob
turtle.mainloop()
