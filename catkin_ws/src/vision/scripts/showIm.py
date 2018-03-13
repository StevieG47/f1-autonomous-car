#!/usr/bin/env python

# rospy for the subscriber
import rospy

# ROS Image message
from sensor_msgs.msg import Image

# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError

# OpenCV2 for saving an image
import cv2


# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

    except CvBridgeError, e:
        print(e)

    else:
        # display
        cv2.imshow('Image', cv2_img)
	cv2.waitKey(3)

def main():
    rospy.init_node('image_listener')

    # Define your image topic
    image_topic = "/camera/rgb/image_raw"

    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)

    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
	main()
