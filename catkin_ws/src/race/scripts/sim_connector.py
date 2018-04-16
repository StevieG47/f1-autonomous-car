#!/usr/bin/env python


# Subscribe to drive_param topic, which control.py is publishing to
# Need to convert info from that topic to ackermann commands since thats what drives our car in simulation here
# Read velocity from drive_param, set AckermannDriveStamped msg.speed
# Read angle from drive_param, set AckermannDriveStamped msg. angle
# Use default values for acceleration, jerk, steering angle
# publish ackermann commands

import rospy
from race.msg import drive_param
from ackermann_msgs.msg import AckermannDriveStamped

import math

pub = rospy.Publisher('/vesc/ackermann_cmd_mux/input/teleop', AckermannDriveStamped, queue_size=5)

def vel_and_angle(data):
	

	msg = AckermannDriveStamped();
	msg.header.stamp = rospy.Time.now();
	msg.header.frame_id = "base_link";

	msg.drive.speed = data.velocity
	msg.drive.acceleration = 1
	msg.drive.jerk = 1
	msg.drive.steering_angle = data.angle
	msg.drive.steering_angle_velocity = 1
	# print "velocity", data.velocity
	# print "angle", data.angle

	pub.publish(msg)



def listener():
	rospy.init_node('sim_connect', anonymous=True)
	rospy.Subscriber('drive_parameters', drive_param, vel_and_angle)
	rospy.spin()





if __name__=="__main__":
	listener()
