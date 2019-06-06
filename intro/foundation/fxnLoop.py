#!/usr/bin/env python
print("\n")

# Prints out numbers from 0 to "limit"
def variableLoop1(limit):
    print("print numbers between 0-{}".format(limit))
    for x in range(limit):
        print(x)
    print("\n")

# Prints out numbers from "start" to "limit"
def variableLoop2(start, limit):
    print("print numbers between {}-{}".format(start, limit - 1))
    for x in range(start, limit):
        print(x)
    print("\n")

# prints from 0-9
print("print 0-9")
variableLoop1(10)

# prints from 0-14
print("print 0-14")
variableLoop1(15)

# prints from 5-9
print("print 5-9")
variableLoop2(5, 10)

# prints from 20-29
print("print 20-29")
variableLoop2(20, 30)

#CHALLENGE:
# create a function that prints all odd numbers from between 0 and 20
