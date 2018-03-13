#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
import sys, select, termios, tty
import numpy as np

angle = 0


def getRange(data, theta):
    """ Find the index of the arary that corresponds to angle theta.
    Return the lidar scan value at that index
    Do some error checking for NaN and absurd values
	data: the LidarScan data
	theta: the angle to return the distance for
	"""
    car_theta = math.radians(theta) - math.pi / 2
    if car_theta > 3 * math.pi / 4:
        car_theta = 3 * math.pi / 4
    elif car_theta < -3 * math.pi / 4:
        car_theta = -3 * math.pi / 4

    float_index = (car_theta + 3 * math.pi / 4) / data.angle_increment
    index = int(float_index)
    return data.ranges[index]



def getRange2(data,theta):
# Find the index of the arary that corresponds to angle theta.
# Return the lidar scan value at that index
# Do some error checking for NaN and ubsurd values
## Your code goes here
    ranges = data.ranges
    index = int ( (theta + 45) / 0.25)	
    return ranges[index]
    


def laserCallback(data):
    global angle, speed
    theta = 50;
    
    angleRight = 50
    angleLeft = 140
    angleForward = 90
    
    distRight = getRange2(data,angleRight)
    distLeft = getRange2(data,angleLeft)
    distForward = getRange2(data,angleForward)
      
    angle = 0
    speed = .3
    if distRight < .8:
        speed = .1
        angle = .3
    
    if distLeft < .8:
        speed = .1
        angle = -.3
    
    if distForward < 2:
        speed = .05
        if distLeft < distRight:
            angle = -.8
        if distRight < distLeft:
            angle = .8
    
    print "distRight: ",distRight
    print "distLeft: ",distLeft
    print "distForward: ",distForward
    print "angle: ", angle
    print " "
        
    
    
#    angleTheta = getRange(data, theta); a = angleTheta
#    angleZero = getRange(data, 0); b = angleZero
#    
#    swing = math.radians(theta)
#
#    alpha = math.atan2( a * math.cos(swing) - b , a * math.sin(swing) )
#    AB = b * math.cos(alpha)
#
#    AC = 1
#    CD = AB + AC * math.sin(alpha)
#    
#    if angleZero > 1.2:
#        angle = -.3 # turn wheel
#    elif angleZero < 1:
#        angle = .3 # turn wheel
#    else: 
#        angle = 0 # wheel straight
#    
#    # angle min/max boundaries
#    if abs(angle) > 1.5:
#        angle = 1.5*np.sign(angle)

    #error = AB - desired_trajectory
   # error = CD - desired_trajectory

    #ABprime = a * math.cos(math.asin(a * math.sin(swing) / math.sqrt(a*a + b*b - 2*a*b*math.cos(swing))) - math.pi / 2 + swing)
    #print "alpha: ",alpha
    #print "Reading at angle = ", theta, ": ",angleTheta 
#    print "Reading at angle = 0: ", angleZero
#    print "angle: ",angle
#    print " "
   # print "  "


if __name__ == '__main__':
    global angle, speed

	# Initiate node and publisher
    print "Starting Wall Follower"
    rospy.init_node('Wall_Follow')
    pub = rospy.Publisher('~/ackermann_cmd', AckermannDriveStamped, queue_size=10)
	
	
	# Initialize speed/steering angle	
    speed = .1
    angle = 0 # 1.5
	
	# Initialize ackermann msg
    drivemsg = AckermannDriveStamped();
    drivemsg.header.stamp = rospy.Time.now();
    drivemsg.header.frame_id = "base_link";

    drivemsg.drive.speed = speed
    drivemsg.drive.acceleration = 1;
    drivemsg.drive.jerk = 1;
    drivemsg.drive.steering_angle = angle
    drivemsg.drive.steering_angle_velocity = 1;
	
    
	# Loop
    while not rospy.is_shutdown():
		
		# Subscribe to the lidar
        rospy.Subscriber("scan", LaserScan, laserCallback)
        drivemsg.drive.steering_angle = angle
		#rospy.loginfo("Zero Angle Dist: ",angleZero)

		# publish drive msgs
        pub.publish(drivemsg)
        rospy.sleep(.15)




















