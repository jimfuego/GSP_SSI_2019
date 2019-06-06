#!/usr/bin/env python
print("")

def trueFalse(condition):
    if(condition == True):
        print("You entered True!")
    elif(condition == False):
        print("You entered False!")
    else:
        print("You did not enter a boolean!")

#print the true condition
trueFalse(True)

#print the false condition
trueFalse(False)

#print else condition
trueFalse(30)
