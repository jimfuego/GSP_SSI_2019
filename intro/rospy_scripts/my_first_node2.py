#!/usr/bin/env python

#just like we had to import the turtle mod
import rospy

'''
    for more info on this, visit
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185
'''
if __name__ == '__main__':

    # init node (name of node may be different than name of file)
    # cannot run two nodes with the same name
    rospy.init_node("my_first_python_node")

    #set rate to 10 hz
    rate = rospy.Rate(10)

    # ctrl + C to shutdown nodes from terminal
    while not rospy.is_shutdown():

        #just like our first node
        rospy.loginfo("Hello, SSI!")

        #sleeps execution to predefined value (10hz / every 0.1 seconds)
        rate.sleep()

        # what happens if we try to launch the same node twice??
