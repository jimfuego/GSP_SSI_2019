#!/usr/bin/env python
import turtle

# define a function to make a square
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# instantiate object
bob = turtle.Turtle()

# call function with bob as a parameter
square(bob, 150)

square(bob, 200)

square(bob, 250) 

# stay with us, bob
turtle.mainloop()
