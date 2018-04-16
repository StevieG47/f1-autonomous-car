#!/usr/bin/env python


# Subsrcibe to /scan, use callback(data) as the callback function
import rospy
import math
from sensor_msgs.msg import LaserScan
from race.msg import pid_input
import numpy as np
#import matplotlib.pyplot as plt

angle_range = 180
# angle_range = np.pi
car_length = 1.5

desired_trajectory = 0

vel = 1
path = [1,0,1,1,1]
turn = 0
preva = 0
flag = 0
errorList = [0,0,0,0,0]
turnStarted = 0
error = 0.0
alpha = 0.0
final_desired_trajectory = -1
final_direction = 1

left_dist = []
objbuffer = [-1]*25

flag_left = 0

pub = rospy.Publisher('error', pid_input, queue_size=10)


# Returns the distance read by laser scan at a given angle
def getRange(data,angle):
	if angle > 179.9:
		angle = 179.9
	# if angle > np.pi-1e-4:
		# angle = np.pi-1e-4
	index = len(data.ranges)*angle/angle_range
	dist = data.ranges[int(index)]
	if math.isinf(dist) or math.isnan(dist):
		return 4.0
	return data.ranges[int(index)]

# Checks over a range of angles to see if there are obstacles closer than a certin distance
# Return all dist ranges and number of times a reading was < distance
def obs_particles(data, start, end, distance):
	global alpha
	front_values = []
	num_points = 0
	obs = 0
	alpha_degree = int(math.degrees(alpha))
	k = -1
	for i in range(start - alpha_degree, end - alpha_degree):
	# for i in range(start - alpha, end - alpha):
		k = k+1
		front_values.append(getRange(data,i)*math.sin(math.radians(i+alpha_degree)))
		
		if front_values[k] <= distance:
			num_points = num_points + 1
	return front_values,num_points	

def obs_decide(data):
	global alpha
	
	# Given start and end angle, and a distance thresh, loop over range of angles between start and end
	# If the distance reading at any angle is less than the dist threshold, num_points += 1
	# values will hold all of the distances recorded, 
	# num_points is number of angles with in the given range that have a distance reading < distance variable
	start = 84
	end = 96
	distance = 2.0
	values,num_points = obs_particles(data,start,end,distance) ; start_point = 0; end_point = 0
	
	# If num_points < 3, there are pretty much no obstacles in the angle range, clear path
	if num_points < 3:
		#print "Go go go - clear path"
		return -1,-1

	# Else if we got more than 3, less than 15 angle readings < distance var, there is obstacle there
	# start_point and end point are the range of angles from first angle seeing small dist to last angle seeing small dist
	elif num_points <= 15:
		#print "normal obstacle"

		# Loop through all distances recorded, find first point where dist reading is < distance var
		# Save angle that corresponded to that first point where dist reading < distance var
		# start_point is this angle
		k =-1
		for i in values:
			k = k + 1
			if i<= (distance):
				start_point = k + start
				break

		# Do the same but for the end point, so start at the end of all distancse recorded,
		# stop at first point where dist < reading is < distance variable, get corresponding angle
		# end_point is the end angle
		k = -1
		for i in reversed(values):
			k = k+1
			if i<= (distance):
				end_point = end - k
				break

		# If the very first reading from values had a small distance, that means that an angle outside of the range
		# (smaller than our first angle, start) might have a distance reading < distance variable
		# We gotta expand the range on that side to check
		if start_point <= (start+1):
			#print "Start point extended"
			start1 = start - 10
			end1 = start
			start_point = start1
			
			# Get a new values, num_points with the range start, start - 10, so 10 degrees less than our previous start range
			values,num_points = obs_particles(data,start1,end1,distance)
			#print "Right extended", values

			# With new values array, get new start_point angle variable with extended range readings
			# remember:
			# start_point and end point are the range of angles from first angle seeing small dist to last angle seeing small dist
			k = 0
			for i in reversed(values):
				k = k + 1
				if i > (distance):
					start_point = end1 - k
					break
		
		# Same deal with end_point, if the end range from start, end range has a small dist, an angle outside might also have
		# a small dist so we're not seeing the whole obstacle, extend the range
		if end_point >= (end-1):
			start2 = end + 1
			end2 = end + 10
			end_point = end2

			# Get new values, num_points with range end+1, end+10, so 10 degrees more than our previous range
			values,num_points = obs_particles(data,start2,end2,distance)			
			#print "Right extended", values
			
			# With new values array, get new end_point angle variable with extended range readings
			k = len(values)-1
			for i in values:
				k = k-1
				if i > (distance):
					end_point = end2 - k
					break
		
		# Return start_point, end_point, the min/max angles in the range that had a small dist reading
		#print "Start Point", start_point
		#print "End Point", end_point
		return start_point,end_point

	
	# Else if we got more than 15 points with small dist, it's a super wide obstacle	
	else:
		#print "wide obstacle"
		# With a wide ass obstacle, start from an expanded range, this is the start angle side expanded
		start1 = start - 10
		end1 = start - 1
		start_point = end1 + 3
		
		# Get new values, num_points for extension range
		values,num_points = obs_particles(data,start1,end1,distance)

		# Get new start_point angle from this extended range
		k = len(values) - 1
		for i in reversed(values):
			k = k - 1
			if i > (distance):
				start_point = k + start1
				break
	
		# Now do extended range for the other side, end angle side
		start2 = end + 1
		end2 = end + 10
		end_point = start2 - 3
		
		# Get new values, num_points with range end+1 to end+10
		values,num_points = obs_particles(data,start2,end2,distance)

		# Get new end_point angle from extended range			
		k = len(values)-1
		for i in values:
			k = k-1
			if i > (distance):
				end_point = end2 - k
				break

		# If the first angle has a small dist and the last angle has a small dist even with extended ranges, we got a wall boys
		#print "wall"		
		if start_point <= start1+1:
			start_point = -1
		if end_point >= end2-1:
			end_point = -1
		
		# Return start_point, end_point, the min/max angles in the range that had a small dist reading
		#print "Start Point", start_point
		#print "End Point", end_point
		return start_point,end_point


def decide_obstacle_direction(data,start_point,end_point):
	global alpha
	left = 0
	right = 1
	centre = 2
	stop = 3
	alpha_degree = int(math.degrees(alpha))
	desired_trajectory = -1

	direction = centre
	
	# If we saw no obstacles or saw a wall, start_point = end_point = -1
	# If we saw an obstacle or wide obstacle, continue
	if start_point!=-1 or end_point!=-1:

		# Get laser range values of start angle and end angle
		laser_start = getRange(data,start_point-alpha_degree)
		laser_end = getRange(data,end_point-alpha_degree)
		
		start_pointdistance = laser_start*math.cos(math.radians(start_point))
		end_pointdistance = laser_end*math.cos(math.radians(end_point))
		#print "Right Width",start_pointdistance
		#print "left Width",end_pointdistance

		# Get distance directly left and directly right of the car
		car_dist_right = getRange(data,0)*math.cos(alpha)
		car_dist_left = getRange(data,179)*math.cos(alpha)
		#print "Car dist right",car_dist_right
		#print "Car dist left",car_dist_left

		# Get left/right obstacle distances, account for left/right distances of car
		obstacle_distance_right = car_dist_right - start_pointdistance
		obstacle_distance_left = car_dist_left + end_pointdistance
		#print "Right edge",obstacle_distance_right
		#print "left edge",obstacle_distance_left

		# If right obstalce closer want to go left
		if (obstacle_distance_left > obstacle_distance_right):
			desired_trajectory = obstacle_distance_left/2
			direction =left
			#print "left"

		# If left obstalce closer want to go right
		elif (obstacle_distance_left < obstacle_distance_right):
			desired_trajectory = obstacle_distance_right/2
			direction =right
			#print "right"
		
		# If theyre the same stop i guess
		else:
			direction = stop

	# If start_point = end_point = -1, then we're going straight
	else:
		desired_trajectory = -1
		direction = centre
		#print "Go centre"

	# Uhh it looks like no matter what the readings are they set desired trajectory to -1 and direction to center every time
	desired_trajectory = -1
	direction = centre
	#print "Go centre"
	#print "Desired dist", desired_trajectory

	# Return the direction and desired_trajectory, which is just a distance i think
	return desired_trajectory, direction



def followRight(data,desired_trajectory):
	global alpha
	
	# Get laser ranges at 0 degrees (exatly right) and 60 degrees
	a = getRange(data,60)
	b = getRange(data,0)
	swing = math.radians(60)
	alpha = math.atan((a*math.cos(swing)-b)/(a*math.sin(swing)))
	#print "a","b", a, b
	#print "Alpha right",math.degrees(alpha)

	# Get the current distance to the right
	curr_dist = b*math.cos(alpha)

	# Get future distance to the right
	future_dist = curr_dist+car_length*math.sin(alpha)

	#print "Right : ",future_dist

	# We want to be a value of 2 away from the right, error is 2 - future dist calculated
	error = desired_trajectory - future_dist
	#print "Error : ",error

	# Return our error from the right, current distance from the right
	return error, curr_dist

def followLeft(data,desired_trajectory):
	global alpha

	a = getRange(data,120)
	b = getRange(data,179.9)
	swing = math.radians(60)
	#print "a","b", a, b
	alpha = -math.atan((a*math.cos(swing)-b)/(a*math.sin(swing)))
	#print "Alpha left",math.degrees(alpha)
	curr_dist = b*math.cos(alpha)
	future_dist = curr_dist-car_length*math.sin(alpha)

	#print "Left : ",future_dist

	error = future_dist - desired_trajectory
	return error, curr_dist


def followCentre(data,desired_trajectory):
	global alpha

	a = getRange(data,130)
	b = getRange(data,179.9)
	swing = math.radians(50)
	#print "center distances: ", a, b
	alpha = -math.atan((a*math.cos(swing)-b)/(a*math.sin(swing)))
	#print "Alpha left",math.degrees(alpha)
	curr_dist1 = b*math.cos(alpha)
	future_dist1 = curr_dist1-car_length*math.sin(alpha)



	a = getRange(data,50)
	b = getRange(data,0)
	swing = math.radians(50)
	alpha = math.atan((a*math.cos(swing)-b)/(a*math.sin(swing)))
	#print "Alpha right",math.degrees(alpha)
	curr_dist2 = b*math.cos(alpha)

	future_dist2 = curr_dist2+car_length*math.sin(alpha)

	desired_trajectory = (future_dist1 + future_dist2)/2

	#print "dist 1 : ",future_dist1
	#print "dist 2 : ",future_dist2
	# print "dist : ",future_dist
	error = future_dist1 - future_dist2
	#print "Error : ",error
	return error, curr_dist2-curr_dist1



def decideReturn(start_point,end_point):
	global objbuffer
	objbuffer.append(start_point)
	objbuffer.append(end_point)
	del objbuffer[0]
	del objbuffer[0]
	if objbuffer.count(-1)==len(objbuffer):
		return 1
	else:
		return 0

def callback(data):
	global error
	global alpha
	#print " "
	global flag_obstacle
	global final_desired_trajectory
	global final_direction
	global prev_direction
	global flag_left

	# Get start_point, end_point, the min/max angles in the /scan range (defined in obs_decide function) that had a small dist reading
	#start_point,end_point = obs_decide(data)

	# Get trajectory, which is a distance, and direction: center, right, or left based on the obstacles in the laser range
	# start_point, end_point
	#final_desired_trajectory, direction = decide_obstacle_direction(data,start_point,end_point)

	# OK so it seems like final_desired_trajectory and direction are not even used which means start_point, end_point are not even used
	# So yea

	# Get errror from the right and current distance from the right. Desired distance from right is 2
	error_right, curr_dist_right = followRight(data,2.)

	# Get error from left and current distance from the left. Desired distance from left is 1
	error_left, curr_dist_left = followLeft(data,1.)

	# Get error from center and current center distance. Desired distance is 1
	error_center, curr_dist_center = followCentre(data,1.)

	# If distance to the left is smaller do wall following w/ the left wall (pid to get to desired distance from left wall)
	if curr_dist_right >= curr_dist_left:
		error = error_left
		print 'Following Left'
		print 'Error', error
	
	# else if distance to right is smaller do wall following w/ the right wall (pid to get desired distance from right wall)
	else:
		error = error_right
		print 'Following Right'
		print 'Error', error


	#print 'Is error same?', error
	msg = pid_input()
	msg.pid_error = error
	msg.pid_vel = vel
	pub.publish(msg)

	print ' '
	
# So what this is currently doing is checking if it is clsoer to the left or right wall
# Whatever wall it is closer to it uses that error as the pid error
# For left wall desired distance is 1, for right wall desired distance is 2 (since it is always making left turns)
# The error is the distance the car will be to the wall - desired distance
# The error is published and sent to the controller which will pid steering angle to reduce error
if __name__ == '__main__':
	print("Laser node started")
	rospy.init_node('dist_finder',anonymous = True)
	rospy.Subscriber("scan",LaserScan,callback)
	rospy.spin()
