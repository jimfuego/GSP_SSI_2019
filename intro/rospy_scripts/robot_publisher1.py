#!/usr/bin/env python

# just like we had to import the turtle mod
import rospy
# import message type from std_msgs dependency
from std_msgs.msg import String

'''
    for more info on this, visit
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185
'''
if __name__ == '__main__':

    # init node (name of node may be same as name of file)
    rospy.init_node("robot_publisher")

    '''
    -create a publication("topic name", message_type, size_of_message_queue)
    -our message type here is part of the std_msgs package
     we installed when we created our package
    -define queue size for when nodes publish many messages;
     this acts as a buffer for busy subscribers
    '''
    publisher = rospy.Publisher("/robot_news", String, queue_size=10)

    # set the rate of publication
    rate = rospy.Rate(2)

    # while the node is running
    while not rospy.is_shutdown():
        # instantiate a standard message String object
        msg = String()
        # set that object's data to our desired message
        msg.data = "This is Rob Robotica, and this is the Robot News!"
        # broadcast that message
        pub.publish(msg)
        # delay between publications
        rate.sleep()

    # let users know that the node has been shutdown
    rospy.loginfo("robot_publisher_node has been shutdown")
