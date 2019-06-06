#!/usr/bin/env python
print("\n")

# set false condition
condition1 = False
if(condition1 == True):
    print("this SHOULD NOT print")

# set true condition
condition2 = True
if(condition2 == True):
    print("this SHOULD print\n")

# numeric example
x = 10
y = 20
z = x + y
if(z == 30):
    print("z equals 30, folks\n")

# greater than
if(z > 20):
    print("z is greater than 30, so this will print\n")

# less than
if(z < 20):
    print("z is greater than 30, so this won't print")
