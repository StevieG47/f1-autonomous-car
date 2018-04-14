#include "ros/ros.h"
#include "nav_msgs/OccupancyGrid.h"
#include "std_msgs/Header.h"
#include "nav_msgs/MapMetaData.h"
#include "sensor_msgs/LaserScan.h"
#include "ackermann_msgs/AckermannDriveStamped.h"
#include <bits/stdc++.h>
#include <vector>
#include <algorithm> 
#include <iostream>
#include <unistd.h> // usleep(microseconds)


// Set publisher
ros::Publisher ackPub;

float getRange(const sensor_msgs::LaserScan::ConstPtr &data, int angle) {
	
	// Set msg laser scan msg variable
	sensor_msgs::LaserScan laserScan; // variable for /scan data. rostopic info /scan shows sensor_msgs/LaserScan
	laserScan = *data;
	
	// Get index associated with angle
	int index = (angle + 45) / .25;
	
	// Return range at index
	std::vector<float> laserRanges; // Create laserRanges vector. Use rosmsg show sensor_msgs/LaserScan to view all
	laserRanges = laserScan.ranges;
	return laserRanges[index];
}


void scanCallback(const sensor_msgs::LaserScan::ConstPtr &data) {
	
	// Set left, right, forward angles
	int angleRight = 50;
	int angleLeft = 130;
	int angleForward = 90;
	
	// Get distance reading for each angle
	float distRight = getRange(data, angleRight);
	float distLeft = getRange(data, angleLeft);
	float distForward = getRange(data, angleForward);
	
	// Set variables for car angle, speed, and for desired left/right/forward spacing
	float angle = 0;
	float speed = .3;
	float lrDist = 1.1; // desired dist spacing for left/right sides
	float fDist = 2; // desired dist spacing in front
	
	// If too close on the right turn left
	if (distRight < lrDist) {
		speed = .25;
		angle = .3;
	}
	
	// If too close on the left turn right
	if (distLeft < lrDist) {
		speed = .25;
		angle = -.3;
	}
	
	// If too close ahead check left/right dist, turn away from closest wall
	if (distForward < fDist) {
		speed = .25;
		if (distLeft < distRight) { 
			angle = -.8;
		}
		else if (distRight < distLeft) {
			angle = .8;
		}
	}
	
	// Print values
	std::cout << "distRight: " << distRight << std::endl;
	std::cout << "distLeft: " << distLeft << std::endl;
	std::cout << "distForward: " << distForward << std::endl;
	std::cout << "angle: " << angle << std::endl << std::endl;
	
	// Set ackermann msg
	ackermann_msgs::AckermannDriveStamped cmd;
	//cmd.header.stamp = 
	cmd.header.frame_id = "base_link";
	cmd.drive.speed = speed;
	cmd.drive.acceleration = 1;
	cmd.drive.jerk = 1;
	cmd.drive.steering_angle = angle;
	cmd.drive.steering_angle_velocity = 1;
	
	// publish
	ackPub.publish(cmd);
	usleep(10);
}


int main(int argc, char **argv) {
	
	ros::init(argc, argv, "lidarmove");
	ros::NodeHandle n;
	
	// Subscribe to /scan
	ros::Subscriber scan_sub = n.subscribe("/scan", 1000, scanCallback);
	
	// Set publisher
	ackPub = n.advertise<ackermann_msgs::AckermannDriveStamped> ("/ackermann_cmd", 100);
			
	// time 
	ros::Duration waitT (.05);
	
	// Loop em
	while (ros::ok() ) {
		
		// spin em
		ros::spinOnce();
		waitT.sleep();
	}

	
	return 0;
}