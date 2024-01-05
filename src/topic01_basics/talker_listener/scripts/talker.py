#!/usr/bin/env python

'''
Important Note:
# The line-1 is a special line starting with #!
# It tells the operating system, how to execute the script.
'''
import rospy
from std_msgs.msg import String

def talker():
    # create a publisher node, (topic_name, type_of_message, queue_size/buffer)
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # initialize the node, (node_name, anonymous=True means that rospy will make sure the name of node is unique)
    rospy.init_node('talker', anonymous=True)

    # speed of message
    rate = rospy.Rate(1) # 1Hz

    # publish the ROS message
    i = 0

    while not rospy.is_shutdown():
        msg = "Hello Veer! {}".format(i)
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass