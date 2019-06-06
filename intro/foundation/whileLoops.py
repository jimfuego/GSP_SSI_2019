#!/usr/bin/env python
print("\n")

# Prints out 0,1,2,3,4
count = 0
print("print 0-4")
while count < 5:
    print(count)
    count += 1
print("\n")

# Prints out 0,1,2,3,4
print("print 0-4; terminate with a break")
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("\n")

# Prints out 0,1,2,3,4
print("print 0-4; terminate with a condition")
condition = True
while (condition):
    print(count)
    count += 1
    if count >= 5:
        condition = False
print("\n")

# Prints out only odd numbers - 1,3,5,7,9
print("print odd numbers between 0-9")
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
print("\n")

# these scripts were stolen (and slightly modified) from learnpython.org ;)
