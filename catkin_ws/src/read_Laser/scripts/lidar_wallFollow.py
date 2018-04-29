#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input
import numpy as np

# Publish the error to give to pdControl.py so we can move the car accordingly
pub = rospy.Publisher('error', pid_input, queue_size=10)

def getRange(scan, angle):
    index = (angle + 45) / .25
    dist = scan.ranges[int(index)]
    return dist

def getRightError(distRight):
    desiredWallDist = 2
    error =  desiredWallDist - distRight # for get left it is dist - desired. This is cause for following right wall we wanna be on left side of wall and following left wall we wanna be on right side of wall
    return error

def getLeftError(distLeft):
    desiredWallDist = 1
    error = distLeft - desiredWallDist
    return error
    
def wallFollower(scan):
    
    # Get distances directly left/right of car
    distRight = getRange(scan,0) # was 0
    distLeft = getRange(scan,180) # was 180
    distForward = getRange(scan,90)
    
    # Pick which wall to follow 
    # If the left wall is closer, follow left wall
    if distRight > distLeft:
        error = getLeftError(distLeft)
        print("Following Left")
        print("dist: ", distLeft)
        print("error: ", error)
    
    # If the right wall is closer, follow the right wall
    else:
        error = getRightError(distRight)
        print(" Following Right")
        print("dist: ", distRight)
        print("error: ", error)
        
        
    # If we're about to go straight into wall we need a behavior separate from the wall following
    # we've been doing. If distForward is < some value we'll check if left or right is closer
    # Then turn away from the closer one
    if distForward < 2:
        
        # Since this function only passes an error, we'll pass a specific error to let
        # pdControl.py know distForward is small. Send a separate one for if left/right wall
        # is closer
        if distLeft < distRight:
            error = 1234567 # send this specific number if we want to turn right
        else:
            error = 12345 # send this specific number if we want to turn left
            
    # If we get to an area where distLeft and distRight are both out of range just turn left
    # If the track we were going on was clockwise as opposed to counter clock wise we would turn right
    # so we would go in the right direction
    if distRight == inf and distLeft == inf: # FIND OUT HOW TO CHECK FOR INF
        error = 12345
        
        
        
    # Publish error 
    msg = pid_input()
    msg.pid_error = error
    msg.pid_vel = 1 # doesnt matter since we change it in pdControl.py
    pub.publish(msg)
    
   # print('Dist Forward: ', distForward)


    
    
    
    
# Initaite node, subsriber
rospy.init_node('wallFollow', anonymous = True)
rospy.Subscriber("scan", LaserScan, wallFollower)
rospy.spin()
    
    
