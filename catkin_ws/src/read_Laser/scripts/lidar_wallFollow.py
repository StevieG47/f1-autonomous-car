import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input
import numpy as np

def getRange(scan, angle):
    index = (angle + 45) / .25
    dist = scan.ranges[int(index)]
    return dist

def getRightError():
    

def getLeftError():
    
    
def wallFollower(scan):
    
    # Get distances directly left/right of car
    distRight = getRange(scan,0)
    distLeft = getRange(scan,180)
    
    # Pick which wall to follow 
    
    
    
# Initaite node, subsriber
rospy.init_node('wallFollow', anonymous = True)
rospy.Subscriber("scan", LaserScan, wallFollower)
rospy.spin()
    
    
