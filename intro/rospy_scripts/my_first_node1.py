#!/usr/bin/env python

#just like we had to import the turtle mod
import rospy

'''
    for more info on this, visit
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185
'''
if __name__ == '__main__':

    #init node (name of node may be different than name of file)
    rospy.init_node("my_first_python_node")

    # we call methods from rospy just like we did from turtle
    rospy.loginfo("my_first_python_node has been started!")

    # delays execution of next command by 1 second
    rospy.sleep(1)

    # log infor after 1 second of sleep
    rospy.loginfo("exiting my_first_python_node!")

    # what happens if we try to launch the same node twice??
