#!/usr/bin/env python

# just like we had to import the turtle mod
import rospy
# import message type from std_msgs dependency
from std_msgs.msg import String

# define a callback function to be passed into the subscriber
# this will execute every time the subscriber is invoked (upon reception of a publication)
def callback_received_publisher_data(msg):
    rospy.loginfo("Message received: ")
    rospy.loginfo(msg)


'''
    for more info on this, visit
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185
'''
if __name__ == '__main__':

    # init node (name of node may be same as name of file)
    rospy.init_node("robot_subscriber")

    '''
    -create a subsciber("topic name", message_type, callback_function)
    -our message type here is part of the std_msgs package
    we installed when we created our package
    -define a callback function to execute a certain block of code
    '''
    rospy.Subscriber("/robot_news", String, callback_received_publisher_data)

    # keep the script running with callback until the node has been terminated
    rospy.spin()
