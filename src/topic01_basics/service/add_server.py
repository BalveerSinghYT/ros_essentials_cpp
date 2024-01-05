#!/usr/bin/env python

from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

import rospy

def handle_add_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    #               (server_name)
    rospy.init_node('add_two_ints_server')

    #                 (service_name, service_type, call_back_func)
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print ("Ready to add two ints.")
    rospy.spin()
    
if __name__ == "__main__":
    add_two_ints_server()
