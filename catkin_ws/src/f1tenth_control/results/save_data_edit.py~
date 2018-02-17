#!/usr/bin/env python

"""Extract images from a rosbag.
"""
import rospy
import os,sys
import argparse
import cv2
import rosbag 
import csv
import string
from std_msgs.msg import Int32, String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ackermann_msgs.msg import AckermannDriveStamped
    

bridge = CvBridge()


def main():

    rospy.init_node('data_listener')

    global count1, count2, count3, count4
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    # Create new folders to store images
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("x", help="Input trial number")
    args = parser.parse_args()

    global camera1path, camera2path, camera3path, camera4path 
    global filename, filewriter, firstIteration
    
    newpath = ((r'/home/labpc/f1tenth_sim/src/f1tenth_control/results/images/trial_%s') % (args.x)) 
    filename = (newpath + '/steering_angle_data_%s.csv' % (args.x))
    
    if not os.path.exists(newpath): os.makedirs(newpath)
 
    camera1path = ((r'/home/labpc/f1tenth_sim/src/f1tenth_control/results/images/trial_%s/camera1_images') % (args.x)) 
    if not os.path.exists(camera1path): os.makedirs(camera1path)
    camera2path = ((r'/home/labpc/f1tenth_sim/src/f1tenth_control/results/images/trial_%s/camera2_images') % (args.x)) 
    if not os.path.exists(camera2path): os.makedirs(camera2path)
    camera3path = ((r'/home/labpc/f1tenth_sim/src/f1tenth_control/results/images/trial_%s/camera3_images') % (args.x)) 
    if not os.path.exists(camera3path): os.makedirs(camera3path)
    camera4path = ((r'/home/labpc/f1tenth_sim/src/f1tenth_control/results/images/trial_%s/camera4_images') % (args.x)) 
    if not os.path.exists(camera4path): os.makedirs(camera4path)
        

    # Define your image topic
    image_topic1 = '/camera1/rgb/image_raw'
    image_topic2 = '/camera2/rgb/image_raw'
    image_topic3 = '/camera3/rgb/image_raw'
    image_topic4 = '/camera4/rgb/image_raw' 
    ackermann_topic = '/ackermann_cmd'

    with open(filename, 'w+') as csvfile:
	filewriter = csv.writer(csvfile, delimiter = ',')
	firstIteration = True	#allows header row
 
    # Set up your subscriber and define its callback

    while True:
              
	    rospy.sleep(1)

	    msg1 = rospy.wait_for_message(image_topic1, Image)

	    print("Received an image!")
	    try:
		# Convert your ROS Image message to OpenCV2
		cv_img = bridge.imgmsg_to_cv2(msg1, desired_encoding="passthrough")
	    except CvBridgeError, e:
		print(e)
	    else:
		# Save your OpenCV2 image as a jpeg 
		cv2.imwrite(os.path.join(camera1path, "frame%06i.png" % count1), cv_img)     
		print "Wrote image %i" % count1
		count1 += 1
	    
            msg2 = rospy.wait_for_message(image_topic2, Image)

	    print("Received an image!")
	    try:
		# Convert your ROS Image message to OpenCV2
		cv_img = bridge.imgmsg_to_cv2(msg2, desired_encoding="passthrough")
	    except CvBridgeError, e:
		print(e)
	    else:
		# Save your OpenCV2 image as a jpeg 
		cv2.imwrite(os.path.join(camera2path, "frame%06i.png" % count2), cv_img)     
		print "Wrote image %i" % count2
		count2 += 1


	    msg3 = rospy.wait_for_message(image_topic3, Image)

	    print("Received an image!")
	    try:
		# Convert your ROS Image message to OpenCV2
		cv_img = bridge.imgmsg_to_cv2(msg3, desired_encoding="passthrough")
	    except CvBridgeError, e:
		print(e)
	    else:
		# Save your OpenCV2 image as a jpeg 
		cv2.imwrite(os.path.join(camera3path, "frame%06i.png" % count3), cv_img)     
		print "Wrote image %i" % count3
		count3 += 1

	    msg4 = rospy.wait_for_message(image_topic4, Image)

	    print("Received an image!")
	    try:
		# Convert your ROS Image message to OpenCV2
		cv_img = bridge.imgmsg_to_cv2(msg4, desired_encoding="passthrough")
	    except CvBridgeError, e:
		print(e)
	    else:
		# Save your OpenCV2 image as a jpeg 
		cv2.imwrite(os.path.join(camera4path, "frame%06i.png" % count4), cv_img)     
		print "Wrote image %i" % count4
		count4 += 1

	    msg5  = rospy.wait_for_message(ackermann_topic, AckermannDriveStamped)

	    with open(filename, 'a') as csvfile:
	   	filewriter = csv.writer(csvfile, delimiter = ',')
		msgString = str(msg5)
		msgList = string.split(msgString, '\n')
		instantaneousListOfData = []
		for nameValuePair in msgList:
			splitPair = string.split(nameValuePair, ':')
		        for i in range(len(splitPair)):	#should be 0 to 1
				splitPair[i] = string.strip(splitPair[i])
			instantaneousListOfData.append(splitPair)
		onlySteeringAngle = instantaneousListOfData[7:8]
		#filewriter.writerow(onlySteeringAngle)
		#write the first row from the first element of each pair
		if firstIteration:	# header
			headers = ["rosbagTimestamp"]	#first column header
			for pair in onlySteeringAngle:
				headers.append(pair[0])
			filewriter.writerow(headers)
			firstIteration = False
		# write the value from each pair to the file
		t = rospy.Time.now()
		values = [str(t)]	#first column will have rosbag timestamp
		for pair in onlySteeringAngle:
			if len(pair) > 1:
				values.append(pair[1])
		filewriter.writerow(values)    


    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    main()

