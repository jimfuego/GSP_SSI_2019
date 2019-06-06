#!/usr/bin/env python
import turtle

# instantiate object
bob = turtle.Turtle()

# make a square, Bob
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
