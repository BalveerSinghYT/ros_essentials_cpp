#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# this will execute as soon as it receive the msg from publisher node
def chatter_callback(message):
    print("I heard", message.data)

def listner():
    # create a listener node, (topic_name, type_of_message, call_back_func)
    sub = rospy.Subscriber('chatter', String, chatter_callback)

    # initialize the node
    rospy.init_node('listner', anonymous=True)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listner()

    
